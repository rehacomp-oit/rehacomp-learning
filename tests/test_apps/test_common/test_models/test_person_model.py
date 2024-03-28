from typing import final

from hypothesis import given
from hypothesis.extra import django
from server.apps.common.models import Person, VOSOrganization


@final
class TestPerson(django.TestCase):
    '''This is a property-based test that ensures model correctness.'''

    @given(django.from_model(Person, vos_organization=django.from_model(VOSOrganization)))
    def test_model_properties(self, instance: Person) -> None:
        '''Tests that instance can be saved and has correct representation.'''
        instance.save()
        assert instance.id > 0
        assert len(str(instance)) <= 30
