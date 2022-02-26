from datacenter.models import Chastisement
from datacenter.get_schoolkid import get_schoolkid


def remove_chastisements(name):
    schoolkid = get_schoolkid(name)
    reprimands = Chastisement.objects.filter(schoolkid=schoolkid)
    reprimands.delete()
