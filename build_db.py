#!/usr/bin/env python3

from subprocess import call, check_output, PIPE, Popen
import glob, sys

#PATH="/var/log/"
PATH        = "./"
PARSER      = "./parse_logs.py"
DB          = "ip.mmdb"
GUNZIP      = "zcat"
RM          = "rm"
CAT         = "cat"
ATTACKS     = "attacks.sqlite3"
SQLITE      = "sqlite3"

RESULTS     = "logs.sql"
ATTACKS_SQL_FILE="attacks.sql"


def build():
    files=[PATH+"auth.log", PATH+"auth.log.1"]
    gz_files=glob.glob(PATH+"auth*.gz")
    
    #Delete database and recreate
    call ([RM, ATTACKS])
    call ([RM, RESULTS])
    
    fd=open(ATTACKS_SQL_FILE, "r")
    command=[SQLITE, ATTACKS]
    call (command, stdin=fd)
    
    log=open(RESULTS, "w")
    
    call([PARSER, DB, files[0]], stdout=log)
    call([PARSER, DB, files[1]], stdout=log)
    
    
    for f in gz_files:
        tmp="delete.log"
        fd=open(tmp, "w")
        command=[GUNZIP, f]
        call ( command , stdout = fd)
        command=[PARSER, DB, tmp]
        call ( command , stdout=log )
    p1=Popen([CAT, RESULTS], stdout=PIPE)
    p2=Popen([SQLITE, ATTACKS], stdin=p1.stdout, stdout=PIPE)
    p1.stdout.close()
    
    
        
        
if __name__ == '__main__':
    build()