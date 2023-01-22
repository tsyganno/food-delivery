from django import forms
from delivery_app.models import Cart
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, HTML


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
                HTML('<br>'),
            ),
            ButtonHolder(Submit('submit', 'Добавить блюдо'))
        )
