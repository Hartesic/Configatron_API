from django.db import models

class Usage(models.Model):
	name = models.CharField(max_length=20)
	def __unicode__(self):
		return self.name

class CPU(models.Model):
	usage = models.ForeignKey(Usage)
	brand = models.CharField(max_length=20)
	name = models.CharField(max_length=20)
	socket = models.CharField(max_length=10)
	frequency = models.DecimalField(max_digits=2, decimal_places=1)
	def __unicode__(self):
		return self.brand + ' - ' + self.name

class Mobo(models.Model):
	usage = models.ForeignKey(Usage)
	brand = models.CharField(max_length=20)
	name = models.CharField(max_length=30)
	socket = models.CharField(max_length=10)
	memory_type = models.CharField(max_length=10)
	def __unicode__(self):
		return self.brand + ' - ' + self.name

class GPU(models.Model):
	usage = models.ForeignKey(Usage)
	brand = models.CharField(max_length=20)
	name = models.CharField(max_length=20)
	chipset = models.CharField(max_length=30)
	memory = models.PositiveSmallIntegerField(default=0)
	def __unicode__(self):
		return self.brand + ' - ' + self.name

class Memory(models.Model):
	usage = models.ForeignKey(Usage)
	brand = models.CharField(max_length=20)
	name = models.CharField(max_length=20)
	count = models.PositiveSmallIntegerField(default=0)
	memory_type = models.CharField(max_length=10)
	frequency = models.DecimalField(max_digits=4, decimal_places=0)
	memory_amount = models.PositiveSmallIntegerField(default=0)
	def __unicode__(self):
		return self.brand + ' - ' + self.name

class SSD(models.Model):
	usage = models.ForeignKey(Usage)
	brand = models.CharField(max_length=20)
	name = models.CharField(max_length=30)
	memory = models.PositiveSmallIntegerField(default=0)
	r_speed = models.PositiveSmallIntegerField(default=0)
	w_speed = models.PositiveSmallIntegerField(default=0)
	def __unicode__(self):
		return self.brand + ' - ' + self.name

class HDD(models.Model):
	usage = models.ForeignKey(Usage)
	brand = models.CharField(max_length=20)
	name = models.CharField(max_length=30)
	memory = models.PositiveSmallIntegerField(default=0)
	speed = models.PositiveSmallIntegerField(default=0)
	size = models.DecimalField(max_digits=2, decimal_places=1)
	def __unicode__(self):
		return self.brand + ' - ' + self.name

class CPUCooling(models.Model):
	usage = models.ForeignKey(Usage)
	brand = models.CharField(max_length=20)
	name = models.CharField(max_length=30)
	socket = models.CharField(max_length=10)
	cooling_type = models.CharField(max_length=10)
	def __unicode__(self):
		return self.brand + ' - ' + self.name

class SoundCard(models.Model):
	usage = models.ForeignKey(Usage)
	brand = models.CharField(max_length=20)
	name = models.CharField(max_length=30)
	interface = models.CharField(max_length=20)
	canal_count = models.DecimalField(max_digits=2, decimal_places=1)
	def __unicode__(self):
		return self.brand + ' - ' + self.name

class OpticalDrive(models.Model):
	usage = models.ForeignKey(Usage)
	brand = models.CharField(max_length=20)
	name = models.CharField(max_length=30)
	disk_type = models.CharField(max_length=10)
	speed = models.PositiveSmallIntegerField(default=0)
	def __unicode__(self):
		return self.brand + ' - ' + self.name

class PSU(models.Model):
	usage = models.ForeignKey(Usage)
	brand = models.CharField(max_length=20)
	name = models.CharField(max_length=30)
	power = models.PositiveSmallIntegerField(default=0)
	modular = models.BooleanField()
	certification = models.CharField(max_length=20)
	def __unicode__(self):
		return self.brand + ' - ' + self.name

class Case(models.Model):
	usage = models.ForeignKey(Usage)
	brand = models.CharField(max_length=20)
	name = models.CharField(max_length=30)
	size = models.CharField(max_length=10)
	def __unicode__(self):
		return self.brand + ' - ' + self.name