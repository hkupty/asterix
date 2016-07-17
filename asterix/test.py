# encoding: utf-8
""" Utility functions to help testing. """
from unittest.mock import Mock


class dummy(object):

    def get(self, name, default):
        return Mock()


class dummy_master(object):

    def __init__(self):
        setattr(self, "__components", dummy())
