from django import forms
from .models import ListItem

class AddItemForm(forms.ModelForm):

    class Meta:
        model = ListItem
        fields = ['shop', 'product', 'amount', 'price']
        labels = {
            'shop': 'Sklep',
            'product': 'Produkt',
            'amount': 'Ilość',
            'price': 'Cena',
        }
        widgets = {
            #'email': forms.fields.TextInput(attrs={'placeholder': 'Mail',}),
            #'name': forms.fields.TextInput(attrs={'placeholder': 'Imię (to pole wyświetla sie klientowi!)',}),
            #'surname': forms.fields.TextInput(attrs={'placeholder': 'Nazwisko',}),
            #'description': forms.fields.TextInput(attrs={'placeholder': 'Opis (Tego pola klient nie widzi',}),
            #'phone_number': forms.TextInput(attrs={'placeholder': 'Telefon'}),
            }
        error_messages = {
            #'name': {'required': "Pole nie może być puste",
            #         'max_length': 'Nazwa jest za długa'},
            #'email': {'invalid': 'Email nieprawidłowy','max_length': 'Email jest za długi'},
            #'surname': {'max_length': 'Nazwisko jest za długie'},
            #'description': {'max_length': 'Opis jest za długi'},
            #'phone_number': {'required': 'Pole nie może być puste',
            #                 'max_length': 'Numer jest za długi'},
        }