#!/usr/bin/env python2.7
import datetime

import smtplib
from email.mime.text import MIMEText

# IMPORTANT: This script expects a python file with these globals set.
from config import FROM, HOST, PORT, USER, PASSWORD, TO, SUBJECT,\
                        LOGDIR, CHANNELS, CHANNEL_HEADER, SSL

def send_mail(to, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = FROM
    msg['To'] = to

    if SSL:
        s = smtplib.SMTP_SSL(HOST, PORT)
    else:
        s = smtplib.SMTP(HOST, PORT)
    s.login(USER, PASSWORD)
    s.sendmail(FROM, [to], msg.as_string())
    s.quit()

def main():
    subject = SUBJECT.format(date=datetime.date.today().strftime('%x'))
    BODY = []

    LOGFILE = "{logdir}{channel}/{channel}.{date.year:04d}-{date.month:02d}-{date.day:02d}.log"

    BODY.append('Don\'t want a line to show up in these logs? Prepend it with "[nolog]".')
    BODY.append("Limnoria ignores those and they never get logged to disk.")

    for c in CHANNELS:
        BODY.append("")
        BODY.append(CHANNEL_HEADER.format(channel=c))
        BODY.append("")

        filename = LOGFILE.format(logdir=LOGDIR, channel=c, date=datetime.date.today())
        try:
            with open(filename, "r") as f:
                data = f.readlines()
        except IOError as exc:
            data = ["ERROR: " + exc.strerror]
        for line in data:
            BODY.append(" "+line)

    # Assemble the BODY into a proper string.
    BODY = '\n'.join(BODY)

    send_mail(TO, subject, BODY)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Email some IRC logs.')
    parser.add_argument('--host', default=None, help='')
    parser.add_argument('--port', default=None, help='')
    parser.add_argument('--ssl', action='store_true', default=False, help='')
    parser.add_argument('--user', default=None, help='')
    parser.add_argument('--password', default=None, help='')
    parser.add_argument('--to', default=None, help='')
    parser.add_argument('--from', default=None, help='')
    parser.add_argument('--logdir', default=None, help='')
    parser.add_argument('--subject', default=None, help='')
    parser.add_argument('--channel-header', default=None, help='')
    parser.add_argument('--channels', default=None, nargs='*', help='')
    args = parser.parse_args()

    # Set globals based on arguments passed.
    for arg, value in args.__dict__.iteritems():
        if value:
            globals()[arg.upper()] = value

    main()


