from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContactForm(forms.ModelForm):
    #Possibilidade de criar ou modificar o campo do formulario.
    imagem = forms.ImageField(
        widget=forms.FileInput(
            attrs={
            'accept':'image/*',
            }
        )
    )

    class Meta:
        model = models.Contact
        fields = (
            'nome', 'sobrenome', 'phone', 'email', 'descricao', 'categoria', 'imagem',
        )

    def clean(self):

        cleaned_data = self.cleaned_data
        nome = cleaned_data.get('nome')
        sobrenome = cleaned_data.get('sobrenome')

        if nome == sobrenome:
            msg = ValidationError(
                'Primeiro nome nao pode ser igual ao segundo',
                code = 'invalid',
            )
            self.add_error('nome', msg)
            self.add_error('sobrenome', msg)
        return super().clean()
        
    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if nome == 'ABC':
            self.add_error(
                'nome',
                ValidationError(
                    'Veio do add error',
                    code='invalid'
                )
            )
        return nome

