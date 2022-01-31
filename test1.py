# Test Code to exercise the Apprise Python Library from Chris Caron
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
#X apobj.add('ifttt://'+secrets['IFTTT_key'])

# A sample Pushover notification - Working 100%
#X apobj.add("pover://" + secrets["Pushover_key"])

# A sample Telegram notification - Working 100%
#X apobj.add("apprise tgram://" + secrets["Telegram_key"])

# A sample Microsoft Teams notification  - Working 100% -> "General" Channel
#X apobj.add("msteams://" + secrets["Teams_key"])

# A simple Techulus Push notification - Working 100%
#X apobj.add("push:///" + secrets["Techulus_key"] + "/")

# A simple Pushed notification - Working 100%
#X apobj.add("pushed://" + secrets["Pushed_key"])

# A simple PushSafer notification - Working 100%
#X apobj.add("psafers://" + secrets["PushSafer_key"])

# A simple Mac Desktop notification - Broken
apobj.add("macosx://")

# A simple Spontit notification - App broken??
#Y apobj.add("spontit://" + secrets["Spontit_key"] + "/")

# A simple LaMetric notification - Working 100%
#X apobj.add("lametric://" + secrets["LaMetric_key"])

# A simple Notica notification - Working 100%
#X apobj.add("notica://" + secrets["Notify_key"])

# A simple Popcornnotify notification - Works 100%
#X apobj.add("popcorn:///" + secrets["Popcornnotify_key"] +"/12483462166")

# A simple AWS SNS notification - Working 100%!
#X apobj.add("sns:///" + secrets["SNS_key"] +"/12483462166")

# A simple Twist notification - Works 100%
#X apobj.add("twist://" + secrets["Twist_key"])

# A simple Reddit notification - DOES NOT WORK!!! Issue filed in GitHub
apobj.add("reddit://" + secrets["Reddit_key"])

# A sample Join notification  - I no longer use this tool, it needs Android
#apobj.add("join://" + secrets["Join_key"])

# A simple Pushbulet notification  - I no longer use this tool, it needs Android
#apobj.add("pbul://" + secrets["Pushbullet_key"])

# A sample Join notification  - I no longer use this tool, it needs Android
#apobj.add("twilio://" + secrets["Twilio_Account_SID"] + secrets["Twilio_Auth_Token"] + "@12482189476/1243462166")

# Then notify these services any timeyou desire. The below would
# notify all of the services loaded into our Apprise object.
apobj.notify(
    body="Body of notification, random text",
    title="Test to Various Notification Services",
)
