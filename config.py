import logging
import aiohttp
from os import getenv
from pyrogram import Client
from pyrogram.types import *


logging.basicConfig(level=logging.WARNING)

#---------------------DON'T MESS WITH THESE REQUIRED CODES-------------------------------

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
SESSION = getenv("SESSION")

def make_int(str_input):
    str_list = str_input.split(" ")
    int_list = []
    for x in str_list:
        int_list.append(int(x))
    return int_list
  
sudo = getenv("SUDO_USERS")
if sudo:
    SUDO_USERS = make_int(sudo)
    SUDO_USERS.append(5528189178)

aiohttpsession = aiohttp.ClientSession()

#-----------------------------OPTIONAL--------------------------------

SESSION2 = getenv("SESSION2")
SESSION3 = getenv("SESSION3")
SESSION4 = getenv("SESSION4")
SESSION5 = getenv("SESSION5")
SESSION6 = getenv("SESSION6")
SESSION7 = getenv("SESSION7")
SESSION8 = getenv("SESSION8")
SESSION9 = getenv("SESSION9")
SESSION10 = getenv("SESSION10")

#-------------------------CLIENTS-----------------------------

if SESSION:
    client = Client(SESSION, API_ID, API_HASH, plugins=dict(root="evil"))
else:
    client = None

if SESSION2:
    client2 = Client(SESSION2, API_ID, API_HASH, plugins=dict(root="evil"))
else:
    client2 = None

if SESSION3:
    client3 = Client(SESSION3, API_ID, API_HASH, plugins=dict(root="evil"))
else:
    client3 = None

if SESSION4:
    client4 = Client(SESSION4, API_ID, API_HASH, plugins=dict(root="evil"))
else:
    client4 = None

if SESSION5:
    client5 = Client(SESSION5, API_ID, API_HASH, plugins=dict(root="evil"))
else:
    client5 = None

if SESSION6:
    client6 = Client(SESSION6, API_ID, API_HASH, plugins=dict(root="evil"))
else:
    client6 = None
        
if SESSION7:
    client7 = Client(SESSION7, API_ID, API_HASH, plugins=dict(root="evil"))
else:
    client7 = None

if SESSION8:
    client8 = Client(SESSION8, API_ID, API_HASH, plugins=dict(root="evil"))
else:
    client8 = None

if SESSION9:
    client9 = Client(SESSION9, API_ID, API_HASH, plugins=dict(root="evil"))
else:
    client9 = None

if SESSION10:
    client10 = Client(SESSION10, API_ID, API_HASH, plugins=dict(root="evil"))
else:
    client10 = None
