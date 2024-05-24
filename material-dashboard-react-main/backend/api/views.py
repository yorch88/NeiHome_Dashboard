from django.shortcuts import render
from dynamic_db_router import in_database
import os
from django.core import serializers
from rest_framework import views
from rest_framework import generics, status
from rest_framework.response import Response
from .models import SubDivision, Street, Neigbor, SubdividionUsers, AdminUsers, SubdivisionNumberDB
from .helpers import find_db_in_path_subdivision
from .serializers import SubDivisionSerializer, StreetSerializer, NeigborSerializer, SubdivisionUsersSerializer, AdminUserSerializer, SubdivisionNumerDBSerializer, GetNumberDBSerializer, GetUserSerializer, AdminUsersDBSerializers


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


##############################SERIALLIZERS#################################
# Create your views here.
class GetdbNumber(views.APIView):
    
    def get(self, request):
        # kill_sessions
        results = ""
        query_data= ""        
        find_db = find_db_in_path_subdivision(request, self.request.query_params.get("db_number"))
        #find_db = True
        if find_db:
            with in_database(request.session["db_number"]):
            #with in_database("1100"):
                queryset = SubDivision.objects.first()
                if queryset:
                    query_data = [{"db_number": request.session["db_number"], "found": True, "subdivision_name" : queryset.subdivision_name}]
                results = GetNumberDBSerializer(query_data, many=True).data
        return Response(results)


class GetUser(views.APIView):
    
    def get(self, request):
        db_number = request.session["db_number"]
        email = self.request.query_params.get("email")
        password = self.request.query_params.get("password")
        serialize_data = ""
        with in_database(db_number):   
                queryset = AdminUsers.objects.filter(email=email, password=password).first()
                if queryset:
                    serialize_data = [{"email":queryset.email, "password":queryset.password}]
        results = GetUserSerializer(serialize_data, many=True).data
        return Response(results)

    
class AdminUsersSerializer(views.APIView):
    def get(self, request):
        # un-comment line below to test with frontend
        #db_number = request.session["db_number"]
        db_number = "1100"
        serialize_data = ""
        with in_database(db_number):
            queryset = AdminUsers.objects.using(db_number).values()
            if queryset:
                serialize_data = list(queryset)
        results = AdminUsersDBSerializers(serialize_data, many=True).data
        return Response(results)
    
    def post(self, request, *args, **kwargs):
        name = request.data["name"]
        role = request.data["role"]
        email = request.data["email"]
        password = request.data["password"]
        id_subdivision = request.data["id_subdivision"]
        phone_number = request.data["phone_number"]
        # un-comment line below to test with frontend
        # db_number = request.session["db_number"]
        db_number = "1100"
        find_subdivision = SubDivision.objects.using(db_number).get(id=id_subdivision)
        create_user = AdminUsers.objects.using(db_number).create(name=name, role=role, email=email, password=password, phone_number=phone_number, id_subdivision=find_subdivision)
        if create_user:
            return Response([{"message":"success"}], status=status.HTTP_201_CREATED)

