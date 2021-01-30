import weasyprint

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.contrib.admin.views.decorators import staff_member_required
from .forms import OrderCreateForm
from .models import OrderItem, Order
from catalog.models import Product
from cart.cart import Cart
from .tasks import order_created


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                product = get_object_or_404(
                    Product, id=item['product']['id'], name=item['product']['name'])
                OrderItem.objects.create(
                    order=order, product=product, price=item['price'], quantity=item['quantity'])
            cart.clear()
            order_created.delay(order.id)
            return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'form': form, 'cart': cart})


@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('orders/order/pdf.html', {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
    weasyprint.HTML(string=html).write_pdf(response, stylesheets=[
        weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')])
    return response
