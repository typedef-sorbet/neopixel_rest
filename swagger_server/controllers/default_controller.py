import connexion
import six
from colorsys import rgb_to_hsv, hsv_to_rgb

from swagger_server.models.gradient import Gradient  # noqa: E501
from swagger_server.models.rgb import RGB  # noqa: E501
from swagger_server import util

current_rgb = None
current_gradient = None

def color_get():  # noqa: E501
    """Returns the current set color.

     # noqa: E501


    :rtype: RGB
    """
    global current_rgb
    return current_rgb


def color_post(body=None):  # noqa: E501
    """Sets new color.

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    global current_rgb

    if connexion.request.is_json:
        body = RGB.from_dict(connexion.request.get_json())  # noqa: E501
    
    for i in range(util.NUM_LIGHTS):
        util.lights[i] = (body.r, body.g, body.b)

    current_rgb = body
    current_gradient = None

    return current_rgb


def gradient_get():  # noqa: E501
    """Returns the current set gradient.

     # noqa: E501


    :rtype: Gradient
    """
    global current_gradient
    return current_gradient


def gradient_post(body=None):  # noqa: E501
    """Sets new gradient.

     # noqa: E501

    :param body: 
    :type body: list | bytes

    :rtype: None
    """
    global current_gradient
    
    if connexion.request.is_json:
        body = [RGB.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501

    if len(body) > 1:
        hsv_list = [rgb_to_hsv(entry.r / 255, entry.g / 255, entry.b / 255) for entry in body]
        chunk_length = util.NUM_LIGHTS // (len(hsv_list) - 1)

        for section_index, (hsv_interpolate_from, hsv_interpolate_to) in enumerate(zip(hsv_list, hsv_list[1:])): 
            # section_index: the "chunk" of the light strip that we're working on
            # hsv_interpolate_from: HSV color point we're interpolating from
            # hsv_interpolate_to: HSV color point we're interpolating to (this color will NOT be part of the current chunk)

            for light_index in range(chunk_length):
                delta_h = (hsv_interpolate_to[0] - hsv_interpolate_from[0]) * (light_index / chunk_length)
                delta_s = (hsv_interpolate_to[1] - hsv_interpolate_from[1]) * (light_index / chunk_length)
                delta_v = (hsv_interpolate_to[2] - hsv_interpolate_from[2]) * (light_index / chunk_length)
                
                pixel_index = (section_index * chunk_length) + light_index
                
                new_rgb = hsv_to_rgb(hsv_interpolate_from[0] + delta_h, hsv_interpolate_from[1] + delta_s, hsv_interpolate_from[2] + delta_v)

                util.lights[pixel_index] = tuple(map(lambda i: i * 255, new_rgb))

        util.lights[-1] = (body[-1].r, body[-1].g, body[-1].b)

        # TODO calculate positions of interpolants, then calculate interpolations between them.

        current_gradient = body

    return current_gradient
