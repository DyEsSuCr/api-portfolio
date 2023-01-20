# Rest Framework
from rest_framework.serializers import ModelSerializer

# Local
from apps.portfolio.models import Project
from apps.skills.api.serealizer import SkillSerealizer

# Serealizers
class ProjectSerealizer(ModelSerializer):

  skills = SkillSerealizer(many=True)

  class Meta:
    model = Project
    exclude = ('state', )