# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Aduana(models.Model):
    id_aduana = models.AutoField(primary_key=True)
    nombre_aduana = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    created_user = models.CharField(max_length=10)
    updated_at = models.DateTimeField(auto_now=True)
    updated_user = models.CharField(max_length=10)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'aduana'

    def __str__(self):
        return self.nombre_aduana


class Archivo(models.Model):
    id_archivo = models.AutoField(primary_key=True)
    id_municipio = models.ForeignKey('Municipio', models.DO_NOTHING, db_column='id_municipio', null=True, related_name='archivos')
    id_cliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='id_cliente', null=True)
    id_aduana = models.ForeignKey(Aduana, models.DO_NOTHING, db_column='id_aduana', null=True)
    id_transporte = models.ForeignKey('Transporte', models.DO_NOTHING, db_column='id_transporte', null=True)
    id_carga = models.ForeignKey('Carga', models.DO_NOTHING, db_column='id_carga', null=True)
    numero_registro = models.IntegerField()
    aprobado = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_user = models.CharField(max_length=10)
    updated_at = models.DateTimeField(auto_now=True)
    updated_user = models.CharField(max_length=10)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'archivo'

    def __str__(self):
        return str(self.numero_registro)
    def not_deleted(self):
        return self.filter(deleted_at=None)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Carga(models.Model):
    id_carga = models.AutoField(primary_key=True)
    id_transporte = models.ForeignKey('Transporte', models.DO_NOTHING, db_column='id_transporte', null=True)
    tipo = models.CharField(max_length=10)
    peso = models.FloatField()
    descripcion = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    created_user = models.CharField(max_length=10)
    updated_at = models.DateTimeField(auto_now=True)
    updated_user = models.CharField(max_length=10)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'carga'

    def __str__(self):
        return str(self.id_carga) + " " + self.descripcion

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=20)
    apellido_cliente = models.CharField(max_length=20)
    dui_cliente = models.IntegerField()
    nit_cliente = models.IntegerField()
    direccion_cliente = models.CharField(max_length=20)
    empresa = models.CharField(max_length=20)
    telefono_cliente = models.IntegerField()
    genero = models.CharField(max_length=9)
    created_at = models.DateTimeField(auto_now_add=True)
    created_user = models.CharField(max_length=10)
    updated_at = models.DateTimeField(auto_now=True)
    updated_user = models.CharField(max_length=10)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'cliente'

    def __str__(self):
        return self.nombre_cliente + " " + self.apellido_cliente + " " + str(self.dui_cliente)


class Departamento(models.Model):
    id_departamento = models.CharField(primary_key=True, max_length=5)
    nombre_departamento = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    created_user = models.CharField(max_length=10)
    updated_at = models.DateTimeField(auto_now=True)
    updated_user = models.CharField(max_length=10)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'departamento'

    def __str__(self):
        return self.nombre_departamento

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Municipio(models.Model):
    id_municipio = models.CharField(primary_key=True, max_length=5)
    id_departamento = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='id_departamento', null=True)
    nombre_municipio = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    created_user = models.CharField(max_length=10)
    updated_at = models.DateTimeField(auto_now=True)
    updated_user = models.CharField(max_length=10)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'municipio'

    def __str__(self):
        return self.nombre_municipio

class Transporte(models.Model):
    id_transporte = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', null=True)
    numero_vin = models.CharField(max_length=17)
    numero_motor = models.CharField(max_length=10)
    numero_chasis = models.CharField(max_length=17)
    ano = models.IntegerField()
    marca = models.CharField(max_length=10)
    capacidad_maxima = models.FloatField()
    modelo = models.CharField(max_length=10)
    numero_placas = models.CharField(max_length=7)
    procedencia = models.CharField(max_length=50)
    destino = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    created_user = models.CharField(max_length=10)
    updated_at = models.DateTimeField(auto_now=True)
    updated_user = models.CharField(max_length=10)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'transporte'
    
    def __str__(self):
        return self.numero_vin + ' ' + self.marca + ' ' + self.modelo + ' ' + self.numero_placas


class Transportista(models.Model):
    id_transportista = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_user = models.CharField(max_length=10)
    updated_at = models.DateTimeField(auto_now=True)
    updated_user = models.CharField(max_length=10)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'transportista'

    def __str__(self):
        return str(self.id_transportista)