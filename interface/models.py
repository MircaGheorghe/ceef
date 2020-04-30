from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class MenuLvl1(models.Model):
  item_title = models.CharField('Item de nivelul 1', max_length=100)
  numarul_de_ordine = models.IntegerField('Numărul de ordine în meniu', default=1)
  pub_date = models.DateTimeField('Data publicarii', auto_now_add=True)

  def __str__(self):
    return self.item_title

  class Meta:
    verbose_name = "Item de nivelul 1"
    verbose_name_plural = "Itemi de nivelul 1"

class MenuLvl2(models.Model):
  top_lvl = models.ForeignKey(MenuLvl1, on_delete = models.CASCADE)
  item_title = models.CharField('Itemi de nivelul 2', max_length=100)
  numarul_de_ordine = models.IntegerField('Numărul de ordine în meniu', default=1)
  pub_date = models.DateTimeField('Data publicarii', auto_now_add=True)

  def __str__(self):
    return self.item_title

  class Meta:
    verbose_name = "Item de nivelul 2"
    verbose_name_plural = "Itemi de nivelul 2"

class MenuLvl3(models.Model):
  top_lvl = models.ForeignKey(MenuLvl2, on_delete = models.CASCADE)
  item_title = models.CharField('Itemi de nivelul 3', max_length=100)
  numarul_de_ordine = models.IntegerField('Numărul de ordine în meniu', default=1)
  pub_date = models.DateTimeField('Data publicarii', auto_now_add=True)

  def __str__(self):
    return self.item_title

  class Meta:
    verbose_name = "Item de nivelul 3"
    verbose_name_plural = "Itemi de nivelul 3"

class Top_menu(models.Model):
  item_title = models.CharField('Itemi de nivelul 3', max_length=100)
  numarul_de_ordine = models.IntegerField('Numărul de ordine în meniu', default=1)
  pub_date = models.DateTimeField('Data publicarii', auto_now_add=True)

  def __str__(self):
    return self.item_title

  class Meta:
    verbose_name = "Item din top meniu"
    verbose_name_plural = "Itemi din top meniu"

class Tags(models.Model):
  tag_title = models.CharField('Denumirea tagului', max_length=100)
  pub_date = models.DateTimeField('Data publicarii', auto_now_add=True, editable=False)

  def __str__(self):
    return self.tag_title

  class Meta:
    verbose_name = "Tag pentru postări"
    verbose_name_plural = "Taguri pentru postări"


class Posts(models.Model):
  title = models.CharField('Titlu', max_length=100)
  subtitle = models.CharField('Subtitlu', blank=True, null=True, max_length=100)
  body = models.TextField('Descrierea')
  image = models.ImageField('Imagine ', blank=True, null=True, upload_to="interface/static/interface/posts_images")
  author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
  pub_date = models.DateTimeField('Data publicarii', auto_now_add=True)
  tags = models.ManyToManyField(Tags, blank=True)

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = "Postare"
    verbose_name_plural = "Păstări"


