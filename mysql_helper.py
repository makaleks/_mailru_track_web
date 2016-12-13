#!/usr/bin/env python2

# Note: to create backup you have to use your MySQL-admin user, who has RELOAD privilege, that affects all database

import sys, argparse, os
from os.path import isfile

def main(argv):
    user = ''
    filename = 'db_gzip_backup'

    arg_user = [
            '-u', 
            '--user', 
            'username', 
            'set MySQL user, that can create database and its owner', 
            'username'
            ]
    arg_file = [
            '-f', 
            '--file', 
            'filename', 
            'set MySQL backup file to restore', 
            'filename'
            ]
    parser = argparse.ArgumentParser(description='Restore MySQL database.')

    parser.add_argument('user', type=str, help='database user')
    parser.add_argument('-r', '--restore', action='store_true', help='restore database from backup file; creates backup by default')
    parser.add_argument('-s', '--sql_file', action='store_true', help='save as sql text, not compressed .sql.gz')
    parser.add_argument('-f', '--file', type=str, default=filename, required=False, help='set backup file')

    args = parser.parse_args()

    args.file += '.sql'
    if args.sql_file == False:
        args.file += '.gz'
    
    if args.restore:
        if isfile(args.file) == False:
            sys.exit("File '{0}' does not exist!".format(args.file))
        command_str = 'gunzip -ck db_gzip_backup.sql.gz | mysql -u webofthem_admin -p'
    else:
        command_str = "mysqldump --single-transaction --flush-logs --master-data=2 -B WEBOFTHEM -u {0} -p {1} > {2}".format(args.user, '' if args.sql_file else '| gzip', args.file)
        
    #print args

    print 'Trying to process:\n$ ', command_str
    os.system(command_str)

if __name__ == "__main__":
    main(sys.argv[1:])
