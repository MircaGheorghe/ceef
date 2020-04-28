from django.db import models

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

