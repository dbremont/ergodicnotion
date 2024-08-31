import requests
import json
import util

# Replace with your integration token and page ID
NOTION_API_TOKEN = util.Context.NOTION_API_KEY
PAGE_ID = "cb13f491-dca6-4192-839a-9594b3a79825"

# Define the endpoint URL for updating the page
url = f'https://api.notion.com/v1/blocks/{PAGE_ID}/children'

# Define the headers for the request
headers = {
    'Authorization': f'Bearer {NOTION_API_TOKEN}',
    'Content-Type': 'application/json',
    'Notion-Version': '2022-06-28'  # Update to the current API version
}

# Define the body for the request
# Here we add a new text block to the page
# body = {
#     "properties": {
#         "title": [
#             {
#                 "type": "text",
#                 "text": {
#                     "content": "- ..."
#                 }
#             }
#         ]
#     }
# }

# body = {
#     "children": [
#         {
#             "object": "block",
#             "type": "paragraph",
#             "paragraph": {
#                 "rich_text": [
#                     {
#                         "type": "text",
#                         "text": {
#                             "content": "- ..."
#                         }
#                     }
#                 ]
#             }
#         }
#     ]
# }

links = [
    {"text": "Link 1", "url": "https://www.notion.so/Horn-Effect-1827a6dbb77e4815bb25274966517745"}
]

# Create the body for the request
body = {
    "children": [
        {
            "object": "block",
            "type": "bulleted_list_item",
            "bulleted_list_item": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": link["text"],
                            "link": {"url": link["url"]}
                        }
                    }
                ]
            }
        } for link in links
    ]
}



# Make the request to the Notion API
response = requests.patch(url, headers=headers, json=body)

# Check if the request was successful
if response.status_code == 200:
    print("Page updated successfully!")
else:
    print(f"Error: {response.status_code} - {response.text}")
