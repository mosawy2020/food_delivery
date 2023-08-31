from django.core.validators import ValidationError
from django.utils.translation import gettext as _


class Confirmed:
    requires_context = True

    def __init__(self, other_field):
        self.other_field = other_field

    def __call__(self, value, ser):
        if value != ser.parent.initial_data.get(self.other_field):
            raise ValidationError(_('This field is not confirmed'))
