from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
]

schema_view = get_schema_view(
    openapi.Info(
        title='Music Albums Guide API',
        default_version='v1',
        description='Документация для приложения backend проекта Music Albums Guide',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
