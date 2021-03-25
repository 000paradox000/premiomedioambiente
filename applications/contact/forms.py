from django.shortcuts import reverse
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout

from .layouts import contact_us_layout
from .models import contact_us_model


class contact_us_form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(contact_us_form, self).__init__(*args, **kwargs)

        self.helper = FormHelper()

        self.helper.form_id = 'contact-form'
        self.helper.form_methoddjan = 'post'
        self.helper.form_action = reverse("contact:home")
        self.helper.layout = Layout()
        self.helper.layout.fields = contact_us_layout(self.helper.layout.fields)

    class Meta:
        model = contact_us_model
        exclude = []

