from pyrogram import Client, filters

# Initialize the Pyrogram client
app = Client("my_bot")

# Define the banned URLs
banned_urls = ["example.com", "spam.com"]

# Custom filter to check if the message is from a user
def from_user(_, __, message):
    return not message.from_user.is_bot

# Event handler for new messages
@app.on_message(filters.private & from_user)
async def handle_message(client, message):
    # Check if the message contains any banned URLs
    for url in banned_urls:
        if url in message.text:
            # Ban the user who uploaded the banned URL
            await client.kick_chat_member(message.chat.id, message.from_user.id)
            await message.reply_text("You have been banned for uploading a banned URL.")
            return

# Run the bot
app.run()
