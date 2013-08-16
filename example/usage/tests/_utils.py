"""Random utilities needed throughout the test suite"""
import random


class RandomDatesMixin(object):
    @property
    def random_year(self):
        return '{0}'.format(random.randint(1000, 3000))

    @property
    def random_month(self):
        return '{0:02d}'.format(random.randint(1, 12))

    @property
    def random_day(self):
        # Avoid possible issues with February dates by only going to 28
        return '{0:02d}'.format(random.randint(1, 28))
