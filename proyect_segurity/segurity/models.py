from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=50)
    extension = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Directory(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='directories')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subdirectories')

    def __str__(self):
        return self.name

class CodeFile(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    directory = models.ForeignKey(Directory, on_delete=models.CASCADE, related_name='code_files')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='code_files')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ScanResult(models.Model):
    code_file = models.ForeignKey(CodeFile, on_delete=models.CASCADE, related_name='scan_results')
    line_number = models.PositiveIntegerField()
    code_line = models.TextField()
    vulnerability = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scan_results')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
