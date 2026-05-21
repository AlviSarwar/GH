from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from music import views as music_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Root → landing page (login/signup gateway)
    path('', music_views.landing, name='landing'),

    # Django built-in auth: login / logout
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    # App routers
    path('music/', include('music.urls')),
    path('users/', include('users.urls')),
]

# Serve media & static files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
