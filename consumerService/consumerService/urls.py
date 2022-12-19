"""consumerService URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from consumer.views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView



router=DefaultRouter()
router.register('admin/signin',AdminSignInViewSet,basename="admin-signin")
router.register('admin/signup',AdminViewSet,basename="admin-signin")
router.register('admin/district',DistrictViewSet,basename="admin-district")
router.register('admin/block',BlockViewSet,basename="admin-block")
router.register('admin/panchayat',PanchayatViewSet,basename="admin-panchayat")
router.register('admin/village',VillageViewSet,basename="admin-village")
router.register('admin/division',DivisionViewSet,basename="admin-division")
router.register('admin/subdivision',SubdivisionViewSet,basename="admin-subdivision")
router.register('admin/section',SectionViewSet,basename="admin-section")
router.register('admin/connectiontype',ConnectionTypeViewSet,basename="admin-connectiontype")
router.register('admin/tensiontype',TensionTypeViewSet,basename="admin-tensiontype")
router.register('admin/tariff',TariffViewSet,basename="admin-tariff")
router.register('admin/phase',PhaseViewSet,basename="admin-phase")
router.register('admin/load',LoadViewSet,basename="admin-load")
router.register('admin/service',ServiceViewSet,basename="admin-service")
router.register('applicant/signin',ApplicantSignInViewSet,basename="applicant-signin")
router.register('applicant/signup',ApplicantViewSet,basename="applicant-signup")
router.register('application',ApplicationViewSet,basename="application")
router.register('user/changepassword',UserChangePasswordViewSet,basename="user-changepassword")
router.register('user/forgetpassword',UserForgetPasswordViewSet,basename="user-forgetpassword")
router.register('officer/signin',OfficerSignInViewSet,basename="officer-signin")
router.register('officer/signup',OfficerViewSet,basename="officer-signup")
router.register('officer/signup',OfficerViewSet,basename="officer-signup")
router.register('admin/getuser',AdminGetUser,basename="admin-getuser")
router.register('officer/verify',VerifyViewSet,basename="officer-verify")










urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  
   
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
