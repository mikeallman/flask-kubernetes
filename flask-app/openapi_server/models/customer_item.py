# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class CustomerItem(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, first_name=None, surname=None, dob=None):  # noqa: E501
        """CustomerItem - a model defined in OpenAPI

        :param id: The id of this CustomerItem.  # noqa: E501
        :type id: str
        :param first_name: The first_name of this CustomerItem.  # noqa: E501
        :type first_name: str
        :param surname: The surname of this CustomerItem.  # noqa: E501
        :type surname: str
        :param dob: The dob of this CustomerItem.  # noqa: E501
        :type dob: datetime
        """
        self.openapi_types = {
            'id': str,
            'first_name': str,
            'surname': str,
            'dob': datetime
        }

        self.attribute_map = {
            'id': 'id',
            'first_name': 'first_name',
            'surname': 'surname',
            'dob': 'dob'
        }

        self._id = id
        self._first_name = first_name
        self._surname = surname
        self._dob = dob

    @classmethod
    def from_dict(cls, dikt) -> 'CustomerItem':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CustomerItem of this CustomerItem.  # noqa: E501
        :rtype: CustomerItem
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this CustomerItem.


        :return: The id of this CustomerItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CustomerItem.


        :param id: The id of this CustomerItem.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def first_name(self):
        """Gets the first_name of this CustomerItem.


        :return: The first_name of this CustomerItem.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this CustomerItem.


        :param first_name: The first_name of this CustomerItem.
        :type first_name: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def surname(self):
        """Gets the surname of this CustomerItem.


        :return: The surname of this CustomerItem.
        :rtype: str
        """
        return self._surname

    @surname.setter
    def surname(self, surname):
        """Sets the surname of this CustomerItem.


        :param surname: The surname of this CustomerItem.
        :type surname: str
        """
        if surname is None:
            raise ValueError("Invalid value for `surname`, must not be `None`")  # noqa: E501

        self._surname = surname

    @property
    def dob(self):
        """Gets the dob of this CustomerItem.


        :return: The dob of this CustomerItem.
        :rtype: datetime
        """
        return self._dob

    @dob.setter
    def dob(self, dob):
        """Sets the dob of this CustomerItem.


        :param dob: The dob of this CustomerItem.
        :type dob: datetime
        """
        if dob is None:
            raise ValueError("Invalid value for `dob`, must not be `None`")  # noqa: E501

        self._dob = dob
