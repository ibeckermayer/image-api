# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_image_process_post(self):
        """Test case for image_process_post

        Takes an image and processes it according to accompanying json.
        """
        data = dict(image=(BytesIO(b'some file data'), 'file.txt'),
                    processes=(BytesIO(b'some file data'), 'file.txt'))
        response = self.client.open(
            '/image/image-process',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
