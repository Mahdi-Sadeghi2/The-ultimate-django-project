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
    path('model/', views.pass_model, name='model'),
    path('filtrs/', views.buitlt_in_filters, name='filters'),
    path('customfilters/', views.custom_filter, name='customfilters'),
    path('test/', views.test_static, name='test'),
    path('list/', views.employee_list, name='list'),
    path('list/<int:id>/', views.employee_details, name='detail'),
    path('delete/<int:id>/', views.employee_delete, name='delete'),
    path('edit/<int:id>/', views.employee_update, name='edit'),
    path('create/', views.employee_insert, name='create'),
]
