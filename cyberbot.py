import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Connecté en tant que : ')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Bienvenue {0.mention} ! Et bien sûr :'.format(member, guild)
            await guild.system_channel.send(to_send, file=discord.File('presente_toi.gif'))


intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)

client.run("TOKEN")