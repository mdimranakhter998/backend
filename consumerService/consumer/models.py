from __future__ import division
from django.contrib.auth.models import AbstractUser
from django.db import models
from .manager import UserManage


# Create your models here.
class User(AbstractUser):
    username=None
    first_name=None
    last_name=None 
    name=models.CharField(max_length=100) 
    photo=models.ImageField(upload_to='user/',null=True,blank=True)  
    phone=models.CharField(max_length=12,unique=True)
    email = models.EmailField(max_length=100, unique=True,null=True,blank=True)      
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=('phone','name')
    objects=UserManage()
    def __str__(self):
        return self.email
    



    

   








# applicant models
class Application(models.Model):
    choise_document=[('adhar card','Adhar Card'),
    ('pan card','Pan Card'),
    ('voder id card','Voder Id Card'),
    ('driving license','Driving License'),
    ('ration card','Ration Card'),
    ('BPL','BPL'),
    ('passport','Passport')
    ]
    gender_choice=[
        ('M','Male'),
        ('F','Female'),
        ('O','Other')
    ]
    
    request_no=models.CharField(max_length=100,null=True,blank=True)
    photo=models.ImageField(upload_to='applicant/',null=True,blank=True) 
    father_name=models.CharField(max_length=200)
    gender=models.CharField(max_length=30,choices=gender_choice)  
    address=models.CharField(max_length=200,blank=True,null=True)    
    pincode=models.CharField(max_length=10)
    document_type=models.CharField(max_length=100,choices=choise_document)
    document_file=models.FileField(upload_to="applicant/")
    address_type=models.CharField(max_length=100,choices=choise_document)
    address_front=models.FileField(upload_to='applicant/')
    address_back=models.FileField(upload_to='applicant/')
    owner_file=models.FileField(upload_to="applicant/")    
    district=models.CharField(max_length=100)
    block=models.CharField(max_length=100)
    panchayat=models.CharField(max_length=100)
    village=models.CharField(max_length=100)
    division=models.CharField(max_length=100)
    subdivision=models.CharField(max_length=100)
    section=models.CharField(max_length=100)
    connection_type=models.CharField(max_length=100)
    tension_type=models.CharField(max_length=100)
    tariff=models.CharField(max_length=100)
    phase=models.PositiveBigIntegerField()
    load=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)  
    created_date=models.DateTimeField(auto_now=True) 
    is_verified=models.BooleanField(default=False) 
    is_submited=models.BooleanField(default=False)  
    is_defected=models.BooleanField(default=False)
    is_rejected=models.BooleanField(default=False)    


    status=models.CharField(max_length=300,null=True,blank=True)
    # def __str__(self):
    #     return self.user  
    
    class Meta:
        db_table="Application"  
    

    
    

class District(models.Model):   
    district=models.CharField(max_length=200,unique=True)
    def __str__(self):
        return self.district
    class Meta:
        db_table="District"
   


class Block(models.Model):    
    block=models.CharField(max_length=200,unique=True)
    district=models.ForeignKey(District,on_delete=models.SET_NULL,null=True)    
    def __str__(self):
        return self.block
    class Meta:
        db_table="Block"
    

