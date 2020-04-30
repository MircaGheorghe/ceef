from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.urls import reverse
from interface.models import *

def index(request):
  return render(request, 'interface/index.html', {
    'menu1' : MenuLvl1.objects.all().order_by('numarul_de_ordine'),
    'menu2' : MenuLvl2.objects.all().order_by('numarul_de_ordine'),
    'top_menu' : Top_menu.objects.all().order_by('numarul_de_ordine'),
    'current_user' : request.user
  })

def despre(request):
  return render(request, 'interface/despre.html', {
    'menu1' : MenuLvl1.objects.all().order_by('numarul_de_ordine'),
    'menu2' : MenuLvl2.objects.all().order_by('numarul_de_ordine')
  })

def educatie(request):
  return render(request, 'interface/educatie.html', {
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

def traseu(request):
  return render(request, 'interface/traseul_profesional.html', {
    'menu1' : MenuLvl1.objects.all().order_by('numarul_de_ordine'),
    'menu2' : MenuLvl2.objects.all().order_by('numarul_de_ordine')
  })

def rez_adm(request):
  return render(request, 'interface/rezultatele_admiterii.html', {
    'menu1' : MenuLvl1.objects.all().order_by('numarul_de_ordine'),
    'menu2' : MenuLvl2.objects.all().order_by('numarul_de_ordine')
  })

def proiecte(request):
  return render(request, 'interface/proiecte.html', {
    'menu1' : MenuLvl1.objects.all().order_by('numarul_de_ordine'),
    'menu2' : MenuLvl2.objects.all().order_by('numarul_de_ordine')
  })

def pract_tehn(request):
  return render(request, 'interface/practica_tehnologica.html', {
    'menu1' : MenuLvl1.objects.all().order_by('numarul_de_ordine'),
    'menu2' : MenuLvl2.objects.all().order_by('numarul_de_ordine')
  })

def pract_init(request):
  return render(request, 'interface/practica_initiere.html', {
    'menu1' : MenuLvl1.objects.all().order_by('numarul_de_ordine'),
    'menu2' : MenuLvl2.objects.all().order_by('numarul_de_ordine')
  })

def pract_spec(request):
  return render(request, 'interface/practica_specialitate.html', {
    'menu1' : MenuLvl1.objects.all().order_by('numarul_de_ordine'),
    'menu2' : MenuLvl2.objects.all().order_by('numarul_de_ordine')
  })

def pract_abs(request):
  return render(request, 'interface/practica_absolvire.html', {
    'menu1' : MenuLvl1.objects.all().order_by('numarul_de_ordine'),
    'menu2' : MenuLvl2.objects.all().order_by('numarul_de_ordine')
  })

def practica(request):
  return render(request, 'interface/practica.html', {
    'menu1' : MenuLvl1.objects.all().order_by('numarul_de_ordine'),
    'menu2' : MenuLvl2.objects.all().order_by('numarul_de_ordine')
  })

def oferte(request):
  return render(request, 'interface/oferte_de_angajare.html', {
    'menu1' : MenuLvl1.objects.all().order_by('numarul_de_ordine'),
    'menu2' : MenuLvl2.objects.all().order_by('numarul_de_ordine')
  })

def ghidare(request):
  return render(request, 'interface/ghidare_in_cariera.html', {
    'menu1' : MenuLvl1.objects.all().order_by('numarul_de_ordine'),
    'menu2' : MenuLvl2.objects.all().order_by('numarul_de_ordine')
  })

def info(request):
  return render(request, 'interface/informatii_generale.html', {
    'menu1' : MenuLvl1.objects.all().order_by('numarul_de_ordine'),
    'menu2' : MenuLvl2.objects.all().order_by('numarul_de_ordine')
  })

def mobilitate(request):
  return render(request, 'interface/mobilitate_academica.html', {
    'menu1' : MenuLvl1.objects.all().order_by('numarul_de_ordine'),
    'menu2' : MenuLvl2.objects.all().order_by('numarul_de_ordine')
  })

def elevi(request):
  return render(request, 'interface/elevi.html', {
    'menu1' : MenuLvl1.objects.all().order_by('numarul_de_ordine'),
    'menu2' : MenuLvl2.objects.all().order_by('numarul_de_ordine')
  })

def muguri(request):
  return render(request, 'interface/mugurii_performantei.html', {
    'menu1' : MenuLvl1.objects.all().order_by('numarul_de_ordine'),
    'menu2' : MenuLvl2.objects.all().order_by('numarul_de_ordine')
  })

def absolventi(request):
  return render(request, 'interface/absolventi.html', {
    'menu1' : MenuLvl1.objects.all().order_by('numarul_de_ordine'),
    'menu2' : MenuLvl2.objects.all().order_by('numarul_de_ordine')
  })

def consiliu(request):
  return render(request, 'interface/consiliul_elevilor.html', {
    'menu1' : MenuLvl1.objects.all().order_by('numarul_de_ordine'),
    'menu2' : MenuLvl2.objects.all().order_by('numarul_de_ordine')
  })

def admitere(request):
  return render(request, 'interface/admitere.html', {
    'menu1' : MenuLvl1.objects.all().order_by('numarul_de_ordine'),
    'menu2' : MenuLvl2.objects.all().order_by('numarul_de_ordine')
  })

def comisia(request):
  return render(request, 'interface/comisia.html', {
    'menu1' : MenuLvl1.objects.all().order_by('numarul_de_ordine'),
    'menu2' : MenuLvl2.objects.all().order_by('numarul_de_ordine')
  })

def conditii_admitere(request):
  return render(request, 'interface/conditii_admitere.html', {
    'menu1' : MenuLvl1.objects.all().order_by('numarul_de_ordine'),
    'menu2' : MenuLvl2.objects.all().order_by('numarul_de_ordine')
  })

def management(request):
  return render(request, 'interface/managementul_calitatii.html', {
    'menu1' : MenuLvl1.objects.all().order_by('numarul_de_ordine'),
    'menu2' : MenuLvl2.objects.all().order_by('numarul_de_ordine')
  })

def formare(request):
  return render(request, 'interface/formare_continua.html', {
    'menu1' : MenuLvl1.objects.all().order_by('numarul_de_ordine'),
    'menu2' : MenuLvl2.objects.all().order_by('numarul_de_ordine')
  })

def cercuri(request):
  return render(request, 'interface/cercuri.html', {
    'menu1' : MenuLvl1.objects.all().order_by('numarul_de_ordine'),
    'menu2' : MenuLvl2.objects.all().order_by('numarul_de_ordine')
  })

def firma_exercitiu(request):
  return render(request, 'interface/firma_exercitiu.html', {
    'menu1' : MenuLvl1.objects.all().order_by('numarul_de_ordine'),
    'menu2' : MenuLvl2.objects.all().order_by('numarul_de_ordine')
  })

def avize(request):
  return render(request, 'interface/avize.html', {
    'menu1' : MenuLvl1.objects.all().order_by('numarul_de_ordine'),
    'menu2' : MenuLvl2.objects.all().order_by('numarul_de_ordine'),
    'posts' : Posts.objects.all(),
    'tags' : Tags.objects.all(),
  })

def aviz(request, post_id):
  try:
    a = Posts.objects.get( id = post_id )
  except:
    return render(request, 'interface/404.html')

  comments = a.comment_set.order_by('-id')

  return render(request, 'interface/aviz.html', {
    'menu1' : MenuLvl1.objects.all().order_by('numarul_de_ordine'),
    'menu2' : MenuLvl2.objects.all().order_by('numarul_de_ordine'),
    'post' : a,
    'comments': comments
  })

def leave_comment(request, post_id):
  try:
    a = Posts.objects.get( id = post_id )
  except:
    return render(request, 'interface/404.html')

  a.comment_set.create(author = request.POST['name'], body = request.POST['message'], email = request.POST['email'])

  return HttpResponseRedirect( reverse('aviz', args = (a.id,)) )

def error_404(request, exception):
  data = {}
  return render(request,'interface/404.html', data)
