from django.conf.urls import url
from .views import HeroesView

urlpatterns = [
	url(r'^$',HeroesView.as_view(), name='heroes'),
]