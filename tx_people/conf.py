# Import here to ensure AppConf is always loaded properly
from django.conf import settings

from appconf import AppConf


class PeopleAppConf(AppConf):
    UPLOAD_TO = 'tx_people/'

    class Meta:
        prefix = 'tx_people'
