import discord
from discord.ext import tasks
import os
from keep_alive import keep_alive
import requests
from bs4 import BeautifulSoup
import re


client = discord.Client()

#Otomatik mesaj atma burada BAŞLIYOR#
@tasks.loop(minutes=60)
async def send():
  CoinLink = "https://api.binance.com/api/v3/ticker/price"
  channel = client.get_channel(835869225066692668)
  r = requests.get(CoinLink)
  soup = BeautifulSoup(r.text, 'html.parser')
  string_soup = str(soup)

  #BTC PRICE INFO
  price_btc= (re.search(r'"BTCUSDT","price":"(.*?)"}', string_soup).group(1))
  
  #ETH PRICE INFO
  price_eth= (re.search(r'"ETHUSDT","price":"(.*?)"}', string_soup).group(1))
  
  #SOL PRICE INFO
  price_sol= (re.search(r'"SOLUSDT","price":"(.*?)"}', string_soup).group(1))
  
  #WAXP PRICE INFO
  price_waxp= (re.search(r'"WAXPUSDT","price":"(.*?)"}', string_soup).group(1))

  #TLM PRICE INFO
  price_tlm= (re.search(r'"TLMUSDT","price":"(.*?)"}', string_soup).group(1))

  """
  await channel.send("BTC=$"+str(price_btc))
  await channel.send("ETH=$"+str(price_eth))
  await channel.send("SOL=$"+str(price_sol))
  await channel.send("WAXP=$"+str(price_waxp))
  await channel.send("TLM=$"+str(price_tlm))
  """

  embed=discord.Embed(title="Crypto Market Prices by Karboran", url="https://twitter.com/karboran", description="You can learn more details about crypto world in my twitter.", color=0x109319)
  embed.add_field(name="BTC", value=str("$"+str(price_btc)), inline=False) 
  embed.add_field(name="ETH", value=str("$"+str(price_eth)), inline=True)
  embed.add_field(name="SOL", value=str("$"+str(price_sol)), inline=True)
  embed.add_field(name="WAXP", value=str("$"+str(price_waxp)), inline=True)
  embed.add_field(name="TLM", value=str("$"+str(price_tlm)), inline=True)

  embed.set_footer(text="Thank you for using this bot.")
  await channel.send(embed=embed)
#Otomatik mesaj atma burada BİTİYOR#

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  send.start()

keep_alive()
client.run(os.environ['TOKEN'])
