# SMTP Settings
HOST = "smtp.gmail.com"
PORT = 465
SSL = True

USER = "yourname@gmail.com"
PASSWORD = "yourgmailpassword"

TO = "outgoing@example.com"
FROM = "yourname@gmail.com"

# Other settings.
LOGDIR = "~/Limnoria/logs/ChannelLogger/yournetworkname/" # Wherever ChannelLogger writes its log files.
SUBJECT = "IRC Logs for {date}"
CHANNEL_HEADER = "Today's logs for {channel}:"
CHANNELS = ["#engineering"]
