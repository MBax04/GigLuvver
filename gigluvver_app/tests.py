from django.test import TestCase
from django.urls import reverse, path
from gigluvver_app import urls,test_resources,views

class PageResponseTests(TestCase):
    def test_response(self):
        for url in urls.urlpatterns:
            if url.name in test_resources.links['non_log_in']:
                response = self.client.get(reverse(f"gigluvver_app:{url.name}"))
                self.assertEquals(response.status_code, 200, f"{test_resources.HEADER_FOOTER}Failed to retrieve {url.name}.{test_resources.HEADER_FOOTER}")

class PageLinkLoginTests(TestCase):
    def test_links(self):
        for url in urls.urlpatterns:
            if url.name != "gig" and url.name != "my_tickets":
                response = self.client.get(reverse(f"gigluvver_app:{url.name}"))
                if url.name in test_resources.links['non_log_in'].keys():
                    for link in test_resources.links['non_log_in'][url.name]:
                        self.assertContains(response, f'<a href="{reverse(f"gigluvver_app:{link}")}">',
                                            msg_prefix=f"{test_resources.HEADER_FOOTER}The {url.name} page is missing a {link} link.{test_resources.HEADER_FOOTER}")

class AuthenticationTests(TestCase):
    def test_create_artist_get(self):
        test_resources.test_create_get(self,'create_artist_account', test_resources.create_artist_fields)
    
    def test_create_user_get(self):
        test_resources.test_create_get(self,'create_user_account', test_resources.create_user_fields)

    
    def test_blank_create_user_post(self):
        test_resources.test_blank_create_post(self,'create_user_account')

    def test_blank_create_artist_post(self):
        test_resources.test_blank_create_post(self,'create_artist_account')

class LogInTests(TestCase):
    def create_account_user(self):
        response = self.client.post("create_account/", data={'username':'testing_user','password':'12345'})
        self.assertEquals(response.status_code, 302, msg_prefix=f"{test_resources.HEADER_FOOTER}Could not create user account.{test_resources.HEADER_FOOTER}")

    def create_account_artist(self):
        response = self.client.post("create_artist_account/", data={'username':'testing_artist',
                                                                    'password':'12345',
                                                                    'StageName':'Testing Artist',
                                                                    'Genre':'Test',
                                                                    'ProfilePicture':'media\profile_images\test_image.png'})
        self.assertEquals(response.status_code, 302, msg_prefix=f"{test_resources.HEADER_FOOTER}Could not create artist account.{test_resources.HEADER_FOOTER}")

    def log_in_user(self):
        response = self.client.post("log_in/", data={'username':'testing_user',
                                                     'password':'12345'})
        self.assertEquals(response.status_code, 302, msg_prefix="Could not log in as user.")

    def log_in_artist(self):
        response = self.client.post("artist_log_in/", data={'username':'testing_artist',
                                                     'password':'12345'})
        self.assertEquals(response.status_code, 302, msg_prefix="Could not log in as artist.")