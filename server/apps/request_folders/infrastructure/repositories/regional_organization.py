from typing import final, TypedDict

from django.db import Error as DatabaseError
from server.apps.request_folders.domain.entities import RegionalOrganization
from server.apps.request_folders.domain.value_objects import OrganizationCode, OrganizationId
from server.apps.request_folders.models import VOSOrganization
from server.common.domain import EntityId
from server.common.infrastructure import make_safe
from ulid import ULID


@final
class _DBInternal(TypedDict):
    id: ULID  # noqa: VNE003
    name: str
    code: int


@final
class RegionalOrganizationDjangoRepository:
    __slots__ = ('__manager')


    def __init__(self) -> None:
        self.__manager = VOSOrganization.objects


    @make_safe(DatabaseError)
    def fetch_all(self) -> tuple[RegionalOrganization, ...]:
        queryset = self.__manager.order_by('name').values()
        return tuple(self.__build_entity(row) for row in queryset)


    @make_safe(DatabaseError)
    def exists(self) -> bool:
        return self.__manager.exists()


    def __build_entity(self, src: _DBInternal) -> RegionalOrganization:
        organization_id = OrganizationId(EntityId(src['id']))
        organization_name = src['name']
        organization_code = OrganizationCode(src['code'])
        return RegionalOrganization(organization_id, organization_name, organization_code)
