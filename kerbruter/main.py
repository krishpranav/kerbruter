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
        