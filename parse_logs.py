#!/usr/bin/env python3
import sys
import glob, re
import geoip2.database

ERROR_TOKEN="preauth]"
re_error=re.compile(ERROR_TOKEN)

IP_ADDRESS="[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
re_address=re.compile(IP_ADDRESS)




def process_ip(reader, ip):
    response=reader.city(str(ip))
    
    sql="insert into attacks values (\"{0}\", \"{1}\", \"{2}\");"
    print(sql.format(ip, response.country.name, response.city.name))

def parse_log(reader, fd):
    print()
    print()
    print()
    
    print ("BEGIN TRANSACTION;")
    
    print()
    print()
    print()
    lines=fd.readlines()
    for line in lines:
        if re_error.search(line[:-1])!=None:
            ip=re_address.search(line)
            if ip!=None:
                process_ip (reader, ip.group(0))
    fd.close()
    print()
    print()
    print()
    
    print("COMMIT TRANSACTION;")
    
    print()
    print()
    print()


if __name__ == '__main__':
    reader = geoip2.database.Reader(sys.argv[1])
    file=sys.argv[2]
    last_slice=file[-3:]
    fd=open(sys.argv[2])
    parse_log(reader, fd)