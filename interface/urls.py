from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name="home"),
  path('Despre_noi', views.about, name="about"),
  path('Educație', views.education, name="education"),
  path('Specialități', views.specialitati, name="specials"),
  path('Catedre', views.catedre, name="catedre"),
]
