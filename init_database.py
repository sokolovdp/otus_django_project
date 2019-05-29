import os
from django.conf import settings
from django.test.runner import DiscoverRunner

from main_app.models import ItemModel
from otus_django_project import settings

from faker import Faker
from faker.providers import company, lorem


class SimpleRunner(DiscoverRunner):
    def __init__(self, *args, **kwargs):
        settings.IN_TEST_MODE = True
        super().__init__(*args, **kwargs)

    def setup_databases(self, **kwargs):
        fake = Faker('ru_RU')
        fake.add_provider(lorem)
        fake.add_provider(company)

        for i in range(3):
            name = fake.word()
            price = fake.pyint()
            description = fake.text(max_nb_chars=300, ext_word_list=None)
            image_file = f"image_{i}.jpg"
            item = ItemModel(name, price, description, image_file)
            item.save_to_db()
            print(item)

    def teardown_databases(self, old_config, **kwargs):
        pass
