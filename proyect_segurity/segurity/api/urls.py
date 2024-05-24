from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, LanguageViewSet, DirectoryViewSet, CodeFileViewSet, ScanResultViewSet

router = DefaultRouter()
router.register('projects', ProjectViewSet, basename='project')
router.register('languages', LanguageViewSet, basename='language')
router.register('directories', DirectoryViewSet, basename='directory')
router.register('code-files', CodeFileViewSet, basename='code-file')
router.register('scan-results', ScanResultViewSet, basename='scan-result')

urlpatterns = router.urls