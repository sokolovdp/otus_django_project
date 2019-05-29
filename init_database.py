from django.test import TestCase

from main_app.models import ItemModel

from faker import Faker
from faker.providers import company, lorem


class ItemTestCase(TestCase):
    """
        to keep database changes run test with --keepdb options
    """
    def setUp(self):
        fake = Faker('ru_RU')
        fake.add_provider(lorem)
        fake.add_provider(company)

        for i in range(3):
            name = fake.word()
            price = fake.pyint()
            description = fake.text(max_nb_chars=300, ext_word_list=None)
            image_file = f"image_{i}.jpg"
            item = ItemModel.objects.create(
                name=name,
                price=price,
                description=description,
                image=image_file
            )
            print('created:', item.id, item.name, item.price)

    def test_1(self):
        items = ItemModel.objects.all()
        for item in items:
            print('retrieve from db:', item.id, item.name, item.price)
        self.assertEqual(len(items), 3)
        print('--- 1st test passed ---')
