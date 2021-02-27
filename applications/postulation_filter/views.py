from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = "postulation_filter/home.html"
