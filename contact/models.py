from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    #Classe meta para alterar o nome entre singular e plural la no menu admin
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    nome = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.nome

class Contact(models.Model):
    nome = models.CharField('Nome', max_length=50)
    sobrenome = models.CharField('Sobrenome', max_length=50,  blank=True)
    phone = models.CharField('Phone', max_length=50)
    email = models.EmailField('E-mail', max_length=250, blank=True)
    create_data = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    mostrar = models.BooleanField(default=True)
    imagem = models.ImageField(blank=True, upload_to='imagens/%y/%m/')
    categoria = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True, null=True
        )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True 
    )


    def __str__(self) -> str:
        return f'{self.nome} {self.sobrenome}'

