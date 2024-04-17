from django.shortcuts import render, redirect
from contact.forms import ContactForm

def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        context = {
            'form' : form
        }
        #Verificando a validade dos dados
        if form.is_valid():
            form.save()
                #modificando dados antes de enviar pro banco de dados.
                #contact = form.save(commit=False)
                #exemplo de modificação
                #contact.show = False
                #salvando contato modificado.
                #contact.save()
            return redirect('contact:create')

        return render(
            request,
            'contact/create.html',
            context,
        )
    context = {
        'form': ContactForm()
    }
    return render(
        request,
        'contact/create.html',
        context,
    )