from typing import final

from django.db.migrations import AddConstraint
from django.db.migrations import Migration as BaseMigration
from django.db.models import CheckConstraint, Q


_disability_group_check = CheckConstraint(
    check=Q(('disability_group__in', ('v1', 'v2', 'v3', 'o', 'n',),)),
    name='disability_group_check'
)

_personal_phone_check = CheckConstraint(
    check=Q(('personal_phone__regex', '^\\d+$',), ('personal_phone', '',), _connector='OR'),
    name='phone_nunber_check'
)

_email_pattern_check = CheckConstraint(
    check=Q(('email__regex', '^\\S+@\\S+\\.\\S+$',), ('email', '',), _connector='OR'),
    name='email_pattern_check'
)


@final
class Migration(BaseMigration):
    dependencies = (('core', '0003_person_model'),)

    operations = (
        AddConstraint(model_name='person', constraint=_disability_group_check),
        AddConstraint(model_name='person', constraint=_email_pattern_check),
        AddConstraint(model_name='person', constraint=_personal_phone_check),
    )
