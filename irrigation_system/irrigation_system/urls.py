from django.conf.urls import patterns, include, url
from django.contrib import admin
from irrigation import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'irrigation_system.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index,name="index"),
        url(r'^logs/', views.logs,name="logs"),
    url(r'^arduinos/', views.arduinos,name="Arduinos"),
    url(r'^getMoisture', views.getMoisture,name="getMoisture"),
                       
                       
)
