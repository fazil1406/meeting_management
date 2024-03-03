from django.urls import path
from . import views
app_name='book'
urlpatterns=[
    path('meeting',views.meeting,name='meeting')
]