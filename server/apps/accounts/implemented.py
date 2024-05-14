from punq import Container

from .helpers import validate_password_format
from .interfaces import PasswordValidator, UserCredentialsRepository
from .repositories import DatabaseRepository
from .usecases import SignUp


signup_service = Container()
signup_service.register(PasswordValidator, lambda: validate_password_format)
signup_service.register(UserCredentialsRepository, DatabaseRepository)
signup_service.register('service', SignUp)
