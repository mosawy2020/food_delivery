from django.core.validators import ValidationError
from django.utils.translation import gettext as _


class Same:
    requires_context =True
    def __init__(self, other_field):
        self.other_field = other_field

    def __call__(self, value, ser):
        if value != ser.parent.initial_data.get(self.other_field):
            raise ValidationError(_("this field is not confirmed"))
        return value


class Confirmed:
    requires_context = True

    def __init__(self, other_field):
        self.other_field = other_field

    def __call__(self, value, ser):
        if value != ser.parent.initial_data.get(self.other_field):
            raise ValidationError(_('This field is not confirmed'))


class Exists:
    requires_context = True

    def __init__(self, check_field):
        self.check_field = check_field

    def __call__(self, value, ser):
        to_check = self.check_field
        if not ser.parent.Meta.model.objects.filter(**{to_check: value}).exists():
            raise ValidationError(
                _("%(value)s does not exist"),
                params={"value": value},
            )
