"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
import users.views as user_views

urlpatterns = [

    # django admin stuff
    url(r'^signup/$', user_views.user_signup, name='signup'),
    url(r'^login/$', user_views.user_login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^admin/', admin.site.urls),

    # main website apps
    url(r'^$', include('homepage.urls')),
    url(r'^food/', include('food.urls')),
    url(r'^beauty/', include('beauty.urls')),
    url(r'^fitness/', include('fitness.urls')),
    url(r'^travel/', include('travel.urls')),
    url(r'^search/', include('search.urls')),
    url(r'^users/', include('users.urls')),

    # additional tools
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


