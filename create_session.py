from pyrogram import Client

api_id = 27499643              # <-- сюда твой API ID (число)
api_hash = "45c1f3fd54a139d8d5480703ecf58059"  # <-- твой API HASH (строка)
session_name = "new_account"  # имя для файла сессии

app = Client(session_name, api_id=api_id, api_hash=api_hash)

app.run()
