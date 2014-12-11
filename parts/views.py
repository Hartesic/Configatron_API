from rest_framework import viewsets
from parts.models import CPU, Mobo, GPU, Memory, SSD, HDD, CPUCooling, SoundCard, OpticalDrive, PSU, Case
from parts.serializers import CPUSerializer, MoboSerializer, GPUSerializer, MemorySerializer, SSDSerializer, HDDSerializer, CPUCoolingSerializer, SoundCardSerializer, OpticalDriveSerializer, PSUSerializer, CaseSerializer

class CPUViewSet(viewsets.ModelViewSet):
    queryset = CPU.objects.all()
    serializer_class = CPUSerializer

class MoboViewSet(viewsets.ModelViewSet):
    queryset = Mobo.objects.all()
    serializer_class = MoboSerializer

class GPUViewSet(viewsets.ModelViewSet):
    queryset = GPU.objects.all()
    serializer_class = GPUSerializer

class MemoryViewSet(viewsets.ModelViewSet):
    queryset = Memory.objects.all()
    serializer_class = MemorySerializer

class SSDViewSet(viewsets.ModelViewSet):
    queryset = SSD.objects.all()
    serializer_class = SSDSerializer

class HDDViewSet(viewsets.ModelViewSet):
    queryset = HDD.objects.all()
    serializer_class = HDDSerializer

class CPUCoolingViewSet(viewsets.ModelViewSet):
    queryset = CPUCooling.objects.all()
    serializer_class = CPUCoolingSerializer

class SoundCardViewSet(viewsets.ModelViewSet):
    queryset = SoundCard.objects.all()
    serializer_class = SoundCardSerializer

class OpticalDriveViewSet(viewsets.ModelViewSet):
    queryset = OpticalDrive.objects.all()
    serializer_class = OpticalDriveSerializer

class PSUViewSet(viewsets.ModelViewSet):
    queryset = PSU.objects.all()
    serializer_class = PSUSerializer

class CaseViewSet(viewsets.ModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer