import asyncio

import os

import time

import pixeldrain

import aiohttp

import requests

import aiofiles

from main.modules.utils import format_time, get_duration, get_epnum, get_filesize, status_text, tags_generator, get_messages, b64_to_str, str_to_b64, send_media_and_reply, get_durationx

from main.modules.anilist import get_anime_name

from main.modules.anilist import get_anime_img

from main.modules.db import present_user, add_user, is_fid_in_db

from main.modules.thumbnail import generate_thumbnail

from config import UPLOADS_ID

from pyrogram import Client, filters

from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from main.modules.progress import progress_for_pyrogram

from os.path import isfile

import os

import time

from main import app, status

from pyrogram.errors import FloodWait

from main.inline import button1

async def upload_video(msg: Message,file,id,tit,name,ttl,sourcetext,untext,subtitle,nyaasize,thumbnail):

    try:

        fuk = isfile(file)

        if fuk:

            r = msg

            c_time = time.time()

            duration = get_duration(file)

            durationx = get_durationx(file)

            size = get_filesize(file)

            ep_num = get_epnum(name)

            

            rest = tit


            filed = os.path.basename(file)

            filed = filed.replace("[1080p Web-DL]", "[720p x265] @animxt")

            fukpath = "downloads/" + filed

            caption = f"{filed}"

            caption = caption.replace("[720p x265] @animxt.mkv", "") 

            gcaption=f"**{caption}**" + "\n" +  f"__({tit})__" + "\n" + "━━━━━━━━━━━━━━━━━━━" + "\n" + "✓  `720p x265 10Bit`" + "\n" + f"✓  `{subtitle} ~ Subs`" + "\n" + "#Encoded #HEVC"

            kayo_id = -1001642923224

            gay_id = 1159872623

            x = await app.send_document(

                kayo_id,

            document=file,

            caption=gcaption,

            file_name=filed,

            force_document=True,     

            thumb=thumbnail

            )

            os.rename(file,fukpath)
            
 
            fid = str(x.message_id)
            da_url = "https://da.gd/"
            share_link = f"https://telegram.me/somayukibot?start=animxt_{str_to_b64(fid)}"
            enshare_link = f"http://yoururl.in/api?api=41b0b500ae8a0ab78c9c6abefb9583530c2e0ec7&url={share_link}&format=text"
            fukshare = requests.get(enshare_link)
            tshare = fukshare.text
            cshare = tshare
            xshare_url = f"{da_url}shorten"
            tgshare = requests.get(xshare_url, params={"url": cshare})
            teleshare = tgshare.text.strip() 
            await asyncio.sleep(10)
    
        
            repl_markup=InlineKeyboardMarkup(

                [

                    [

                         InlineKeyboardButton(

                            text="🐌TG FILE",

                            url=teleshare,

                        ),
  
                    ],
                    
                ],
            )

            encodetext =  f"{sourcetext}" "\n" + f"**‣ File Size**: `{size}`" + "\n" + f"**‣ Duration**: {durationx}" + "\n" + f"**‣ Downloads**: [🔗Telegram File]({teleshare})"

            await asyncio.sleep(5)

            entext = await untext.edit(encodetext, disable_web_page_preview=True, reply_markup=repl_markup)

    except Exception:

            await app.send_message(kayo_id, text="Something Went Wrong!")

    try:
        
            
            await r.delete()

            os.remove(file)

            os.remove(thumbnail)

    except:

        pass

    return x.message_id
