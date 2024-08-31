import util
from rich import print
import json

# response  = util.list_databases()
# databases = [ "e1463d2e-7f99-4dcd-8652-6a6888021fe8"]

# Check if the request was successful
# if response.status_code == 200:
#     databases = [ x for x in response.json()["results"]]
# else:
#     print(f"Failed to retrieve database")

## List Pages
# response  = util.list_pages(databases[0])

# with open('result.json', mode = "w") as handler:
#       json.dump(response.json(), handler, indent=4, ensure_ascii=False, sort_keys=True)  # `indent=4` makes the JSON output more readable


## Search a Page
# response  = util.search("Ergodic Explorer")


## List Blocks in a Page
PAGE_ID = "cb13f491-dca6-4192-839a-9594b3a79825"
response  = util.list_blocks(PAGE_ID)
print(response.json())