import uuid
from django.db import models
from user.models import User


class PaitentProfile(models.Model):

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='paitent_profile')
	first_name = models.CharField(max_length=50, unique=False)
	last_name = models.CharField(max_length=50, unique=False)
	phone_number = models.CharField(max_length=10, unique=True, null=False, blank=False)
	age = models.PositiveIntegerField(null=False, blank=False)
	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
	)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	case = models.TextField()

	class Meta:
		'''
		to set table name in database
		'''
		db_table = "paitent_profile"

class DoctorProfile(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
	first_name = models.CharField(max_length=50, unique=False)
	last_name = models.CharField(max_length=50, unique=False)
	phone_number = models.CharField(max_length=10, unique=True, null=False, blank=False)
	age = models.PositiveIntegerField(null=False, blank=False)
	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
	)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

	class Meta:
		'''
		to set table name in database
		'''
		db_table = "doctor_profile"