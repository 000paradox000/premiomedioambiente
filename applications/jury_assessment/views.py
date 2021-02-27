from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = "jury_assessment/home.html"
