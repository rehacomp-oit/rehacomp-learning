from django.db.migrations import CreateModel
from django.db.migrations import Migration as BaseMigration
from django.db.models import CharField, FileField, OneToOneField
from django.db.models.deletion import SET_NULL
from server.apps.learning_requests.helpers import build_upload_path


_fields = (
    ('target_name', CharField(
        db_comment='File name without extention.',
        max_length=80,
        primary_key=True,
        serialize=False
    )),
    ('uploaded_file', FileField(
        db_comment='Фull path to the uploaded file with the original learning request.',
        max_length=128,
        unique=True,
        upload_to=build_upload_path
    )),
    ('learning_request', OneToOneField(
        db_comment='Related learning request metadata.',
        null=True,
        on_delete=SET_NULL,
        to='learning_requests.learningrequestmetadata'
    )),
)

_options = {
    'db_table': 'attachments',
    'db_table_comment': 'Defines the source file with the text of a learning request.',
}


class Migration(BaseMigration):

    dependencies = (('learning_requests', '0001_learning_request_metadata_model'),)
    operations = (CreateModel(name='Attachment', fields=_fields, options=_options,),)
