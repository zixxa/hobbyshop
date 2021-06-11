from django.test import TestCase
from src.store.models import Item, Category

class ItemsTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name='Мебель')
        Category.objects.create(name='Шкафы', parent=Category.objects.get(name='Мебель'))
        Category.objects.create(name='Стулья', parent=Category.objects.get(name='Мебель'))
        Item.objects.create(title='Альфа', category=Category.objects.get(name='Стулья'))
        Item.objects.create(title='Бета', category=Category.objects.get(name='Шкафы'))

    def test_categorys(self):
        category1 = Category.objects.get(name='Шкафы')
        category2 = Category.objects.get(name='Стулья')
        parent = Category.objects.get(name='Мебель')

    def test_items(self):
        chair = Item.objects.get(title='Альфа',category=Category.objects.get(name='Стулья'))
        shelf = Item.objects.get(title='Бета', category=Category.objects.get(name='Шкафы'))

        self.assertEqual(chair.__str__(), 'Альфа')
        self.assertTrue(chair.get_articel())

        self.assertEqual(shelf.__str__(), 'Бета')
        self.assertTrue(shelf.get_articel())
