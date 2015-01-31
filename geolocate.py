#! /usr/bin/python

import pygeoip
gi = pygeoip.GeoIP('/opt/GeoIP/Geo.dat')
def printRecord(gt):
	rec = gi.record_by_name(gt)
	city = rec['city']
	region = rec['region_name']
	country = rec
