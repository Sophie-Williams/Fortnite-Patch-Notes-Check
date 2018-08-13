import requests
from config.py import operating_system, url
try:
    import os
except ImportError:
    print('Did not import os.')
    pass
try:
    import winsound
except ImportError:
    print('Did not import winsound.')
    pass

#please don't use this ridiculously ahead of time, as it continiously requests epicgames.
#use 15 minutes before downtime for a big patch and the bot will notify you and shut off once the page goes live.
#404 = Error, page didn't load.
#replace the below URL with whatever the upcoming version is.

get_version = url.split('patch-notes/')
get_version = get_version[1].replace('-','.')
r = requests.get(url=url)
checked = 0
while r.status_code == 404:
    checked += 1
    print('[' + str(checked) + '] Status of ' + str(get_version) + ' Patch Notes: ' + str(r.status_code))
    r = requests.get(url=url)

if operating_system == 'macOS':
    os.system('say "Patch notes for ' + str(get_version) + ' are now available!"')
elif operating_system == 'linux':
    os.system('spd-say "Patch notes for ' + str(get_version) + ' are now available!"')
elif operating_system == 'windows':
    duration = 1000  # millisecond
    freq = 440  # Hz
    winsound.Beep(freq, duration)
else:
    pass

print('Fortnite Patch Notes are now live! Take a look below: \n' + str(url))
