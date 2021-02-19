from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from .models import HomeModel
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.
class HomeView(generic.ListView):
    template_name = 'home/home.html'
    model = HomeModel

class AboutView(generic.ListView):
    template_name = 'home/about.html'
    model = HomeModel

class ProjectView(generic.ListView):
    template_name = "home/project.html"
    model = HomeModel

class SkillsView(generic.ListView):
    template_name = "home/skills.html"
    model = HomeModel

class Yes(generic.ListView):
    template_name = "home/yes.html"
    model = HomeModel