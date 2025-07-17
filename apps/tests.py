import pytest

from apps.models import Category, User
from rest_framework.test import APIClient


class TestCategory:
    @pytest.fixture
    def api_client(self):
        Category.objects.create(name="Book", user_id=1)
        Category.objects.create(name="Texnika", user_id=1)
        Category.objects.create(name="Home", user_id=1)
        Category.objects.create(name="C1", user_id=1)
        Category.objects.create(name="C2", user_id=1)

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
        assert response1.json().get("id") == 6
        assert response2.json().get("name") == ["This field is required."]
        assert response2.status_code == 400

    @pytest.mark.django_db
    def test_category_get_list(self, api_client: APIClient):
        url = 'http://127.0.0.1:8000/api/v1/category/get/list'
        rh = api_client.get(url)
        re = api_client.get(url)

        # Happy Path
        assert rh.status_code == 200
        assert len(rh.json()) == 5

        # Edge Cases
        assert re.status_code != 404

    @pytest.mark.django_db
    def test_category_get(self, api_client: APIClient):
        url = 'http://127.0.0.1:8000/api/v1/category/get/5'
        rh = api_client.get(url)
        re = api_client.get(url)

        # Happy Path
        assert rh.status_code == 200
        assert rh.json().get("id") == 5
        assert rh.json().get("name") == "C2"
        assert rh.json().get("user") == 1
        # Edge Cases
        assert re.status_code != 404
        assert re.json().get("name") != ['No Category matches the given query.']

    @pytest.mark.django_db
    def test_category_update(self, api_client: APIClient):
        url = 'http://127.0.0.1:8000/api/v1/category/update/5'
        rh = api_client.put(url, data={"name" : "Category2", "user" : 1})
        re = api_client.put(url, data={"name" : "Category2", "user" : 0})
        re1= api_client.put(url, data={"name" : "", "user" : 1})

        # Happy Path
        assert rh.status_code == 200
        assert rh.json().get("id") == 5
        assert rh.json().get("name") == "Category2"
        assert rh.json().get("user") == 1
        # Edge Cases re and re1
        # re
        assert re.status_code == 400
        assert re.json().get("name") == ['This category is already exists!']
        assert re.json().get("user") == ['Invalid pk \"0\" - object does not exist.']
        # re1
        assert re1.json().get("name") == ['This field may not be blank.']

    @pytest.mark.django_db
    def test_category_delete(self, api_client: APIClient):
        url = 'http://127.0.0.1:8000/api/v1/category/delete/'
        rh = api_client.delete(url + "5")
        # re = api_client.delete(url) # problem
        re1 = api_client.delete(url + "6")

        # Happy Path
        assert rh.status_code == 204
        # Edge Cases re and re1
        # re
        # assert re.json().get("id") == 1 # the same
        # re1
        assert re1.status_code == 404
