# Welcome Discord Bot

Bot welcomes new members on Discord's Guild.

## Requirements

- Create a bot application on [Discord's developers portal](https://discord.com/developers/applications). Special attention to the [intent permissions](https://discordpy.readthedocs.io/en/latest/intents.html)

- Install Docker

## Basic Usage

0. Edit the ``src/welcome-message.md`` as you please

1. Set the API_TOKEN env var from the Discord Application bot

2. Run ``make`` to build and run the docker container

3. When you are done run ``make clean`` to remove the docker container and image