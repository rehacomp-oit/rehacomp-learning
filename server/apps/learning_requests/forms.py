from typing import final

from django.forms import BooleanField, Form, Textarea


@final
class LearningRequestForm(Form):
    fil1 = BooleanField(required=True)
    fil2 = Textarea()
