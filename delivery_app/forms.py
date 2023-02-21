from django import forms

from delivery_app.models import Cart, Order
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('payment_method', 'user_phone', 'address', 'user_comment', )

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Fieldset(
                '',
                'payment_method',
                'user_phone',
                'address',
                'user_comment',
            ),
            ButtonHolder(Submit('submit', 'Оформить заказ'))
        )


class CartForm(forms.ModelForm):

    class Meta:
        model = Cart
        fields = ('count_of_dishes',)

    def __init__(self, *args, **kwargs):
        super(CartForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Fieldset(
                '',
                'count_of_dishes',
            ),
            ButtonHolder(Submit('submit', 'Добавить блюдо'))
        )


class UpdateCartForm(forms.ModelForm):

    class Meta:
        model = Cart
        fields = ('count_of_dishes',)

    def __init__(self, *args, **kwargs):
        super(UpdateCartForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Fieldset(
                '',
                'count_of_dishes',
            ),
            ButtonHolder(Submit('submit', 'Изменить количество'))
        )


class FeedBackForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'name',
            'placeholder': "Ваше имя"
        })
    )
    email = forms.CharField(
        max_length=100,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'id': 'email',
            'placeholder': "Ваша почта"
        })
    )
    subject = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'subject',
            'placeholder': "Тема"
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control md-textarea',
            'id': 'message',
            'rows': 2,
            'placeholder': "Ваше сообщение"
        })
    )
