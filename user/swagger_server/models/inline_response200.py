# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse200(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, enter_at: datetime=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger

        :param enter_at: The enter_at of this InlineResponse200.  # noqa: E501
        :type enter_at: datetime
        """
        self.swagger_types = {
            'enter_at': datetime
        }

        self.attribute_map = {
            'enter_at': 'enter_at'
        }
        self._enter_at = enter_at

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse200':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200 of this InlineResponse200.  # noqa: E501
        :rtype: InlineResponse200
        """
        return util.deserialize_model(dikt, cls)

    @property
    def enter_at(self) -> datetime:
        """Gets the enter_at of this InlineResponse200.

        Time of user's gym enter  # noqa: E501

        :return: The enter_at of this InlineResponse200.
        :rtype: datetime
        """
        return self._enter_at

    @enter_at.setter
    def enter_at(self, enter_at: datetime):
        """Sets the enter_at of this InlineResponse200.

        Time of user's gym enter  # noqa: E501

        :param enter_at: The enter_at of this InlineResponse200.
        :type enter_at: datetime
        """
        if enter_at is None:
            raise ValueError("Invalid value for `enter_at`, must not be `None`")  # noqa: E501

        self._enter_at = enter_at
