from telethon import TelegramClient, events
from telethon.sessions import StringSession

‎# ========== ڕێکخستنەکان ==========
api_id = 33774652
api_hash = "c438941d8f43a0ff59fcc4b3f3c2fb42"
session = "1AZWarzgBu3-KiH74R8lf-DsuIsRdxleaXi6S7pBPvKYH-SZLulIUltJTYR7WvTXR7Qgr04wYFVZVipBSn6FR8cZXa_oiJjmvskEtzYMr5W1CLF8hmYFyzqhq3ZM3rt_htKJLrpLuy5XWNMYoiBrPtSie9kfd1riyqcW1b34fTNhueoWZ4mcPGSeXdH1GaEMTG6URjaTBacCrEBlUzEexQEy5RMn6lUsdHLHrW30T79Mp5lNhK09aI9Mi0U0vtR7rnTXEUuVIXgyZxkkcgNDVS88eOcs24cCykxTyLdAsmvUXJJK0UY-G3p9xRnsQ06628-04aBuDm8aBRk4-ZDTrCclHxTN6Ojc="
# ===================================

SOURCE_CHANNEL = "@approved_card4"    # سەرچاوە (لێیەوە دەخوێنیتەوە)
TARGET_CHANNEL = "@Cc428Card"         # ئامانج (بۆی دەنێریت) ← گۆڕدرا بۆ Cc428Card

client = TelegramClient(StringSession(session), api_id, api_hash)

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def handler(event):
    msg = event.message

    new_text = msg.text or ""
‎    # گۆڕینی هەموو ئاماژە کۆنەکان بۆ ناوی نوێ
    new_text = new_text.replace("@About_Warnisx", "@warven_24")
    new_text = new_text.replace("@Warnisx", "@warven_24")
    new_text = new_text.replace("@scrc1bot", "@warven_24")

‎    # تەنیا تەکست دەنێرین (وێنە و میدیا فڕێ دەدرێن)
    if new_text.strip() != "":
        await client.send_message(
            TARGET_CHANNEL,
            new_text,
            formatting_entities=msg.entities
        )

print("Bot is running... (Media/Photos are IGNORED, Target is now @Cc428Card)")
client.start()
client.run_until_disconnected()
