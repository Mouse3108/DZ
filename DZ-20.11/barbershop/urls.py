from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cabinet/', include('cabinet.urls', namespace='cabinet')),
    path("", MainPageView.as_view(), name="main"),
    path("thanks/", ThankYouPageView.as_view(), name="thanks"),
    path(
        "get_services_by_master/<int:master_id>/",
        ServiceFetchView.as_view(),
        name="get_services_by_master",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
