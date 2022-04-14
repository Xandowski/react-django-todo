from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('backend.todo.urls', namespace='todo')),
    path('admin/', admin.site.urls),
]
