from __future__ import annotations

from typing import Any, final

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models import BooleanField, CharField, DateTimeField, EmailField
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _


@final
class CustomUserManager(BaseUserManager):
    use_in_migrations = True


    def create_user(self, email: str, password: str | None=None, **extra_fields: Any) -> User:
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self.__create_user_model(email, password, **extra_fields)


    def create_superuser(self, email: str, password: str | None=None, **extra_fields: Any) -> User:
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.__create_user_model(email, password, **extra_fields)


    def __create_user_model(self, email: str, password: str | None=None, **extra_fields: Any) -> User:
        if not email:
            raise ValueError('Users require an email field')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


@final
class User(AbstractBaseUser, PermissionsMixin):

    email = EmailField(unique=True)
    first_name = CharField(_('first name'), max_length=150, blank=True)
    last_name = CharField(_('last name'), max_length=150, blank=True)
    is_active = BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active'
            'Unselect this instead of deleting accounts.'
        )
    )
    is_staff = BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_superuser = BooleanField(default=False)
    date_joined = DateTimeField(_('date joined'), default=now)

    objects = CustomUserManager()  # noqa
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ()


    def __str__(self) -> str:
        return self.email
