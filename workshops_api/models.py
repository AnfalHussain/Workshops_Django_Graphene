from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator, MinValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class Workshop(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    image = models.ImageField()
    price = models.PositiveIntegerField(default=10)

    def __str__(self):
        return self.name


class Profile(models.Model):
    GENDER = [
        ("FEMALE", "Female"),
        ("MALE", "Male"),
    ]
    GOVERNORATE = [
        ("AHMADI", "Ahmadi"),
        ("AL_ASIMAH", "Al-Asimah"),
        ("FARWANIYA", "Farwaniya"),
        ("HAWALLI", "Hawalli"),
        ("JAHRA", "Jahra"),
        ("MUBARAK_AL_KABEER", "Mubarak Al-Kabeer"),
    ]
    EDUCATION = [
        ("Primary_School Student", "Primary School Student"),
        ("Secondary School Student", "Secondary School Student"),
        ("High School Student", "High School Student"),
        ("College", "College/University Student"),
        ("Graduate", "College University Graduate"),
    ]

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=150, null=True)
    middle_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    gender = models.CharField(
        max_length=8, choices=GENDER, null=True
    )
    nationality = models.CharField(max_length=150, null=True)
    mobile_number = PhoneNumberField(null=True)
    secondary_contact_number = PhoneNumberField(null=True)
    # assuming that the civil id max length is 12 and validating that it consists of digits only
    civil_id_number = models.CharField(max_length=12, null=True, validators=[
                                       RegexValidator(r'^[0-9]*$')])

    # birthdate = models.DateField(null=True)
    governorate = models.CharField(
        max_length=20, choices=GOVERNORATE, null=True
    )
    area = models.CharField(max_length=150, null=True)
    education_level = models.CharField(max_length=150, null=True)
    major = models.CharField(max_length=150, blank=True, null=True)
    age = models.PositiveIntegerField(null=True)
    # @property
    # def age(self):
    #     current_age = 0
    #     if self.birthdate:
    #         current_age = int(
    #             (datetime.now().date() - self.birthdate).days / 365.25)
    #     return current_age

    #     def __str__(self):
    #         return self.user.username


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created and instance.is_staff == False:
        Profile.objects.create(user=instance)


class Registration(models.Model):
    STATUS = [
        ("FAILED", "Failed"),
        ("SUCCESSFUL", "Successful"),
        ("PENDING", "Pending"),
    ]

    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='registrations')
    total = models.DecimalField(max_digits=8, decimal_places=3, validators=[
                                MinValueValidator(0.0)])
    payment_status = models.CharField(
        max_length=20, choices=STATUS, default="PENDING"
    )
    reference_number = models.CharField(max_length=10)

    def __str__(self):
        return ("Registration " + self.reference_number)


class Cart(models.Model):
    workshop = models.ForeignKey(
        Workshop, on_delete=models.CASCADE, related_name='workshops')
    registration = models.ForeignKey(
        Registration, on_delete=models.CASCADE, related_name='carts')
