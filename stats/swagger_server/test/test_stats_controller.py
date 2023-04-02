# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.test import BaseTestCase


class TestStatsController(BaseTestCase):
    """StatsController integration test stubs"""

    def test_stats_get_total_gym_attendance_stats_get(self):
        """Test case for stats_get_total_gym_attendance_stats_get

        Get gym's attendance stats
        """
        response = self.client.open(
            '/stats/get_total_gym_attendance_stats',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
