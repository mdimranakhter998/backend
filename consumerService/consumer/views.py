from email import message
from email.mime import application

from requests import request
from .serializers import *
from rest_framework.response import Response
from .models import *
from rest_framework import status
from rest_framework.viewsets import *
from django.db.models import Q
from .utils import *
from rest_framework.permissions import *
import uuid


class ApplicationViewSet(ViewSet):   
    def list(self,request):       
        try:
            application=Application.objects.filter(is_verified=False)         
            serializers=ApplicationSerializer(application,many=True)
            return Response(data=serializers.data)
        except Application.DoesNotExist:
            return Response(data={"message":"No data is Found"},status=status.HTTP_204_NO_CONTENT)
    def create(self,request):               
        serializers=ApplicationSerializer(data=request.data)         
        if serializers.is_valid():                    
            serializers.save()
            return Response(data={"message":"your applicantion has succefully submitted"},status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
        
    def retrieve(self,request,pk):        
        try:
            application=Application.objects.filter(Q(request_no=pk)|Q(user__phone=pk)).select_related('user')
            serializers=ApplicationSerializer(application,many=True,context={'request': request})
            return Response(data=serializers.data,status=status.HTTP_202_ACCEPTED)
        except Application.DoesNotExist:
            return Response({"message":"your data have not Found"},status=status.HTTP_406_NOT_ACCEPTABLE)

    def partial_update(self,request,pk):           
        try:   
            print(request.data)
            application=Application.objects.get(Q(id=pk)|Q(request_no=pk)) 
            print(application.father_name)                             
            serializers=ApplicationSerializer(application,data=request.data,partial=True)            
            if serializers.is_valid():                                         
                serializers.save() 
                print("success")                      
                return Response(data={"message":"you have successfuly update your data"},status=status.HTTP_202_ACCEPTED,content_type="application/json")
            else:
                return Response(data=serializers.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

        
    def destroy(self,request,pk):
        try:
            application=Application.objects.get(id=pk)
            serializers=ApplicationSerializer(application)
            serializers.delete()
            return Response(data={"your data is deleted successfully"},status=status.HTTP_202_ACCEPTED)
        except Application.DoesNotExist:
            return Response({"message":"your data have not Found"},status=status.HTTP_204_NO_CONTENT)
   

class DistrictViewSet(ViewSet):
    def list(self, request):  
        try: 
            districts=District.objects.all()        
            serializers=DistrictSerializer(districts,many=True)            
            return Response(data=serializers.data,status=status.HTTP_200_OK)
        except District.DoesNotExist:
            return Response(data=serializers.errors,status=status.HTTP_404_NOT_FOUND)

    def retrieve(self,request,pk):       
        try:  
            district=District.objects.filter(id=pk)                 
            serializers=DistrictSerializer(district,many=True)            
            return Response(data=serializers.data,status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def create(self,request):            
        serializers=DistrictSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=["you have added Successfully"],status=status.HTTP_201_CREATED,content_type="application/json")
        else:
            return Response(data=serializers.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

    def partial_update(self,request,pk):           
        try:  
            district=District.objects.get(id=pk)                         
            serializers=DistrictSerializer(district,data=request.data,partial=True)
            if serializers.is_valid():
                dis=serializers.validated_data['district']               
                serializers.save()           
            return Response(data={"message":"you have successfuly update your data"},status=status.HTTP_202_ACCEPTED,content_type="application/json")
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk):       
        try:          
            district=District.objects.get(id=pk).delete()               
            return Response(data={"message":"you have successfuly delete your data"},status=status.HTTP_202_ACCEPTED)
        except District.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)




class BlockViewSet(ViewSet):
    def list(self, request):           
            block=Block.objects.all()       
            serializers=BlockSerializer(block,many=True)            
            return Response(data=serializers.data,status=status.HTTP_200_OK)

    def retrieve(self,request,pk):
        try:  
            block=Block.objects.filter(Q(district=pk)|Q(id=pk))
            serializers=BlockSerializer(block,many=True)           
            return Response(data=serializers.data,status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)  


    def create(self,request):                      
        serializers=BlockSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()                   
            return Response({"message":"you have added Successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

    def destroy(self,request,pk):       
        try:  
            block=Block.objects.get(id=pk)       
            block.delete()
            return Response(data={"message":"you have successfuly delete your data"},status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def partial_update(self,request,pk):          
        try:  
            block=Block.objects.get(id=pk)               
            serializers=BlockSerializer(block,data=request.data,partial=True)
            if serializers.is_valid():
                serializers.save()           
            return Response(data={"message":"you have successfuly update your data"},status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class PanchayatViewSet(ViewSet):
    def list(self,request):       
        panchayat=Panchayat.objects.all()        
        serializers=PanchayatSerializer(panchayat,many=True)            
        return Response(data=serializers.data,status=status.HTTP_200_OK)

    def retrieve(self,request,pk):
        try:  
            panchayat=Panchayat.objects.filter(Q(block=pk)|Q(id=pk))       
            serializers=PanchayatSerializer(panchayat,many=True)
            return Response(data=serializers.data,status=status.HTTP_202_ACCEPTED)
        except:
                return Response(status=status.HTTP_400_BAD_REQUEST)  

    def create(self,request):             
        serializers=PanchayatSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"message":"you have added Successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

    def destroy(self,request,pk):       
        try:  
            panchayat=Panchayat.objects.get(id=pk)       
            panchayat.delete()
            return Response(data={"message":"you have successfuly delete your data"},status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self,request,pk):        
        try:  
            panchayat=Panchayat.objects.get(id=pk)               
            serializers=PanchayatSerializer(panchayat,data=request.data,partial=True)
            if serializers.is_valid():
                serializers.save()           
            return Response(data={"message":"you have successfuly update your data"},status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class VillageViewSet(ViewSet):
    def list(self, request):       
        village=Village.objects.all()      
        serializers=VillageSerializer(village,many=True)            
        return Response(data=serializers.data,status=status.HTTP_200_OK)

    def retrieve(self,request,pk):
        try:  
            village=Village.objects.filter(Q(panchayat=pk)|Q(id=pk))       
            serializers=VillageSerializer(village,many=True)
            return Response(data=serializers.data,status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)  



    def create(self,request):       
        serializers=VillageSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"message":"you have added Successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

    def destroy(self,request,pk):       
        try:  
            village=Village.objects.get(id=pk)       
            village.delete()
            return Response(data={"message":"you have successfuly delete your data"},status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self,request,pk):   
            
        try:  
            village=Village.objects.get(id=pk)               
            serializers=VillageSerializer(village,data=request.data,partial=True)
            if serializers.is_valid():
                serializers.save()           
            return Response(data={"message":"you have successfuly update your data"},status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)





class DivisionViewSet(ViewSet):
    def list(self, request):      
        division=Division.objects.all()        
        serializers=DivisionSerializer(division,many=True)            
        return Response(data=serializers.data,status=status.HTTP_200_OK)

    def retrieve(self,request,pk):
        try:  
            division=Division.objects.filter(id=pk)       
            serializers=DivisionSerializer(division,many=True)
            return Response(data=serializers.data,status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST) 


    def create(self,request):       
        serializers=DivisionSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"message":"you have added Successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

    def destroy(self,request,pk):       
        try:  
            division=Division.objects.get(id=pk)       
            division.delete()
            return Response(data={"message":"you have successfuly delete your data"},status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self,request,pk):        
        try: 
           
            division=Division.objects.get(id=pk)               
            serializers=DivisionSerializer(division,data=request.data,partial=True)
            if serializers.is_valid():
                serializers.save()           
            return Response(data={"message":"you have successfuly update your data"},status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)




class SubdivisionViewSet(ViewSet):
    def list(self, request):      
        subdivision=SubDivision.objects.all()       
        serializers=SubDivisionSerializer(subdivision,many=True)            
        return Response(data=serializers.data,status=status.HTTP_200_OK)

    def retrieve(self,request,pk):
        try:  
            subdivision=SubDivision.objects.filter(Q(division=pk)|Q(id=pk))       
            serializers=SubDivisionSerializer(subdivision,many=True)
            return Response(data=serializers.data,status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)  


    def create(self,request):       
        serializers=SubDivisionSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"message":"you have added Successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

    def destroy(self,request,pk):       
        try:  
            subdivision=SubDivision.objects.get(id=pk)       
            subdivision.delete()
            return Response(data={"message":"you have successfuly delete your data"},status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self,request,pk):        
        try:  
            subdivision=SubDivision.objects.get(id=pk)               
            serializers=SubDivisionSerializer(subdivision,data=request.data,partial=True)
            if serializers.is_valid():
                serializers.save()           
            return Response(data={"message":"you have successfuly update your data"},status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)



class SectionViewSet(ViewSet):
    def list(self, request):       
        section=Section.objects.all()       
        serializers=SectionSerializer(section,many=True)            
        return Response(data=serializers.data,status=status.HTTP_200_OK)

    def retrieve(self,request,pk):        
        try:  
            section=Section.objects.filter(Q(id=pk)|Q(subdivision=pk))       
            serializers=SectionSerializer(section,many=True)
            return Response(data=serializers.data,status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)  



    def create(self,request):       
        serializers=SectionSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"message":"you have added Successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

    def destroy(self,request,pk):       
        try:  
            section=Section.objects.get(id=pk)       
            section.delete()
            return Response(data={"message":"you have successfuly delete your data"},status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def partial_update(self,request,pk):            
        try:  
            section=Section.objects.get(id=pk)               
            serializers=SectionSerializer(section,data=request.data,partial=True)
            if serializers.is_valid():
                serializers.save()           
            return Response(data={"message":"you have successfuly update your data"},status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        
class ConnectionTypeViewSet(ViewSet):
    def list(self, request):       
        connection=ConnectionType.objects.all()        
        serializers=ConnectionTypeSerializer(connection,many=True)            
        return Response(data=serializers.data,status=status.HTTP_200_OK)

    def retrieve(self,request,pk):        
        try:  
            connection=ConnectionType.objects.filter(id=pk)       
            serializers=ConnectionTypeSerializer(connection,many=True)
            return Response(data=serializers.data,status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)  



    def create(self,request):   
           
        serializers=ConnectionTypeSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"message":"you have added Successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

    def destroy(self,request,pk):       
        try:  
            connection=ConnectionType.objects.get(id=pk)       
            connection.delete()
            return Response(data={"message":"you have successfuly delete your data"},status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def partial_update(self,request,pk):             
        try:  
            connection=ConnectionType.objects.get(id=pk)               
            serializers=ConnectionTypeSerializer(connection,data=request.data,partial=True)
            if serializers.is_valid():
                serializers.save()           
            return Response(data={"message":"you have successfuly update your data"},status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
class TensionTypeViewSet(ViewSet):
    def list(self, request):       
        tension=TensionType.objects.all()        
        serializers=TensionTypeSerializer(tension,many=True)            
        return Response(data=serializers.data,status=status.HTTP_200_OK)

    def retrieve(self,request,pk):        
        try:  
            tension=TensionType.objects.filter(id=pk)       
            serializers=TensionTypeSerializer(tension,many=True)
            return Response(data=serializers.data,status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)  



    def create(self,request):       
        serializers=TensionTypeSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"message":"you have added Successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

    def destroy(self,request,pk):       
        try:  
            tension=TensionType.objects.get(id=pk)       
            tension.delete()
            return Response(data={"message":"you have successfuly delete your data"},status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def partial_update(self,request,pk):        
        try:  
            tension=TensionType.objects.get(id=pk)               
            serializers=TensionTypeSerializer(tension,data=request.data,partial=True)
            if serializers.is_valid():
                serializers.save()           
            return Response(data={"message":"you have successfuly update your data"},status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
class TariffViewSet(ViewSet):
    def list(self, request):       
        tariff=Tariff.objects.all()        
        serializers=TariffSerializer(tariff,many=True)            
        return Response(data=serializers.data,status=status.HTTP_200_OK)

    def retrieve(self,request,pk):        
        try:  
            tariff=Tariff.objects.filter(id=pk)       
            serializers=TariffSerializer(tariff,many=True)
            return Response(data=serializers.data,status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)  



    def create(self,request):       
        serializers=TariffSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"message":"you have added Successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

    def destroy(self,request,pk):       
        try:  
            tariff=Tariff.objects.get(id=pk)       
            tariff.delete()
            return Response(data={"message":"you have successfuly delete your data"},status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def partial_update(self,request,pk):        
        try:  
            tariff=Tariff.objects.get(id=pk)               
            serializers=TariffSerializer(tariff,data=request.data,partial=True)
            if serializers.is_valid():
                serializers.save()           
            return Response(data={"message":"you have successfuly update your data"},status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class PhaseViewSet(ViewSet):
    def list(self, request):       
        phase=Phase.objects.all()        
        serializers=PhaseSerializer(phase,many=True)            
        return Response(data=serializers.data,status=status.HTTP_200_OK)

    def retrieve(self,request,pk):        
        try:  
            phase=Phase.objects.filter(id=pk)       
            serializers=PhaseSerializer(phase,many=True)
            return Response(data=serializers.data,status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)  



    def create(self,request):       
        serializers=PhaseSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"message":"you have added Successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

    def destroy(self,request,pk):       
        try:  
            phase=Phase.objects.get(id=pk)       
            phase.delete()
            return Response(data={"message":"you have successfuly delete your data"},status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def partial_update(self,request,pk):        
        try:  
            phase=Phase.objects.get(id=pk)               
            serializers=PhaseSerializer(phase,data=request.data,partial=True)
            if serializers.is_valid():
                serializers.save()           
            return Response(data={"message":"you have successfuly update your data"},status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class LoadViewSet(ViewSet):
    def list(self, request):       
        load=Load.objects.all()        
        serializers=LoadSerializer(load,many=True)            
        return Response(data=serializers.data,status=status.HTTP_200_OK)

    def retrieve(self,request,pk):        
        try:  
            load=Load.objects.filter(id=pk)       
            serializers=LoadSerializer(load,many=True)
            return Response(data=serializers.data,status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)  



    def create(self,request):       
        serializers=LoadSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"message":"you have added Successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

    def destroy(self,request,pk):       
        try:  
            load=Load.objects.get(id=pk)       
            load.delete()
            return Response(data={"message":"you have successfuly delete your data"},status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def partial_update(self,request,pk):        
        try:  
            load=Load.objects.get(id=pk)               
            serializers=LoadSerializer(load,data=request.data,partial=True)
            if serializers.is_valid():
                serializers.save()           
            return Response(data={"message":"you have successfuly update your data"},status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class ServiceViewSet(ViewSet):
    def list(self, request):       
        service=Service.objects.all()        
        serializers=ServiceSerializer(service,many=True)            
        return Response(data=serializers.data,status=status.HTTP_200_OK)
    
    def create(self,request):       
        serializers=ServiceSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"message":"you have added Successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

    def destroy(self,request,pk):       
        try:  
            service=Service.objects.get(id=pk)       
            service.delete()
            return Response(data={"message":"you have successfuly delete your data"},status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def partial_update(self,request,pk):        
        try:  
            service=Service.objects.get(id=pk)               
            serializers=ServiceSerializer(service,data=request.data,partial=True)
            if serializers.is_valid():
                serializers.save()           
            return Response(data={"message":"you have successfuly update your data"},status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self,request,pk):        
        try:  
            service=Service.objects.filter(Q(connection_type=pk)|Q(id=pk)).select_related('connection_type').select_related('tension_type').select_related('tariff').select_related('phase').select_related('load').distinct()     
            serializers=ServiceSerializer(service,many=True)
            return Response(data=serializers.data,status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST) 
        

class ApplicantViewSet(ViewSet):   
    def create(self,request):          
        serializers=ApplicantSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"message":"you have added Successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
            
    def retrieve(self,request,pk):  
        print("imran chal")      
        try:  
            user=User.objects.filter(Q(phone=pk)|Q(email=pk))       
            serializers= ApplicantSerializer(user,many=True)
            return Response(data=serializers.data,status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)  
    def destroy(self,request,pk):       
        try:  
            user=User.objects.get(id=pk)       
            user.delete()
            return Response(data={"message":"you have successfuly delete your data"},status=status.HTTP_202_ACCEPTED)
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def partial_update(self,request,pk):        
        try:
            print(request.data,pk)  
            user=User.objects.get(id=pk)               
            serializers=AdminSerializer(user,data=request.data,partial=True)
            if serializers.is_valid():
                serializers.save()           
            return Response(data={"message":"you have successfuly update your data"},status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ApplicantSignInViewSet(ViewSet):
    def create(self,request):       
        phone=request.data.get('phone')
        password=request.data.get('password')
        try:
            applicant=User.objects.get(Q(phone=phone)&Q(password=password))
           
            token=get_token(applicant)           
            return Response(data=token,status=status.HTTP_202_ACCEPTED)        
        except User.DoesNotExist:
            return Response(data={"message":"your phone or password is incorrect"},status=status.HTTP_401_UNAUTHORIZED)
    
class UserChangePasswordViewSet(ViewSet):
    permission_classes=[IsAuthenticated]    
    def create(self,request):
        print(request.user)
        serializer=UserChangePasswordSerializer(data=request.data,instance=request.user)
        if serializer.is_valid():                      
            return Response(data={"message":"your password has successfully changed"},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

class UserForgetPasswordViewSet(ViewSet):   
    def create(self,request):        
        serializer=UserForgetPasswordSerializer(data=request.data,instance=request.user)
        if serializer.is_valid():                     
            return Response(data={"message":"your password has changed successfully" },status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

class AdminSignInViewSet(ViewSet):
   def create(self,request):              
        email=request.data.get('email')
        password=request.data.get('password')
        try:
            user=User.objects.get(Q(email=email)&Q(password=password)) 
            print(user)          
            token=get_token(user)  
            print(token)         
            return Response(data=token,status=status.HTTP_202_ACCEPTED)        
        except User.DoesNotExist:
            return Response(data={"message":"your phone or password is incorrect"},status=status.HTTP_401_UNAUTHORIZED)

class AdminGetUser(ViewSet):
    permission_classes=[IsAuthenticated]   
    def list(self,request):
        serializer=AdminSerializer(request.user,context={'request': request})
        print(serializer.data)        
        return Response(data=serializer.data,status=status.HTTP_202_ACCEPTED)


class AdminViewSet(ViewSet):       
    def create(self,request):         
        serializers=AdminSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"message":"you have added Successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
        
    def list(self,request):           
        try:  
            user=User.objects.all()     
            serializers=AdminSerializer(user,many=True, context={'request': request})
            return Response(data=serializers.data,status=status.HTTP_202_ACCEPTED)
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST) 
        
    def retrieve(self,request,pk):             
        try:  
            print(pk)
            print("imran")
            user=User.objects.filter(Q(phone=pk)|Q(email=pk))       
            serializers= AdminSerializer(user,many=True)
            return Response(data=serializers.data,status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)  
        
         
    def destroy(self,request,pk):       
        try:  
            user=User.objects.get(id=pk)       
            user.delete()
            return Response(data={"message":"you have successfuly delete your data"},status=status.HTTP_202_ACCEPTED)
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def partial_update(self,request,pk):  
        print(pk,request.data)      
        try:  
            user=User.objects.get(Q(id=pk)|Q(phone=pk)|Q(email=pk))  
            print(user)                              
            serializers=AdminSerializer(user,data=request.data,partial=True)           
            if serializers.is_valid():
                serializers.save()  
                print("imran")  
                print(serializers.data)       
            return Response(data={"message":"you have successfuly update your data"},status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    

class OfficerViewSet(ViewSet):
    def create(self,request):              
        serializers=OfficerSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"message":"you have added Successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
        
    def list(self,request):           
        try:  
            officer=Officer.objects.all()     
            serializers=OfficerSerializer(officer,many=True)
            return Response(data=serializers.data,status=status.HTTP_202_ACCEPTED)
        except Officer.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST) 
         
    def destroy(self,request,pk):       
        try:  
            officer=Officer.objects.get(id=pk)       
            officer.delete()
            return Response(data={"message":"you have successfuly delete your data"},status=status.HTTP_202_ACCEPTED)
        except Officer.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def partial_update(self,request,pk):        
        try:   
            print(request,pk)      
            officer=Officer.objects.get(id=pk)               
            serializers=OfficerSerializer(officer,data=request.data,partial=True)
            if serializers.is_valid():
                serializers.save()                  
            return Response(data={"message":"you have successfuly update your data"},status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class OfficerSignInViewSet(ViewSet):
   def create(self,request):             
        email=request.data.get('email')
        password=request.data.get('password')
        try:
            officer=Officer.objects.get(Q(email=email)&Q(password=password))                     
            token=get_token(officer)                  
            return Response(data=token,status=status.HTTP_202_ACCEPTED)        
        except Officer.DoesNotExist:
            return Response(data={"message":"your email or password is incorrect"},status=status.HTTP_401_UNAUTHORIZED)

class VerifyViewSet(ViewSet):
    def create(self,request):    
        print(request.data)          
        serializers=VerifySerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"message":"you have added Successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

    def retrieve(self,request,pk): 
        print(request.data,pk)            
        try:           
            verify=Verify.objects.select_related('application').select_related('officer').filter(application__request_no=pk) 
            print(verify)      
            serializers=VerifySerializer(verify,many=True)
            return Response(data=serializers.data,status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)  
        
    def list(self,request):           
        try:  
            verify=Verify.objects.all()     
            serializers=VerifySerializer(verify,many=True)
            return Response(data=serializers.data,status=status.HTTP_202_ACCEPTED)
        except Verify.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST) 
         
    def destroy(self,request,pk):       
        try:  
            verify=Verify.objects.get(id=pk)       
            verify.delete()
            return Response(data={"message":"you have successfuly delete your data"},status=status.HTTP_202_ACCEPTED)
        except Officer.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def partial_update(self,request,pk):        
        try:                 
            verify=Verify.objects.get(request_no=pk)               
            serializers=OfficerSerializer(verify,data=request.data,partial=True)
            if serializers.is_valid():
                serializers.save()                  
            return Response(data={"message":"you have successfuly update your data"},status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

   








    
















    















    
















    
















    
















    
















    











