email_irc_logs
==============

A simple script to email IRC logs from Limnoria's ChannelLogger plugin.

This can be ran in one of two ways. With arguments:
```bash
./email_logs.py \
--host="smtp.gmail.com" --port="465" --ssl \
--user="you@gmail.com" --password="yourpass" \
--to="devs.project@gmail.com" --from="you@gmail.com" \
--logdir="~/Limnoria/logs/ChannelLogger/yournetworkname/" \
--channels "#devs" "#standup" "#support" \
```

Or with no or few arguments, and load missing settings/defaults from config.py:
```bash
./email_logs.py
```
