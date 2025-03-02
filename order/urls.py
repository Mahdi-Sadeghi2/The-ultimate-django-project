from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('signup/', views.sign_up, name="signup"),
    path('login/', views.login_view, name="login"),
    path('password/', views.change_password, name="password"),
    path('profile/', views.change_profile, name="profile"),
    path('delete_account/', views.delete_account, name="delete_account"),
    path('signout/', views.sign_out, name="signout"),
    path('cookie/', views.cookie_page, name="cookie"),
    path('add_cookie/', views.create_cookies, name="add_cookie"),
    path('clear_cookies/', views.clear_cookies, name="clear_cookies"),
    path('read_cookie/<str:cookie_name>/', views.read_cookies, name="read_cookie"),
    path('delete_cookie/<str:cookie_name>/', views.delete_cookie, name="delete_cookie"),
    path('session_data/', views.session_page, name="session_data"),
    path('add_session/', views.add_session, name="add_session"),
    path('clear_sessions/', views.clear_sessions, name="clear_sessions"),
    path('read_session/<str:session_key>/', views.read_sessions, name="read_session"),
     path('delete_session/<str:session_key>/', views.delete_session, name="delete_session"),
]
