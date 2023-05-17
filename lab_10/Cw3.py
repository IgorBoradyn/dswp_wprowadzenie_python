from datetime import datetime
from zoneinfo import ZoneInfo

user_input = input("Podaj czas w formacie HH:MM:SS: ")
time = datetime.combine(
    datetime.now().date(),
    datetime.strptime(user_input, "%H:%M:%S").time(),
    ZoneInfo('Europe/Warsaw'),
)

tokyo_time = time.astimezone(ZoneInfo('Asia/Tokyo')).strftime("%H:%M:%S")
washington_time = time.astimezone(ZoneInfo('America/New_York')).strftime("%H:%M:%S")
sydney_time = time.astimezone(ZoneInfo('Australia/Sydney')).strftime("%H:%M:%S")
london_time = time.astimezone(ZoneInfo('Europe/London')).strftime("%H:%M:%S")

print(f"Czas w Tokio: {tokyo_time}")
print(f"Czas w Waszyngtonie: {washington_time}")
print(f"Czas w Sydney: {sydney_time}")
print(f"Czas w Londynie: {london_time}")
