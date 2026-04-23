import os
import random

# ১. তোমার অ্যাড লিঙ্কগুলো
AD_LINKS = [
    "https://www.profitablecpmratenetwork.com/ud2qw6p3d7?key=275a836a0d6ce5c21562f245c57cdf1a",
    "https://www.profitablecpmratenetwork.com/zaa9nppna?key=e42ebc0a997943ef4b244903273e1743"
]

# ২. বাইরের দেশের ট্রাফিকের জন্য আকর্ষণীয় টাইটেল
VIRAL_TITLES = [
    "Exclusive Leaked Scene - Viral Video",
    "Watch Trending Viral Content 2026",
    "Full HD Movie Clip - Limited Time Access",
    "Viral Media Update - Watch Before Removed"
]

def create_landing_page():
    target_link = random.choice(AD_LINKS)
    trend_name = random.choice(VIRAL_TITLES)
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{trend_name}</title>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0a0a0a; color: white; text-align: center; padding: 50px; }}
            .container {{ border: 2px solid #e50914; padding: 30px; border-radius: 15px; display: inline-block; background: #141414; box-shadow: 0 0 15px rgba(229, 9, 20, 0.4); }}
            h1 {{ color: #e50914; font-size: 28px; }}
            .btn {{ background-color: #e50914; color: white; padding: 18px 35px; text-decoration: none; font-size: 22px; border-radius: 5px; font-weight: bold; display: inline-block; margin-top: 25px; transition: 0.3s; }}
            .btn:hover {{ background-color: #ff0f1f; transform: scale(1.05); }}
            p {{ font-size: 18px; color: #ccc; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Trending: {trend_name}</h1>
            <p>High-quality content is ready for you.</p>
            <p>Click below to watch or download immediately!</p>
            <a href="{target_link}" class="btn">WATCH / DOWNLOAD NOW</a>
            <p style="margin-top: 20px; font-size: 12px; color: #666;">*Secure connection established.</p>
        </div>
    </body>
    </html>
    """
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Success: Global Page Created for {trend_name}")

if __name__ == "__main__":
    create_landing_page()
