#Hooded Justice
#when members join a game, all votes are annon, and the least liked is kicked, but at the end of the game, all votes are dm'ed to all the players
#Let drama commence
import discord
import week1

@client.event
async def on_member_join(member):
	if dm_channel == True:
		await message.member.send["Welcome to the game!"]
	else:
		await create_dm(member)
		await message.member.send["Welcome to the game!"]
@client.event
async def on_member_remove(member):
	await message.member["BYE"]

@client.event
async def on_member_remove(member):
	print(f'{member} has left the server!')

@client.event
async def on_member_join(member):

@client.event
async def on_ready():
	print("Binkie is online.")
	print("Built by NotU")
#------------------------------------------------------------------

week1_path = Path("week1.JSON").resolve()
with open(week1_path, encoding='utf-8-sig') as week1:
	rawToken = json.load(week1)
	TOKEN = rawToken["TOKEN"]
	client = discord.Client()

vote1 = []
vote2 = []
vote3 = []
vote4 = []
vote5 = []
#game commands
@client.command
async def begin(message):
	if message.content.lower() == "-begin":
		gameStart == True
		players = []
		await message.channel.send("The game has begun...")
	return gameStart
	return players
	
@client.command
async def add(message):
	if message.content.lower() == "-join":
		if gameStart == True:
			players.append(message.author)
		print (players)
		await message.channel.send(f'{message.author} has joined the game.')
@client.command
async def close(message):
	if message.content.lower() == "-close":
		if gameStart == True:
			gameStart == False
			await message.channel.send("All player slots are now filled")
		return gameStart

#@client.command
#async def betting(message):
#	if message.content.lower
#implement this later

@client.command
async def vote(message):
	lower = message.content.lower()
	words = lower.split()
	if "-vote" in words:
		if message.author not in vote1:
		





	

client.run(TOKEN)

