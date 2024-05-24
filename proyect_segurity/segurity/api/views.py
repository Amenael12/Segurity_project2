from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from segurity.models import Project, Language, Directory, CodeFile, ScanResult
from .serializer import ProjectSerializer, LanguageSerializer, DirectorySerializer, CodeFileSerializer, ScanResultSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    #permission_classes = [IsAuthenticated]
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    #permission_classes = [IsAuthenticated]
    permission_classes = [permissions.AllowAny]

class DirectoryViewSet(viewsets.ModelViewSet):
    queryset = Directory.objects.all()
    serializer_class = DirectorySerializer
    #permission_classes = [IsAuthenticated]
    permission_classes = [permissions.AllowAny]

class CodeFileViewSet(viewsets.ModelViewSet):
    queryset = CodeFile.objects.all()
    serializer_class = CodeFileSerializer
    #permission_classes = [IsAuthenticated]
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ScanResultViewSet(viewsets.ModelViewSet):
    queryset = ScanResult.objects.all()
    serializer_class = ScanResultSerializer
    #permission_classes = [IsAuthenticated]
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)