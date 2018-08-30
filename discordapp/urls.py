from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from .views import *

urlpatterns = [
    # navigational page rendering
    url('^$', render_homepage, name='index'),
    url('^about/$', render_about_us, name='about_us'),
    url('^about/([\w\d]+)$', render_about_member, name='about_member'),
    url('^ourstuff/$', render_our_stuff, name='our_stuff'),
]