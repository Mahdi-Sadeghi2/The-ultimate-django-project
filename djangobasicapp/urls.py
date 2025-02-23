from django.urls import path

from . import views 


urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('messages/', views.more_messages, name='messages'),
    path('var/', views.use_variables_ass_resppnse, name='var'),
    path('get/', views.get_request_variables, name='get'),
    path('time/', views.show_time, name='time'),
    path('data/', views.if_tag_demo,name='data'),
    path('product/', views.show_products,name='product'),
    # path('show/', views.load_users,name='show'),
    path('show/', views.load_users2,name='show'),
    path('index/', views.index,name='index'),
    path('userdetail/', views.load_user_details,name='userdetail'),
]
