import connexion
import six

from openapi_server.models.customer_item import CustomerItem  # noqa: E501
from openapi_server import util

# simple in memory customer db
customers = {}


def add_customer(inventory_item=None):  # noqa: E501
    """adds a customer item

    Adds an item to the system # noqa: E501

    :param inventory_item: Inventory item to add
    :type inventory_item: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        inventory_item = CustomerItem.from_dict(connexion.request.get_json())  # noqa: E501

    customers[inventory_item.id] = inventory_item
    return 'added'


def search_customers(id=None, skip=None, limit=None):  # noqa: E501
    """searches customers

    By passing in the appropriate options, you can search for available inventory in the system  # noqa: E501

    :param id: pass an optional id for looking up customers
    :type id: str
    :param skip: number of records to skip for pagination
    :type skip: int
    :param limit: maximum number of records to return
    :type limit: int

    :rtype: List[CustomerItem]
    """

    if id:
        return [customers.get(id)]
    if skip:
        return list(customers.values())[skip:limit]
    return list(customers.values())
