from django.conf.urls import patterns, include, url
import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^setup/$', views.setup),
    url(r'^results/$', views.results),
    url(r'^savemeals/$', views.savemenu),
    url(r'^shoppinglist/$', views.shoppinglist),

    # Examples:
    # url(r'^$', 'ehfl.views.home', name='home'),
    # url(r'^ehfl/', include('ehfl.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
