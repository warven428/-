import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# ========== ڕێکخستنەکان ==========
API_ID = 33790522
API_HASH = "00e4131295f55452e143c06099c1ddae"

# 🔴 سێشنە نوێیەکەت (گۆڕدرا بۆ ئەم سێشنە نوێیە)
SESSION_STRING = "1AZWarzgBu24Baus9-uFQx-d_JbeuAGeajVqHfn5he3Ka6I4VS1LT1k3LPigjLzFXVe7GV1csKeCeN3dp3pWjRyrkIGI_Q8IZ12n6-RQUoHLb9Ybov1l2Rpff-qTR1yiBPs1OQjtQiGOr_K4gjBXTyAO6dpOA9kkJcUYpp-gaJKZI_iv9hz6gBmOopSFsq9LdvoTxCpj8_etlwJNsN10h1IarWJNPopEx_SEKC8pLJSQzgeaPkjyrkykNxlMmuJ3H_0LQZFg5OIHYpC5DASBW1m-fa6FDpRlTddi-7b3era05TvLjewIugzuKVHSsC0jKglS4T9GEjRG7_msr71UnVQBmAvt1y-U="

SOURCE_CHANNEL = "@approved_card4"  # سەرچاوە
TARGET_CHANNEL = "@Cc428Card"       # ئامانج
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
        print(f"Bot disconnected due to network error: {e}")
    finally:
        await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
