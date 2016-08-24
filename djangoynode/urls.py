from django.conf.urls import patterns, include, url
from django.contrib import admin

from principal.views import IndexView,InicioView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoynode.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', IndexView.as_view()),
    url(r'^inicio/$', InicioView.as_view()),
    url(r'^crear-comentario$', 'principal.views.create_comment'),
    url(r'^admin/', include(admin.site.urls)),
)
