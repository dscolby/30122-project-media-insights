"""
    Authored by Jessup Jong
"""

import comments
import json
import pdb

with open("../data/comment_data.json", "r") as f:
    video_responses = json.load(f)

cleaned_comments = {}
for video_response in video_responses:
    cleaned_video = []
    for i, comment in enumerate(video_response["items"]):
        pdb.set_trace()
        try:
            text = comment["snippet"]["topLevelComment"]["snippet"]["textOriginal"]
            date = comment["snippet"]["topLevelComment"]["snippet"]["publishedAt"]
            cleaned_video += [(text, date)]
        except:
            print(f"Structure Different for Comment {i}")
    cleaned_comments[video_response["items"][0]["snippet"]["videoId"]] = cleaned_video

with open("../data/cleaned_comment_data.json", "w") as f:
    json.dump(cleaned_comments, f)
