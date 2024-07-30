from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseUserManager(models.Manager):
    @classmethod
    def normalize_email(cls, email):
        """
        Normalize the username by lowercasing it.
        """
        email = email or ""
        if len(email) < 8:
            raise ValueError(_('email must have at least 8 characters'))
        return email.lower()

    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD: username})


class UserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None):
        if not email:
            raise ValueError(_('The Email field must be set'))
        if not full_name:
            raise ValueError(_('The Full Name field must be set'))

        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password=None):
        user = self.create_user(
            email=email,
            full_name=full_name,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
