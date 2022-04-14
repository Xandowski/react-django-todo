from django.db import models
from django.urls import reverse_lazy

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=120)
    completed = models.BooleanField(default=False)
    description = models.TextField()

    def _str_(self):
        return self.title

    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
    

    def get_absolute_url(self):
        return reverse_lazy('todo:todo_detail', kwargs={'pk': self.pk })
