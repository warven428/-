from telethon import TelegramClient, events
from telethon.sessions import StringSession

# ========== ڕێکخستنەکان ==========
# !! ئاگاداری: تکایە api_id و api_hashـەکەت لە my.telegram.orgـەوە بە نوێ بکەوە !!
api_id = 33774652
api_hash = "c438941d8f43a0ff59fcc4b3f3c2fb42"

# سێشنە نوێیەکەت
session = "1AZWarzgBu5kDz__vBJKG_yn1ldfgAd6cbqOCWEt1J7MJLwMxDzQ6TUYQ342FZAyPp4pfF0vD0L-JVGtsIqRhwzmCxj18l9m_eLqftF3F-_DYEDEFR4o7jdP82hjbAOQjx6qO5L50ZP9yYH3rKP0mhoNZfD98fPnqo9Hp81Qsw9L1bXVLkJKLbivSDPCz1vRtQMpUMytCaeDpuCbJeyxf5essFwqnYH6leNkT8VKak2E241SpV-l9DV2-0vpZFMPYlpUk6oau5UCExM6l_xaUNYTXNULg7HqdISO9JnC_kju5cmDg_6zDShAnJz_0_TEiF77bUbqP0yCC2j06esL6l-PnJNMIP1o="
# ===================================

SOURCE_CHANNEL = "@approved_card4"    # سەرچاوە
TARGET_CHANNEL = "@Cc428Card"         # ئامانج

client = TelegramClient(StringSession(session), api_id, api_hash)

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def handler(event):
    msg = event.message

    new_text = msg.text or ""
    new_text = new_text.replace("@About_Warnisx", "@warven_24")
    new_text = new_text.replace("@Warnisx", "@warven_24")
    new_text = new_text.replace("@scrc1bot", "@warven_24")

    # تەنیا تەکست دەنێرین
    if new_text.strip() != "":
        await client.send_message(
            TARGET_CHANNEL,
            new_text,
            formatting_entities=msg.entities
        )

print("Bot is running... (Media/Photos are IGNORED)")
client.start()
client.run_until_disconnected()
