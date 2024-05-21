from django.urls import path
from . import views

urlpatterns = [
    path("subdivision/", views.SubDivisionListCreate.as_view(), name="subdivision-view-create"),
    path("subdivision/<int:pk>", views.SubDivisionRetrieveUpdate.as_view(), name="update"),
    path("street/", views.StreetListCreate.as_view(), name="street-view-create"),
    path("neigbor/", views.NeigborListCreate.as_view(), name="neigbor-view-create"),
    path("admins/", views.AdminsListCreate.as_view(), name="admin-view-create"),
    path("subdivisionuser/", views.SubdivisionUsersListCreate.as_view(), name="users-view-create"),
    path("subdivisiondb/", views.SubdivisionNumberDBListCreate.as_view(), name="subdb-view-create"),
    path("adminusers/", views.AdminsListCreate.as_view(), name="adminusers-view-create"),
    path("r'^adminusers/(?P<email>\w{0,50})/(?P<password>\w{0,50})/$'", views.AdminsListCreate.as_view(), name="adminusers-view-get"),
    path("getdbnumber/", views.GetdbNumber.as_view(), name="comment-view-create"),
    path("getuser/", views.GetUser.as_view(), name="user-view-create") 
    

]