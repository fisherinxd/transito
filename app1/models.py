# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Clasevehiculo(models.Model):
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    idclasev = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'clasevehiculo'
	verbose_name = u'Clase de vehiculo'
        verbose_name_plural = u'Clase de vehiculos'
    def __unicode__(self):
	return self.descripcion


class Combustibles(models.Model):
    nombrecomb = models.CharField(max_length=60, blank=True, null=True)
    idcomb = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'combustibles'
	verbose_name = u'Clase de combustibles'
        verbose_name_plural = u'Clase de combustibles'
    def __unicode__(self):
	return self.nombrecomb        


class Provincias(models.Model):
    nombreprov = models.CharField(max_length=60, blank=True, null=True)
    idprov = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'provincias'
    def __unicode__(self):
	return self.nombreprov


class Tipovehiculo(models.Model):
    nombretipov = models.CharField(max_length=60, blank=True, null=True)
    idtipov = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'tipovehiculo'
    def __unicode__(self):
	return self.nombretipov


class Vehiculos(models.Model):
    placa = models.CharField(max_length=15, blank=True, null=True)
    modelo = models.CharField(max_length=6, blank=True, null=True)
    marca = models.CharField(max_length=30, blank=True, null=True)
    tonelaje = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    asientos = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    idtipov = models.ForeignKey(Tipovehiculo, models.DO_NOTHING, db_column='idtipov', blank=True, null=True)
    idclasev = models.ForeignKey(Clasevehiculo, models.DO_NOTHING, db_column='idclasev', blank=True, null=True)
    idcomb = models.ForeignKey(Combustibles, models.DO_NOTHING, db_column='idcomb', blank=True, null=True)
    idprov = models.ForeignKey(Provincias, models.DO_NOTHING, db_column='idprov', blank=True, null=True)
    idvehiculo = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'vehiculos'

    def __unicode__(self):         
	return self.placa 
