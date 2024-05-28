from punq import Container

from .helpers import validate_password_format
from .interfaces import PasswordValidator, UserCredentialsRepository
from .repositories import DatabaseRepository
from .services import SignUpService


signup_implementation = Container()
signup_implementation.register(PasswordValidator, lambda: validate_password_format)
signup_implementation.register(UserCredentialsRepository, DatabaseRepository)
signup_implementation.register('service', SignUpService)
