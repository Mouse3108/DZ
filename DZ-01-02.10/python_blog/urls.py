from django.contrib import admin
from django.urls import path, include
from blog_app.views import main, about
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", main, name="main"),
    path("about/", about, name="about"),
    path('blog/', include('blog_app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
