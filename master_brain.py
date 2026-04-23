import random

# তোমার নেটওয়ার্ক লিঙ্ক (ধাপ ২ এ এগুলো বাটনে বসবে)
AD_LINKS = [
    "https://www.profitablecpmratenetwork.com/ud2qw6p3d7?key=275a836a0d6ce5c21562f245c57cdf1a",
    "https://www.profitablecpmratenetwork.com/zaa9nppna?key=e42ebc0a997943ef4b244903273e1743"
]

# ভাইরাল ক্যাটাগরি এবং ট্রেন্ড (এটিই ধাপ ১ এর ব্রেইন)
TRENDS = {
    "Movies": ["Latest Hollywood Action", "Bollywood Blockbuster 2026", "Viral Movie Clips"],
    "Models": ["Top Global Models", "Trending Fashion Clips"],
    "Countries": ["USA", "UK", "Germany", "Bangladesh"] # হাই সিপিএম দেশ
}

def check_viral_trends():
    selected_trend = random.choice(TRENDS["Movies"])
    selected_target = random.choice(TRENDS["Countries"])
    print(f"Targeting: {selected_trend} in {selected_target}")
    return selected_trend, selected_target

if __name__ == "__main__":
    trend, country = check_viral_trends()
    print("AI Master Brain Initialized Step 1!")
