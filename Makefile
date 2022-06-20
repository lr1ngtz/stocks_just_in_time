makemigrations:
	docker-compose run web python manage.py makemigrations

migrate:
	docker-compose run web python manage.py migrate

create_or_update_stocks:
	docker-compose run web python manage.py create_or_update_stocks

create_quote $(QUOTE):
	docker-compose run web python manage.py create_quote $(QUOTE)
