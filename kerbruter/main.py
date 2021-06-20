#!/usr/bin/env python3

# imports
import argparse
import sys
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

from impacket import version
from impacket.examples import logger
from impacket.krb5.kerberosv5 import getKerberosTGT, KerberosError, SessionKeyDecryptionError
from impacket.krb5 import constants
from impacket.krb5.types import Principal
from impacket.krb5.ccache import CCache

class KerbruteArgumentParser:

    def __init__(self):
        self._parser = argparse.ArgumentParser()
        self._define_args()

    def _define_args(self):
        self._parser.add_argument('-debug', action='store_true', help='Turn DEBUG output ON')

        user_group = self._parser.add_mutually_exclusive_group(required=True)
        user_group.add_argument('-user', help='User to perform bruteforcing')
        user_group.add_argument('-users', help='File with user per line')

        password_group = self._parser.add_mutually_exclusive_group()
        password_group.add_argument('-password', help='Password to perform bruteforcing')
        password_group.add_argument('-passwords', help='File with password per line')

        self._parser.add_argument('-domain', required=True, help='Domain to perform bruteforcing')

        self._parser.add_argument('-dc-ip', action='store', metavar='<ip_address>',
                                  help='IP Address of the domain controller')

        self._parser.add_argument('-threads', type=int, default=1,
                                  help='Number of threads to perform bruteforcing. Default = 1')

        self._parser.add_argument('-outputfile', help='File to save discovered user:password')

        self._parser.add_argument('-outputusers', help='File to save discovered users')

        self._parser.add_argument('-no-save-ticket', action='store_true',
                                  help='Do not save retrieved TGTs with correct credentials')