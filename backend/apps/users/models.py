from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.utils.translation import ugettext_lazy as _

from .validators import UnicodeUsernameValidator


class User(AbstractUser):
    username = CharField(
        _('Username'), max_length=150, unique=True,
        validators=[UnicodeUsernameValidator()],
        help_text=_('Required. 150 characters or fewer. Letters, digits and ./+/-/_ only.'),
        error_messages={
            'unique': _('A user with that username already exists.'),
        },
    )
