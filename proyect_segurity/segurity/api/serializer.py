from rest_framework import serializers
from segurity.models import Project, Language, Directory, CodeFile, ScanResult

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'name', 'extension']

class DirectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Directory
        fields = ['id', 'name', 'project', 'parent']

class CodeFileSerializer(serializers.ModelSerializer):
    language = LanguageSerializer(read_only=True)

    class Meta:
        model = CodeFile
        fields = ['id', 'name', 'content', 'directory', 'language', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class ScanResultSerializer(serializers.ModelSerializer):
    code_file = CodeFileSerializer(read_only=True)

    class Meta:
        model = ScanResult
        fields = ['id', 'code_file', 'line_number', 'code_line', 'vulnerability', 'user', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at', 'code_file', 'line_number', 'code_line', 'vulnerability']

class ProjectSerializer(serializers.ModelSerializer):
    directories = DirectorySerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'user', 'directories', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']