from django.shortcuts import render
from dynamic_db_router import in_database
import os
from rest_framework import views
from rest_framework import generics, status
from rest_framework.response import Response
from .models import SubDivision, Street, Neigbor, SubdividionUsers, AdminUsers, SubdivisionNumberDB
from .helpers import find_db_in_path_subdivision
from .serializers import SubDivisionSerializer, StreetSerializer, NeigborSerializer, SubdivisionUsersSerializer, AdminUserSerializer, SubdivisionNumerDBSerializer, GetNumberDBSerializer, GetUserSerializer


# SUBDIVISION INFORMATION
class SubDivisionListCreate(generics.ListCreateAPIView):
    queryset = SubDivision.objects.all()
    serializer_class = SubDivisionSerializer
    
    def delete(self, request, *args, **kwargs):
        SubDivision.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class SubDivisionRetrieveUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubDivision.objects.all()
    serializer_class = SubDivisionSerializer
    lookup_field = "pk"


# STREETS INFORMATION
class StreetListCreate(generics.ListCreateAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer 

# NEIGBOR INFORMATION
class NeigborListCreate(generics.ListCreateAPIView):
    queryset = Neigbor.objects.all()
    serializer_class = NeigborSerializer

# SUBDIVISION USERS
class SubdivisionUsersListCreate(generics.ListCreateAPIView):
    queryset = SubdividionUsers.objects.all()
    serializer_class = SubdivisionUsersSerializer

# ADMINS

class AdminsListCreate(generics.ListCreateAPIView):
    serializer_class = AdminUserSerializer
    def get_queryset(self):
        """
        This view returns a list of all the authors for the currently
        authenticated user.

        Returns empyt list if user Anonymous
        """
        # queryset = AdminUsers.objects.all()
        email = self.request.query_params.get("email")
        password = self.request.query_params.get("password")
        # if not email and not password:
        queryset = AdminUsers.objects.filter(email=email, password=password)
        return queryset


# SUBDIVISION NUMBER DB
class SubdivisionNumberDBListCreate(generics.ListCreateAPIView):
    queryset = SubdivisionNumberDB.objects.all()
    serializer_class = SubdivisionNumerDBSerializer

# Create your views here.
class GetdbNumber(views.APIView):
    
    def get(self, request):
        # kill_sessions
        results = ""
        yourdata=""        
        find_db = find_db_in_path_subdivision(request, self.request.query_params.get("db_number"))
        #find_db = True
        if find_db:
            with in_database(request.session["db_number"]):
            #with in_database("1100"):
                queryset = SubDivision.objects.first()
                if queryset:
                    yourdata = [{"db_number": request.session["db_number"], "found": True, "subdivision_name" : queryset.subdivision_name}]
                    #yourdata = [{"db_number": "1100", "found": True, "subdivision_name" : "test"}]
                results = GetNumberDBSerializer(yourdata, many=True).data
        return Response(results)


class GetUser(views.APIView):
    
    def get(self, request):
        db_number = request.session["db_number"]
        email = self.request.query_params.get("email")
        password = self.request.query_params.get("password")
        yourdata=""
        with in_database(db_number):   
                queryset = AdminUsers.objects.filter(email=email, password=password).first()
                if queryset:
                    yourdata = [{"email":queryset.email, "password":queryset.password}]
        results = GetUserSerializer(yourdata, many=True).data
        return Response(results)