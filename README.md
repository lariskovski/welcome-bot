# Welcome Discord Bot

Bot welcomes new members on Discord's Guild.

## Requirements

- Create a bot application on [Discord's developers portal](https://discord.com/developers/applications). Special attention to the [Server Members Intent permissions](https://discordpy.readthedocs.io/en/latest/intents.html)

- Python >= 3.6 installed

- Docker >= 20.10.5 installed (Optional)

## Basic Usage

1. Edit the ``src/welcome-message.md`` as you please.

2. Set the API_TOKEN env var from the Discord Application bot

3. Then run the project with local Python or as a Docker container (recommended).

### Local

``make local`` installs dependencies and run the application.

### Docker

Execute ``make`` or ``make run`` command to build and run the docker container. When you are done, ``make clean`` will remove the docker container and image.