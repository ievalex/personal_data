from django import forms
from django.forms import ModelForm, DateInput
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from .models import *

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


class RequesterForm(forms.ModelForm):
    class Meta:
        model = RequesterData
        exclude = ['id']
        labels = {
            'name': _('ФИО'),
            'birth_date': _('Дата рождения'),
            'passport_no': _('Паспорт'),
            'phone_no': _('Телефон'),
            'check_date': _('Дата запроса'),
        }
        widgets = {
            'birth_date': DateInput(),
        }

class CandidateForm(forms.ModelForm):
    class Meta:
        model = CandidateData
        exclude = ['id']

class IndividualForm(forms.ModelForm):
    class Meta:
        model = IndividualBusinessman
        exclude = ['id']