# Test Code to exercise the Apprise Python Library from Chris Caron - 
# Using an Object

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
#Xapobj.add('ifttt://'+secrets['IFTTT_key'])

# A sample Pushover notification - Working 100%
#Xapobj.add("pover://" + secrets["Pushover_key"])

# A sample Telegram notification - Working 100%
#Xapobj.add("apprise tgram://" + secrets["Telegram_key"] + "/")

# A sample Microsoft Teams notification  - Working 100% -> "General" Channel
#Xapobj.add("msteams://" + secrets["Teams_key"])

# A sample Join notification  - I no longer use this tool, it needs Android
#apobj.add("join://" + secrets["Join_key"])

# A simple Pushbulet notification  - I no longer use this tool, it needs Android
#apobj.add("pbul://" + secrets["Pushbullet_key"])

# A simple Techulus Push notification - Works but I get 3 messages
#Xapobj.add("push:///" + secrets["Techulus_key"] + "/")

# A simple Pushed notification - Working 100%
#Xapobj.add("pushed://" + secrets["Pushed_key"])

# A simple PushSafer notification - Working 100%
#Xapobj.add("psafers://" + secrets["PushSafer_key"])

# A simple Mac Desktop notification - Working 100%
#Xapobj.add("macosx://")

# A simple Spontit notification - Working 100%
#Xapobj.add("spontit://" + secrets["Spontit_key"] + "/")

# A simple LaMetric notification - Working 100%
#Xapobj.add("lametric://" + secrets["LaMetric_key"])

# A simple Notica notification - TEST THIS!
apobj.add("notica://?" + secrets["Notify_key"])

# A simple Popcornnotify notification - TEST THIS!
#apobj.add("popcorn:///" + secrets["Popcornnotify_key"] +"/12483462166")

# A simple AWS SNS notification - Working 100%!
#Xapobj.add("sns:///" + secrets["SNS_key"] +"/12483462166")

# A simple Twist notification - Works but throws errors!
#Xapobj.add("twist://" + secrets["Twist_key"])

# A simple Twist notification - Works but throws errors!
apobj.add("reddit://" + secrets["Reddit_key"])

# Then notify these services any time you desire. The below would
# notify all of the services loaded into our Apprise object.
apobj.notify(
    body="Body of notification, random text",
    title="Test to Various Notification Services",
)
