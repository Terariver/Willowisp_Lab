from django.views.generic.base import TemplateView


class HeroesView(TemplateView):
	template_name = "heroes.html"