from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import Http404

from contact.models import Contact

# Create your views here.
def index(request):
    contacts = Contact.objects\
        .filter(mostrar=True)\
        .order_by('-id')
    
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    

    context = {
        'page_obj' : page_obj,
        'site_title' : 'Contatos - '
    }
    return render(
        request,
        'contact/index.html',
        context,
    )

def search (request):
    search_value = request.GET.get('q','').strip()

    if search_value == '':
        return redirect('contact:index')
    
    contacts = Contact.objects\
        .filter(mostrar=True)\
        .filter(
            Q(nome__icontains=search_value) |
            Q(sobrenome__icontains=search_value) |
            Q(phone__icontains=search_value) |
            Q(email__icontains=search_value)
        )\
        .order_by('-id')
    
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj' : page_obj,
        'site_title' : 'Contatos - '
    }
    return render(
        request,
        'contact/index.html',
        context,
    )

def contato(request, contato_id):

    #single_contact = Contact.objects.filter(pk=contato_id).first()
    single_contact = get_object_or_404(
        Contact, pk=contato_id, mostrar=True
    )

   # if single_contact is None:
    #    raise Http404()

    contact_name = f'{single_contact.nome} {single_contact.sobrenome} '

    context = {
        'contact' : single_contact,
        'site_title' : contact_name
    }
    return render(
        request,
        'contact/contato.html',
        context,
    )