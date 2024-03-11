from django.test import TestCase
from django.urls import reverse
from gigluvver_app import urls,test_resources

class PageResponseTests(TestCase):
    def test_response(self):
        for url in urls.urlpatterns:
            response = self.client.get(reverse(f"gigluvver_app:{url.name}"))
            self.assertEquals(response.status_code, 200, f"{test_resources.HEADER_FOOTER}Failed to retrieve {url.name}.{test_resources.HEADER_FOOTER}")

class PageLinkLoginTests(TestCase):
    def test_links(self):
        for url in urls.urlpatterns:
            response = self.client.get(reverse(f"gigluvver_app:{url.name}"))
            for link in test_resources.links[url.name]:
                self.assertContains(response, f'<a href="{reverse(f"gigluvver_app:{link}")}">', msg_prefix=f"{test_resources.HEADER_FOOTER}The {url.name} page is missing a {link} link.{test_resources.HEADER_FOOTER}")

class AuthenticationTests(TestCase):
    def test_create_artist_get(self):
        test_resources.test_create_get(self,'create_artist_account', test_resources.create_artist_fields)
    
    def test_create_user_get(self):
        test_resources.test_create_get(self,'create_user_account', test_resources.create_user_fields)

    
    def test_blank_create_user_post(self):
        test_resources.test_blank_create_post(self,'create_user_account')

    def test_blank_create_artist_post(self):
        test_resources.test_blank_create_post(self,'create_artist_account')
