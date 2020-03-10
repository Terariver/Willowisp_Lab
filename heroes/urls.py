from django.conf.urls import url
from .views import HeroesView, CloudView, JesterView

urlpatterns = [
	url(r'^$',HeroesView.as_view(), name='heroes'),
	url(r'^hero/cloud$', CloudView.as_view(), name='Cloud Detail'),
	url(r'^hero/jester$', JesterView.as_view(), name='Jester Detail'),

]