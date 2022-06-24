import pytest

from portfolio.tests.utils import json_deserialize


@pytest.mark.django_db
def test_PortfolioViewSet_get__portfolio_absence(api_client):
    endpoint = "/portfolios/"
    response = api_client().get(endpoint)

    assert response.status_code == 200
    assert response.data == []


@pytest.mark.django_db
def test_PortfolioViewSet_get__success(api_client, portfolio):
    endpoint = "/portfolios/"
    response = api_client().get(endpoint)

    assert response.status_code == 200

    endpoint_portfolio = response.data[0]

    assert endpoint_portfolio["user"] == portfolio.user.id
    assert endpoint_portfolio["id"] == portfolio.id
    assert endpoint_portfolio["name"] == portfolio.name


@pytest.mark.django_db
def test_PortfolioViewSet_post__required_fields_absence(api_client):
    endpoint = "/portfolios/"
    data = json_deserialize("portfolio__required_fields_absence.json")
    response = api_client().post(endpoint, data=data)
    expected_result = json_deserialize(
        "portfolio__required_fields_absence_response.json"
    )

    assert response.status_code == 400
    assert response.data == expected_result


@pytest.mark.django_db
def test_PortfolioViewSet_post__invalid_data(api_client):
    endpoint = "/portfolios/"
    data = json_deserialize("portfolio__invalid_data.json")
    response = api_client().post(endpoint, data=data)
    expected_result = json_deserialize("portfolio__invalid_data_response.json")

    assert response.status_code == 400
    assert response.data == expected_result


@pytest.mark.django_db
def test_PortfolioViewSet_post__null_data(api_client):
    endpoint = "/portfolios/"
    data = json_deserialize("portfolio__null_data.json")
    response = api_client().post(endpoint, data=data)
    expected_result = json_deserialize("portfolio__null_data_response.json")

    assert response.status_code == 400
    assert response.data == expected_result


@pytest.mark.django_db
def test_PortfolioViewSet_post__success(api_client, user):
    endpoint = "/portfolios/"
    data = json_deserialize("portfolio__success.json")
    data["user"] = user.id
    response = api_client().post(endpoint, data=data)

    assert response.status_code == 201
    assert response.data["name"] == data["name"]
    assert response.data["user"] == data["user"]


@pytest.mark.django_db
def test_PortfolioViewSet_portfolio_get__success(api_client, portfolio):
    endpoint = "/portfolios/" + str(portfolio.id) + "/"
    response = api_client().get(endpoint)

    assert response.status_code == 200
    assert response.data["name"] == portfolio.name
    assert response.data["id"] == portfolio.id
    assert response.data["user"] == portfolio.user.id


@pytest.mark.django_db
def test_PortfolioViewSet_portfolio_put__success(api_client, portfolio):
    endpoint = "/portfolios/" + str(portfolio.id) + "/"
    data = json_deserialize("portfolio_put__success.json")
    data["user"] = portfolio.user.id
    response = api_client().put(endpoint, data=data)

    assert response.status_code == 200
    assert response.data["name"] == "updated_name"
