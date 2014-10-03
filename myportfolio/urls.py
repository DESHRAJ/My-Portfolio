from django.conf.urls import patterns, include, url
from django.conf.urls.static import static


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'myportfolio.views.home', name='home'),
    # url(r'a', 'myportfolio.views.function', name='function'),

    # url(r'^myportfolio/', include('myportfolio.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
