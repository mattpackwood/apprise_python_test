# Test Code to excercise the Apprise Python Library from Chris Caron
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
# A sample IFTTT notification
apobj.add('ifttt://'+secrets['IFTT_key'])

# A sample Pushover notification - NEED TO TEST MORE
#apobj.add('pover://'+secrets['Pushover_key'])

# A sample Telegram notification - The issue is in creating a Telegram Bot that can receive the signal
#apobj.add('apprise tgram://'+secrets['Telegram_key']+'/')

# A sample Microsoft Teams notification - seems to be broken
# apobj.add('msteams://'+secrets['Teams_key'])

# A sample Join notification - NEED TO TEST MORE
#apobj.add('join://'+secrets['Join_key'])

# A simple Pushbulet notification - NEED TO TEST MORE
#apobj.add('pbul://'+secrets['Pushbullet_key'])

# A simple Techulus Push notification - Seem to get 3 messages
#apobj.add('push:///'+secrets['Techulus_key']+'/')

# A simple Pushed notification - Working 100%
#apobj.add('pushed://'+secrets['Pushed_key'])

# A simple PushSafer notification - Working 100%
#apobj.add('psafers://'+secrets['PushSafer_key'])

# A simple Mac Desktop notification
# apobj.add('macosx://')

# Then notify these services any time you desire. The below would
# notify all of the services loaded into our Apprise object.
apobj.notify(
    body='Body of notification, random text',
    title='Test to Various Notification Services',
)
