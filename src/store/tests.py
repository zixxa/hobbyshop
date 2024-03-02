import os

from django.test import TestCase
from src.store.models import Item, Category

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')


class TestModelCase(TestCase):
    parent_category: Category
    category_1: Category
    category_2: Category
    unactive_category: Category
    item_1: Item
    item_2: Item

    def setUp(self):
        self.parent_category = Category.objects.create(name='Мебель', active_on=True)
        self.category_1 = Category.objects.create(name='Шкафы', parent=self.parent_category, active_on=True)
        self.category_2 = Category.objects.create(name='Стулья', parent=self.parent_category, active_on=True)
        self.item_1 = Item.objects.create(name='Альфа', category=self.category_1, active_on=True)
        self.item_2 = Item.objects.create(name='Бета', category=self.category_2, active_on=True)
        self.unactive_category = Category.objects.create(name='Автомобили')

    def test_auto_unactive(self):
        self.assertTrue(self.unactive_category.active_on == False)

    def test_items(self):
        item_1 = self.item_1
        item_2 = self.item_2

        self.assertEqual(item_1.__str__(), 'Альфа')
        self.assertEqual(item_2.__str__(), 'Бета')

    def test_categories(self):
        category1 = Category.objects.get(name='Шкафы')
        category2 = Category.objects.get(name='Стулья')
        parent = Category.objects.get(name='Мебель')


class TestCalls(TestCase):
    parent_category: Category
    child_category: Category
    child_item: Item
    single_category: Category
    single_item: Item

    def setUp(self):
        self.parent_category = Category.objects.create(name='Мебель', active_on=True)
        self.child_category = Category.objects.create(name='Стулья', parent=self.parent_category, active_on=True)
        self.child_item = Item.objects.create(name='Стул', category=self.child_category, active_on=True)
        self.single_category = Category.objects.create(name='Машины', active_on=True)
        self.single_item = Item.objects.create(name='Лопата', active_on=True)

    def test_call_index(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_call_by_auto_slug(self):
        response = self.client.get(f"/items/{self.single_item.slug}/")
        self.assertEqual(response.status_code, 200)

    def test_call_item_list_in_category(self):
        response = self.client.get(f"/category/{self.single_category.slug}/")
        self.assertEqual(response.status_code, 200)

    def test_call_category_list(self):
        response = self.client.get(f"/categories/")
        self.assertEqual(response.status_code, 200)
