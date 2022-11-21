from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


def upload_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/admin-uploads/<filename>
    return 'admin-uploads/{0}'.format(filename)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, account_type=None, balance=None, phone_number=None, profile_photo=None, firstname=None, lastname=None, username=None, location=None, address=None, is_staff=False, is_active=True, is_superuser=False):
        if not email:
            raise ValueError("All the fields haven't been adequately filled")
        if not password:
            raise ValueError(
                "All the fields haven't been adequately filled - password")

        user_obj = self.model(
            email=self.normalize_email(email),
        )

        user_obj.set_password(password)

        user_obj.profile_photo = profile_photo
        user_obj.account_type = account_type
        user_obj.phone_number = phone_number
        user_obj.firstname = firstname
        user_obj.location = location
        user_obj.lastname = lastname
        user_obj.username = username
        user_obj.address = address
        user_obj.balance = balance

        user_obj.staff = is_staff
        user_obj.active = is_active
        user_obj.admin = is_superuser

        user_obj.save(using=self._db)

        return user_obj

    def create_staffuser(self, email, password=None, username=None):
        user = self.create_user(email,  password=password, username=username)

        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, username=None):
        user = self.create_user(email,  password=password,  username=username)

        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


# Create your user models here.
class Users(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)

    phone_number = models.CharField(max_length=255, blank=True, null=True)
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    balance = models.FloatField(default=0.0, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    account_type = models.CharField(max_length=255, blank=True, null=True, choices=[('savings', ('savings')), ('current', ('current'))])

    # profile photo
    profile_photo = models.FileField(
        upload_to=upload_path, blank=True, null=True)

    # django defaults
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    # django default functions
    @property
    def get_full_name(self):
        return f"{self.lastname} {self.firstname}"

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_superuser(self):
        return self.admin
