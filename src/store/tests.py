from django.test import TestCase
from store.models import Item, Type

class ItemsTestCase(TestCase):
    def setUp(self):
        Type.objects.create(name='Мебель')
        Item.objects.create(title='табуретка', type=Type.objects.get(name='Мебель'))
        Item.objects.create(title='шкаф', type=Type.objects.get(name='Мебель'))
        Item.objects.create(title='стол', type=Type.objects.get(name='Мебель'))

    def test_items(self):
        shelf = Item.objects.get(title='табуретка')
        table = Item.objects.get(title='стол')
        closet = Item.objects.get(title='шкаф')
        self.assertEqual(table.slug(), 'stol')
        self.assertEqual(closet.slug(), 'shkaf')
