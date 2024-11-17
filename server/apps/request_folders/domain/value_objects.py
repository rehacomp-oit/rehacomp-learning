from typing import NewType

from server.common.domain import EntityId


CourseFolderId = NewType('CourseFolderId', EntityId)
OrganizationId = NewType('OrganizationId', EntityId)
