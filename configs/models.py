from django.db import models
from categories.models import Category
from parts.models import CPU, Mobo, GPU, Memory, SSD, HDD, CPUCooling, SoundCard, OpticalDrive, PSU, Case

class Config(models.Model):
	title = models.CharField(max_length=50)
	category = models.ForeignKey(Category)
	description = models.TextField()
	created = models.DateTimeField(auto_now=True)
	cpu = models.ForeignKey(CPU)
	mobo = models.ForeignKey(Mobo)
	gpu = models.ForeignKey(GPU)
	memory = models.ForeignKey(Memory)
	ssd = models.ForeignKey(SSD)
	hdd = models.ForeignKey(HDD)
	cpu_cooling = models.ForeignKey(CPUCooling)
	sound_card = models.ForeignKey(SoundCard)
	optical_drive = models.ForeignKey(OpticalDrive)
	psu = models.ForeignKey(PSU)
	case = models.ForeignKey(Case)