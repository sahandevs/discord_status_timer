import discord
import asyncio
import datetime
import sys

def min_to_formatted_time(mins):
  delta = datetime.timedelta(minutes=mins)
  time = datetime.datetime(year=1000,month=1,day=1 ,minute=0, hour=0, second=0) + delta
  return time.strftime("%H:%M")



class StatusUpdaterClient(discord.Client):

    async def on_ready(self):
        pass
        # on_ready doesnt work with user token so we use this dirty trick with on_message

    is_first_time = True

    async def on_message(self, message):
        if self.is_first_time:
            self.is_first_time = False
            print(f"Logged in as {self.user}")
            await self.update_status_loop()

    timer = 0
    update_threshold = 0
    message = "Coding session ends in {time}"

    async def update_status_loop(self):
        while True:
            activity = discord.Game(self.message.replace("{time}", min_to_formatted_time(self.timer)))
            await self.change_presence(status=discord.Status.idle, activity=activity)
            await asyncio.sleep(self.update_threshold * 60)
            self.timer -= self.update_threshold


if __name__ == "__main__":
    client = StatusUpdaterClient()
    client.timer = int(sys.argv[1])
    client.update_threshold = int(sys.argv[2])
    client.message = sys.argv[3]
    client.run(
        sys.argv[4],
        bot=False
    )
