from decimal import Decimal

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

import pytest

from churchill.tests.factories.profiles import ProfileDictFactory
from churchill.tests.factories.users import UserFactory


@pytest.mark.django_db
class TestProfilesView:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.client = APIClient()
        self.url = reverse("api:v1:profiles:profiles")
        self.user = UserFactory()
        self.profile_data = ProfileDictFactory()

    def test_anonymous_user(self):
        response = self.client.get(self.url, format="json")
        assert response.status_code == status.HTTP_403_FORBIDDEN

    @pytest.mark.parametrize("method", ["post", "delete"])
    def test_not_allowed_methods(self, method):
        self.client.force_authenticate(self.user)
        test_client_callable = getattr(self.client, method)
        response = test_client_callable(self.url, format="json")
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_retrieve_personal_data(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(self.url, format="json")

        assert response.status_code == status.HTTP_200_OK
        assert response.data["email"] == self.user.email
        assert response.data["language"] == self.user.profile.language
        assert response.data["currency"] == self.user.profile.currency.iso3
        assert response.data["avg_consumption"] == self.user.profile.avg_consumption
        assert Decimal(response.data["avg_price"]) == self.user.profile.avg_price

    def test_update_personal_data(self):
        self.client.force_authenticate(self.user)
        response = self.client.patch(self.url, self.profile_data, format="json")

        assert response.status_code == status.HTTP_200_OK
        assert response.data["language"] == self.profile_data["language"]
        assert response.data["currency"] == self.profile_data["currency"]
        assert response.data["avg_consumption"] == self.profile_data["avg_consumption"]
        assert Decimal(response.data["avg_price"]) == self.profile_data["avg_price"]
