# Copyright (C) @subinps
# Update By (C) @theSmartBisnu
# ReUpdate By (C) @abirxdhackz
# Channel : https://t.me/abir_xd_bio


from pytgcalls import PyTgCalls
from pyrogram import Client
from config import Config
from utils import LOGGER

USER = Client("userSession", Config.API_ID, Config.API_HASH, session_string=Config.SESSION, plugins=dict(root="userplugins"))
     
group_call = PyTgCalls(USER, cache_duration=180)
