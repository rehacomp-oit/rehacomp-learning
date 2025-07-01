from importlib import import_module
from logging import getLogger
from threading import Lock
from types import ModuleType
from typing import Iterable

from punq import Container, InvalidRegistrationError


_logger = getLogger(__name__)
_mutex = Lock()
_container: Container | None = None


def _load_module(module_path: str) -> ModuleType:
    try:
        return import_module(module_path)
    except ImportError as exc:
        _logger.exception('Failed to import module %s', module_path)
        raise RuntimeError(f'Error loading module {module_path}') from exc


def _register_dependencies(module: ModuleType, container: Container) -> None:
    module_name = module.__name__
    func_name = 'register_dependencies'
    register_func = getattr(module, func_name, None)
    if not callable(register_func):
        _logger.warning(
            'Module %s does not expose a callable <%s>',
            module_name, func_name
        )
        return

    try:
        module.register_dependencies(container)
    except InvalidRegistrationError as exc:
        _logger.exception(
            'Invalid registration in module %s',
            module_name
        )
        raise RuntimeError(
            f'Failed registration in module {module_name}'
        ) from exc



def _build_dependency_graph(modules: Iterable[str]) -> Container:
    container = Container()
    for module_path in modules:
        module = _load_module(module_path)
        _register_dependencies(module, container)

    return container


def initialize_di_container(bootstrap_modules: Iterable[str]) -> None:
    global _container
    if _container is not None:
        return

    with _mutex:
        if _container is None:
            _container = _build_dependency_graph(bootstrap_modules)
            _logger.info('container registered')


def get_di_container() -> Container:
    if _container is None:
        raise RuntimeError('DI container is not initialized')

    return _container


# Warning: this function is used only for tests
def _reset_di_container() -> None:
    '''
    Reset the global DI container. For testing only.
    '''

    global _container
    with _mutex:
        _container = None
