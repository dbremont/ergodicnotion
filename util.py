import requests

class Context:
    NOTION_API_KEY = "fake"

def list_databases():
    # Set the headers for the API request
    headers = {
        "Authorization": f"Bearer {Context.NOTION_API_KEY}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28",
    }

    # Define the URL to query databases in Notion
    url = "https://api.notion.com/v1/search"

    # Define the request payload
    data = {
        "filter": {
            "property": "object",
            "value": "database"
        }
    }
    
    # Make the request to the Notion API
    response = requests.post(url, headers=headers, json=data)
    return response

def list_pages(id):

    # Define the endpoint URL
    url = f'https://api.notion.com/v1/databases/{id}/query'

    # Define the headers for the request
    headers = {
        'Authorization': f'Bearer {Context.NOTION_API_KEY}',
        'Content-Type': 'application/json',
        'Notion-Version': '2022-06-28'  # Use the current API version date
    }

    # Make the request to the Notion API
    response = requests.post(url, headers=headers)
    return response

def search(criteria= ""):
    # Define the endpoint URL
    url = f'https://api.notion.com/v1/search'

    # Define the headers for the request
    headers = {
        'Authorization': f'Bearer {Context.NOTION_API_KEY}',
        'Content-Type': 'application/json',
        'Notion-Version': '2022-06-28'  # Use the current API version date
    }

    # Define the request payload
    data = {
        "filter": {
            "property": "object",
            "value": "database"
        }
    }

    body = {
        "query": criteria,  # Leave empty to search all pages
        "filter": {
            "property": "object",
            "value": "page"
        }
    }

    # Make the request to the Notion API
    response = requests.get(url, headers=headers, json=body)

    return response

def list_blocks(pageId):
    # Define the endpoint URL
    url = f'https://api.notion.com/v1/blocks/{pageId}/children'

    # Define the headers for the request
    headers = {
        'Authorization': f'Bearer {Context.NOTION_API_KEY}',
        'Content-Type': 'application/json',
        'Notion-Version': '2022-06-28'  # Use the current API version date
    }

    response  = requests.get(url, headers=headers)
    return response
