#!/usr/bin/env python3

import ftplib
import getpass
def getFTp():
    siteName = input('Please Enter the FTp Server Name: ')
    username = input('Please Enter the login Nmae: ')
    password = getpass.getpass('Please Enter the login password for user: ')
    with ftplib.FTP(site_address) as ftp:
        ftp.login(username, password)
        ftp.cwd('/tmp/')
        print(ftp.getwelcome())
        print('----------------------------------------------------------------')
        print('Your Current Dir is:', ftp.pwd())
        print('Listing the contents of the Dir please wait...')
        print('----------------------------------------------------------------')
        ftp.retrlines('LIST')
        print('----------------------------------------------------------------')
        Download = input('Please Enter the Filename to download: ')
        print('----------------------------------------------------------------')
        ftp.retrbinary('RETR ' + Download. open(Download, 'wb').write)
        print('File Download is Successful.')
        print('Goodbye!')

getFTp()
