from django import forms

from mailing.models import Client


class ClientForm(forms.ModelForm):
    """Форма создания клиента"""
    class Meta:
        model = Client
        # указываю только один из 3 способов заполнения поля
        # fields = '__all__'
        fields = ('email', 'first_name', 'last_name', 'comment')
        # exclude = ('email',)
