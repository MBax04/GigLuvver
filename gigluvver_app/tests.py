import tempfile
from django.test import TestCase
from django.urls import reverse, path
from gigluvver_app import urls,test_resources,views, models
import datetime
from django.core.files.uploadedfile import SimpleUploadedFile

class PageResponseTests(TestCase):
    def test_response(self):
        for url in urls.urlpatterns:
            if url.name in test_resources.links['non_log_in']:
                response = self.client.get(reverse(f"gigluvver_app:{url.name}"))
                self.assertEquals(response.status_code, 200, f"{test_resources.HEADER_FOOTER}Failed to retrieve {url.name}.{test_resources.HEADER_FOOTER}")

class PageLinkLoginTests(TestCase):
    def test_links(self):
        for url in urls.urlpatterns:
            if url.name != "gig" and url.name != "my_tickets" and url.name != "success_page":
                response = self.client.get(reverse(f"gigluvver_app:{url.name}"))
                if url.name in test_resources.links['non_log_in'].keys():
                    for link in test_resources.links['non_log_in'][url.name]:
                        self.assertContains(response, f'<a class="nav-link" href="{reverse(f"gigluvver_app:{link}")}">',
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

class LogInAndGigTests(TestCase):
    def test_create_account_user(self):
        self.create_account_user()

    def create_account_user(self):
        response = self.client.post(reverse("gigluvver_app:create_user_account"), data={'username':'testing_user',
                                                             'email':'testing@gmail.com',
                                                             'password':'12345',
                                                             'ProfilePicture': tempfile.NamedTemporaryFile(suffix=".jpg").name})
        self.assertContains(response, "<p>Account successfully created!</p>", msg_prefix=f"{test_resources.HEADER_FOOTER}Could not create user account.{test_resources.HEADER_FOOTER}")
        self.log_in_user()

    def log_in_user(self):
        response = self.client.post(reverse("gigluvver_app:log_in"), data={'username':'testing_user',
                                                                            'password':'12345'})
        self.assertEquals(response.status_code, 302, msg="Could not log in as user.")

    def test_create_account_artist(self):
        self.create_account_artist()

    def create_account_artist(self):
        response = self.client.post(reverse("gigluvver_app:create_artist_account"), data={'username':'testing_artist',
                                                                                            'password':'12345',
                                                                                            'email':'artist@gmail.com',
                                                                                            'StageName':'Testing Artist',
                                                                                            'Genre':'Test',
                                                                                            'ProfilePicture':tempfile.NamedTemporaryFile(suffix=".jpg").name})
        self.assertContains(response, "<p>Account successfully created!</p>", msg_prefix=f"{test_resources.HEADER_FOOTER}Could not create artist account.{test_resources.HEADER_FOOTER}")
        self.log_in_artist()

    def log_in_artist(self):
        response = self.client.post(reverse("gigluvver_app:artist_log_in"), data={'username':'testing_artist',
                                                                                  'password':'12345'})
        self.assertEquals(response.status_code, 302, msg="Could not log in as artist.")

    def create_venue(self):
        models.Venue.objects.create(VenueName='Hydro', Location='Exhibition Way, Stobcross Rd, Glasgow G3 8YW', Position='55.8597412109375,-4.285629749298096')

    def test_create_gig_invalid(self):
        self.create_account_artist()
        self.create_venue()
        response = self.client.post(reverse("gigluvver_app:create_gig"), data={'GigName':'New Gig',
                                                                               'Date':datetime.date(2024, 10, 27),
                                                                               'Time':datetime.time(22,00),
                                                                               'Venue':'1'})
        self.assertContains(response, "<p>Please provide a gig picture.</p>", msg_prefix="New gig form invalidity not acknowledged.")

    def test_create_gig_valid(self):
        self.create_account_artist()
        self.create_venue()
        response = self.client.get(reverse("gigluvver_app:create_gig"))
        response = self.client.post(reverse("gigluvver_app:create_gig"), data={'GigName':'New Gig',
                                                                               'Date':datetime.date(2024, 10, 27),
                                                                               'Time':datetime.time(22,00),
                                                                               'Venue':'1',
                                                                         'GigPicture':SimpleUploadedFile(name="test.png", content=open("./media/profile_images/test_image.png", 'rb').read(), content_type='image/jpeg')})
        self.assertEquals(response.status_code, 302, msg="New gig not created.")
        self.access_new_gig()
    
    def access_new_gig(self):
        response = self.client.get(reverse("gigluvver_app:my_gigs"))
        self.assertContains(response, 'New Gig', msg_prefix="New gig not showing on my gigs page.")
        self.assertContains(response, '<img src="/media/gig_images/test.png"', msg_prefix="New gig image not showing on my gigs page.")
