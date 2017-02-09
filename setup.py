# Setup script for installing techbubbleiotjumpwaymqtt#
# Author:   Adam Milton-Barker <adammiltonbarker@gmail.com>#
# Copyright (C) 2016 - 2017 TechBubble Technologies Limited
# For license information, see LICENSE.txt

import sys
sys.path.insert(0, 'src')

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='iot_jumpway_mqtt_serial',
    version="0.0.1",
    author='Adam Milton-Barker',
    author_email='adammiltonbarker@gmail.com',
    package_dir={'': 'src'},
    url='https://github.com/TechBubbleTechnologies/IoT-JumpWay-Python-MQTT-Serial-Client',
    license='BSD',
    description='IoT JumpWay Python MQTT Serial Client',
    packages=['iot_jumpway_mqtt_serial'],
    install_requires=[
        "pyserial >= 3.2.1",
        "techbubbleiotjumpwaymqtt >= 0.3.9",
    ],
    classifiers=[],
)