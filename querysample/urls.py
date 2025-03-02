from django.urls import path

from .views import drop_down_list, load_cities, load_states 

urlpatterns = [
    path('ajax/',drop_down_list,name='ajax' ),
    path('state/',load_states,name='state' ),
    path('city/',load_cities,name='city' ),
]
