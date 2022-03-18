from django.urls import path,include
from django.contrib.auth.views import LogoutView, LoginView
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register.as_view(), name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/<username>/',views.profile, name='profile'),
    path('wheelAlignment/',views.wheelAlign, name='wheelAlign'),
    path('paintJob/',views.paintJob, name='paintJob'),
    path('engine/',views.engine, name='engine'),
    path('tires/',views.tires, name='tires'),
    path('brake/',views.brake, name='brake'),
    path('battery/',views.battery, name='battery'),
    path('profile/<username>/update/',views.update_profile, name='update_profile'),
    path('profile/<username>/update/mechanic/',views.update_mechanic_profile, name='update_mechanic_profile'),
    path('work-info/<username>/', views.mechanic_info, name='work-info'),
    path('contact/', views.contact, name='contact_mechanic'),
    path('about/', views.about, name='about'),
    path('deletework/<id>/<pk>/', views.work_delete, name='work_delete'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)