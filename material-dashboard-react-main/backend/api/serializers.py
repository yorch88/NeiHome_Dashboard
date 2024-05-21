from rest_framework import serializers
from .models import SubDivision, Street, Neigbor, SubdividionUsers, AdminUsers, SubdivisionNumberDB

class SubDivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubDivision
        fields = ["id", "typedivision", "subdivision_name", "address", "representatives", "cp"]

class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = ["name", "id_subdivision"]

class NeigborSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neigbor
        fields = ["name", "phone",  "email", "home_number", "role", "id_street"]

class SubdivisionUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubdividionUsers
        fields = ["email", "password", "id_subdivision", "id_neigbor"]

class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminUsers
        fields = ["name", "role", "email", "password", "phone_number", "id_subdivision"]

class SubdivisionNumerDBSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubdivisionNumberDB
        fields = ["number", "name_subdivision"]

class GetNumberDBSerializer(serializers.Serializer):
    db_number = serializers.CharField(max_length=200)
    found = serializers.BooleanField()
    subdivision_name = serializers.CharField(max_length=200)

class GetUserSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=200)
    #password = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=100)