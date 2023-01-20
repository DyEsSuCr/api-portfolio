# Rest Framework
from rest_framework.viewsets import ModelViewSet

# Local
from apps.portfolio.api.serealizers import ProjectSerealizer
from apps.portfolio.models import Project

# Models
class ProjectViewSet(ModelViewSet):
  queryset = Project.objects.filter(state = True)
  serializer_class = ProjectSerealizer