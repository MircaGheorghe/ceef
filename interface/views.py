from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template import RequestContext
from interface.models import *

def index(request):
  return render(request, 'interface/index.html', {
    'menu1' : MenuLvl1.objects.all().order_by('numarul_de_ordine'),
    'menu2' : MenuLvl2.objects.all().order_by('numarul_de_ordine')
  })

def about(request):
  return render(request, 'interface/about.html', {
    'menu1' : MenuLvl1.objects.all().order_by('numarul_de_ordine'),
    'menu2' : MenuLvl2.objects.all().order_by('numarul_de_ordine')
  })

def education(request):
  return render(request, 'interface/education.html', {
    'menu1' : MenuLvl1.objects.all().order_by('numarul_de_ordine'),
    'menu2' : MenuLvl2.objects.all().order_by('numarul_de_ordine')
  })

def specialitati(request):
  return render(request, 'interface/specialitati.html', {
    'menu1' : MenuLvl1.objects.all().order_by('numarul_de_ordine'),
    'menu2' : MenuLvl2.objects.all().order_by('numarul_de_ordine')
  })

def catedre(request):
  return render(request, 'interface/catedre.html', {
    'menu1' : MenuLvl1.objects.all().order_by('numarul_de_ordine'),
    'menu2' : MenuLvl2.objects.all().order_by('numarul_de_ordine')
  })

def error_404(request, exception):
  data = {}
  return render(request,'interface/404.html', data)
