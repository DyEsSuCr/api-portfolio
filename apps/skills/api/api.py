# Rest Framework
from rest_framework.viewsets import ModelViewSet

# Local
from apps.skills.api.serealizer import SkillSerealizer
from apps.skills.models import Skill

# Models
class SkillViewSet(ModelViewSet):
  queryset = Skill.objects.filter(state = True)
  serializer_class = SkillSerealizer