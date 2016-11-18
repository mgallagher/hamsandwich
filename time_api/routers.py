from rest_framework import routers

from entries.api import ProjectViewSet, EntryViewSet, EntryTypeViewSet

api_router = routers.SimpleRouter()
api_router.register(r'projects', ProjectViewSet)
api_router.register(r'entries', EntryViewSet)
api_router.register(r'entry-types', EntryTypeViewSet)
