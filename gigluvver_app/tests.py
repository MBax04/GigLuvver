from django.test import TestCase
from django.urls import reverse
from gigluvver_app import urls

class PageResponseTests(TestCase):
    def test_response(self):
        for url in urls.urlpatterns:
            response = self.client.get(reverse(f"gigluvver_app:{url.name}"))
            print(f"Fetching {url.name}")
            self.assertEquals(response.status_code, 200, f"Failed to retrieve {url.name}.")

class PageLinkLoginTests(TestCase):
    pass