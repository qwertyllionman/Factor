import pytest

from apps.models import Category, User
from rest_framework.test import APIClient


class TestCategory:
    @pytest.fixture
    def api_client(self):
        Category.objects.create(name="Book", user_id=1)
        Category.objects.create(name="Texnika", user_id=1)
        Category.objects.create(name="Home", user_id=1)

        user = User.objects.create(username="admin")
        user.set_password("1")
        user.save()
        return APIClient()

    @pytest.mark.django_db
    def test_category_create(self, api_client: APIClient):
        url = 'http://127.0.0.1:8000/api/v1/category/create'
        response1 = api_client.post(url, data={"name": "Technic", "user" : 1})
        response2 = api_client.post(url)

        assert response1.status_code == 201
        assert response1.json().get("id") == 4
        assert response2.json().get("name") == ["This field is required."]
        assert response2.status_code == 400

