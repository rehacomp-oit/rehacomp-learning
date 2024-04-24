from django.db.migrations import AddConstraint, CreateModel
from django.db.migrations import Migration as BaseMigration
from django.db.models import (
    BigAutoField,
    BooleanField,
    CharField,
    CheckConstraint,
    DateTimeField,
    ForeignKey,
    ManyToManyField,
    Q,
    TextField
)
from django.db.models.deletion import SET_NULL
from server.apps.learning_requests.constants import LearningRequestStatuses


_fields = (
    ('id', BigAutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID'
    ),),
    ('created_at', DateTimeField(auto_now_add=True)),
    ('updated_at', DateTimeField(auto_now=True)),
    ('note', TextField(
        db_comment='A short text note about learning request.',
        db_default='',
        default=''
    ),),
    ('relevance', BooleanField(
        db_comment='Is the learning request currently relevant.',
        db_default=True,
        default=True
    ),),
    ('status', CharField(
        db_comment=(
            'Available status variants for learning requests: '
            '<registered>, <approved>, <rejected>, <in_history>'
        ),
        db_default=LearningRequestStatuses['REGISTERED'],
        default=LearningRequestStatuses['REGISTERED'],
        max_length=10
    ),),
    ('candidates', ManyToManyField(db_table='person_learning_requests', to='common.person')),
    ('course', ForeignKey(
        db_comment='Related course.',
        null=True,
        on_delete=SET_NULL,
        related_name='learning_requests',
        to='common.course'
    ),),
)

_options = {
    'db_table': 'learning_requests_metadata',
    'db_table_comment': 'Meta information of learning requests.',
}

_cnt = CheckConstraint(
    check=Q(('status__in', ('registered', 'approved', 'rejected', 'in_history'))),
    name='status_variants'
)


class Migration(BaseMigration):

    initial = True
    dependencies = (('common', '0004_initial_data'),)

    operations = (
        CreateModel(name='LearningRequestMetadata', fields=_fields, options=_options),
        AddConstraint(model_name='learningrequestmetadata', constraint=_cnt),
    )
