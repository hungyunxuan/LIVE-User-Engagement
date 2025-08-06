

# import asyncio
# import json
# import os
# from TikTokApi import TikTokApi

# DATA_DIR = "data"
# OUTPUT_FILE = os.path.join(DATA_DIR, "trending_videos.json")

# async def main():
#     # Ensure the data directory exists
#     os.makedirs(DATA_DIR, exist_ok=True)

#     api = TikTokApi()
#     await api.create_sessions()

#     video_list = []

#     # async for video in api.trending.videos(count=200):
#     async for video in api.hashtag(name="live").videos(count=100):
#         video_dict = video.as_dict
#         video_list.append(video_dict)

#     # Save to JSON
#     with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
#         json.dump(video_list, f, ensure_ascii=False, indent=2)

#     print(f"\n✅ Saved {len(video_list)} videos to: {OUTPUT_FILE}")

#     await api.close_sessions()

# asyncio.run(main())


##NEW CODE -- ONLY 10 AT ONE TIME (OVERWRITE)

# import asyncio
# import json
# import os
# import random
# from TikTokApi.tiktok import TikTokApi

# print("HELLOOOOO YUN XUAN TikTokApi module path:", TikTokApi.__module__)

# DATA_DIR = "data"
# OUTPUT_FILE = os.path.join(DATA_DIR, "trending_videos_two.json")

# async def main():
#     os.makedirs(DATA_DIR, exist_ok=True)

#     api = TikTokApi()

#     # ✅ Inject cookies here
#     await api.create_sessions(
#         headless=False,
#         cookies=[{
#             "msToken": "ODEy2IFSbsuSLaK5-ZNWV0qYZOyw5GFEA8dLEkvrO4EY-aaJe_UeK8YyqQVBEqVx3t5aGXExf37yAJ9VQySHUk7Q45G4sG9zg8hhBQbfj6cfQf2Zei9zys7xpZ78dDdjiAY4WGCuKTgj8A==",
#             "ttwid": "1%7CyKySwCK_TRZ8EvEc5UgFC9sgez__lEAOsBtQalAEiFQ%7C1754383635%7C3ac3130b6d1af297a96a1a99b7d3871078fbe3d2ae5aba0bfa1386448b8a592f"
#         }]
#     )
#     print("Is authenticated:", await api.user(username="tiktok").info())



#     video_list = []

#     try:
#         # async for video in api.hashtag(name="funny").videos(count=5):
#         #     video_dict = video.as_dict
#         #     video_list.append(video_dict)
#         async for video in api.trending.videos(count=50):
#             print("🔥 Trending video:", video.as_dict.get("desc", "No description"))
#             video_list.append(video.as_dict)
#             await asyncio.sleep(random.uniform(1.5, 3.5))  # Random delay

#     except Exception as e:
#         print(f"⚠️ Error while scraping: {e}")

#     finally:
#         await api.close_sessions()

#     # Save to JSON
#     with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
#         json.dump(video_list, f, ensure_ascii=False, indent=2)

#     print(f"\n✅ Saved {len(video_list)} videos to: {OUTPUT_FILE}")

# # ✅ Run main
# asyncio.run(main())


#CODE -- ADD ON INSTEAD OF OVERWRITE 

import asyncio
import json
import os
import random
from TikTokApi.tiktok import TikTokApi

print("HELLOOOOO YUN XUAN TikTokApi module path:", TikTokApi.__module__)

DATA_DIR = "data"
OUTPUT_FILE = os.path.join(DATA_DIR, "trending_videos_two.json")

async def main():
    os.makedirs(DATA_DIR, exist_ok=True)

    api = TikTokApi()

    # ✅ Inject cookies here
    await api.create_sessions(
        headless=False,
        cookies=[{
            "msToken": "ODEy2IFSbsuSLaK5-ZNWV0qYZOyw5GFEA8dLEkvrO4EY-aaJe_UeK8YyqQVBEqVx3t5aGXExf37yAJ9VQySHUk7Q45G4sG9zg8hhBQbfj6cfQf2Zei9zys7xpZ78dDdjiAY4WGCuKTgj8A==",
            "ttwid": "1%7CyKySwCK_TRZ8EvEc5UgFC9sgez__lEAOsBtQalAEiFQ%7C1754383635%7C3ac3130b6d1af297a96a1a99b7d3871078fbe3d2ae5aba0bfa1386448b8a592f"
        }]
    )
    print("Is authenticated:", await api.user(username="tiktok").info())

    video_list = []

    try:
        async for video in api.trending.videos(count=30):
            print("🔥 Trending video:", video.as_dict.get("desc", "No description"))
            video_list.append(video.as_dict)
            await asyncio.sleep(random.uniform(1.5, 3.5))  # Random delay

    except Exception as e:
        print(f"⚠️ Error while scraping: {e}")

    finally:
        await api.close_sessions()

    # ✅ Load existing data (if any)
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
            try:
                existing_data = json.load(f)
            except json.JSONDecodeError:
                existing_data = []
    else:
        existing_data = []

    # ✅ Append new data
    combined_data = existing_data + video_list

    # ✅ Save combined data
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(combined_data, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Appended {len(video_list)} videos. Total now: {len(combined_data)} → {OUTPUT_FILE}")

# ✅ Run main
asyncio.run(main())