class Panchayat(models.Model):    
    panchayat=models.CharField(max_length=200,unique=True)
    block=models.ForeignKey(Block,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.panchayat
    class Meta:
        db_table="Panchayat"
    
class Village(models.Model):    
    village=models.CharField(max_length=200,unique=True)
    panchayat=models.ForeignKey(Panchayat,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.village
    class Meta:
        db_table="Village"
   

class Division(models.Model):    
    division=models.CharField(max_length=200,unique=True)   
    def __str__(self):
        return self.division
    class Meta:
        db_table="Division"
   
class SubDivision(models.Model):    
    subdivision=models.CharField(max_length=200,unique=True)
    division=models.ForeignKey(Division,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.subdivision
    class Meta:
        db_table="SubDivision"
   

class Section(models.Model):    
    section=models.CharField(max_length=200,unique=True)
    subdivision=models.ForeignKey(SubDivision,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.section
    class Meta:
        db_table="Section"
    
class ConnectionType(models.Model):  
    connection_choice=[
        ('Domestic','Domestic'),
        ('Commercial','Commercial'),
        ('Industrial','Industrial'),
        ('Agriculture','Agriculture')
    ]
    connection_type=models.CharField(max_length=200,choices=connection_choice,unique=True)   
    def __str__(self):
        return self.connection_type
    class Meta:
        db_table="Connection Type"
   
class TensionType(models.Model): 
    tension_choice=[
        ('Low Tension','Low Tension'),
        ('High Tension','High Tension')
    ]   
    tension_type = models.CharField(max_length=50,choices=tension_choice,unique=True)
    def __str__(self):
        return self.tension_type
    class Meta:
        db_table="Tension Type"

class Tariff(models.Model): 
    tariff_choice=[
        ('HTS-I','HTS-I'),
        ('HTS-II','HTS-II'),
        ('HTS-III','HTS-III'),
        ('HTS-IV','HTS-IV'),
        ('HTSS','HTSS'),
        ('LTIS1D','LTIS1D'),
        ('LTIS2D','LTIS2D'),
        ('NDS1D','NDS1D'),
        ('LTEV','LTEV'),        
        ('KJ','KJ'),
        ('DS1D','DS1D'),
        ('DS3D','DS3D')

    ]   
    tariff = models.CharField(max_length=50,choices=tariff_choice, unique=True)
    def __str__(self):
        return self.tariff
    class Meta:
        db_table="Tariff"

class Phase(models.Model):
    phase_choice=[
        (1,1),
        (3,3)
    ]
    phase=models.PositiveIntegerField(choices=phase_choice,unique=True)
    def __str__(self):
        return str(self.phase)
    class Meta:
        db_table="Phase"

class Load(models.Model):
    load_choice=[
        ('50-1500 KVA','50-1500 KVA'),
        ('500-15000 KVA','500-15000 KVA'),
        ('7500 KVA and above','7500 KVA and above'),
        ('10000 KVA and above','10000 KVA and above'),
        ('300 KVA and above','300 KVA and above'),
        ('1-7 KW','1-7 KW'),
        ('1-19 KW','1-19 KW'),
        ('20-74 KW','20-74 KW'),
        ('5-70 KW','5-70 KW'),
        ('1-250 WT','1-250 WT'),
        ('7-70 KW','7-70 KW'),        
    ]
    load=models.CharField(max_length=100,choices=load_choice,unique=True)
    def __str__(self):
        return self.load
    class Meta:
        db_table="Load"
    
    
    

    


class Service(models.Model):  
    connection_type=models.ForeignKey(ConnectionType,on_delete=models.SET_NULL,null=True)
    tension_type=models.ForeignKey(TensionType,on_delete=models.SET_NULL,null=True)
    tariff=models.ForeignKey(Tariff,on_delete=models.SET_NULL,null=True)
    phase=models.ForeignKey(Phase,on_delete=models.SET_NULL,null=True)
    load=models.ForeignKey(Load,on_delete=models.SET_NULL,null=True)    
   
    class Meta:
        db_table="Service"

class Officer(User):     
    division=models.CharField(max_length=100)
    subdivision=models.CharField(max_length=100)
    section=models.CharField(max_length=100)
    designation=models.CharField(max_length=200)  
    
    class Meta:
        db_table="Officer"

class Verify(models.Model):
    remark=models.TextField(null=True,blank=True)
    application=models.ForeignKey(Application,on_delete=models.CASCADE)
    officer=models.ForeignKey(Officer,on_delete=models.SET_NULL,null=True)
    created_date=models.DateTimeField(auto_now=True)
    action=models.CharField(max_length=50)
    class Meta:
        db_table="Verify"









