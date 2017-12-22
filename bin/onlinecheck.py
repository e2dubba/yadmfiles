#!/usr/bin/env python3

import webbrowser
import dbusnotify



def main():
    dbusnotify.write('Check the TC for Updates\npurl.org/TC', 
        title='TC Updates', app_name='crontab')
    webbrowser.open_new_tab('http://purl.org/TC')
    

if __name__ == '__main__':
    main()
