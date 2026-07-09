from telethon import TelegramClient, events
from telethon.sessions import StringSession

# ========== ڕێکخستنەکان ==========
api_id = 33774652
api_hash = "c438941d8f43a0ff59fcc4b3f3c2fb42"
session = "1AZWarzgBu5ri3erA6UJlyTT8kJf2Bj4iV2LJTRCBU_9QqcC8CrVpgaSXm-ip4YH3xwNBGzcwJFyGjjHlvOoL0K1pL4cgme7spH9Nn2CQF0_OfEMvqRenIJJvDFYuKsqmVXzzBBYtSh_nOdaBvvfXc9ZPxUOmZDd3neKSmDqulD8IgfuX31gGlgfrky_INYFiIuEKaXYzvMci1hG0YKN41jSr1B0qQnmI7IlRuKD9vg3pYRESvCEiuejW2G3ITruiJJ2-R2Yndwk7Aa8ISHxHzr3eQgRM5_LfA0t3DQz80SyhWIijM15PCUfeRkwRdIKx_elMjsSuFa05VuMmwc57Yg3xw9AWA00="
# ===================================

SOURCE_CHANNEL = "@WarnisxCcScrap"
TARGET_CHANNEL = "@Cc428Card"

client = TelegramClient(StringSession(session), api_id, api_hash)

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def handler(event):
    msg = event.message

    new_text = msg.text or ""

    # گۆڕینی ناوەکان
    new_text = new_text.replace("@About_Warnisx", "[About](https://t.me/warven_24)")
    new_text = new_text.replace("@Warnisx", "[Warnisx](https://t.me/warven_24)")
    new_text = new_text.replace("Warnisx Scrapper", "KURD 428 Scrapper")
    
    # گۆڕینی کۆتایی پەیام بۆ ناوی نوێ و لینک
    new_text = new_text.replace("Developed By: [HamoDy](https://t.me/warven_24)", "Developed By: [B A R W A R I I 🇷🇺](https://t.me/warven_24)")

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
