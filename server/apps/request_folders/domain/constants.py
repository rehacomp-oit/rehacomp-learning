from typing import Final


VOS_ORGANIZATION_NAME_LENGTH: Final = 80

COURSE_FULL_NAME_LENGTH: Final = 256

EMAIL_ADDRESS_PATTERN: Final = r'^\S+@\S+\.\S+$'
PHONE_NUMBER_PATTERN: Final = r'^\+7\(\d{3}\)\d{3}\-\d{2}\-\d{2}$'
PHONE_NUMBER_MAX_LENGTH: Final = 18
# A person's first name, patronymic and last name have the same number of characters.
PERSON_NAME_LENGTH: Final = 20
EDUCATION_INFORMATION_LENGTH: Final = 80
JOB_INFORMATION_LENGTH: Final = 80
