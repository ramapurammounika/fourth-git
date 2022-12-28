from django.urls import path
from app2.views import *
app_name='something2'
urlpatterns=[
    path('raja/',raja,name='raja'),
    path('prakash/',prakash,name='prakash'),
]