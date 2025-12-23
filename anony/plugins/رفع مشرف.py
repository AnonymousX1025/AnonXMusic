from pyrogram import Client, filters
from pyrogram import enums
from pyrogram.enums import ChatMembersFilter, ChatMemberStatus , ChatType
from pyrogram.types import ChatPermissions, ChatPrivileges
import asyncio
from anony import app




welcome_enabled = True






@app.on_chat_member_updated()
async def welcome(client, chat_member_updated):
    if not welcome_enabled:
        return
    
    if chat_member_updated.new_chat_member.status == ChatMemberStatus.BANNED:
        kicked_by = chat_member_updated.new_chat_member.restricted_by
        user = chat_member_updated.new_chat_member.user
        
        if kicked_by is not None and kicked_by.is_self:
            messagee = f"↢ المستخدم {user.username} ({user.first_name}) تم طرده من الدردشة بواسطة البوت"
        else:
            if kicked_by is not None:
                message = f"منع التصفيه التـلقائي 🕵️\n\n↢ المستخدم : [{kicked_by.first_name}](tg://user?id={kicked_by.id}) تـم تنزيله من قائمه الادمنيه\n↢ السبب : حاول تصفيه مجموعتك وطرد العضو : [{user.first_name}](tg://user?id={user.id})"
                try:
                    await client.ban_chat_member(chat_member_updated.chat.id, kicked_by.id)
                except Exception as e:
                    message += f"\n\nيجب ان يكون المشرف مرفوع من البوت حتي استطيع تنزيله من الاشراف \nلـ معرفه كيفيه رفع مشرف : قم بعمل ريبلي علي الشخص المحدد واكتب رفع مشرف"
            else:
                message = f"↢ المستخدم {user.username} ({user.first_name}) - تم طرده من الدردشة"
            
            
        
        await client.send_message(chat_member_updated.chat.id, message)




@app.on_message(filters.command(["رفع مشرف"], "") & filters.channel)
def promote_c_admin(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif message.reply_to_message is None:
        target = message.text.split()[2]
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return
    else:
        target = message.text.split()[1].strip("@")
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return

    
    ToM= ChatPrivileges(
                    can_manage_chat=True,
                    can_delete_messages=True,
                    can_manage_video_chats=True,
                    can_restrict_members=True,
                    can_promote_members=False,
                    can_change_info=False,
                    can_post_messages=True,
                    can_edit_messages=True,
                    can_invite_users=True,
                    can_pin_messages=False,
                    is_anonymous=False
                )
    chat_id = message.chat.id
    client.promote_chat_member(chat_id, user_id, ToM)
    message.reply(f"تم رفع {user_id} ادمن بنجاح")
    



@app.on_message(filters.command(["رفع مشرف"], "") & filters.group)
def promote_g_admin(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif message.reply_to_message is None:
        target = message.text.split()[2]
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return
    else:
        target = message.text.split()[1].strip("@")
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return

    tom_id = message.from_user.id
    chat_id = message.chat.id
    ToM= ChatPrivileges(
                    can_manage_chat=True,
                    can_delete_messages=True,
                    can_manage_video_chats=True,
                    can_restrict_members=True,
                    can_promote_members=False,
                    can_change_info=False,
                    can_post_messages=False,
                    can_edit_messages=False,
                    can_invite_users=True,
                    can_pin_messages=True,
                    is_anonymous=False
                )
    tooom = client.get_chat_members(chat_id, filter=ChatMembersFilter.ADMINISTRATORS)
    for tom in tooom:
    	if tom.user.id == tom_id and (tom.status == enums.ChatMemberStatus.OWNER or tom.status == enums.ChatMemberStatus.ADMINISTRATOR):
    		client.promote_chat_member(chat_id, user_id, ToM)
    		message.reply(f"◍ تم رفع {user_id} ادمن بنجاح \n\n √")
    		
