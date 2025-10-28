import asyncio
from telegram import Bot

TOKEN = '8400123980:AAHFjrY0jd74k8hhZvS1omSyUA74GIIlQvA'

CHAT_ID = -1002538250001

TOPIC_ID = 917

MESSAGES = [
    "ДЕНЬ!",
    "НОЧЬ!"
]

INTERVAL_HOURS = 3600

current_index = 0

async def main():
    global current_index
    bot = Bot(token=TOKEN)
    print("✅ Бот запущен. Отправка в тему начнётся через несколько секунд...")

    while True:
        try:
            msg = MESSAGES[current_index]
            await bot.send_message(
                chat_id=CHAT_ID,
                text=msg,
                message_thread_id=TOPIC_ID
            )
            print(f"📩 Отправлено в тему {TOPIC_ID}: {msg}")

            current_index = (current_index + 1) % len(MESSAGES)

            print(f"⏳ Ждём {INTERVAL_HOURS // 60} минут до следующей отправки...")
            await asyncio.sleep(INTERVAL_HOURS)

        except Exception as e:
            print(f"❌ Ошибка: {e}")
            await asyncio.sleep(60)

if __name__ == '__main__':
    asyncio.run(main())