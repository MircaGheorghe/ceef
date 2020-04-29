from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name="home"),
  path('Despre_noi', views.despre, name="about"),

  path('Educație', views.educatie, name="education"),
  path('Specialități', views.specialitati, name="specials"),
  path('Catedre', views.catedre, name="catedre"),
  path('Proiecte', views.proiecte, name="rezultatele_admiterii"),

  path('Practica', views.practica, name="practica"),
  path('Informații_generale', views.info, name="informatii"),
  path('Ghidare_în_carieră', views.ghidare, name="ghidare"),
  path('Oferte_de_angajare', views.oferte, name="oferte"),
  path('Practica_de_inițiere_în_specialitate', views.pract_init, name="practica_initiere"),
  path('Practica_de_specialitate', views.pract_spec, name="practica_specialitate"),
  path('Practica_tehnologică', views.pract_tehn, name="practica_tehnologica"),
  path('Practica_ce_anticipează_probe_de_absolvire', views.pract_abs, name="practica_absolvire"),
  path('Traseul_profesional', views.traseu, name="traseul_profesional"),
  path('Mobilitatea_academică', views.mobilitate, name="mobilitate"),

  path('Elevi', views.elevi, name="elevi"),
  path('Mugurii_performanței', views.muguri, name="muguri"),
  path('Absolvenți', views.absolventi, name="absolventi"),
  path('Consiliul_elevilor', views.consiliu, name="consiliu"),


  path('Admitere', views.admitere, name="admitere"),
  path('Condiții_de_admitere', views.conditii_admitere, name="conditii_admitere"),
  path('Comisia_de_admitere', views.comisia, name="comisia_de_admitere"),
  path('Rezultatele_admiterii', views.rez_adm, name="rezultatele_admiterii"),

  path('Managementul_calității', views.management, name="management"),

  path('Formare_continuă', views.formare, name="formare_continua"),
]
