from typing import NewType


UserId = NewType('UserId', int)
UserRawPassword = NewType('UserRawPassword', str)
UserHashedPassword = NewType('UserHashedPassword', str)
