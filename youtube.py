import os
import json
import urllib.request

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK"]

VIDEO_TITLE = "NEW VIDEO!"
VIDEO_URL = "https://www.youtube.com/channel/UCEbc4QI1Rbg5fYlL1XRPgQg"

message = {
    "content": f"🎾 **ACE POINT TENNIS — NEW VIDEO!**\n{VIDEO_TITLE}\n{VIDEO_URL}"
}

data = json.dumps(message).encode("utf-8")

request = urllib.request.Request(
    WEBHOOK_URL,
    data=data,
    headers={"Content-Type": "application/json"},
    method="POST"
)

with urllib.request.urlopen(request) as response:
    print("Discord response:", response.status)
