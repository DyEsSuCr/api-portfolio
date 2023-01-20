# Rest Framework
from rest_framework.serializers import ModelSerializer

# Local
from apps.skills.models import Skill

# Serealizers
class SkillSerealizer(ModelSerializer):
  class Meta:
    model = Skill
    exclude = ('state', )