'''
Implementation of a common infrastructure layer.
'''

from ulid import new as generate_ulid

from .domain import EntityId


def get_ulid_for_pk() -> EntityId:
    '''
    Returns the generated ULID for the domain entity
    '''

    return EntityId(generate_ulid())
