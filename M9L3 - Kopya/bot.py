import discord
from discord.ext import commands
import requests
import pyttsx3

TOKEN = "MTUzNDI1NDYzMjMyNTM1MzUzMw.GqKwAL.pdIhkHgz-Ykge7n2LT-16w2M7fgcxaceiHNvA0"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

def get_fact():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            print(data)  # shows full JSON response
            return data["text"]
        else:
            return f"Error: API returned status code {response.status_code}"

    except Exception as e:
        return f"Error while contacting API: {e}"

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

@bot.command()
async def start(ctx):
    await ctx.send("Hello! I am your fact bot 👋")

@bot.command()
async def fact(ctx):
    fact_text = get_fact()

    await ctx.send(f"Interesting fact: {fact_text}")

    speak(fact_text)

bot.run(TOKEN)