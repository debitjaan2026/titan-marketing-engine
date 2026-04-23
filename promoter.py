import random

# Global high-converting hooks for USA/UK traffic
TRAFFIC_HOOKS = {
    "viral": [
        "🔥 UNBELIEVABLE! This clip is breaking the internet right now: ",
        "😱 You won't believe what happened in this video! Watch here: ",
        "🎥 VIRAL ALERT: This secret clip is trending everywhere: "
    ],
    "movie": [
        "🍿 LEAKED: The most searched movie scene of 2026 is here: ",
        "🎥 WATCH NOW: Full HD clip of the trending blockbuster: ",
        "🎬 Everyone is looking for this scene! Found it here: "
    ]
}

def generate_global_promo(link):
    category = random.choice(list(TRAFFIC_HOOKS.keys()))
    hook = random.choice(TRAFFIC_HOOKS[category])
    print(f"\n🚀 Ready for Facebook/Twitter/Reddit (Global):\n\n{hook}\n👉 {link}\n")

if __name__ == "__main__":
    MY_LINK = "https://debitjaan2026.github.io/Titan-AI-Master/"
    generate_global_promo(MY_LINK)
    
