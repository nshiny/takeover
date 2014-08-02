"""Chris's first bot"""
__author__ = 'chriskwan'

from interface import *

class ChrisBot(Bot):
    def __init__(self, identifier):
        self.identifier = identifier

def make_bot(identifier):
    return ChrisBot(identifier)