from datacenter.models import Schoolkid, Mark


def fix_marks(name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=name)
    except Schoolkid.DoesNotExist:
        return 'Нет такого ученика!'
    except Schoolkid.MultipleObjectsReturned:
        return 'Нужно ввести Фамилию и Имя'

    marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    for mark in marks:
        mark.points = 5
        mark.save()
