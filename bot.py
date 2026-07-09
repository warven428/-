from telethon import TelegramClient, events
from telethon.sessions import StringSession

# ========== ڕێکخستنەکان ==========
api_id = 33774652
api_hash = "c438941d8f43a0ff59fcc4b3f3c2fb42"
session = "1AZWarzgBu3CZjzNDevUPZd1UxUvWL-MYU6kS_m9a1mn-GsrXFxwIz3X9iov-8q02E91SCOzTAUP4zv_LfbGip13Mih5AEsunq1pxL27b4MAjdi iBMyb1dju7_mQn4j1zhZjwJQDDRh_z1B0ZNiaMZbBxD3SFkjrbaXZ0wyNyii cPY9OBe0vLpCth-mb0X5897pJXuN2i9YCbznNmNOZEg3Gz2T4EQhJT6pMXnL8pghczA2vg3jsoLuG6eOQJvnZOWzc_4dSH26x5WnfIO1WciaHFy-Y_zUa1sbYWn47oeb_ZyOyCGHeCAGBgICDXk8GGKY4HQtgwSuh19C6HanLOXiX7NeY="
# ===================================

SOURCE_CHANNEL = "@WarnisxCcScrap"
TARGET_CHANNEL = "@Cc428Card"

client = TelegramClient(StringSession(session), api_id, api_hash)

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def handler(event):
    msg = event.message

    new_text = msg.text or ""
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

print("Bot is running...")
client.start()
client.run_until_disconnected()
