# Discord Reaction Role Bot Python (Nextcord)

This Discord bot allows users to assign roles to themselves by reacting to a specific message with a predefined emoji. It's built using Nextcord (formerly known as discord.py) and relies on a configuration file (`config.ini`) to set up the bot's parameters.

## Features

- Assign roles to users based on reactions to a specific message.
- Remove roles when reactions are removed from the message.
- Configurable through `config.ini` file.

## Prerequisites

Before running the bot, make sure you have the following installed:

- Python 3.6 or higher
- `nextcord` library (install via `pip install nextcord`)
- `configparser` library (usually included in Python standard library)

## Configuration

The bot's behavior can be configured using the `config.ini` file. Here's a brief overview of the configuration options:

- `token`: Your Discord bot token.
- `role-id`: The ID of the role to be assigned/removed.
- `message-id`: The ID of the message to which users will react.
- `emoji-name`: The name of the emoji users need to react with.

Make sure to fill out these values correctly before running the bot.

## Usage

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Edit the `config.ini` file and fill in your Discord bot token, **role ID**, **message ID**, and **emoji name**.
4. Run the bot using Python: `python bot.py`.
5. Invite the bot to your Discord server.
6. Set up the reaction role by sending the message specified in the configuration and reacting to it with the designated emoji.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.