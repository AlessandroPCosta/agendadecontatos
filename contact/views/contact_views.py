from django.shortcuts import render, get_object_or_404
from django.http import Http404

from contact.models import Contact
# Create your views here.
def index(request):
    contacts = Contact.objects\
        .filter(mostrar=True)\
        .order_by('-id')[10:20]
    
    context = {
        'contacts' : contacts,
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