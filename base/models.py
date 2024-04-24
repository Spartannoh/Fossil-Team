from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    usuário = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    título = models.CharField(max_length=200, null=True, blank=True)
    descrição = models.TextField(null=True, blank=True)
    completa = models.BooleanField(default=False)
    criar = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.título:
            return self.título
        else:
            return "Tarefa Sem Título"
    
    class Meta:
        ordering = ['completa']
