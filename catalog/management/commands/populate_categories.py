from django.core.management.base import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    help = 'create dummy data to initialize fanfiction'

    def handle(self, *args, **options):
        if not Category.objects.filter(name="Livres, BD, Papetrie").exists():
            Category.objects.create(
                name='Livres, BD, Papetrie')
        if not Category.objects.filter(name="Musique, CD, Vinyles").exists():
            Category.objects.create(
                name='Musique, CD, Vinyles')
        if not Category.objects.filter(name="Jeux vidéo, Consoles").exists():
            Category.objects.create(name='Jeux vidéo, Consoles')
        if not Category.objects.filter(name="Films, Séries TV, DVD, Blue-Ray").exists():
            Category.objects.create(
                name='Films, Séries TV, DVD, Blue-Ray')
        if not Category.objects.filter(name="Maison, Décoration").exists():
            Category.objects.create(
                name='Maison, Décoration')
        if not Category.objects.filter(name="Bricolage, Jardin").exists():
            Category.objects.create(
                name='Bricolage, Jardin')
        if not Category.objects.filter(name="Enfants, Jouets, Bébés").exists():
            Category.objects.create(
                name='Enfants, Jouets, Bébés')
        if not Category.objects.filter(name="Informatique, Tablettes").exists():
            Category.objects.create(
                name='Informatique, Tablettes')
        if not Category.objects.filter(name="Smartphone, Téléphonie").exists():
            Category.objects.create(name='Smartphone, Téléphonie')
        if not Category.objects.filter(name="Vêtements, Maroquinerie").exists():
            Category.objects.create(name='Vêtements, Maroquinerie')

            self.stdout.write(self.style.SUCCESS('Created categories'))
