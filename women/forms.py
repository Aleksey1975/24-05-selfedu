from django import forms
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

from .models import *
from django.core.validators import MinLengthValidator
#
#
# @deconstructible
# class RussianValidator:
#     ALLOWED_CHARS = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁёйцукенгшщзхъэждлорпавыфячсмитьбю1234567890- '
#     code = 'russian'
#
#     def __init__(self, message=None):
#         self.message = message if message else 'Должны присутствовать только русские символы, дефис и пробел'
#
#     def __call__(self, value, *args, **kwargs):
#         if not (set(value) <= set(self.ALLOWED_CHARS)):
#             raise ValidationError(self.message, self.code)
#


class AddPost(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Категория не выбрана', label='Категория')
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), empty_label='Не замужем', label='Муж', required=False)

    class Meta:
        model = Women
        fields = '__all__'
        widgets = {
          'title': forms.TextInput(attrs={'class':'form-input'}),
          'content': forms.Textarea(attrs={'cols': 90, 'rows': 5})
        }
        labels = {
            'title':'Название-ее'
        }



# class AddPost(forms.Form):
#     title = forms.CharField(
#        # validators=[RussianValidator()],
#         max_length=255, min_length=3,
#                             label='Заголовок', widget=forms.TextInput(attrs={'class': 'form-input'})
#                             , error_messages= {
#             'min_length': 'Слишком короткий заголовок',
#             'required': 'Без заголовка никак'
#         })
#     slug = forms.SlugField(max_length=255, validators=[MinLengthValidator(5, message='Минимум 5 символов')])
#     content = forms.CharField(widget=forms.Textarea(attrs={'cols':50, 'rows': 5}), required=False)
#     is_published = forms.BooleanField(required=False, initial=True)
#     cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Категория не выбрана')
#     husband = forms.ModelChoiceField(queryset=Husband.objects.all(), required=False)
#
#     def clean_title(self):
#         title = self.cleaned_data['title']
#         ALLOWED_CHARS = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁёйцукенгшщзхъэждлорпавыфячсмитьбю1234567890- '
#         if not (set(title) <= set(ALLOWED_CHARS)):
#             raise ValidationError('Должны присутствовать только русские символы, дефис и пробел')
#
#         return title
#



