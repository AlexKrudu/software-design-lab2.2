# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ManagerRenewUserSubscriptionBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, user_id: str=None, subscription_duration_days: int=None):  # noqa: E501
        """ManagerRenewUserSubscriptionBody - a model defined in Swagger

        :param user_id: The user_id of this ManagerRenewUserSubscriptionBody.  # noqa: E501
        :type user_id: str
        :param subscription_duration_days: The subscription_duration_days of this ManagerRenewUserSubscriptionBody.  # noqa: E501
        :type subscription_duration_days: int
        """
        self.swagger_types = {
            'user_id': str,
            'subscription_duration_days': int
        }

        self.attribute_map = {
            'user_id': 'user_id',
            'subscription_duration_days': 'subscription_duration_days'
        }
        self._user_id = user_id
        self._subscription_duration_days = subscription_duration_days

    @classmethod
    def from_dict(cls, dikt) -> 'ManagerRenewUserSubscriptionBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The manager_renew_user_subscription_body of this ManagerRenewUserSubscriptionBody.  # noqa: E501
        :rtype: ManagerRenewUserSubscriptionBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def user_id(self) -> str:
        """Gets the user_id of this ManagerRenewUserSubscriptionBody.


        :return: The user_id of this ManagerRenewUserSubscriptionBody.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str):
        """Sets the user_id of this ManagerRenewUserSubscriptionBody.


        :param user_id: The user_id of this ManagerRenewUserSubscriptionBody.
        :type user_id: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def subscription_duration_days(self) -> int:
        """Gets the subscription_duration_days of this ManagerRenewUserSubscriptionBody.

        Продолжительность абонимента в днях  # noqa: E501

        :return: The subscription_duration_days of this ManagerRenewUserSubscriptionBody.
        :rtype: int
        """
        return self._subscription_duration_days

    @subscription_duration_days.setter
    def subscription_duration_days(self, subscription_duration_days: int):
        """Sets the subscription_duration_days of this ManagerRenewUserSubscriptionBody.

        Продолжительность абонимента в днях  # noqa: E501

        :param subscription_duration_days: The subscription_duration_days of this ManagerRenewUserSubscriptionBody.
        :type subscription_duration_days: int
        """
        if subscription_duration_days is None:
            raise ValueError("Invalid value for `subscription_duration_days`, must not be `None`")  # noqa: E501

        self._subscription_duration_days = subscription_duration_days