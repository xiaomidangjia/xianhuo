#鲸鱼异动报警
import time
from pprint import pprint
import pandas as pd
import numpy as np
import datetime,time
# For formatted dictionary printing>>>
import telegram

bot = telegram.Bot(token='6343206405:AAHkaKIXCMvif0yqkzvTYWasYPEIsTmImgQ')
bot.sendDocument(chat_id='-1001975215255', document=open('/root/xianhuo/BTC现货策略数据.doc', 'rb'),message_thread_id=5) #开仓信息同步

