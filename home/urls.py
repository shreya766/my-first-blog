
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index , name='index'),
    path("about",views.about , name='index'),
    path("services",views.services , name='index'),
    path("contact",views.contact , name='index'),
    path("view",views.view , name='view'),
    path("view1",views.view1 , name='view1'),
    path("view2",views.view2 , name='view2'),
    path("view3",views.view3 , name='view3'),
    path("view4",views.view4 , name='view4'),
    path("view5",views.view5 , name='view5'),



]