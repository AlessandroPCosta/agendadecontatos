from django.db import models
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
    nome = models.CharField('Nome', max_length=50)
    sobrenome = models.CharField('Sobrenome', max_length=50,  blank=True)
    phone = models.CharField('Phone', max_length=50)
    email = models.EmailField('E-mail', max_length=250, blank=True)
    create_data = models.DateTimeField(default=timezone.now)
    descrição = models.TextField(blank=True)
    mostrar = models.BooleanField(default=True)
    imagem = models.ImageField(blank=True, upload_to='imagens/%y/%m/')


    def __str__(self) -> str:
        return f'{self.nome} {self.sobrenome}'

