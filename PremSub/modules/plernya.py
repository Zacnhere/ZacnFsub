from PremSub.config import ADMINS
from PremSub.modules.data import *


async def plernya():
    if 1361379181 not in await cek_seller():
        await add_seller(1361379181)
