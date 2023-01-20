# Django
from django.db import models

# Local
from apps.skills.models import Skill

# Models
class Project(models.Model):
  title = models.CharField('Titulo', max_length=100)
  description = models.TextField('Descripción', max_length=120)
  image = models.ImageField('Imagen', default='comingsoon.png', upload_to='projects/')
  demo = models.URLField('Demo', blank=True, null=True)
  date = models.DateField('Fecha')
  state = models.BooleanField('Estado', default=True)
  github = models.URLField('Github', blank=True, null=True)
  skills = models.ManyToManyField(Skill)

  class Meta:
    verbose_name = 'Proyecto'
    verbose_name_plural = 'Proyectos'
    ordering = ['-title']

  def __str__(self):
    return f'Titulo: {self.title}'