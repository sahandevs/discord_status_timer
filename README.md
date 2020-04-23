# discord_status_timer

sets your discord's status with a count down timer

#### usage:

- clone the project
- run `python -m pip install -r requirements.txt`
- run `python main.py <timer> <update_threshold> <message> <token>`

example :
`python.exe main.py 120 2 "this is a test {time}" "MyToken"`

__timer__: start time in minutes (for 1.5 hours set to 90)

__update_threshold__: how frequently updates the status

__message__: message to set in the status. (use `{time}` in your message to define where it should put the remaining time)
__token__: your discord token ([how to obtain token](https://github.com/Tyrrrz/DiscordChatExporter/wiki/Obtaining-Token-and-Channel-IDs#how-to-get-a-user-token))

----


this script uses [discord.py](https://github.com/Rapptz/discord.py) library.
