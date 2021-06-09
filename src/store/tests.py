from django.test import TestCase
from src.store.models import Item, Type

class ItemsTestCase(TestCase):
    def setUp(self):
        Type.objects.create(name='Мебель')
        Type.objects.create(name='Шкафы', parent=Type.objects.get(name='Мебель'))
        Type.objects.create(name='Стулья', parent=Type.objects.get(name='Мебель'))
        Item.objects.create(title='Альфа', itemtype=Type.objects.get(name='Стулья'))
        Item.objects.create(title='Бета', itemtype=Type.objects.get(name='Шкафы'))

    def test_types(self):
        type1 = Type.objects.get(name='Шкафы')
        type2 = Type.objects.get(name='Стулья')
        parent = Type.objects.get(name='Мебель')

    def test_items(self):
        chair = Item.objects.get(title='Альфа', itemtype=Type.objects.get(name='Стулья'))
        shelf = Item.objects.get(title='Бета', itemtype=Type.objects.get(name='Шкафы'))

        self.assertEqual(chair.__str__(), 'Альфа')
        self.assertTrue(chair.get_articel())

        self.assertEqual(shelf.__str__(), 'Бета')
        self.assertTrue(shelf.get_articel())
