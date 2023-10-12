from string import punctuation

import numpy as np 
import pandas as pd

import re

import usaddress

# Use to load in the dataframe from CSV for future use.
def load_data(filename):
	try:
		df = pd.read_csv(filename)
	except:
  		df = None
	return df

# Use to clean addresses using usaddress to make them uniform, then match with verfification if possible.
def address_cleaner(address_list):
	parsed_list= []
	for address in address_list:
		try:
			#address = normalize_address_record(address)
			address_parsed_dict = dict((key, value) for (value, key) in usaddress.parse(address))
			# Standardize StreetNamePreDirectional to NESW
			address_parsed_dict['StreetNamePreDirectiona'] = address_parsed_dict['StreetNamePreDirectiona'][0]
		except:
			address_parsed = None
			continue


