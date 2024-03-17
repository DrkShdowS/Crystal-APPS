import logging
import discord
from discord.ext import commands
from colorama import init, Fore, Style
import ctypes
import asyncio

def set_console_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

init(autoreset=True)

print(Fore.MAGENTA + """
                            ░█████╗░██████╗░██╗░░░██╗░██████╗████████╗░█████╗░██╗░░░░░
                            ██╔══██╗██╔══██╗╚██╗░██╔╝██╔════╝╚══██╔══╝██╔══██╗██║░░░░░
                            ██║░░╚═╝██████╔╝░╚████╔╝░╚█████╗░░░░██║░░░███████║██║░░░░░
                            ██║░░██╗██╔══██╗░░╚██╔╝░░░╚═══██╗░░░██║░░░██╔══██║██║░░░░░
                            ╚█████╔╝██║░░██║░░░██║░░░██████╔╝░░░██║░░░██║░░██║███████╗
                            ░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝


                            [ + ] Made by: neon_321tzzz

                            [ + ] Github: soon guys! 

                            [ ! ] This is a free program, if anyone say this paid is scam!

                            [ + ] Made with health! 

                            [ + ] Use !cmds to continue in discord (: 
""")

def run():
    try:
        auth_token = input(f"{Fore.YELLOW}[!]{Style.RESET_ALL} Please enter an auth token here: ")
    except KeyboardInterrupt:
        print("\nExiting...")
        return

    logging.basicConfig(level=logging.WARNING)
    discord_logger = logging.getLogger('discord')
    discord_logger.setLevel(logging.ERROR)  
    discord_gateway_logger = logging.getLogger('discord.gateway')
    discord_gateway_logger.setLevel(logging.ERROR)
    discord_client_logger = logging.getLogger('discord.client')
    discord_client_logger.setLevel(logging.ERROR)

    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix="!", intents=intents) 

    @bot.event 
    async def on_ready():
        set_console_title(f"{bot.user.name} - Crystal Projects - PUBLIC")

    @bot.command()
    async def cmds(ctx):
        embed = discord.Embed(
            title="Crystal Commands",
            description="Here are the available commands:",
            color=discord.Color.green()
        )
        embed.add_field(name="!cmds", value="Displays available commands.", inline=False)
        embed.add_field(name="!github", value=" Provides a link to the GitHub repository.", inline=False)
        embed.add_field(name="!proxy", value="[Pending Mode] Generates proxies.", inline=False)
        embed.add_field(name="!gif", value="[Pending Mode] Sends random gifs.", inline=False)
        embed.add_field(name="SCAM MESSAGE:", value="Do not trust anyone do you not trust type !scam for more informations !!!")
        embed.add_field(name="Message for users:", value="This is a free program. Anyone claiming it is paid is likely a scam. Do not trust them!", inline=False)
        embed.set_footer(text="Powered by Crystal APP - Made by Neon")
        await ctx.send(embed=embed)

    @bot.command()
    async def github(ctx):
        embed = discord.Embed(
            title="Github Link",
            description="Here this link for you please add a star of my github (please): https://github.com/DrkShdowS/Crystal-APPS",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

    @bot.command()
    async def proxy(ctx):
        embed = discord.Embed(
            title="Proxy Functionality",
            description="This functionality will be available soon. Please wait for an update!",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

    @bot.command()
    async def gif(ctx):
        embed = discord.Embed(
            title="GIF Functionality",
            description="This functionality will be available soon. Please wait for an update!",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)        

    try:
        bot.run(auth_token)
    except discord.LoginFailure:
        print("ERROR: [!] Invalid token provided. Please provide a valid bot token.")
        input()

if __name__ == "__main__":
    run()
