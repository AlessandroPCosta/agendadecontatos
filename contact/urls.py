
from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
    path('contact/<int:contato_id>/detail', views.contato, name='contato'),
    path('contact/create/', views.create, name='create'),

    # contato (CRUD) create/read/update/delete
    # Padronização de urls
    
    #path('contact/<int:contato_id>/update', views.contato, #name='contato'),
    #path('contact/<int:contato_id>/delete', views.contato, name='contato'),
    
]