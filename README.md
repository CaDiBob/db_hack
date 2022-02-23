# Взлом электронного дневника.

Скрипт изменяет оценки, удаляет замечания и добавляет похвалы от учителя для ученика.

Для работы понадобится [этот репозиторий с электронным дневником](https://github.com/devmanorg/e-diary/tree/master). Качаем устанавливаем зависимости командой

```bash
pip install -r requirements.txt
```
## Как запустить:

Все операции проводить в Django shell

### Запуск:
Сначала запускать локальный сервер:

```bash
python manage.py runserver
```
cайт дневника станет доступен по адресу [127.0.0.1:8000](http://127.0.0.1:8000)

затем:

```bash
python manage.py shell
```
Пример запущенной Django shell:

```
(ed) @Python:~/e-diary$ python manage.py shell
Python 3.8.10 (default, Nov 26 2021, 20:14:08) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> 


```

### Скрипт fix_marks.py

Изменяет все плохие оценки ученика т.е двойки и тройки на пятерки.

##### Запуск:

Копируем в папку datacenter, в Django shell импортируем скрипт:

```
>>> from datacenter.fix_marks import fix_marks

```
Затем запускаем, принимает на вход Фамилию и Имя ученика:

```
>>> fix_marks('Иванов Иван')
```
если такого ученика нет в базе оповестит об этом.

### Скрипт remove_chastisements.py

Удаляет все замечания от учителей по данному ученику.

##### Запуск:

Копируем в папку datacenter, в Django shell импортируем скрипт:

```
>>> from datacenter.remove_chastisements import remove_chastisements

```
Затем запускаем, принимает на вход Фамилию и Имя ученика:

```
>>> remove_chastisements('Иванов Иван')
```
если такого ученика нет в базе оповестит об этом.

### Скрипт create_commendation.py

Добавляет одну похвалу от учителей по выбранному предмету для данного ученика.

##### Запуск:

Копируем в папку datacenter, в Django shell импортируем скрипт:

```
>>> from datacenter.create_commendation import create_commendation

```
Затем запускаем, принимает на вход Фамилию и Имя ученика и предмет для которого будет добавлена похвала:

```
>>> create_commendation('Иванов Иван', 'Математика')
```
если такого ученика или предмета нет в базе оповестит об этом.

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).