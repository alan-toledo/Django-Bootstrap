# Django-Bootstrap

ToDo App with Django + Bootstrap 4

# Installation
```bash
virtualenv myenv
```
```bash
.\myenv\Scripts\activate (from Windows)
```
```bash
pip install -r requirements.txt
```
# Migrations
```bash
python manage.py makemigrations app (which is responsible for creating new migrations based on the changes you have made to your models)
```
```bash
python manage.py migrate --fake app zero
```
```bash
python manage.py migrate (which is responsible for applying and unapplying migrations)
```
```bash
python manage.py loaddata .\app\fixtures\dumpdata.json
```
# Execution
```bash
python manage.py runserver
```

![Screenshot](ToDo\login.png)

![Screenshot](ToDo\taks.png)


# Testing
```bash
coverage run manage.py test -v 2
```
```bash
coverage html 
```
```bash
coverage report
```
```bash
Name               Stmts   Miss  Cover
--------------------------------------
ToDo\__init__.py       0      0   100%
ToDo\settings.py      21      0   100%
ToDo\urls.py           3      0   100%
app\__init__.py        0      0   100%
app\admin.py           6      0   100%
app\apps.py            4      0   100%
app\forms.py          13      0   100%
app\models.py         22      0   100%
app\urls.py            3      0   100%
app\views.py          75      0   100%
--------------------------------------
TOTAL                147      0   100%
```