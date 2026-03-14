import os
import random
import datetime
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.service_account import Credentials

print("Shorts Upload Run:", datetime.datetime.now())

# ===== SETTINGS =====
VIDEO_FILE = "short.mp4"   # repo me ek vertical shorts video upload kar dena
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

SERVICE_FILE = "service.json"   # youtube api service account json

titles = [
    "Amazing Fact in 30 Seconds 🤯",
    "Unbelievable Truth 😱",
    "Quick Knowledge Shot ⚡",
    "Viral Reality Check 🔥"
]

descriptions = [
    "Subscribe for daily shorts 🚀",
    "More facts coming daily 💡",
    "Stay tuned for next video ⭐"
]

title = random.choice(titles)
description = random.choice(descriptions)

# ===== AUTH =====
creds = Credentials.from_service_account_file(
    SERVICE_FILE, scopes=SCOPES
)

youtube = build("youtube", "v3", credentials=creds)

# ===== UPLOAD =====
request = youtube.videos().insert(
    part="snippet,status",
    body={
        "snippet": {
            "title": title,
            "description": description,
            "tags": ["shorts","facts","viral"],
            "categoryId": "22"
        },
        "status": {
            "privacyStatus": "public"
        }
    },
    media_body=MediaFileUpload(VIDEO_FILE)
)

response = request.execute()

print("UPLOAD SUCCESS VIDEO ID:", response["id"])
