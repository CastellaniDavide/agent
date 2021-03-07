"""Test agent file
"""
from agent import *

__author__ = "help@castellanidavide.it"
__version__ = "01.01 2020-11-30"

def test():
	"""Tests the agent function in the agent class
	Write here all test you want to do.
	REMEMBER to test your programm you can't use __init__ function
	"""
	assert agent() != "", "test failed (personal_code: 0)" # check all code
	
if __name__ == "__main__":
	test()
