from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('<int:contato_id>/', views.contato, name='contato'),
    path('', views.index, name='index'),
]