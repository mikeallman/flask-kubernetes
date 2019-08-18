# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.customer_item import CustomerItem  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_add_customer(self):
        """Test case for add_customer

        adds a customer item
        """
        inventory_item = {
  "surname" : "Allman",
  "dob" : "2000-01-23T04:56:07.000+00:00",
  "id" : "d290f1ee-6c54-4b01-90e6-d701748f0851",
  "first_name" : "Mike"
}
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/mikeallman/customer-service/1.0.0/customers',
            method='POST',
            headers=headers,
            data=json.dumps(inventory_item),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_customers(self):
        """Test case for search_customers

        searches customers
        """
        query_string = [('id', 'id_example'),
                        ('skip', 1),
                        ('limit', 50)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/mikeallman/customer-service/1.0.0/customers',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
