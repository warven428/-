from telethon import TelegramClient, events
from telethon.sessions import StringSession

# ========== ڕێکخستنەکان ==========
api_id = 33774652
api_hash = "c438941d8f43a0ff59fcc4b3f3c2fb42"
session = "1AZWarzgBu1cI3bDK6Z5t5B_Nm883wvzXDR3WpiW2kcB11209myG8nE015D9JbVByYvFIipC5kQZ2ksQ7ZbytPyUDTTZEJE-80d_oJsKfq21GE7H8Iped8VbzIaTp8P9szTB1h4z6HFKRfE0HKJKUnNQ3g5P0LOdbM71My5njPM1jrF_UfgCi9n1yYE23DioUFM034xPbei2FrMEFgX_TJkvODci5V115KBuskijg9wK1voe1S8oM53wQp3Svn7ZCcJx_zar7113rBqBpdusahrCIwAAFad6RgQ6UhD9ARJDk0wH0JIMh651Lt6YahYJF5JM5CDGcMUVLAJnvRSPK4yoAjiVeALQ="
# ===================================

SOURCE_CHANNEL = "@WarnisxCcScrap"
TARGET_CHANNEL = "@Cc428Card"

client = TelegramClient(StringSession(session), api_id, api_hash)

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def handler(event):
    msg = event.message

    # دەقەکە بۆ فۆرماتی خوازراو دەگۆڕین (ناوەکان گۆڕدراون)
    new_text = msg.text or ""
    
    # گۆڕینی @About_Warnisx بۆ ناوی خۆت
    new_text = new_text.replace("@About_Warnisx", "@warven_24")
    
    # گۆڕینی @Warnisx بۆ ناوی خۆت
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
