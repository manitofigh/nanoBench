#!/usr/bin/env python3

import argparse
from cacheLib import *

import logging
log = logging.getLogger(__name__)


def main():
   parser = argparse.ArgumentParser(description='Cache Information')
   parser.add_argument("-logLevel", help="Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)", default='DEBUG')
   args = parser.parse_args()

   logging.basicConfig(stream=sys.stdout, format='%(message)s', level=logging.getLevelName(args.logLevel))

   cpuidInfo = getCpuidCacheInfo()

   print('')

   print("STARTING WITH getCaheInfo(1/2) from cacheInfo.py")
   print(getCacheInfo(1))
   print(getCacheInfo(2))
   print("DONE WITH getCaheInfo(1/2) from cacheInfo.py")
   if 'L3' in cpuidInfo:
      print(getCacheInfo(3))


if __name__ == "__main__":
    main()
