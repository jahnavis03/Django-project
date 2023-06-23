# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    doctor = models.ForeignKey('Doctor', models.DO_NOTHING, blank=True, null=True)
    room = models.ForeignKey('Room', models.DO_NOTHING)
    department = models.ForeignKey('Department', models.DO_NOTHING, blank=True, null=True)
    appointed_date = models.DateField()
    appointed_time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'appointment'


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
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
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


class Billing(models.Model):
    billing_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    appointment = models.ForeignKey(Appointment, models.DO_NOTHING, blank=True, null=True)
    bill_date = models.DateField()
    bill_time = models.TimeField()
    tax_amount = models.FloatField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    discharge_time = models.TimeField()
    discharge_date = models.DateField()
    bill_amount = models.FloatField()

    class Meta:
        managed = False
        db_table = 'billing'


class Department(models.Model):
    deptartment_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'department'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
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


class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    doctor_name = models.CharField(max_length=30)
    mobile_no = models.CharField(max_length=10)
    user = models.ForeignKey('User', models.DO_NOTHING)
    password = models.CharField(max_length=20)
    department = models.ForeignKey(Department, models.DO_NOTHING)
    salary = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'doctor'


class HospitalAppointment(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField()
    time = models.TimeField()
    doctor = models.ForeignKey('HospitalDoctor', models.DO_NOTHING)
    patient = models.ForeignKey('HospitalPatient', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hospital_appointment'


class HospitalDoctor(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    mobile = models.IntegerField()
    special = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'hospital_doctor'


class HospitalPatient(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    mobile = models.IntegerField(blank=True, null=True)
    address = models.TextField()

    class Meta:
        managed = False
        db_table = 'hospital_patient'


class Medicine(models.Model):
    medicine_id = models.AutoField(primary_key=True)
    medicine_name = models.CharField(max_length=40)
    medicine_cost = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'medicine'


class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    patient_name = models.CharField(max_length=40)
    admission_time = models.TimeField()
    admission_date = models.DateField()
    gender = models.CharField(max_length=10)
    mobile_no = models.CharField(max_length=10)
    dob = models.DateField()
    user = models.ForeignKey('User', models.DO_NOTHING)
    password = models.CharField(max_length=20)
    city = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'patient'


class Prescription(models.Model):
    prescription_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, models.DO_NOTHING)
    doctor = models.ForeignKey(Doctor, models.DO_NOTHING, blank=True, null=True)
    appointment = models.ForeignKey(Appointment, models.DO_NOTHING)
    medicine = models.ForeignKey(Medicine, models.DO_NOTHING)
    medicine_name = models.CharField(max_length=40)
    dosage = models.CharField(max_length=10, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    total_cost = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prescription'


class Room(models.Model):
    room_id = models.IntegerField(primary_key=True)
    room_type = models.CharField(max_length=25)
    room_no = models.IntegerField()
    rooms_left = models.IntegerField()
    room_cost = models.FloatField()

    class Meta:
        managed = False
        db_table = 'room'


class Treatment(models.Model):
    treatment_id = models.IntegerField(primary_key=True)
    patient = models.ForeignKey(Patient, models.DO_NOTHING)
    appointment = models.ForeignKey(Appointment, models.DO_NOTHING)
    treatment = models.CharField(max_length=40)
    treatment_cost = models.IntegerField()
    doctor_id = models.IntegerField(blank=True, null=True)
    treatment_time = models.TimeField(blank=True, null=True)
    treatment_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'treatment'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(unique=True, max_length=40)
    password = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'user'
