# encoding: utf-8
""" Utility functions to help testing. """
from unittest.mock import Mock


class dummy(object):

    def __init__(self):
        self.components = {}

    def get(self, name, default):
        if name not in self.components:
            self.components[name] = Mock()

        return self.components[name]


class dummy_master(object):

    def __init__(self):
        setattr(self, "__components", dummy())
