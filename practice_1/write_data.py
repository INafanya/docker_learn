import time

from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
# Подключение к mongo и проверка соединения
try:
    client = MongoClient("mongodb://localhost:27017/",        
        socketTimeoutMS=5000,  # 5 seconds for socket timeout
        connectTimeoutMS=3000,  # 3 seconds for connection timeout
        serverSelectionTimeoutMS=5000
    )
    client.server_info()  
    print("Подключено к MongoDB!")
except ServerSelectionTimeoutError as e:
    print(f"Нет подключения к MongoDB: {e}")
    exit(1)
# Выбираем бд и коллекцию
db = client["mydatabase"]
collection = db["mycollection"]
# Проверяем количество записей в коллекции
document_count = collection.count_documents({})
print(f"Количество документов в коллекции: {document_count}")
# Запись данных в коллекцию каждую секунду
while True:
    # СОдание документа
    document = {
        "timestamp": time.time(),
        "message": "Hello, Slurm!"
    }
    # Вставка документа в коллекцию
    result = collection.insert_one(document)
    # Вывод лога об добавлении документа
    print(f"Докуменд добавлен с ID: {result.inserted_id} время: {document['timestamp']}")
    # Ожидание 1 секунда
    time.sleep(1)