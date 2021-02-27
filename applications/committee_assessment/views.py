from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = "committee_assessment/home.html"
