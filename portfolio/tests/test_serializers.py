import pytest

from portfolio.serializers import PortfolioSerializer


@pytest.mark.django_db
def test_PortfolioSerializer__success(user):
    data = {"user": user.id, "name": "some_name"}
    serializer = PortfolioSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    expected_result = {"user": user, "name": "some_name"}
    assert serializer.validated_data == expected_result


@pytest.mark.django_db
def test_PortfolioSerializer__invaild_data(user):
    data = {"user": user.id, "name": ["some", "name"]}
    serializer = PortfolioSerializer(data=data)
    serializer.is_valid()
    assert "name" in serializer.errors.keys()


@pytest.mark.django_db
def test_PortfolioSerializer__empty_data(user):
    data = {}
    serializer = PortfolioSerializer(data=data)
    serializer.is_valid()
    assert "name" in serializer.errors.keys()
    assert "user" in serializer.errors.keys()
