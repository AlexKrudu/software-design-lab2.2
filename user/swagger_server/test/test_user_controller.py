# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response403 import InlineResponse403  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_user_enter_gym_turnstile_get(self):
        """Test case for user_enter_gym_turnstile_get

        Tries to enter gym
        """
        query_string = [('phone_number', 'phone_number_example')]
        response = self.client.open(
            '/user/enter_gym_turnstile',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_exit_gym_turnstile_get(self):
        """Test case for user_exit_gym_turnstile_get

        Tries to exit gym
        """
        query_string = [('phone_number', 'phone_number_example')]
        response = self.client.open(
            '/user/exit_gym_turnstile',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
