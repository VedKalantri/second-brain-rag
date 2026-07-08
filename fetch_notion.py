import os
from dotenv import load_dotenv
from notion_client import Client

load_dotenv()

notion = Client(auth=os.environ["NOTION_API_KEY"])

PAGE_ID = "39642510a02280e8a1cdce8665635679"

response = notion.blocks.children.list(block_id=PAGE_ID)


def extract_text(block):
    block_type = block["type"]

    if block_type == "paragraph":
        return "".join(
            text["plain_text"]
            for text in block["paragraph"]["rich_text"]
        )

    elif block_type == "heading_1":
        return "".join(
            text["plain_text"]
            for text in block["heading_1"]["rich_text"]
        )

    return ""


page_content = []

for block in response["results"]:
    text = extract_text(block)

    if text:
        page_content.append(text)

full_text = "\n".join(page_content)

with open("notes.txt", "w", encoding="utf-8") as file:
    file.write(full_text)

print("Notes saved successfully!")