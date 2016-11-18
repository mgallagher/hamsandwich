from rest_framework import serializers

from .models import Project, Entry


class ProjectSerializer(serializers.ModelSerializer):
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
        fields = ('user', 'project', 'hours', 'minutes', 'seconds', 'updated', 'created')
