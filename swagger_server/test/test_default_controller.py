# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.gradient import Gradient  # noqa: E501
from swagger_server.models.rgb import RGB  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_color_get(self):
        """Test case for color_get

        Returns the current set color.
        """
        response = self.client.open(
            '/color',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_color_post(self):
        """Test case for color_post

        Sets new color.
        """
        body = RGB()
        response = self.client.open(
            '/color',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_gradient_get(self):
        """Test case for gradient_get

        Returns the current set gradient.
        """
        response = self.client.open(
            '/gradient',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_gradient_post(self):
        """Test case for gradient_post

        Sets new gradient.
        """
        body = [RGB()]
        response = self.client.open(
            '/gradient',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
