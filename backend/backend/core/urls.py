from django.urls import include, path
from rest_framework import routers

from .views import index

app_name = 'core'

# router = routers.DefaultRouter()
# router.register(r'core', views.TodoView, 'core')

urlpatterns = [
    path('', index, name='index'),
]
