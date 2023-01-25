# import yhe path function from django
from django.urls import path

# import the views file so we can use the funtions
from . import views


#creat a list for all routes we need

urlpatterns = [
  path("january", views.index)
]