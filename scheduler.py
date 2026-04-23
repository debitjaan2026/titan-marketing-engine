import os
from trends import get_trends
from content import generate_content
from generator import create_page

def run():
    # আমেরিকা থেকে ৫টি ট্রেন্ডিং টপিক নিয়ে আসা
    topics = get_trends()
    
    print(f"Found topics: {topics}")

    for topic in topics:
        print(f"Processing: {topic}")
        # এআই দিয়ে কন্টেন্ট তৈরি
        content = generate_content(topic)
        # ল্যান্ডিং পেজ তৈরি
        create_page(topic, content)

if __name__ == "__main__":
    run()
