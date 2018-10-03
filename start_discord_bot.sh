#!/bin/bash
# crontab -e
# @reboot cd /home/dnlab; ./start_discord_bot.sh
# 0 0 * * * cd /home/dnlab; ./start_discord_bot.sh

kill -2 $(ps -ef | awk '/[d]iscord_bot.py/ {print $2}')
sleep 5
cd /home/dnlab/DNLabDiscordBot
rm nohup.out
nohup ./venv/bin/python3 discord_bot.py 2>&1 &
