from datacenter.models import Schoolkid


def get_schoolkid(name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=name)
        return schoolkid
    except Schoolkid.DoesNotExist:
        'Нет такого ученика!'
    except Schoolkid.MultipleObjectsReturned:
        'Нужно ввести Фамилию и Имя'