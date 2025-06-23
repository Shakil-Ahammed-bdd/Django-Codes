from django.urls import path
from . import views
# from first_app.views import homed
# from first_app import views
urlpatterns = [
  path('',views.home),
]