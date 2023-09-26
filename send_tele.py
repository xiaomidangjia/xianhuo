#鲸鱼异动报警
import time
from pprint import pprint
import pandas as pd
import numpy as np
import datetime,time
# For formatted dictionary printing>>>
import telegram

date_now = datetime.datetime.utcnow()
doc_name = '/root/xianhuo/' + '%s日BTC链上数据一览'%(str(date_now)[0:10]) + '.doc'

bot = telegram.Bot(token='6343206405:AAHkaKIXCMvif0yqkzvTYWasYPEIsTmImgQ')
bot.sendDocument(chat_id='-1001975215255', document=open(doc_name, 'rb'),message_thread_id=5) #开仓信息同步

