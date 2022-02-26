from datacenter.models import Mark
from datacenter.get_schoolkid import get_schoolkid

def fix_marks(name):
    schoolkid = get_schoolkid(name)
    marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2,3])
    for mark in marks:
        mark.points = 5
        mark.save()