from __future__ import annotations

from typing import Any, final, override

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models import BooleanField, CharField, DateTimeField, EmailField
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from server.apps.accounts.domain import USER_MAX_NAME_LENGTH


__all__ = (
    'CustomUserManager',
    'User',
)


@final
class CustomUserManager(BaseUserManager['User']):
    use_in_migrations = True


    def create_user(
        self,
        email: str,
        password: str | None=None,
        **extra_fields: Any
    ) -> User:
        '''
        creates and saves a regular unprivileged user
        '''

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self.__create_user_model(email, password, **extra_fields)


    def create_superuser(
        self,
        email: str,
        password: str | None=None,
        **extra_fields: Any
    ) -> User:
        '''
        Creates and saves a superuser account.
        '''

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.__create_user_model(email, password, **extra_fields)


    def __create_user_model(
        self,
        email: str,
        password: str | None=None,
        **extra_fields: Any
    ) -> User:

        if not email:
            raise ValueError('Users require an email field')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


@final
class User(AbstractBaseUser, PermissionsMixin):
    '''
    Users within the Django authentication system are represented by this
    model.

    Email address is used as the user name.
    '''

    email = EmailField(
        verbose_name=_('email address'),
        unique=True
    )

    first_name = CharField(
        verbose_name=_('first name'),
        max_length=USER_MAX_NAME_LENGTH,
        blank=True
    )

    last_name = CharField(
        verbose_name=_('last name'),
        max_length=USER_MAX_NAME_LENGTH,
        blank=True
    )

    is_active = BooleanField(  # type: ignore[mutable-override]
        verbose_name=_('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active'
            'Unselect this instead of deleting accounts.'
        )
    )

    is_staff = BooleanField(
        verbose_name=_('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )

    date_joined = DateTimeField(
        verbose_name=_('date joined'),
        default=now
    )

    objects = CustomUserManager()  # noqa
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    @override
    def __str__(self) -> str:
        return self.email
