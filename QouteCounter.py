import discord, colorama, os, logging
from dotenv import load_dotenv
import pandas as pd



class QuoteCounter(discord.Client):
    """ A bot that counts the number of times a user has qouted another person. """
    async def on_ready(self):
        """ When the bot is ready, print a message to the console. """
        print_result(f"[+] Ready. Logged in as {self.user}")
        
    async def on_message(self, message):
        """ When a message is sent, check if it is a qoute. """ 
        if message.author == self.user:
            return # don't run commands on thyself 

        channel_id = os.environ.get("CHANNEL_ID") 
        csv_name = os.environ.get("OUTPUT_CSV") 

        # Check if message contains a @mention if in qoutes channel 
        if message.content = "!count_qoutes":
            if message.channel.id == channel_id and "@" in message.content.lower():

                data = pd.DataFrame(columns=['content', 'time', 'author'])
                
                async for msg in message.channel.history(): 
                    if msg.author != client.user:                        
                        data = data.append({
                            'author': msg.author.name
                            'time': msg.created_at,
                            'content': msg.content,
                        }, ignore_index=True)
                        

                data.to_csv(csv_name)
        

def print_result(output, color=colorama.Fore.GREEN): 
    """ Base method. Pretty print out results to terminal. """
    print(f"{color} {output} {colorama.Fore.RESET}")
    logging.info(output) 

if __name__ == "__main__":
    # Set up environment
    try:
        load_dotenv()
        token = os.environ["TOKEN"]
    except KeyError:
        print_result("[-] DISCORD_TOKEN not set. Exiting.", colorama.Fore.RED)
        exit(1)
        
    # Actually do stuff 
    intents = discord.Intents.default()
    intents.message_content = True
    QuoteCounter(intents=intents).run(token)
