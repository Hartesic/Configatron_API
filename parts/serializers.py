from rest_framework import serializers
from parts.models import CPU, Mobo, GPU, Memory, SSD, HDD, CPUCooling, SoundCard, OpticalDrive, PSU, Case


base_fields = ['category', 'brand', 'name']

class BasePartSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(many=False, read_only=False, slug_field="name")



class CPUSerializer(BasePartSerializer):
    class Meta:
        model = CPU
        fields = base_fields + ['socket', 'frequency']

class MoboSerializer(BasePartSerializer):
    class Meta:
        model = Mobo
        fields = base_fields + ['socket', 'memory_type']

class GPUSerializer(BasePartSerializer):
    class Meta:
        model = GPU
        fields = base_fields + ['chipset', 'memory']

class MemorySerializer(BasePartSerializer):
    class Meta:
        model = Memory
        fields = base_fields + ['count', 'memory_type', 'frequency', 'memory_amount']

class SSDSerializer(BasePartSerializer):
    class Meta:
        model = SSD
        fields = base_fields + ['memory', 'r_speed', 'w_speed']

class HDDSerializer(BasePartSerializer):
    class Meta:
        model = HDD
        fields = base_fields + ['memory', 'speed', 'size']

class CPUCoolingSerializer(BasePartSerializer):
    class Meta:
        model = CPUCooling
        fields = base_fields + ['socket', 'cooling_type']

class SoundCardSerializer(BasePartSerializer):
    class Meta:
        model = SoundCard
        fields = base_fields + ['interface', 'canal_count']

class OpticalDriveSerializer(BasePartSerializer):
    class Meta:
        model = OpticalDrive
        fields = base_fields + ['disk_type', 'speed']

class PSUSerializer(BasePartSerializer):
    class Meta:
        model = PSU
        fields = base_fields + ['power', 'modular', 'certification']

class CaseSerializer(BasePartSerializer):
    class Meta:
        model = Case
        fields = base_fields + ['size']
