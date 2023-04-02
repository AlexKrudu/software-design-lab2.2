import datetime

import connexion
import six
from datetime import timedelta

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.manager_register_user_body import ManagerRegisterUserBody  # noqa: E501
from swagger_server.models.manager_renew_user_subscription_body import \
    ManagerRenewUserSubscriptionBody  # noqa: E501
from swagger_server import util
from swagger_server.db import *
from swagger_server import connection


def manager_get_user_subcription_info_get(phone_number):  # noqa: E501
    """Gets information about user&#x27;s subscription

     # noqa: E501

    :param phone_number: User&#x27;s phone number to fetch info for
    :type phone_number: str

    :rtype: InlineResponse200
    """
    user_name, user_id, events = get_user_subscription_events(connection.conn, phone_number)
    if user_name is None:
        return {}, 404

    active_until = None
    for event in events:
        event_at = event["event_at"]
        membership_duration_days = timedelta(
            days=event["membership_duration_days"])

        if active_until is None:
            active_until = event_at + membership_duration_days
            continue

        active_until = max(active_until, event_at) + membership_duration_days

    return InlineResponse200(active_until, user_name, user_id, events)


def manager_register_user_post(body):  # noqa: E501
    """Add new user with given username

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2001
    """

    if connexion.request.is_json:
        body = ManagerRegisterUserBody.from_dict(connexion.request.get_json())  # noqa: E501
        user_id = add_user_info(connection.conn, body.name, body.phone_number)
        if user_id is None:
            return {"message": "Duplicate phone number"}, 409

        add_user_membership_event(connection.conn, user_id, body.subscription_duration_days, 'CREATED')
        return InlineResponse2001(user_id)


def manager_renew_user_subscription_post(body=None):  # noqa: E501
    """Add new user with given username

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2002
    """

    body = ManagerRenewUserSubscriptionBody.from_dict(connexion.request.get_json())  # noqa: E501

    add_user_membership_event(connection.conn, body.user_id, body.subscription_duration_days, 'RENEWED')
    return InlineResponse2002()
