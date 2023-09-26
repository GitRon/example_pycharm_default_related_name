# example_pycharm_default_related_name
Example project to prove that the default related name with pycharm is not detected

## Issue 1 (False negative)

> apps/myapp/views.py l.10+
 
## Issue 2 (False positive)

> pip install -r requirements.txt

> manage.py runserver
 
> Navigate to "127.0.0.1:8000"

You'll see the crash of the Django default attribute which PyCharm thinks is fine.
