mig:
	python manage.py makemigrations
	python manage.py migrate
run:
	python manage.py runserver
admin:
	python manage.py createsuperuser
