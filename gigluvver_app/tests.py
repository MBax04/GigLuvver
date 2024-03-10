from django.test import TestCase
from django.urls import reverse
from gigluvver_app import urls

class PageResponseTests(TestCase):
    def test_response(self):
        for url in urls.urlpatterns:
            response = self.client.get(reverse(f"gigluvver_app:{url.name}"))
            print(f"Fetching {url.name}")
            self.assertEquals(response.status_code, 200, f"Failed to retrieve {url.name}.")

general_links = ['home','log_in','artist_log_in','gigs']
log_in_links = ['home','my_tickets','sign_out','user_profile','gigs']
log_in_artist_links = ['home','my_tickets','sign_out','artist_profile','gigs']

links = {'home':general_links,
         'log_in':general_links,
         'my_tickets':log_in_links,
         'user_profile':log_in_links,
         'create_account':general_links,
         'create_user_account':general_links,
         'create_artist_account':general_links,
         'artist_log_in':general_links,
         'my_gigs':log_in_artist_links,
         'artist_profile':log_in_artist_links,
         'gigs':general_links,
         'gig':general_links,
         'map':general_links}

class PageLinkLoginTests(TestCase):
    def test_links(self):
        for url in urls.urlpatterns:
            response = self.client.get(reverse(f"gigluvver_app:{url.name}"))
            print(f"Fetching {url.name}: ", end="")
            for link in links[url.name]:
                self.assertContains(response, f'<a href="{reverse(f"gigluvver_app:{link}")}">', msg_prefix=f"The {url.name} page is missing a {link} link.")