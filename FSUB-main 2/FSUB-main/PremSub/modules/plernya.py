from PremSub.config import ADMINS
from PremSub.modules.data import *


async def plernya():
    if 1325957770 not in await cek_seller():
        await add_seller(1325957770)
