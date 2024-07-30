from django.db import models
from accounts.managers import UserManager
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)  # ایمیل به‌عنوان شناسه اصلی
    full_name = models.CharField(max_length=100)  # نام کامل کاربر
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']  # فیلدهای مورد نیاز برای ثبت‌نام

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        """
        Return True if the user is a staff member.
        """
        return self.is_admin

    def has_perm(self, perm, obj=None):
        """
        Checks if the user has a specific permission.
        """
        return True

    def has_module_perms(self, app_label):
        """
        Checks if the user has permissions for a specific app.
        """
        return True
