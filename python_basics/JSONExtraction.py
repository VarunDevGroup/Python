import json

data = '''{
    "users": [
        {
            "status": {
                "text": "@jazzychad I just bought one .__."
            },
            "location": "San Francisco, California",
            "screen_name": "leahculver",
            "name": "Leah Culver"
        }
    ]
}'''

lstData= json.loads(data)

print("Name:", lstData["users"][0]["name"])
