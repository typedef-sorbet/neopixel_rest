## Overview

This is a Swagger-generated REST API used to control a NeoPixel WS2812 light strip controlled by a Raspberry Pi.
This repository is not intended for public use, but if you find some use for what's contained here, more power to you.

## First-Time Configuration

Set the number of LEDS on the strip in the NUM_LIGHTS variable in swagger_server/util.py.

## Endpoints

- [GET/POST] /color
  - GET: Returns the current color of the light strip.
  - POST: Sets all lights on the strip to the color contained within the request body. Accepts application/json only.
- [GET/POST] /gradient
  - GET: Returns the current gradient points of the light strip.
  - POST: Applies the gradient contained within the request body to the light strip. All gradient points are assumed to
  be equidistant from one another. Accepts application/json only.
