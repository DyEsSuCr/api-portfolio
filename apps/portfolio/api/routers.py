# Rest Framework
from rest_framework.routers import DefaultRouter

# Local
from apps.portfolio.api.api import ProjectViewSet

# Routers
router = DefaultRouter()
router.register('projects', ProjectViewSet, 'projects')

urlpatterns = router.urls