makemigrations:
	docker-compose run web python manage.py makemigrations

migrate:
	docker-compose run web python manage.py migrate

update_stocks:
	docker-compose run web python manage.py update_stocks
