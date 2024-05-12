from punq import Container
from server.common_tools.interfaces import Repository, Validator

from .helpers import validate_password_format
from .repositories import UserCredentialsRepository
from .usecases import SignUp


signup_service = Container()
signup_service.register(Validator, lambda: validate_password_format)
signup_service.register(Repository, UserCredentialsRepository)
signup_service.register('service', SignUp)
