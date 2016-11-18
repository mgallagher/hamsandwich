from rest_framework import serializers

from .models import Project, Entry


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('manager', 'members', 'name', 'description', 'updated', 'created')
        depth = 1


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('user', 'project', 'hours', 'minutes', 'seconds', 'updated', 'created')
