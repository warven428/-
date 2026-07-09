from telethon import TelegramClient, events
from telethon.sessions import StringSession

# ========== ڕێکخستنەکان ==========
api_id = 33774652
api_hash = "c438941d8f43a0ff59fcc4b3f3c2fb42"
# سێشنی نوێ کرایەوە
session = "1AZWarzgBu1GQLrQ91M39iRl40nFBTXB1PP_m48YeUd5A0Dacfv-DBQ_Uf4ZuQ4ylVFsFu_W3WtM1F0qILszQKcikvHv1u04IfEP08FQMBHcppp9TTjnYgJJ9he-wIBkoVxego1uO3SL1kIPYEHELpXfpfhgBCF9amvMlh1hk46_OV3wZVO5Ae0g7YH5r8LFerPKM_NdQQOmVBpjLlkgO7lkcIiJQQcuKoy8n-Eh8RaWXRT-hVBCjJAqOONFT7YaEY7IY7bjUmKun6_l_Abm_POFj_nUobLNoWs8KDFu38g7sLhfg72kJ4ZdexeQqoWe2cPiXPxYsaYkXQ0elnj-DdxAK729-ybM="
# ===================================

SOURCE_CHANNEL = "@WarnisxCcScrap"
TARGET_CHANNEL = "@Cc428Card"

client = TelegramClient(StringSession(session), api_id, api_hash)

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def handler(event):
    msg = event.message

    new_text = msg.text or ""
    # گۆڕینی "Warnisx Scrapper" بۆ "KURD Scrapper"
    new_text = new_text.replace("Warnisx Scrapper", "KURD Scrapper")
    # گۆڕینی هەر ناوێکی تر
    new_text = new_text.replace("@About_Warnisx", "@warven_24")
    new_text = new_text.replace("@Warnisx", "@warven_24")

    if msg.media:
        data = await msg.download_media(file=bytes)
        await client.send_file(
            TARGET_CHANNEL,
            data,
            caption=new_text,
            formatting_entities=msg.entities
        )
    else:
        await client.send_message(
            TARGET_CHANNEL,
            new_text,
            formatting_entities=msg.entities
        )

print("Bot is running with new session...")
client.start()
client.run_until_disconnected()
