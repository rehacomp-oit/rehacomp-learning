from typing import NewType

from server.common.domain import EntityId


CourseId = NewType('CourseId', EntityId)
OrganizationId = NewType('OrganizationId', EntityId)
