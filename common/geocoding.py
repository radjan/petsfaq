# -*- coding: utf-8 -*-
import urllib2
#TODO requests?
import json

GEOCODING_URL = u'http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=%s'
SENSOR_TRUE = 'true'
SENSOR_FALSE = 'false'

def get_coordinate(addr):
    '''
    Get the coordinate of the address.
    Note: google geocoding is limited by 2500 times per day.

    @param addr: the address string

    return {'lng': float, 'lat': float}
    '''
    #TODO doc format
    url = GEOCODING_URL % (addr, SENSOR_FALSE)
    response = urllib2.urlopen(url.encode('utf-8'))
    results = json.load(response)
    the_one = results['results'][0]
    return the_one.get('geometry', {}).get('location', None)

#TODO: Test
if __name__ == '__main__':
    print get_coordinate(u'台北市大安區敦化南路二段216號5F')
