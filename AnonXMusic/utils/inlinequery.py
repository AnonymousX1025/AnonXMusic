from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

answer = [
    InlineQueryResultArticle(
        title="Pᴀᴜsᴇ",
        description="ᴩᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.",
        thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
        input_message_content=InputTextMessageContent("/pause"),
    ),
    InlineQueryResultArticle(
        title="Rᴇsᴜᴍᴇ",
        description="ʀᴇsᴜᴍᴇ ᴛʜᴇ ᴩᴀᴜsᴇᴅ sᴛʀᴇᴀᴍ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.",
        thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
        input_message_content=InputTextMessageContent("/resume"),
    ),
    InlineQueryResultArticle(
        title="Sᴋɪᴩ",
        description="sᴋɪᴩ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ ᴀɴᴅ ᴍᴏᴠᴇs ᴛᴏ ᴛʜᴇ ɴᴇxᴛ sᴛʀᴇᴀᴍ.",
        thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
        input_message_content=InputTextMessageContent("/skip"),
    ),
    InlineQueryResultArticle(
        title="Eɴᴅ",
        description="ᴇɴᴅ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.",
        thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
        input_message_content=InputTextMessageContent("/end"),
    ),
    InlineQueryResultArticle(
        title="Sʜᴜғғʟᴇ",
        description="sʜᴜғғʟᴇ ᴛʜᴇ ǫᴜᴇᴜᴇᴅ sᴏɴɢs ɪɴ ᴩʟᴀʏʟɪsᴛ.",
        thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
        input_message_content=InputTextMessageContent("/shuffle"),
    ),
    InlineQueryResultArticle(
        title="Lᴏᴏᴩ",
        description="ʟᴏᴏᴩ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ ᴛʀᴀᴄᴋ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.",
        thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
        input_message_content=InputTextMessageContent("/loop 3"),
    ),
]
