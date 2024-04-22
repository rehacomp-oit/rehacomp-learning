from django_test_migrations.migrator import Migrator
from pytest import mark, raises


@mark.django_db
def test_0001_learning_request_metadata_model(migrator: Migrator) -> None:
    '''Tests the initial migration forward application.'''

    old_state = migrator.apply_initial_migration(('common', '0004_initial_data'))
    with raises(LookupError):
        old_state.apps.get_model('learning_requests', 'LearningRequestMetadata')

    new_state = migrator.apply_tested_migration(
        ('learning_requests', '0001_learning_request_metadata_model')
    )
    model = new_state.apps.get_model('learning_requests', 'LearningRequestMetadata')
    assert model.objects.create()
