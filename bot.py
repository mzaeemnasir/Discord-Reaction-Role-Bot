import nextcord,configparser
from nextcord.ext import commands

bot = commands.Bot()
config = configparser.ConfigParser()
config.read("config.ini")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print("--------------------")
    print("---Bot is ready!----")
    print("--------------------")


# Function to get guild object
# This function will return the guild object of the guild id passed
async def get_guild(guild_id):
    return await bot.fetch_guild(guild_id)


# Function to get role object
# This function will return the role object of the role id passed
async def get_role(guild):
    return guild.get_role(int(config["bot-settings"]["role-id"]))


# Function to check the condition
# This function will check if the reaction is added to the correct message and the correct emoji is used
def condition(emoji_name,message_id):
    if emoji_name.lower() == config["bot-settings"]["emoji-name"].lower() and message_id == int(config["bot-settings"]["message-id"]):
        return True

    return False

# Function to get member object
# This function will return the member object of the member id passed
async def get_member(guild,member_id):
    return await guild.fetch_member(member_id)


# Receive reaction event
# This event will be triggered when a reaction is added to a message
@bot.event
async def on_raw_reaction_add(payload):
    if condition(payload.emoji.name,payload.message_id):
        print("User reacted with a smile emoji!")
        guild = await get_guild(payload.guild_id)
        role = await get_role(guild)
        memeber = await get_member(guild,payload.user_id)
        await  memeber.add_roles(role)
        print(f"Role {role.name} added to {memeber.name}")

# Remove reaction event
# This event will be triggered when a reaction is removed from a message
@bot.event
async def on_raw_reaction_remove(payload):
    if condition(payload.emoji.name,payload.message_id):
            guild = await get_guild(payload.guild_id)
            role = await get_role(guild)
            memeber = await get_member(guild,payload.user_id)
            await memeber.remove_roles(role)
            print(f"Role {role.name} removed from {memeber.name}")



# Run the bot with the token from the config file
bot.run(config["bot-settings"]["token"])
