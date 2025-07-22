mig:
	python manage.py makemigrations
	python manage.py migrate
run:
	python manage.py runserver
admin:
	python manage.py createsuperuser
socket:
	daphne -b 0.0.0.0 -p 8080 Factor.asgi:application