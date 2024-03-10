from django.urls import path
from gigluvver_app import views

app_name = "gigluvver_app"

urlpatterns = [
    path('', views.home, name = 'home'),
    path('log_in/', views.log_in, name = 'log_in'),
    path('my_tickets/', views.my_tickets, name = 'my_tickets'),
    path('user_profile/', views.user_profile, name = 'user_profile'),
    path('create_account/', views.create_account, name = 'create_account'),
    path('create_user_account/', views.create_user_account, name = 'create_user_account'),
    path('create_artist_account/', views.create_artist_account, name = 'create_artist_account'),
    path('artist_log_in/', views.artist_log_in, name = 'artist_log_in'),
    path('my_gigs/', views.my_gigs, name = 'my_gigs'),
    path('artist_profile/', views.artist_profile, name = 'artist_profile'),
    path('gigs/', views.gigs, name = 'gigs'),
    path('gig/', views.gig, name = 'gig'),
    path('map/', views.map, name = 'map'),
    path('log_out/', views.log_out, name='log_out')
]