from django.conf.urls import patterns, include, url
from configs import views as configs_views
from parts import views as parts_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'configatron/config', configs_views.ConfigViewSet)
router.register(r'configatron/usage', parts_views.UsageViewSet)
router.register(r'configatron/cpu', parts_views.CPUViewSet)
router.register(r'configatron/mobo', parts_views.MoboViewSet)
router.register(r'configatron/gpu', parts_views.GPUViewSet)
router.register(r'configatron/memory', parts_views.MemoryViewSet)
router.register(r'configatron/ssd', parts_views.SSDViewSet)
router.register(r'configatron/hdd', parts_views.HDDViewSet)
router.register(r'configatron/cpucooling', parts_views.CPUCoolingViewSet)
router.register(r'configatron/soundcard', parts_views.SoundCardViewSet)
router.register(r'configatron/opticaldrive', parts_views.OpticalDriveViewSet)
router.register(r'configatron/psu', parts_views.PSUViewSet)
router.register(r'configatron/case', parts_views.CaseViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
