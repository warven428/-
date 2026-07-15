import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# ========== ڕێکخستنەکان (بە تەواوی پڕکراونەتەوە) ==========
API_ID = 33774652
API_HASH = "c438941d8f43a0ff59fcc4b3f3c2fb42"

# سێشنە نوێیەکەت (کە لە iSH وەرتبوو)
SESSION_STRING = "1AZWarzgBu30Ism7pw5g2mNXlXvweZchZNbLZMZO25GCIKOHTb_i7VSz1flfG5OR1nwZehL5pm0rw98tJLYqM1i32amzCi5IoIOLJGU_AXdFPAEH9ZHYHlOxOwdOlouh5329PYS0aJGxYRd7a5iPkh1A0WRO6BWyCoY6fnMbkQcEgNbes_XwnPml6p1RaR6sXptNV0v5gftR5UtUManyJGEdO2bm32qKLyGC39m5dX402melaD3fNvCRxiDCGZRn-1rjYdAbpc3U1LdoeWgQ5nFiptLSvYuVMFKcy81B2aEBeifg_Kcm6uQ8w-fW9Xgj7ZYsFE4Tt_iXD85oY2p2LHty3WxL4UUo="

SOURCE_CHANNEL = "@approved_card4"  # سەرچاوە
TARGET_CHANNEL = "@Cc428Card"       # ئامانج
# ========================================================

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def handler(event):
    msg = event.message
    new_text = msg.text or ""

    # گۆڕینی ناوە کۆنەکان
    new_text = new_text.replace("@About_Warnisx", "@warven_24")
    new_text = new_text.replace("@Warnisx", "@warven_24")
    new_text = new_text.replace("@scrc1bot", "@warven_24")

    # تەنیا تەکست دەنێرێت و میدیا (وێنە/ڤیدیۆ) فڕێدەدات
    if new_text.strip() != "":
        await client.send_message(
            TARGET_CHANNEL,
            new_text,
            formatting_entities=msg.entities
        )

async def main():
    print("Bot is starting up...")
    await client.start()
    print("Bot is now ONLINE and listening! (Media is being ignored)")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
