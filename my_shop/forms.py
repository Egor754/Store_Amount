from django.forms import ModelForm, TextInput, ChoiceField,Select
from django.utils.translation import gettext_lazy as _

from my_shop.models import Orders


class CheckoutForm(ModelForm):
    class Meta:
        model = Orders
        exclude = ['paid', 'updated', 'created']
        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First name'
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last name'
            }),
            'email': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Email",
            }),
            'country': Select(attrs={
                'class': 'w-100'
            }),
            'address': TextInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': "Street address",
            }),
            'town': TextInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Town'
            }),
            'zip_code': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Zip Code'
            }),
            'phone_number': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number'
            }),
            'comment': TextInput(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Comment'
            }),
        }

    #
    # first_name = models.CharField(max_length=255, verbose_name='Имя')
    # last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    # email = models.EmailField(verbose_name='Электронная почта')
    # country = models.CharField(max_length=255, verbose_name='Страна')
    # address = models.TextField(verbose_name='Адрес')
    # town = models.CharField(max_length=255, verbose_name='Город')
    # zip_code = models.PositiveIntegerField(verbose_name='Почтовый индекс')
    # phone_number = PhoneNumberField(verbose_name='Номер телефона')
    # comment = models.TextField(verbose_name='Коментарий', null=True)
    # created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    # updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    # paid = models.BooleanField(default=False, verbose_name='Отправлено')
