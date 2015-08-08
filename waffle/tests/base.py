
import django
from django import test
from django.core import cache


class TestCase(test.TransactionTestCase):

    def _pre_setup(self):
        cache.cache.clear()
        super(TestCase, self)._pre_setup()

IS_DJANGO_18 = django.VERSION[0] == 1 and django.VERSION[1] == 8
