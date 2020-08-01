from django import forms

from webapp.models import STATUS_CHOICE, DEFAUL_STATUS
BROWSER_DATETIME_FORMAT = '%Y-%m-%dT%H:%M'


class NoteForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Название')
    email = forms.EmailField(max_length=100, label='Электронная почта')
    text = forms.CharField(max_length=2000, required=True, label='Текст записи', widget=forms.Textarea)
    # created_at = forms.DateTimeField(required=True, label='Время записи',
    #                                 input_formats=['%Y-%m-%d', BROWSER_DATETIME_FORMAT,
    #                                                '%Y-%m-%dT%H:%M:%S', '%Y-%m-%d %H:%M',
    #                                                '%Y-%m-%d %H:%M:%S'],
    #                                 widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    status = forms.ChoiceField(choices=STATUS_CHOICE, required=True, initial=DEFAUL_STATUS, label='Статус')





    # name = models.CharField(max_length=100, verbose_name='Имя')
    # email = models.EmailField(max_length=100, verbose_name='Электронная почта')
    # text = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Текст записи')
    # created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    # updated_at = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Время изменения')
    # status = models.CharField(max_length=20, verbose_name='Статус', choices=STATUS_CHOICE, default=DEFAUL_STATUS)