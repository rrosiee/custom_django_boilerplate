from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include, re_path
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# Main Section
admin.site.site_header = "Boiler Plate"
admin.site.site_title = "Boiler Plate"
admin.site.index_title = "Boiler Plate"

# Admin 설정
urlpatterns = [
    path("", lambda request: redirect("/admin/")),
    path("admin/", admin.site.urls),
]

# Swagger 설정
schema_view = get_schema_view(
    openapi.Info(
        title="Boiler Plate",
        default_version="0.1.0"
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
urlpatterns += [
    path("docs", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("docs<format>", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("redoc", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc-v1"),
]

# API Urls
urlpatterns += [
    path("api/v1/", include("config.routers.api_router"))
]

# Static 파일 설정 (CSS, JS 등)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
