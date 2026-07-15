import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# ========== ڕێکخستنەکان ==========
API_ID = 33790522
API_HASH = "00e4131295f55452e143c06099c1ddae"

# 🔴 سێشنە نوێیەکەت (گۆڕدرا بۆ ئەم سێشنە نوێیەی کە ناردووت)
SESSION_STRING = "1AZWarzgBu0uU3sU7X0yxSsfs3Zmc2-5axcQ-R_y2elHPIwTL3L00aRpWoVhvfZuKoYEqW8uYYJtYF374DjBtvM85wEakiNNKFPN_p8GcNVRecOdLA25hM6QtSilbZQ1WBhsXxRUL6HQKRTGsUtZPlofmGOFdcEuUg_1hsRSOftyjaELMU55cd6tEPOTeDvss94GQvOsV2EtiH8Mq1h9P5b3UvFPFKv0sUokYWUzrnzB1YanEzonF2gnCWWgcEiw8UGIMg0ZAUHlKox97OML0ipwOUP1dYOyeYEAKjRCrGeaN5NcMpennHlHHwkF707oTerI48DQVpF8SEGhAt6b4wrFFZUpMCc428duA="

SOURCE_CHANNEL = "@approved_card4"  # سەرچاوە
TARGET_CHANNEL = "@Card"       # ئامانج
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

    # تەنیا تەکست دەنێرێت (میدیا فڕێدەدات)
    if new_text.strip() != "":
        await client.send_message(
            TARGET_CHANNEL,
            new_text,
            formatting_entities=msg.entities
        )

async def main():
    try:
        print("Bot is starting up...")
        await client.start()
        print("Bot is now ONLINE and listening! (Media is being ignored)")
        await client.run_until_disconnected()
    except Exception as e:
        print(f"Bot disconnected due to network error: {e}")
    finally:
        await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
