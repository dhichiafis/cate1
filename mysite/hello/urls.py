from django.urls import path
from . import views
app_name='hello'
urlpatterns=[
    path('hello/',views.hello,name='hello'),
    path('again/',views.again,name='again')
]