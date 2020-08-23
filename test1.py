# Test Code to excercise the Apprise Python Library from Chris Caron - MJP Using an Object
import apprise

# Move keys to an external file
try:
    from secrets import secrets
except ImportError:
    print("Keys are kept in secrets.py, you need to find them!!!")
    raise

# Create an Apprise instance
apobj = apprise.Apprise()

# Add all of the notification services by their server url.
# A sample IFTTT notification  - Working 100%
#apobj.add('ifttt://'+secrets['IFTT_key'])

# A sample Pushover notification - Working 100%
apobj.add('pover://'+secrets['Pushover_key'])

# A sample Telegram notification - Working 100%
#apobj.add('apprise tgram://'+secrets['Telegram_key']+'/')

# A sample Microsoft Teams notification  - Working 100% -> "General" Channel
#apobj.add('msteams://'+secrets['Teams_key'])

# A sample Join notification  - Working 100%
#apobj.add('join://'+secrets['Join_key'])

# A simple Pushbulet notification  - Working 100% (Android ONLY)
apobj.add('pbul://'+secrets['Pushbullet_key'])

# A simple Techulus Push notification - Works but I get 3 messages
#apobj.add('push:///'+secrets['Techulus_key']+'/')

# A simple Pushed notification - Working 100%
#apobj.add('pushed://'+secrets['Pushed_key'])

# A simple PushSafer notification - Working 100%
#apobj.add('psafers://'+secrets['PushSafer_key'])

# A simple Mac Desktop notification - Working 100%
#apobj.add('macosx://')

# A simple Spontit notification - Working 100%
apobj.add('spontit://'+secrets['Spontit_key']+'/')

# A simple LaMetric notification - TEST!!!!
#apobj.add('lametric://'+secrets['LaMetric_key'])


# Then notify these services any time you desire. The below would
# notify all of the services loaded into our Apprise object.
apobj.notify(
    body='Body of notification, random text',
    title='Test to Various Notification Services',
    
)
