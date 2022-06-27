from django.urls import reverse
import pytest


@pytest.mark.django_db
def test_PortfolioViewSet_get__portfolio_absence(api_client):
    endpoint = reverse("portfolio-list")
    response = api_client().get(endpoint)

    assert response.status_code == 200
    assert response.data == []


@pytest.mark.django_db
def test_PortfolioViewSet_get__success(api_client, portfolio):
    endpoint = reverse("portfolio-list")
    response = api_client().get(endpoint)

    assert response.status_code == 200

    endpoint_portfolio = response.data[0]

    assert endpoint_portfolio["user"] == portfolio.user.id
    assert endpoint_portfolio["id"] == portfolio.id
    assert endpoint_portfolio["name"] == portfolio.name


@pytest.mark.django_db
def test_PortfolioViewSet_post__required_fields_absence(api_client):
    endpoint = reverse("portfolio-list")
    data = {"invalid_field_1": 1, "invalid_field_2": "invalid_data"}
    response = api_client().post(endpoint, data=data)

    assert response.status_code == 400
    assert "user" in response.data.keys()
    assert "name" in response.data.keys()


@pytest.mark.django_db
def test_PortfolioViewSet_post__invalid_data(api_client):
    endpoint = reverse("portfolio-list")
    data = {"name": "some_name", "user": "some_user"}
    response = api_client().post(endpoint, data=data)
    expected_result = {"user": ["Incorrect type. Expected pk value, received str."]}

    assert response.status_code == 400
    assert response.data == expected_result


@pytest.mark.django_db
def test_PortfolioViewSet_post__null_data(api_client):
    endpoint = reverse("portfolio-list")
    data = {"name": "some_name", "user": ""}
    response = api_client().post(endpoint, data=data)
    expected_result = {"user": ["This field may not be null."]}

    assert response.status_code == 400
    assert response.data == expected_result


@pytest.mark.django_db
def test_PortfolioViewSet_post__success(api_client, user):
    endpoint = reverse("portfolio-list")
    data = {"name": "some_name", "user": user.id}
    response = api_client().post(endpoint, data=data)

    assert response.status_code == 201
    assert response.data["name"] == data["name"]
    assert response.data["user"] == data["user"]


@pytest.mark.django_db
def test_PortfolioViewSet_portfolio_get__success(api_client, portfolio):
    endpoint = reverse("portfolio-detail", args=(portfolio.id,))
    response = api_client().get(endpoint)

    assert response.status_code == 200
    assert response.data["name"] == portfolio.name
    assert response.data["id"] == portfolio.id
    assert response.data["user"] == portfolio.user.id


@pytest.mark.django_db
def test_PortfolioViewSet_portfolio_put__success(api_client, portfolio):
    endpoint = reverse("portfolio-detail", args=(portfolio.id,))
    data = {"id": 1, "name": "updated_name", "user": portfolio.user.id}
    response = api_client().put(endpoint, data=data)

    assert response.status_code == 200
    assert response.data["name"] == "updated_name"


@pytest.mark.django_db
def test_PortfolioViewSet_stock_symbols__get(api_client, portfolio):
    endpoint = reverse("portfolio-stock-symbols", args=(portfolio.id,))
    response = api_client().get(endpoint)
    assert response.status_code == 200


@pytest.mark.django_db
def test_PortfolioViewSet_stock_symbols_post__success(
    api_client, portfolio, apple_stock
):
    endpoint = reverse("portfolio-stock-symbols", args=(portfolio.id,))
    data = {"stock_symbols": ["AAPL"]}
    response = api_client().post(endpoint, data)

    assert response.status_code == 200


@pytest.mark.django_db
def test_PortfolioViewSet_stock_symbols_post__wrong_symbols(
    api_client, portfolio, apple_stock
):
    endpoint = reverse("portfolio-stock-symbols", args=(portfolio.id,))
    data = {"stock_symbols": ["SOME", "SYMBOLS"]}
    response = api_client().post(endpoint, data)

    assert response.status_code == 400
    assert "stock_symbols" in response.data.keys()
