import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response403 import InlineResponse403  # noqa: E501
from swagger_server import util


def user_enter_gym_turnstile_get(phone_number):  # noqa: E501
    """Tries to enter gym

     # noqa: E501

    :param phone_number: User&#x27;s phone number
    :type phone_number: str

    :rtype: InlineResponse200
    """
    return 'do some magic!'


def user_exit_gym_turnstile_get(phone_number):  # noqa: E501
    """Tries to exit gym

     # noqa: E501

    :param phone_number: User&#x27;s phone number
    :type phone_number: str

    :rtype: InlineResponse2001
    """
    return 'do some magic!'
