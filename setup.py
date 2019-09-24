#!/usr/bin/env python
from setuptools import setup

setup(
    name='patroni-exporter',
    version='0.0.7',
    description='Export Patroni metrics in Prometheus format',
    author='Jan Tomsa',
    author_email='ops@showmax.com',
    scripts=['patroni-exporter.py'],
)
