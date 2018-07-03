import logging
import socket
from logging import DEBUG
from logging import Formatter
from logging import getLogger
from logging import StreamHandler
import sys

"""

.. note::
    About Log Level
     0  NOTEST
    10  DEBUG
    20  INFO
    30  WARNING, WARN
    40  ERROR
    50  CRITICAL, FATAL
"""

mylogger = getLogger(__name__)
mylogger.setLevel(DEBUG)
stream = sys.stderr

handler = StreamHandler(stream)
fmt = '%(processName)s\t' \
      '%(asctime)s\t%(module)-8s\tL%(lineno)-3s'\
      '\t%(levelname)-7s\t%(message)s'
handler.setFormatter(Formatter(fmt=fmt, datefmt='%Y/%m/%d %H:%M:%S'))
mylogger.addHandler(handler)
