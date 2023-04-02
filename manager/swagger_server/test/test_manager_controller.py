# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.manager_register_user_body import ManagerRegisterUserBody  # noqa: E501
from swagger_server.models.manager_renew_user_subscription_body import ManagerRenewUserSubscriptionBody  # noqa: E501
from swagger_server.test import BaseTestCase


class TestManagerController(BaseTestCase):
    """ManagerController integration test stubs"""

    def test_manager_get_user_subcription_info_get(self):
        """Test case for manager_get_user_subcription_info_get

        Gets information about user's subscription
        """
        query_string = [('phone_number', 'phone_number_example')]
        response = self.client.open(
            '/manager/get_user_subcription_info',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_manager_register_user_post(self):
        """Test case for manager_register_user_post

        Add new user with given username
        """
        body = ManagerRegisterUserBody()
        response = self.client.open(
            '/manager/register_user',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_manager_renew_user_subscription_post(self):
        """Test case for manager_renew_user_subscription_post

        Add new user with given username
        """
        body = ManagerRenewUserSubscriptionBody()
        response = self.client.open(
            '/manager/renew_user_subscription',
            method='POST',
            data=json.dumps(body),
            content_type='*/*')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
