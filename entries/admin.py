from django.contrib import admin
from .models import Entry, EntryType, Project


admin.site.register(Entry)
admin.site.register(EntryType)
admin.site.register(Project)
