from django.views.generic import CreateView
from django.shortcuts import reverse

from .forms import contact_us_form


class Home(CreateView):
    template_name = "contact/home.html"
    form_class = contact_us_form

    def form_valid(self, form):
        name = form.cleaned_data.get("name")
        email = form.cleaned_data.get("email")
        message = form.cleaned_data.get("message")

        return form

    def get_success_url(self):
        return reverse("contact:home")
