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
        self.data = []
        self.delimiter = delimiter
        self.daytime_format = daytime_format
        self.header_info = header_info
        self.header = header
        self.unit = unit

        self._read()

    def _read(self):
        """
        day-time, Open(BID), High(BID), Low(BID), Close(BID),
        """
        self.data = pandas.read_csv(str(self.csvfile),
                                    sep=self.delimiter,
                                    header=self.header
        )
                
    def size(self):
        return (self.n_row, self.n_col)
    
    def info(self):
        """
        show storing information.
        """
        print(self.__str__())

    def reload(self):
        self.iter_idx = 0

    def convert_daytime_to_seconds(self, daytime) -> int:
        s = self.datetime.strptime(daytime, self.daytime_format)
        return  calendar.timegm(s.utctimetuple())
    
    def convert_seconds_to_daytime(self, seconds):
        return self.datetime.utcfromtimestamp(seconds).strftime(self.daytime_format)

    def __str__(self):
        x, y = self.size()
        load_flag = not( not self.data )
        out = '\
        file: {}\n\
        load: {}\n\
        size: ({:6d},{:2d})\n\
        '.format(self.filename, load_flag, x, y)
        return out
    
    def __add__(self):
        pass

    def __getitem__(self, key):
        if isinstance(key, slice):
            return [self[i] for i in range(*key.indices(len(self)))]
        elif isinstance(key, int):
            if key < 0:
                key += len(self)
            if key < 0 or key >= len(self):
                raise IndexError("The index (%d) is out of range." % key)
            return self.data[key]
        else:
            raise TypeError("Invalid argument type.")

    def __iter__(self):
        return self

    def __next__(self):
        if self.iter_idx >= len(self):
            raise StopIteration
        else:
            self.iter_idx += 1
            return self[self.iter_idx - 1]

    def __len__(self):
        return len(self.data)
        
