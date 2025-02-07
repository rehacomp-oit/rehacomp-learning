from django.db.migrations import CreateModel
from django.db.migrations import Migration as BaseMigration
from django.db.models import (
    BigAutoField,
    BooleanField,
    CharField,
    DateTimeField,
    EmailField,
    ManyToManyField
)
from django.utils.timezone import now
from server.apps.accounts.infrastructure.models import CustomUserManager


_fields = (
    ('id', BigAutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID'
    )),
    ('password', CharField(
        max_length=128,
        verbose_name='password'
    )),
    ('last_login', DateTimeField(
        blank=True,
        null=True,
        verbose_name='last login'
    )),
    ('is_superuser', BooleanField(
        default=False,
        help_text='Designates that this user has all permissions without explicitly assigning them.',
        verbose_name='superuser status'
    )),
    ('email', EmailField(
        unique=True,
        verbose_name='email address'
    )),
    ('first_name', CharField(
        blank=True,
        max_length=80,
        verbose_name='first name'
    )),
    ('last_name', CharField(
        blank=True,
        max_length=80,
        verbose_name='last name'
    )),
    ('is_active', BooleanField(
        default=True,
        help_text='Designates whether this user should be treated as activeUnselect this instead of deleting accounts.',
        verbose_name='active'
    )),
    ('is_staff', BooleanField(
        default=False,
        help_text='Designates whether the user can log into this admin site.',
        verbose_name='staff status'
    )),
    ('date_joined', DateTimeField(
        default=now,
        verbose_name='date joined'
    )),
    ('groups', ManyToManyField(
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='user_set',
        related_query_name='user',
        to='auth.group',
        verbose_name='groups'
    )),
    ('user_permissions', ManyToManyField(
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='user_set',
        related_query_name='user',
        to='auth.permission',
        verbose_name='user permissions'
    )),
)


class Migration(BaseMigration):
    initial = True
    dependencies = [('auth', '0012_alter_user_first_name_max_length'),]

    operations = [
        CreateModel(
            name='User',
            fields=_fields,
            options={'abstract': False},
            managers=[('objects', CustomUserManager()),],
        ),
    ]
