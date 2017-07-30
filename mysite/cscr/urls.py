from django.conf.urls import url,include
from . import views

urlpatterns=[
	url(r"^$",views.index, name="index"),
	url(r"^introduction",views.introduction,name="introduction"),
	url(r"^bulletin",views.bulletin,name="bulletin"),
	url(r"^people",views.people,name="people"),
	url(r"^administrative",views.people_administrative,name="people_administrative"),
	url(r"^scholar",views.people_scholar,name="people_scholar"),
	url(r"^committee",views.people_committee,name="people_committee"),	
	url(r"^projects",views.projects,name="projects"),
	url(r"^publications",views.publications,name="publications"),
	url(r"^all",views.publications_all,name="publications_all"),
	url(r"^conference&books",views.publications_conference,name="conference&books"),
	url(r"^achievements",views.achievements,name="achievements"),
	url(r"^database",views.database,name="database"),
	url(r'^search/', include('haystack.urls')),

]

