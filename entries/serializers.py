from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Project, Entry

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'date_joined')


class ProjectSerializer(serializers.ModelSerializer):
    manager = UserSerializer()
    members = UserSerializer(many=True)
    number_of_entries = serializers.SerializerMethodField()

    def get_number_of_entries(self, project):
        return project.entries.count()

    class Meta:
        model = Project
        fields = ('manager', 'members', 'name', 'description', 'updated', 'created', 'number_of_entries')
        depth = 1


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('user', 'project', 'type', 'start_time', 'end_time', 'updated', 'created')
