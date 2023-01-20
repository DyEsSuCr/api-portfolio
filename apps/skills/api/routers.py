# Rest Framework
from rest_framework.routers import DefaultRouter

# Local
from apps.skills.api.api import SkillViewSet

# Routers
router = DefaultRouter()
router.register('skills', SkillViewSet, 'skills')

urlpatterns = router.urls