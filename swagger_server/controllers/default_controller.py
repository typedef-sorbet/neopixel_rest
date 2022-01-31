import connexion
import six

from swagger_server.models.gradient import Gradient  # noqa: E501
from swagger_server.models.rgb import RGB  # noqa: E501
from swagger_server import util


def color_get():  # noqa: E501
    """Returns the current set color.

     # noqa: E501


    :rtype: RGB
    """
    return 'do some magic!'


def color_post(body=None):  # noqa: E501
    """Sets new color.

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = RGB.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def gradient_get():  # noqa: E501
    """Returns the current set gradient.

     # noqa: E501


    :rtype: Gradient
    """
    return 'do some magic!'


def gradient_post(body=None):  # noqa: E501
    """Sets new gradient.

     # noqa: E501

    :param body: 
    :type body: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = [RGB.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'
