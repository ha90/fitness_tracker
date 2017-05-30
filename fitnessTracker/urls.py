from django.conf.urls import url

from . import views

app_name = "fitnessTracker"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'measurements', views.measurements, name="measurements")
]
