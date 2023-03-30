from django.urls import path
from .import views

urlpatterns = [
    path("",views.pdisplay,name="pdisplay"),
    path("create",views.pinsert,name="pinsert"),
    path("edit/<int:id>",views.pedit,name="pedit"),
    path("delete/<int:id>",views.pdelete,name="pdelete"),
    path("Logout/",views.Logout,name="Logout"),
]
