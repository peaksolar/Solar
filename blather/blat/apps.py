from django.apps import AppConfig
from suit.apps import DjangoSuitConfig


class BlatConfig(AppConfig):
    name = 'blat'


class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'
