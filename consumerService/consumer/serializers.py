from dataclasses import field, fields
from rest_framework import serializers
from .models import *
from django.db import models
from django.db.models import Q
from django.contrib.auth import authenticate, login

   


    
class DistrictSerializer(serializers.ModelSerializer):       
    class Meta:
        model=District
        fields='__all__'
   


class BlockSerializer(serializers.ModelSerializer):   
    district=serializers.SlugRelatedField(       
       queryset=District.objects.all(),   
       slug_field='district'       
     )
    class Meta:
        model=Block
        fields='__all__'   
   
    

    


class PanchayatSerializer(serializers.ModelSerializer):
    block=serializers.SlugRelatedField(       
       queryset=Block.objects.all(),   
       slug_field='block'       
     )
   
    class Meta:
        model=Panchayat
        fields='__all__'
    

class VillageSerializer(serializers.ModelSerializer):
    panchayat=serializers.SlugRelatedField(       
       queryset=Panchayat.objects.all(),   
       slug_field='panchayat'       
     )
    
    class Meta:
        model=Village
        fields='__all__'
  

class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Division
        fields='__all__'
   

class SubDivisionSerializer(serializers.ModelSerializer):
    division=serializers.SlugRelatedField(       
       queryset=Division.objects.all(),   
       slug_field='division'       
     )
    class Meta:
        model=SubDivision
        fields='__all__'
    
class SectionSerializer(serializers.ModelSerializer):
    subdivision=serializers.SlugRelatedField(       
       queryset=SubDivision.objects.all(),   
       slug_field='subdivision'       
     )
    class Meta:
        model=Section
        fields='__all__'
   

class ConnectionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=ConnectionType
        fields='__all__'
   
class TensionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=TensionType
        fields='__all__'
   
class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tariff
        fields='__all__'
class PhaseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Phase
        fields='__all__'

class LoadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Load
        fields='__all__' 

class ServiceSerializer(serializers.ModelSerializer):
    connection_type=serializers.SlugRelatedField(       
       queryset=ConnectionType.objects.all(),   
       slug_field='connection_type'       
     )
    tension_type=serializers.SlugRelatedField(       
       queryset=TensionType.objects.all(),   
       slug_field='tension_type'       
     )
    tariff=serializers.SlugRelatedField(       
       queryset=Tariff.objects.all(),   
       slug_field='tariff'       
     )
    phase=serializers.SlugRelatedField(       
       queryset=Phase.objects.all(),   
       slug_field='phase'       
     )
    load=serializers.SlugRelatedField(       
       queryset=Load.objects.all(),   
       slug_field='load'       
     )
    class Meta:
        model=Service
        fields='__all__'

class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class UserChangePasswordSerializer(serializers.ModelSerializer):
    new_password=serializers.CharField(max_length=50)
    class Meta:
        model=User
        fields=['password','new_password']
    def validate(self,attrs):       
        old_password=self.instance.password
        password=attrs['password']
        if old_password!=password:
            raise serializers.ValidationError("your password is not match")
        self.instance.password=attrs['new_password']
        self.instance.save()       
        return self.instance
        
class UserForgetPasswordSerializer(serializers.ModelSerializer):
    new_password=serializers.CharField(max_length=50)
    class Meta:
        model=User
        fields=['new_password']
    def validate(self,attrs):       
        old_password=self.instance.password        
        self.instance.password=attrs['new_password']
        self.instance.save()
        return attrs

class ApplicationSerializer(serializers.ModelSerializer):
    user_pk = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', write_only=True
    )
    class Meta:
        model=Application
        fields='__all__'
        depth=1
    
    
    


class AdminSerializer(serializers.ModelSerializer):   
    class Meta:
        model=User
        fields='__all__'
   
      
class OfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Officer
        fields='__all__'  

class VerifySerializer(serializers.ModelSerializer):
    officer_pk = serializers.PrimaryKeyRelatedField(
        queryset=Officer.objects.all(), source='officer', write_only=True
    )
    application_pk = serializers.PrimaryKeyRelatedField(
        queryset=Application.objects.all(), source='application', write_only=True
    )
    
    class Meta:
        model=Verify
        fields='__all__'
        depth=2





