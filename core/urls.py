from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main.views import BannerListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('banners/', BannerListView.as_view(), name='banner_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


