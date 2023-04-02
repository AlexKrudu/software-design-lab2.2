# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse2002(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, active_until: datetime=None):  # noqa: E501
        """InlineResponse2002 - a model defined in Swagger

        :param active_until: The active_until of this InlineResponse2002.  # noqa: E501
        :type active_until: datetime
        """
        self.swagger_types = {
            'active_until': datetime
        }

        self.attribute_map = {
            'active_until': 'active_until'
        }
        self._active_until = active_until

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2002':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_2 of this InlineResponse2002.  # noqa: E501
        :rtype: InlineResponse2002
        """
        return util.deserialize_model(dikt, cls)

    @property
    def active_until(self) -> datetime:
        """Gets the active_until of this InlineResponse2002.

        date until gym subscription is active  # noqa: E501

        :return: The active_until of this InlineResponse2002.
        :rtype: datetime
        """
        return self._active_until

    @active_until.setter
    def active_until(self, active_until: datetime):
        """Sets the active_until of this InlineResponse2002.

        date until gym subscription is active  # noqa: E501

        :param active_until: The active_until of this InlineResponse2002.
        :type active_until: datetime
        """
        if active_until is None:
            raise ValueError("Invalid value for `active_until`, must not be `None`")  # noqa: E501

        self._active_until = active_until
