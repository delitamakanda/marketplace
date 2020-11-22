from django.shortcuts import render, get_object_or_404
from .forms import OrderCreateForm
from .models import OrderItem
from catalog.models import Product
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                product = get_object_or_404(Product, id=item['product']['id'], name=item['product']['name'])
                OrderItem.objects.create(
                    order=order, product=product, price=item['price'], quantity=item['quantity'])
            cart.clear()
            return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'form': form, 'cart': cart})
