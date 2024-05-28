from punq import Container
from server.apps.accounts.helpers import validate_password_format
from server.apps.accounts.interfaces import PasswordValidator, UserCredentialsRepository
from server.apps.accounts.repositories import DatabaseRepository
from server.apps.accounts.usecases import SignUpService


signup_implementation = Container()
signup_implementation.register(PasswordValidator, lambda: validate_password_format)
signup_implementation.register(UserCredentialsRepository, DatabaseRepository)
signup_implementation.register('service', SignUpService)
