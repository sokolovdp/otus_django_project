from django.test import TestCase

from main_app.models import ItemModel

from faker import Faker
from faker.providers import company, lorem


class AnimalTestCase(TestCase):
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
            print(item)
