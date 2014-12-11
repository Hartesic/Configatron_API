from rest_framework import serializers
from categories.models import Category
from parts.serializers import CPUSerializer, MoboSerializer, GPUSerializer, MemorySerializer, SSDSerializer, HDDSerializer, CPUCoolingSerializer, SoundCardSerializer, OpticalDriveSerializer, PSUSerializer, CaseSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class SpecificPartsSerializer(serializers.ModelSerializer):
	cpu = CPUSerializer(many=True, read_only=True)
	mobo = MoboSerializer(many=True, read_only=True)
	gpu = GPUSerializer(many=True, read_only=True)
	memory = MemorySerializer(many=True, read_only=True)
	ssd = SSDSerializer(many=True, read_only=True)
	hdd = HDDSerializer(many=True, read_only=True)
	cpu_cooling = CPUCoolingSerializer(many=True, read_only=True)
	sound_card = SoundCardSerializer(many=True, read_only=True)
	optical_drive = OpticalDriveSerializer(many=True, read_only=True)
	psu = PSUSerializer(many=True, read_only=True)
	case = CaseSerializer(many=True, read_only=True)
	class Meta:
		model = Category
		fields = ['cpu', 'mobo', 'gpu', 'memory', 'ssd', 'hdd', 'cpu_cooling', 'sound_card', 'optical_drive', 'psu', 'case']
