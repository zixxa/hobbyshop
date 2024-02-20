import os

from django.contrib.auth.models import User
from django.test import TestCase

from src.store.admin import ItemAdmin
from src.store.models import Item, Category
from unittest.mock import Mock

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')


class TestModelCase(TestCase):
    parent_category: Category
    category_1: Category
    category_2: Category
    item_1: Item
    item_2: Item

    def setUp(self):
        self.parent_category = Category.objects.create(name='Мебель')
        self.category_1 = Category.objects.create(name='Шкафы', parent=self.parent_category)
        self.category_2 = Category.objects.create(name='Стулья', parent=self.parent_category)
        self.item_1 = Item.objects.create(name='Альфа', category=self.category_1)
        self.item_2 = Item.objects.create(name='Бета', category=self.category_2)

    def test_items(self):
        item_1 = self.item_1
        item_2 = self.item_2

        self.assertEqual(item_1.__str__(), 'Альфа')
        self.assertTrue(item_1.slug)
        self.assertTrue(item_1.get_articel())

        self.assertEqual(item_2.__str__(), 'Бета')
        self.assertTrue(item_2.slug)
        self.assertTrue(item_2.get_articel())

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
        self.parent_category = Category.objects.create(name='Мебель')
        self.child_category = Category.objects.create(name='Стулья', parent=self.parent_category)
        self.child_item = Item.objects.create(name='Стул', category=self.child_category)
        self.single_category = Category.objects.create(name='Машины')
        self.single_item = Item.objects.create(name='Лопата')

    def test_call_index(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_call_by_auto_slug(self):
        response = self.client.get(f"/items/{self.single_item.slug}/")
        self.assertEqual(response.status_code, 200)

    def test_call_category(self):
        response = self.client.get(f"/category/{self.single_category.slug}/")
        self.assertEqual(response.status_code, 200)

    def test_call_category_with_parent(self):
        response = self.client.get(f"/category/{self.parent_category.slug}/{self.child_category.slug}/")
        self.assertEqual(response.status_code, 200)