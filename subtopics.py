import json
from azure.storage.queue import QueueClient

AZURE_STORAGE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=cmetyphoid;AccountKey=2hk2g3+VvyKJ4jqyY0QQkVI953Yf0HbLFUbhGNFjLA+Egnh7S+vgWf6JE1iDBT0OYYUEt3uKO3Hu+ASt9SxsHg==;EndpointSuffix=core.windows.net"

QUEUE_NAME = "subtopic-queue"
subtopic_ids = [
 "30131816-8FC5-4387-8F89-4202F7DC65D7",
 "0C5C695C-87A6-4DC1-AD27-5228A1BE2BD1",
 "644F8A74-01EF-4F21-A10E-C21F892C05FD"
]
queue = QueueClient.from_connection_string(
    AZURE_STORAGE_CONNECTION_STRING,
    QUEUE_NAME
)

for sid in subtopic_ids:
    message = {"subtopic_id": sid}
    queue.send_message(json.dumps(message))
    print(f"Queued: {sid}")

print(f"\n✅ {len(subtopic_ids)} subtopics pushed to {QUEUE_NAME}")