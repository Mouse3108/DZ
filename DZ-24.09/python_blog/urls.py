from django.contrib import admin
from django.urls import path, include
from blog_app.views import main, about


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", main, name="main"),
    path("about/", about, name="about"),
    path('blog/', include('blog_app.urls')),
]
