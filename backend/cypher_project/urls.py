"""cypher_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

from apps.common.global_swagger import urlpatterns as swagger_urlpatterns
from apps.cypher.views import CypherView, DecypherView

urlpatterns = [
    path("", RedirectView.as_view(url="docs/swagger/")),
    path("admin/", admin.site.urls),
    path("docs/", include(swagger_urlpatterns)),
    path("api/v1/cypher", CypherView.as_view(), name="cypher"),
    path("api/v1/decypher", DecypherView.as_view(), name="decypher"),
]

# In production should be handled by another tool (nginx, apache, etc)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
