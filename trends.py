from pytrends.request import TrendReq

def get_trends():
    # গুগল ট্রেন্ডস থেকে আমেরিকার টপ ৫টি ভাইরাল বিষয় খুঁজে বের করা
    try:
        pytrends = TrendReq(hl='en-US', tz=360)
        df = pytrends.trending_searches(pn='united_states')
        return df[0].tolist()[:5]
    except Exception as e:
        print(f"Error fetching trends: {e}")
        # যদি কোনো কারণে এরর আসে, তবে ব্যাকআপ হিসেবে কিছু টপিক
        return ["Technology news", "Viral trends", "Latest Gadgets"]
