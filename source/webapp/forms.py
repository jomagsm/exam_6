from django import forms

from webapp.models import STATUS_CHOICE, DEFAUL_STATUS
BROWSER_DATETIME_FORMAT = '%Y-%m-%dT%H:%M'


class NoteForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Название')
    email = forms.EmailField(max_length=100, label='Электронная почта')
    text = forms.CharField(max_length=2000, required=True, label='Текст записи', widget=forms.Textarea)
    status = forms.ChoiceField(choices=STATUS_CHOICE, required=True, initial=DEFAUL_STATUS, label='Статус')
