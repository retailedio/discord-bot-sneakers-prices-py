# Retailed Discord Bot Sneakers Prices

> ⭐️ A star would be highly appreciated

## Features

* `/payout [sku]` Get the best payout for a sneaker

![image](https://tlyriaxy.sirv.com/Retailed/discord/snk-price-command.png)

# Setup

## Install

`pip install -r requirements.txt`

## Step 1: Create a Discord bot

1. Go to https://discord.com/developers/applications create an application

2. Build a Discord bot under the application

3. Get the token from bot setting

4. Store the token to `.env` under the `TOKEN`

5. Turn **MESSAGE CONTENT INTENT** `ON`

   ![image](https://tlyriaxy.sirv.com/Retailed/discord/discord-bot-intent.png)
6. Invite your bot through OAuth2 URL Generator

   ![image](https://tlyriaxy.sirv.com/Retailed/discord/discord-bot-oauth.png)

## Step 2: Retailed API

Save both in `.env`

1. Register on https://app.retailed.io
2. Go to `https://app.retailed.io/app/<YOUR-TENANT>/settings/api/keys`
3. Create new API key
4. Store the token to `.env` under the `API`

## Step 3: Run the bot

1. Open a terminal or command prompt
2. Navigate to the directory where you installed the Retailed Discord Bot
3. Run `python main.py` to start the bot

Enjoy !
