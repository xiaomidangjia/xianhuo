#鲸鱼异动报警
import time
from pprint import pprint
import pandas as pd
import numpy as np
import datetime,time
# For formatted dictionary printing>>>
import telegram

date_now = datetime.datetime.utcnow()
doc_name = '%s日BTC链上数据一览'%(str(date_now)[0:10]) + '.doc'


text_4 = '【综合分析】：经过近几日的价格上涨，有持续上升趋势，所以继续观察走势，不操作。'

tg_doc_name = '/root/xianhuo/' + str(doc_name)
print(tg_doc_name)
bot = telegram.Bot(token='6343206405:AAHkaKIXCMvif0yqkzvTYWasYPEIsTmImgQ')
bot.sendDocument(chat_id='-1001975215255', document=open(tg_doc_name, 'rb'),message_thread_id=5) #链上数据分享
bot.sendMessage(chat_id='-1001975215255', text = text_4,message_thread_id=5) #链上数据分享


'''
text_0 = '【综合分析】：经过近几日的价格上涨，有持续上升趋势，所以继续观察走势，不操作。'
text_1 = '【综合分析】：可以尝试小资金进行抄底，虽然小资金，但是也要分批,因为价格下跌会有一个惯性趋势。'
text_2 = '【综合分析】：BTC价格持续下跌，前期小资金抄底博反弹失效，目前已经进入到了定投阶段，可以稍微加大资金量，但不能ALL IN，防止黑天鹅事件。'
text_3 = '【综合分析】：经过近几日的价格反弹，BTC已经暂时走出底部区域，前期抄底或定投的也可以分批套现。'

if asopr_v >=1 and sopr_7v >=1:
    text_4 = text_3
elif asopr_v < 1 and sopr_7v >=1:
    text_4 = text_1
elif asopr_v >= 1 and sopr_7v <1:
    text_4 = text_0
elif asopr_v < 1 and sopr_7v <1:
    text_4 = text_2
else:
    text_4 = 'unknow'

content_1 ='【行情分析】目前是BTC现货开始大资金定投的状态，理由如下：BTC的价格均线呈现多头排列形式，但是当前价格低于120日均线，结合BTC风险指数处于较低状态，昨日交易所BTC处于净流出，稳定币USDT处于净流入状态，说明市场对BTC有一定的购买力，判断当前BTC的价格是低估状态。从短期链上指标SOPR和7MA SOPR来看，其值都是小于1，说明链上的BTC购买的价格是大于当前BTC价格，而长期行情的链上指标 MVRV_Z_Score，Puell Multiple，RHODL Ratio和Percent Supply in Profit都处于中间状态，不属于黑天鹅后带来的底部机会，所以从总体来看目前BTC的拥有者都处于略微亏损状态，结合目前是大周期中的萧条期，价格下跌在低位盘整后都会有一定反弹，所以现货层面可以分批买入。'
content_2 ='【行情分析】目前是BTC现货可以小资金尝试抄底的状态，理由如下：短期链上指标SOPR值小于1，说明从总体来看目前BTC的拥有者都处于略微亏损状态，结合目前是大周期中的萧条期，价格下跌在低位盘整后都会有一定反弹，所以现货层面可以小资金买入，虽然是小资金，但是还是要进行分批买入。接下来我们需要观察7MA SOPR是否要小于1，如果小于1，可以逐渐加大资金量。'
content_3 ='【行情分析】目前是BTC现货可以用中等资金进行定投状态，理由如下：经过前几天的BTC价格下跌，7MA SOPR开始小于1了，结合BTC风险指数处于较低状态，说明整体市场都处于比较严重亏损状态，经过前面的小资金的投入，目前可以继续执行定投策略，我们要时刻警惕黑天鹅事件到来，所以定投也不要打完自己所有的子弹，留一手为了黑天鹅准备。大周期行情的底部我们要密切观察长期行情的链上指标 MVRV_Z_Score，Puell Multiple，RHODL Ratio和Percent Supply in Profit这四个指标值。'
content_4 ='【行情分析】目前是BTC现货需要继续观察，不建议进行投资，理由如下：短期链上指标SOPR值和7MA SOPR都大于 ，说明链上买BTC的用户都处于盈利状态，比特币风险指数也处于较高的状态，说明短期内有一定的抛压压力。'

date_now = datetime.datetime.utcnow()
'''