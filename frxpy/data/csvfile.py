"""
csvfile.py
---------------

This module contains some classes which can treat csv files.


.. autoclass:: fileio.csvfile.CSV

"""


import time
import codecs
import pathlib
import calendar

import h5py
import pandas
import numpy as np


class CSVFile(object):
    def __init__(self, csvfile, header_info='ohlc', bitask_fmt='bitask',
                 daytime_format='%Y%m%d %H%M%S', delimiter=';', header=None,
                 unit='minute'):
        
        self.csvfile = pathlib.Path(csvfile).expanduser().resolve()
        self.data = None
        self.delimiter = delimiter
        self.daytime_format = daytime_format
        self.header_info = header_info
        self.header = header
        self.unit = unit

        self._read()

    def _read(self):
        '''
        day-time, Open(BID), High(BID), Low(BID), Close(BID),
        '''
        self.data = pandas.read_csv(str(self.csvfile),
                                    sep=self.delimiter,
                                    header=self.header
        )

    def convert_daytime_to_seconds(self, daytime) -> int:
        s = self.datetime.strptime(daytime, self.daytime_format)
        return  calendar.timegm(s.utctimetuple())
    
    def convert_seconds_to_daytime(self, seconds):
        return self.datetime.utcfromtimestamp(seconds).strftime(self.daytime_format)

        
    def show(self):
        '''
        create an image. 
        '''
        pass
