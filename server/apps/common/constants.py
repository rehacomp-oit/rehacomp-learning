'''
A set of constants used in defining models
as well as in related business scenarios.
'''

from typing import Final
from typing import final

from django.db.models import IntegerChoices, TextChoices


VOS_ORGANIZATION_NAME_LENGTH: Final = 80
COURSE_FULL_NAME_LENGTH: Final = 256
COURSE_SHORT_NAME_LANGTH: Final = 10
EMAIL_ADDRESS_PATTERN: Final = r'^\S+@\S+\.\S+$'
PHONE_NUMBER_PATTERN: Final = r'^\+7\(\d{3}\)\d{3}\-\d{2}\-\d{2}$'
PHONE_NUMBER_MAX_LENGTH: Final = 20
# A person's first name, patronymic and last name
# have the same number of characters.
FULL_NAME_LENGTH: Final = 20
DISABILITY_GROUP_LENGTH: Final = 5
EDUCATION_INFORMATION_LENGTH: Final = 80
JOB_INFORMATION_LENGTH: Final = 80


@final
class TrainingLevels(IntegerChoices):
    '''Options for possible levels of computer or smartphone proficiency.'''

    ZERO = (0, 'Нуливой уровень',)
    BEGINNER = (1, 'Начинающий пользователь',)
    BASIC = (2, 'Базовый уровень',)
    CONFIDENT = (3, 'Уверенный пользователь',)
    EXPERIENCED = (4, 'Опытный пользователь',)
    ADVANCED = (5, 'Продвинутый пользователь',)


@final
class DisabilityGroups(TextChoices):
    '''Options for possible disability groups.'''

    VISION_FIRST = ('v1', 'Первая по зрению',)
    VISION_SECOND = ('v2', 'вторая по зрению',)
    VISION_THURD = ('v3', 'третья по зрению',)
    OTHER = ('o', 'другая',)
    NOTHING = ('n', 'нет инволидности')
