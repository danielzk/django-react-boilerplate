import re

from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import ugettext_lazy as _


class AtLeastOneDigitPasswordValidator(object):
    # pylint: disable=unused-argument
    def validate(self, password, user=None):
        if not any(char.isdigit() for char in password):
            raise ValidationError(
                _('Password must contain at least 1 digit.'),
                code='password_no_digits'
            )

    def get_help_text(self):
        return _('Your password must contain at least 1 digit.')


class AtLeastOneLetterPasswordValidator(object):
    # pylint: disable=unused-argument
    def validate(self, password, user=None):
        if not any(char.isalpha() for char in password):
            raise ValidationError(
                _('Password must contain at least 1 letter.'),
                code='password_no_letters'
            )

    def get_help_text(self):
        return _('Your password must contain at least 1 letter.')


@deconstructible
class UnicodeUsernameValidator(validators.RegexValidator):
    """
    Same as django.contrib.auth.validators.UnicodeUsernameValidator but
    without @.
    """

    regex = r'^[\w.+-]+$'
    message = _(
        'Enter a valid username. This value may contain only letters, '
        'numbers, and ./+/-/_ characters.'
    )
    flags = re.UNICODE
