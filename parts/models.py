from django.db import models
from categories.models import Category

class CPU(models.Model):
	category = models.ForeignKey(Category, related_name='cpu')
	brand = models.CharField(max_length=20)
	name = models.CharField(max_length=20)
	socket = models.CharField(max_length=10)
	frequency = models.DecimalField(max_digits=2, decimal_places=1)
	def __unicode__(self):
		return self.brand + ' - ' + self.name

class Mobo(models.Model):
	category = models.ForeignKey(Category, related_name='mobo')
	brand = models.CharField(max_length=20)
	name = models.CharField(max_length=30)
	socket = models.CharField(max_length=10)
	memory_type = models.CharField(max_length=10)
	def __unicode__(self):
		return self.brand + ' - ' + self.name

class GPU(models.Model):
	category = models.ForeignKey(Category, related_name='gpu')
	brand = models.CharField(max_length=20)
	name = models.CharField(max_length=20)
	chipset = models.CharField(max_length=30)
	memory = models.PositiveSmallIntegerField(default=0)
	def __unicode__(self):
		return self.brand + ' - ' + self.name

class Memory(models.Model):
	category = models.ForeignKey(Category, related_name='memory')
	brand = models.CharField(max_length=20)
	name = models.CharField(max_length=20)
	count = models.PositiveSmallIntegerField(default=0)
	memory_type = models.CharField(max_length=10)
	frequency = models.DecimalField(max_digits=4, decimal_places=0)
	memory_amount = models.PositiveSmallIntegerField(default=0)
	def __unicode__(self):
		return self.brand + ' - ' + self.name

class SSD(models.Model):
	category = models.ForeignKey(Category, related_name='ssd')
	brand = models.CharField(max_length=20)
	name = models.CharField(max_length=30)
	memory = models.PositiveSmallIntegerField(default=0)
	r_speed = models.PositiveSmallIntegerField(default=0)
	w_speed = models.PositiveSmallIntegerField(default=0)
	def __unicode__(self):
		return self.brand + ' - ' + self.name

class HDD(models.Model):
	category = models.ForeignKey(Category, related_name='hdd')
	brand = models.CharField(max_length=20)
	name = models.CharField(max_length=30)
	memory = models.PositiveSmallIntegerField(default=0)
	speed = models.PositiveSmallIntegerField(default=0)
	size = models.DecimalField(max_digits=2, decimal_places=1)
	def __unicode__(self):
		return self.brand + ' - ' + self.name

class CPUCooling(models.Model):
	category = models.ForeignKey(Category, related_name='cpu_cooling')
	brand = models.CharField(max_length=20)
	name = models.CharField(max_length=30)
	socket = models.CharField(max_length=10)
	cooling_type = models.CharField(max_length=10)
	def __unicode__(self):
		return self.brand + ' - ' + self.name

class SoundCard(models.Model):
	category = models.ForeignKey(Category, related_name='sound_card')
	brand = models.CharField(max_length=20)
	name = models.CharField(max_length=30)
	interface = models.CharField(max_length=20)
	canal_count = models.DecimalField(max_digits=2, decimal_places=1)
	def __unicode__(self):
		return self.brand + ' - ' + self.name

class OpticalDrive(models.Model):
	category = models.ForeignKey(Category, related_name='optical_drive')
	brand = models.CharField(max_length=20)
	name = models.CharField(max_length=30)
	disk_type = models.CharField(max_length=10)
	speed = models.PositiveSmallIntegerField(default=0)
	def __unicode__(self):
		return self.brand + ' - ' + self.name

class PSU(models.Model):
	category = models.ForeignKey(Category, related_name='psu')
	brand = models.CharField(max_length=20)
	name = models.CharField(max_length=30)
	power = models.PositiveSmallIntegerField(default=0)
	modular = models.BooleanField()
	certification = models.CharField(max_length=20)
	def __unicode__(self):
		return self.brand + ' - ' + self.name

class Case(models.Model):
	category = models.ForeignKey(Category, related_name='case')
	brand = models.CharField(max_length=20)
	name = models.CharField(max_length=30)
	size = models.CharField(max_length=10)
	def __unicode__(self):
		return self.brand + ' - ' + self.name