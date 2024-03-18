from django.urls import reverse

HEADER_FOOTER = "\n----------------------------------\n"

general_links = ['home','gigs']
log_in_links = ['home','my_tickets','user_profile','gigs']
log_in_artist_links = ['home','my_tickets','artist_profile','gigs']

links = {'non_log_in':{ 'home':general_links,
                        'log_in':general_links,
                        'create_user_account':general_links,
                        'create_artist_account':general_links,
                        'artist_log_in':general_links,
                        'gigs':general_links,},
        'log_in':     { 'my_tickets':log_in_links,
                        'user_profile':log_in_links,
                        'my_gigs':log_in_artist_links,
                        'artist_profile':log_in_artist_links,}}

create_user_fields = [('username','Username','text'),
                      ('email','Email address'),
                      ('password','Password')]


create_artist_fields = [('username','Username','text'),
                        ('email','Email address'),
                        ('password','Password'),
                        ('StageName','StageName','text'),
                        ('Genre','Genre','text'),
                        ('ProfilePicture','ProfilePicture', 'file')]

def test_create_get(self, page, create_fields):
    request = self.client.get(reverse(f'gigluvver_app:{page}'))
    content = request.content.decode('utf-8')

    for tuple in create_fields:
        self.assertTrue(f'<label for="id_{tuple[0]}">{tuple[1]}:</label>' in content, f"{HEADER_FOOTER}Missing {tuple[1]} label in {page}.{HEADER_FOOTER}")
        if len(tuple) == 3:
            type = tuple[2]
        else:
            type = tuple[0]
        self.assertTrue(f'<input type="{type}" name="{tuple[0]}"' in content, f"{HEADER_FOOTER}Missing {tuple[1]} input in {page}.{HEADER_FOOTER}")

def test_blank_create_post(self, page):
        request = self.client.post(reverse(f'gigluvver_app:{page}'))
        content = request.content.decode('utf-8')

        self.assertTrue('<ul class="errorlist">' in content, "Blank entries accepted in {page} form.")