import os

# Bot Settings
BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
ADMIN_IDS = [int(x) for x in os.getenv("ADMIN_IDS", "6926993789").split(",")]

# Plan Limits
LIMIT_BASIC_LOGS = 20
LIMIT_PRIME_LOGS = 100 # Unlimited logic can be applied, but 100 is safe for DB
DATABASE_NAME = "uptime.db"

# Intervals in seconds
ALLOWED_INTERVALS = {
    "1m": 60,
    "5m": 300,
    "15m": 900,
    "30m": 1800,
    "1h": 3600
}
