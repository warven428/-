import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# ========== ڕێکخستنەکان ==========
API_ID = 33790522
API_HASH = "00e4131295f55452e143c06099c1ddae"

SESSION_STRING = "1AZWarzgBuwtiHErne9Ht3cfd6fU0vzPKofRgjM-l2VMrN5C_SXcU7tEx9vSZmHXUAMvNxPPZeYXppdDrJhqKKnM_-t__4cQ8ZaKlv2tzQ5nGcp_bsPosAttaeEf3dulVBjXl4WGLViGmWCgvCV7eu-5F49eRXqcejZ2sCOa7bBd8FDrmBk6_njBL-EhihzqXkowk87NFdbDiZaDlrqx0f_q64i0nLYu62YX0WZa5wKGO4TnBQ1uEnXawARV67owrT4hAXqBysL9vjKv1-2wdp1wr-9dm31vReCLvd5NwOukWJb5d0cc8ftSsQJBBrMymqD8TC9GlfpkI81cZ2da6tQPnu1EmDv4="

SOURCE_CHANNEL = "@approved_card4"
TARGET_CHANNEL = "@Cc428Card"
# ========================================================

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def handler(event):
    msg = event.message
    new_text = msg.text or ""
    new_text = new_text.replace("@About_Warnisx", "@warven_24")
    new_text = new_text.replace("@Warnisx", "@warven_24")
    new_text = new_text.replace("@scrc1bot", "@warven_24")

    if new_text.strip() != "":
        await client.send_message(TARGET_CHANNEL, new_text, formatting_entities=msg.entities)

async def main():
    try:
        print("Bot is starting up...")
        await client.start()
        print("Bot is now ONLINE and listening! (Media is being ignored)")
        await client.run_until_disconnected()
    except Exception as e:
        # ئەم بەشە هەڵەی تۆڕ دەگرێت و ڕێگە لە کەوتنی ڕەیڵوەی دەگرێت
        print(f"Bot disconnected due to network error: {e}")
    finally:
        await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
