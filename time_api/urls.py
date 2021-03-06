"""time_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token

from entries.views import entry_list, ProjectList, ProjectDetail, ProjectCreate, ProjectUpdate
from .routers import api_router

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^entries/', entry_list),
    url(r'^projects/$', ProjectList.as_view()),
    url(r'^projects/(?P<pk>[0-9]+)/$', ProjectDetail.as_view()),
    url(r'^projects/create/', ProjectCreate.as_view()),
    url(r'^projects/(?P<pk>[0-9]+)/update/$', ProjectUpdate.as_view()),
    url(r'^v1/', include(api_router.urls)),
    url(r'v1/api-token-auth/$', obtain_jwt_token)
]
