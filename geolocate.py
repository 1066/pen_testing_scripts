#! /usr/bin/python

import pygeoip
gi = pygeoip.GeoIP('/opt/GeoIP/Geo.dat')
def printRecord(gt):
	rec = gi.record_by_name(gt)
	city = rec['city']
	region = rec['region_name']
	country = rec['country_name']
	long = rec['longitude']
	lat = rec['latitude']
	print '[*] Target: ' + ' Geo-located. '
	print '[+] '+str(city)+', '+star(region)+' '+str(country)
	print '[+] Latitude: '+str(lat)+ ', Longitude: '+ str(long)
tgt = '173.255.226.98'
printRecord(tgt)

