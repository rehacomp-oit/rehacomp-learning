from django.db.migrations import CreateModel
from django.db.migrations import Migration as BaseMigration
from django.db.models import BigAutoField, CharField


_fields = (
    ('id', BigAutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID'
    )),
    ('course_name', CharField(
        db_comment='Full name of the training course',
        max_length=80,
        unique=True,
        verbose_name='Полное название курса'
    )),
    ('course_short_name', CharField(
        db_comment='Abbreviation of the course name',
        max_length=10,
        unique=True,
        verbose_name='Аббревиатура названия курса'
    )),
)

_options = {
    'verbose_name': 'курс',
    'verbose_name_plural': 'курсы',
    'db_table': 'courses',
    'db_table_comment': 'Training course conducted at the Institute',
}


class Migration(BaseMigration):

    dependencies = [('common', '0001_vos_organization_model'),]
    operations = (
        CreateModel(name='Course', fields=_fields, options=_options,),
    )
