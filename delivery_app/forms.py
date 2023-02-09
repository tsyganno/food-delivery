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
