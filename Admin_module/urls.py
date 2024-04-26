from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.ProjectHomePage, name='ProjectHomePage'),
    path('EventManagerHomePage', views.EventManagerHomePage, name='EventManagerHomePage'),
    path('EventParticipantHomePage', views.EventParticipantHomePage, name='EventParticipantHomePage'),
    path('signup', views.Signup, name='signup'),
    path('signup1', views.signup1, name='signup1'),
    path('login', views.login, name='login'),
    path('login1', views.login1, name='login1'),
    path('logout', views.logout, name='logout'),
    path('account_details', views.account_details, name='account_details'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('AboutUs', views.AboutUs, name='AboutUs'),
    path('OurServices', views.OurServices, name='OurServices'),
    path('ContactUs', views.ContactUs, name='ContactUs'),
    path('Gallery', views.Gallery, name='Gallery'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

]
