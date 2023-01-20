# Django
from django.db import models

# Models
class Skill(models.Model):
  name = models.CharField('Nombre', max_length=25, null=False, blank=False)
  url = models.URLField('URL', null=False, blank=False)
  logo = models.ImageField("Logo", upload_to='skills/', null=False, blank=False)
  state = models.BooleanField('Estado', default=True)

  class Meta:
    verbose_name = 'Skill'
    verbose_name_plural = 'Skills'
    ordering = ['-name']

  def __str__(self):
    return f'Nombre: {self.name}'