from pyrogram import Client

app = Client(
	session_name='my-user-session',
	api_hash=input("Enter Api Hash: "),
	api_id=input("Enter Api id: ")
)
with app:
	print(app.export_session_string())