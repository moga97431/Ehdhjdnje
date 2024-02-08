import os, time, re
from pyrogram import *
from pyrogram.types import *
from pyrogram.errors import *
os.system("clear")



#+++++++++ array list +++++++++
mabda = -1001313710720 # ایدی عددی کانال مبدا
maqsad = "iran_tiktok_1402" # یوزرنیم کانال مقصد
stats = ["on"]
phone_numer = "+989938570259" # شماره اکانت
admins = [6574781108] # ایدی عددی ادمین






cli = Client("cli" , api_id = "26038305" , api_hash = "42af11940df49409f80c73195d01f86b", phone_number = phone_numer)








@cli.on_message(filters.user(admins) & filters.regex('(?i)^وضعیت$'))
async def mode(client, message):
    if stats[0] == "on":
        await message.reply_text("در حال حاضر ربات در وضعیت **روشن** قرار دارد.")
    else:
        await message.reply_text("در حال حاضر ربات در وضعیت **خاموش** قرار دارد.")



@cli.on_message(filters.user(admins) & filters.regex('(?i)^راهنما$'))
async def helper(client, message):
    await message.reply_text("1 . وضعیت\n2 . تغییر وضعیت")



@cli.on_message(filters.user(admins) & filters.regex('(?i)^تغییر وضعیت$'))
async def change_mode(client, message):
    if stats[0] == "on":
        stats.clear()
        stats.append("off")
        await message.reply_text("وضعیت ربات از **روشن** به **خاموش** تغییر کرد.")
    else:
        stats.clear()
        stats.append("on")
        await message.reply_text("وضعیت ربات از **خاموش** به **روشن** تغییر کرد.")



async def send_photo(client, message, caption, url):
    text = re.sub(r"\B@\w+", f"@{maqsad}", caption)
    await cli.send_photo(maqsad, url, caption=text)


async def send_video(client, message, caption, url):
    text = re.sub(r"\B@\w+", f"@{maqsad}", caption)
    await cli.send_video(maqsad, url, caption=text)



async def send_gif(client, message, caption, url):
    text = re.sub(r"\B@\w+", f"@{maqsad}", caption)
    await cli.send_animation(maqsad, url, caption=text)


async def send_text(client, message, text):
    text = re.sub(r"\B@\w+", f"@{maqsad}", text)
    await cli.send_message(maqsad, text)




@cli.on_message(filters.chat(mabda))
async def filter_all_cli(client, message):
    msg_id = message.id
    chat_id = message.chat.id
    if stats[0] == "on":
        if message.media:
#photo
            if str(message.media) == "MessageMediaType.PHOTO":
                if message.caption_entities:
                    caption = str(message.caption)
                    await send_photo(client, message, caption, message.photo.file_id)
                else:
                    caption = str(message.caption)+"\n\n🆔 @"+str(maqsad)+" 🌐"
                    await cli.send_photo(maqsad, message.photo.file_id, caption=caption)
#video
            elif str(message.media) == "MessageMediaType.VIDEO":
                if message.caption_entities:
                    caption = str(message.caption)
                    await send_video(client, message, caption, message.video.file_id)
                else:
                    caption = str(message.caption)+"\n\n🆔 @"+str(maqsad)+" 🌐"
                    await cli.send_video(maqsad, message.video.file_id, caption=caption)
#gif
            elif str(message.media) == "MessageMediaType.ANIMATION":
                if message.caption_entities:
                    caption = str(message.caption)
                    await send_gif(client, message, caption, message.animation.file_id)
                else:
                    caption = str(message.caption)+"\n\n🆔 @"+str(maqsad)+" 🌐"
                    await cli.send_animation(maqsad, message.animation.file_id, caption=caption)
#text
        else:
            if message.entities:
                text = str(message.text)
                await send_text(client, message, text)
            else:
                text = str(message.text)+"\n\n🆔 @"+str(maqsad)+" 🌐"
                await cli.send_message(maqsad, text)
    else:
        ThePurea = "ThePurea"









cli.run()
