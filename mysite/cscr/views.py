from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Bulletin
from .models import Project
from .models import Achievement
from .models import Publication,Journal
from .models import Database
from .models import People,People_Researcher,People_Administrator,People_Committee,People_Scholar
from django.db.models import Q
import operator
from django import forms

# Create your views here.


def test(request):
	return render(request,"cscr/test.html")
	
def index(request):
	#show the latest five news
	latest_bulletin_list = Bulletin.objects.order_by('-created_date')[:5]
	context = {'latest_bulletin_list': latest_bulletin_list,}
	return render(request,"cscr/index.html",context)


def introduction(request):
	return render(request,"cscr/introduction.html")

def bulletin(request):
	#show the latest  news
	latest_bulletin_list = Bulletin.objects.order_by('-top','-created_date')
	context = {'latest_bulletin_list': latest_bulletin_list,}
	return render(request,"cscr/bulletin.html",context)

def people(request):
	people_list=People.objects.order_by('-name')
	reserchers_list=People_Researcher.objects.order_by('-name')
	context={'people_list': people_list,'reserchers_list':reserchers_list,}
	return render(request,"cscr/people.html",context)

def people_committee(request):
	people_list=People_Committee.objects.order_by('-name')
	context={'people_list': people_list,}
	return render(request,"cscr/committee.html",context)

def people_scholar(request):
	people_list=People_Scholar.objects.order_by('-name')
	context={'people_list': people_list,}
	return render(request,"cscr/scholar.html",context)

def people_administrative(request):
	people_list=People_Administrator.objects.order_by('-name')
	context={'people_list': people_list,}
	return render(request,"cscr/administrative.html",context)

def projects(request):
	#put all projects into a dictionary
	project_list=Project.objects.order_by('-created_date')
	context={'project_list': project_list,}
	return render(request,"cscr/projects.html",context)

def achievements(request):
	achievement_list=Achievement.objects.order_by('-created_date')
	context={'achievement_list': achievement_list,}
	return render(request,"cscr/achievements.html",context)

def publications(request):
	journals_list=Journal.objects.order_by('-created_date')
	context={'journals_list':journals_list,}
	return render(request,"cscr/publication_2.html",context)




def publications_all(request):
	publications_list=Publication.objects.order_by('-created_date')
	journals_list=Journal.objects.order_by('-created_date')
	context={'journals_list':journals_list,'publications_list':publications_list}
	return render(request,'cscr/all_publications.html',context)

def publications_conference(request):
	publications_list=Publication.objects.order_by('-created_date')
	context={'publications_list':publications_list,}
	return render(request,"cscr/conference_book.html",context)


def database(request):
	database_list=Database.objects.order_by('-created_date')
	context={'database_list': database_list,}
	return render(request,"cscr/database.html",context)




def search():
	form=PublicationForm()

	return render(request,'search/search.html',{'form':form})


