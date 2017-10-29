# attack_report
A simple tool to generate an HTML of received attacks in a server (tested in Ubuntu Server 16.10)

## Prerequisites

* Python 3
* A version of MaxMind GeoLite2 City database (download at http://dev.maxmind.com/geoip/geoip2/geolite2/)
* Python 3 bindings for MaxMind databases (pip3 install geolite2 or pip3 install geoip2)

## Usage


Edit build.py and modify:

* DB: it contains the path name of the geolite2 city database
* ATTACKS: the path name of the SQLite database that will be generated

Building the attacks database:
    
    ./build.py
    
Generating the report:

    ./generate_report > report.html


This software uses:

* Free MaxMind Geolite2 city database.
* Min CSS framework by Owen Versteeg (http://owenversteeg.com)
