from rest_framework import routers
from .api import SpecialtyView, DoctorView, DetailDoctorView


router = routers.DefaultRouter()
router.register(r'specialty' ,SpecialtyView , 'specialty')
router.register(r'doctor' ,DoctorView , 'doctor') 
router.register(r'detail' ,DetailDoctorView , 'detail') 

urlpatterns = router.urls
