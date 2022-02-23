from datacenter.models import Schoolkid, Chastisement


def remove_chastisements(name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=name)
    except Schoolkid.DoesNotExist:
        return 'Нет такого ученика!'
    except Schoolkid.MultipleObjectsReturned:
        return 'Нужно ввести Фамилию и Имя'
    reprimands = Chastisement.objects.filter(schoolkid=schoolkid)
    reprimands.delete()
