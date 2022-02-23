import random

from datacenter.models import Schoolkid, Lesson, Subject, Commendation


def create_commendation(name, subject_title):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=name)
    except Schoolkid.DoesNotExist:
        return 'Нет такого ученика!'
    except Schoolkid.MultipleObjectsReturned:
        return 'Нужно ввести Фамилию и Имя'
    try:
        lesson_title = Subject.objects.filter(
            title=subject_title,
            year_of_study=6
            ).get()
    except Subject.DoesNotExist:
        return 'Нет такого предмета!'

    text_commendation=[
        'Молодец!',
        'Отлично!',
        'Хорошо!',
        'Гораздо лучше, чем я ожидал!',
        'Ты меня приятно удивил!',
        'Великолепно!',
        'Прекрасно!',
        'Ты меня очень обрадовал!',
        'Именно этого я давно ждал от тебя!',
        'Сказано здорово – просто и ясно!',
        'Ты, как всегда, точен!',
        'Очень хороший ответ!',
        'Талантливо!',
        'Ты сегодня прыгнул выше головы!',
        'Я поражен!',
        'Уже существенно лучше!',
        'Потрясающе!',
        'Замечательно!',
        'Прекрасное начало!',
        'Так держать!',
        'Ты на верном пути!',
        'Здорово!',
        'Это как раз то, что нужно!',
        'Я тобой горжусь!',
        'С каждым разом у тебя получается всё лучше!',
        'Мы с тобой не зря поработали!',
        'Я вижу, как ты стараешься!',
        'Ты растешь над собой!',
        'Ты многое сделал, я это вижу!',
        'Теперь у тебя точно все получится!',
    ]

    lesson = Lesson.objects.filter(
        subject=lesson_title,
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        ).order_by('?').first()

    commendation = Commendation.objects.create(
        text=random.choice(text_commendation),
        created=lesson.date,
        schoolkid=schoolkid,
        teacher=lesson.teacher
        )
    commendation.save()
