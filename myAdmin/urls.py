from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('administrator', views.AdminDashboard, name='admin'),
    path('doctor_list', views.DoctorsDashboard, name='doclist'),
    path('register/', views.registration, name='register'),
    path('login/', views.loginPage, name='login'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
