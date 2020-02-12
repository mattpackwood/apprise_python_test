# Test Code to excercise the Apprise Python Library
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

# A sample Pushover notification
apobj.add('pover://'+secrets['Pushover_key'])

# A sample Telegram notification - not working yet
# apobj.add('apprise tgram:///secrets['Telegram_key']')

# A sample Microsoft Teams notification - seems to be broken
# apobj.add('msteams://'+secrets['Teams_key'])

# A sample Join notification
apobj.add('join://'+secrets['Join_key'])

# Then notify these services any time you desire. The below would
# notify all of the services loaded into our Apprise object.
apobj.notify(
    body='Body of notification, random text',
    title='Test to IFTTT, Pushover Microsoft Teams and Join',
)
