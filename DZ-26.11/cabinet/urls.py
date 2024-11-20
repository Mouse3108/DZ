from django.urls import path
from . import views

app_name = 'cabinet'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('all-visits/', views.ApplicationListView.as_view(), name='all_visits'),
    path('new-visits/', views.ApplicationListView.as_view(), {'visit_type': 'new'}, name='new_visits'),
    path('visit-archive/', views.ApplicationListView.as_view(), {'visit_type': 'archive'}, name='visit_archive'),
    path('change-password/', views.ChangePasswordView.as_view(), name='change_password'),
    path('visit/<int:pk>/', views.ApplicationDetailView.as_view(), name='visit_detail'),
    path('visit/<int:pk>/delete/', views.ApplicationDeleteView.as_view(), name='visit_delete'),
    path('visit/<int:pk>/update/', views.ApplicationUpdateView.as_view(), name='visit_update'),
    path('create-visit/', views.ApplicationCreateView.as_view(), name='create_visit'),
]