from __future__ import annotations

from typing import TYPE_CHECKING

from .application import RegisterUserUsecase, RegisterUserUsecaseImpl
from .domain import UserPasswordManager, UserRepository
from .infrastructure.repositories import DjangoUserRepository
from .infrastructure.services import DjangoUserPasswordManager

if TYPE_CHECKING:
    from punq import Container


def register_dependencies(container: Container) -> None:
    container.register(UserPasswordManager, DjangoUserPasswordManager)
    container.register(UserRepository, DjangoUserRepository)
    container.register(RegisterUserUsecase, RegisterUserUsecaseImpl)
