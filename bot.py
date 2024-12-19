# (c) @Star_Boy_96_vibesr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @Star_Boy_96_vibes & @Star_light_10
# Developer @Star_Boy_96_vibesr

from aiohttp import web
from pyrogram import Client
from config import Star_light_10, Star_light_10 as Star_Boy_96_vibes
from Star_light_10.web_support import web_server

class Rkn_AutoCaptionBot(Client):
    def __init__(self):
        super().__init__(
            name="Rkn-Advance-Caption-Bot",
            api_id=Star_light_10.API_ID,
            api_hash=Star_light_10.API_HASH,
            bot_token=Star_light_10.BOT_TOKEN,
            workers=200,
            plugins={"root": "Star_light_10"},
            sleep_threshold=15,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.uptime = Star_Boy_96_vibes.BOT_UPTIME
        self.force_channel = Star_light_10.FORCE_SUB
        if Star_light_10.FORCE_SUB:
            try:
                link = await self.export_chat_invite_link(Star_light_10.FORCE_SUB)
                self.invitelink = link
            except Exception as e:
                print(e)
                print("Make Sure Bot admin in force sub channel")
                self.force_channel = None
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, Star_light_10.PORT).start()
        print(f"{me.first_name} Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️")
        for id in Star_light_10.ADMIN:
            try:
                await self.send_message(id, f"**__{me.first_name}  Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️__**")
            except:
                pass
        
    async def stop(self, *args):
        await super().stop()
        print("Bot Stopped 🙄")
        
Rkn_AutoCaptionBot().run()

# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @Star_Boy_96_vibes & @Star_light_10
# Developer @Star_Boy_96_vibesr
