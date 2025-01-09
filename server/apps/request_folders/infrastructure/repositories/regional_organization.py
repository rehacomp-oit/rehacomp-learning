from typing import final, TypedDict

from django.core.cache import cache
from server.apps.request_folders.domain.entities import RegionalOrganization
from server.apps.request_folders.domain.value_objects import OrganizationCode, OrganizationId
from server.apps.request_folders.models import VOSOrganization
from server.common.domain import EntityId
from server.common.exceptions import EmptyRepositoryError
from server.common.infrastructure import make_safe
from ulid import ULID


@final
class _DBInternal(TypedDict):
    id: ULID  # noqa: VNE003
    name: str
    code: int


@final
class RegionalOrganizationDjangoRepository:
    __slots__ = (
        '__cache_timeout',
        '__organizations_cache',
    )


    def __init__(self) -> None:
        # 10 minutes
        self.__cache_timeout = 600
        self.__organizations_cache = 'courses'


    @make_safe
    def fetch_all(self) -> tuple[RegionalOrganization, ...]:
        organizations = cache.get(self.__organizations_cache)
        if organizations is not None:
            return organizations

        queryset = VOSOrganization.objects.order_by('name').values()
        organizations = tuple(self.__build_entity(row) for row in queryset)
        if organizations is None:
            raise EmptyRepositoryError('message')

        cache.set(self.__organizations_cache, organizations, self.__cache_timeout)
        return organizations


    def __build_entity(self, src: _DBInternal) -> RegionalOrganization:
        organization_id = OrganizationId(EntityId(src['id']))
        organization_name = src['name']
        organization_code = OrganizationCode(src['code'])
        return RegionalOrganization(organization_id, organization_name, organization_code)
