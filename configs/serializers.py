from rest_framework import serializers
from configs.models import Config

class ConfigSerializer(serializers.ModelSerializer):
    cpu = serializers.PrimaryKeyRelatedField()
    mobo = serializers.PrimaryKeyRelatedField()
    gpu = serializers.PrimaryKeyRelatedField()
    memory = serializers.PrimaryKeyRelatedField()
    ssd = serializers.PrimaryKeyRelatedField()
    hdd = serializers.PrimaryKeyRelatedField()
    cpu_cooling = serializers.PrimaryKeyRelatedField()
    sound_card = serializers.PrimaryKeyRelatedField()
    optical_drive = serializers.PrimaryKeyRelatedField()
    psu = serializers.PrimaryKeyRelatedField()
    case = serializers.PrimaryKeyRelatedField()
    class Meta:
        model = Config
        fields = ['title', 'description', 'created', 'cpu', 'mobo', 'gpu', 'memory', 'ssd', 'hdd', 'cpu_cooling', 'sound_card', 'optical_drive', 'psu', 'case']