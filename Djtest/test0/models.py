from django.db import models


class Healthdata(models.Model):
    id = models.OneToOneField('User', models.DO_NOTHING, db_column='ID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    permission = models.ForeignKey('Permission', models.DO_NOTHING, db_column='permission', blank=True, null=True)
    tempreture = models.TextField(blank=True, null=True)  # This field type is a guess.
    blood_pressure = models.TextField(db_column='blood pressure', blank=True, null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    pulse = models.TextField(blank=True, null=True)  # This field type is a guess.
    oximeter = models.TextField(blank=True, null=True)  # This field type is a guess.
    weight = models.TextField(blank=True, null=True)  # This field type is a guess.
    glucometer = models.TextField(blank=True, null=True)  # This field type is a guess.
    time = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Healthdata'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Device(models.Model):
    divice_id = models.TextField(db_column='divice id', primary_key=True)  # Field renamed to remove unsuitable characters. This field type is a guess.
    sku = models.TextField(db_column='SKU')  # Field name made lowercase. This field type is a guess.
    serial_number = models.TextField(db_column='serial number')  # Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'device'


class Divrec(models.Model):
    id = models.OneToOneField('User', models.DO_NOTHING, db_column='ID', primary_key=True)  # Field name made lowercase.
    deviceid = models.IntegerField(db_column='deviceID', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'divrec'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

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


class Permission(models.Model):
    role = models.IntegerField(db_column='ROLE', unique=True)  # Field name made lowercase.
    permission = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'permission'


class Test0Test(models.Model):
    a = models.CharField(max_length=30)
    b = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'test0_test'


class User(models.Model):
    name = models.TextField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    role = models.ForeignKey(Permission, models.DO_NOTHING, db_column='role', blank=True, null=True)
    birth = models.DateField(blank=True, null=True)
    sex = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'user'