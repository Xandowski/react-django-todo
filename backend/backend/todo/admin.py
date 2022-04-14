from backend.todo.models import Todo
from django.contrib import admin


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'completed')
    search_fields = ('title',)
    list_filter = ('completed',)
    # date_hierarchy = 'title'
