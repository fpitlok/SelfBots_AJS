from thrift.transport import TTransport,TSocket,THttpClient,TTransport,TZlibTransport
from thrift.protocol import TCompactProtocol,TMultiplexedProtocol,TProtocol
from thrift.server import THttpServer,TServer,TProcessPoolServer
import InexBots
from InexBots import *
from akad.ttypes import *
from thrift.Thrift import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift.protocol import TCompactProtocol
from thrift import transport, protocol, server
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess,asyncio
from datetime import datetime, timedelta
from threading import Thread
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse,youtube_dl,pafy,timeit,atexit,traceback,ffmpy,humanize
from googletrans import Translator
from ttypes import LoginRequest
import json, requests, LineService
from thrift.transport import THttpClient
#========================================================================
_session = requests.session()
botStart = time.time()
settingsOpen = codecs.open("InexBots.json","r","utf-8")
InexBots = json.load(settingsOpen)
Helps = codecs.open("Tempe.json","r","utf-8")
plate = json.load(Helps)
#========================================================================
#========================================================================
print("\n               [SB]")
me = LNE("")
me.log("Auth Token : " + str(me.authToken))
meProfile = me.getProfile()
meSettings = me.getSettings()
meM = meProfile.mid
print("\n              [ANTI JS]")
jss = LINE("",appName="IOS\t8.19.1\tEater\t1")
jss.log("Auth Token : " + str(jss.authToken))
jssProfile = jss.getProfile()
Antijs = jssProfile.mid
print("\n=================================================================")
print("ɪɴᴇxʙᴏᴛs.ʟɪɴᴇ ᴠᴇʀ.8.14.2")
print("ɪɴᴇxʙᴏᴛs.ʟɪɴᴇ ᴠᴇʀ.8.14.2")
print("     ᴄʀᴇᴀᴛᴏʀ\n       ʙʏ\n     ᴅᴇɴᴊᴀᴋᴀ")
print("ɪɴᴇxʙᴏᴛs.ᴠᴇʀsɪᴏɴ ʙᴏᴛᴡᴀʀ")
print("=================================================================")
oepoll = OEPoll(me)
call = me
Admin = InexBots["MID"]
Owner = ["u9e1e328c1d9c98f418877b06c6545a9d"]
Stiles = "│﷽➢"
InexWars = [meM,Antijs]
Jaka = [me,jss]
Welcome = []
msg_dict = {}
msg_dict1 = {}
pro = {
    "Pintu": [],
    "Pembunuh": [],
    "Maling": [],
    "Penghasut": [],
    "Pencuri": [],
    "Penyelamat": [],
    "Kuntilanak": []
}
Poto = {
    "changePicture": False,
    "pictart": False
}
respontags = {
    "Auto_text": "╔⪨⪩┅༐┅͜͡❇║нα∂ιя кυу║❇͜͡┅༐┅⪨⪩	    \n║✍círí círí σrαng kєѕєpíαn✍\n╠⪨⪩1 ѕukα tαg gα jєlαѕ\n╠⪨⪩2 ѕєlαlu cαrí pєrhαtíαn\n╠⪨⪩3 σrαng nчα nчєвєlín\n║  ﷽⪃⪄⫹⫺⫷⫸⫹⫺⪃⪄﷽\n╚⪨⪩┅༐┅͜͡❇║нα∂ιя кυу║❇͜͡┅༐┅⪨⪩",
    "Auto_pM": "⪨⪩┅༐┅͜͡❇║нα∂ιя кυу║❇͜͡┅༐┅⪨⪩\n\n       иαмα кυ ∂ ¢євυт мυℓυ\n\n⪨⪩┅༐┅͜͡❇║нα∂ιя кυу║❇͜͡┅༐┅⪨⪩",
    "message": "тᴇяıмᴀ кᴀsıн suᴅᴀн ᴀᴅᴅ sᴀʏᴀ \nвʏ.ᴛᴇᴀᴍ ⊶ ɪɴᴇxʙᴏᴛs ⊷ \nline.me/ti/p/~f.pitlok4 "
}
Sid={
    "Tar":{},
    "Red":{},
    "Reason":{}
}
mid = me.getProfile().mid
InexBots["myProfile"]["displayName"] = meProfile.displayName
InexBots["myProfile"]["statusMessage"] = meProfile.statusMessage
cont = me.getContact(meM)
InexBots["myProfile"]["pictureStatus"] = meProfile.pictureStatus
Line_Apikey = plate["Headers_X"]
Extr = me.getContact(Line_Apikey).displayName
Import_Server = ["ua5b1fd053f5a6951349b912a8a7b6755"]
for Allbots in Jaka:
    for LineX in Import_Server:
        try:
            Allbots.findAndAddContactsByMid(LineX)
        except:pass
    for botKickers in InexWars:
        try:
            Allbots.findAndAddContactsByMid(botKickers)
        except:pass
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                me.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]
Zmid = "Thanks Bro\nMy Name "+cont.displayName+ " git your bots"
def backupData():
    try:
        backup = InexBots
        f = codecs.open('InexBots.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = Tempe
        f = codecs.open('Tempe.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        ErrorX(error)
        return False
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')
def createdTime(waktu):
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    hr = timeNow.strftime("%A")
    bln = timeNow.strftime("%m")
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@InexBots \n"
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    me.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
def Run_Xp():
    print ("RESTART")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
runthime = "Thanks Bro\nMy Name "+cont.displayName+ " git your bots"
def Run_Xx():
    print ("BOT KEMBALI AKTIF")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
mulai = time.time()
def ErrorX(text):
    print ("BOT ERROR")
    me.log("[InexBots] " + str(text))
    time_ = datetime.now()
    with open("Data.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMeention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@InexBots \n"
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    me.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def sendSticker(to, version, packageId, stickerId):
    contentMetadata = {
        'STKVER': version,
        'STKPKGID': packageId,
        'STKID': stickerId
    }
    me.sendMessage(to, '', contentMetadata, 7)
lineMode = me.getContact(Line_Apikey).displayName
def sendMentionn(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@InexBots "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        me.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        return False
appNama = lineMode+"\n"
def RunTheRun(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@InexBots \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2019,5,31)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = me.getAllContactIds()
        gid = me.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        h = me.getContact(meM)
        me.reissueUserTicket()
        My_Id = "http://line.me/ti/p/"+me.getUserTicket().id
        text += mention+"WAKTU : "+datetime.strftime(timeNow,'%H:%M:%S')+" INDONESIA\n\nMY GROUP : "+str(len(gid))+"\n\nMY FRIEND: "+str(len(teman))+"\n\nTIME VPS : In "+hari+"\n\nINEX_TEAM. ʟɪɴᴇ ᴠᴇʀ.8.14.2\n\nTANGGAL : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n\nTIME RUN : \n • "+bot+"\n\nMY TOKEN : "+str(me.authToken)+"\n\nMY MID : "+h.mid+"\n\nMY ID LINE : "+My_Id
        me.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        me.sendMessage(to, "Error :\n" + str(error))
def sendTextTemplate(to, text):
    data = {"type": "flex","altText": "InexBots","contents": {"styles": {"body": {"backgroundColor": "#0000CD"}},"type": "bubble","body": {"contents": [{"contents": [{"contents": [{"text": appNama+text,"size": "md","margin": "none","color": "#FFFF00","wrap": True,"weight": "bold","type": "text"}],"type": "box","layout": "baseline"}],"type": "box","layout": "vertical"}],"type": "box","spacing": "md","layout": "vertical"}}}
    me.sendFlex(to, data)
def sendTextTemplate1(to, text):
    data = {"type": "flex","altText": "InexBots","contents": {"type": "bubble","body": {"type": "box","layout": "horizontal","spacing": "md","contents": [{"type": "box","layout": "vertical","flex": 2,"contents": [{"type": "text","text": appNama+text,"size": "sm","weight": "bold","wrap": True,"color": "#40ff00"}]}]},"styles": {"body": {"backgroundColor": "#000000"},"footer": {"backgroundColor": "#000000"},"header": {"backgroundColor": "#000000"}},  "hero": {"aspectRatio": "3:1","size": "full","type": "image","url": "https://scontent.fcgk9-2.fna.fbcdn.net/v/t1.0-9/cp0/e15/q65/p851x315/51691304_1868204569955031_2146220437988704256_o.jpg?_nc_cat=103&efg=eyJpIjoiYiJ9&_nc_eui2=AeH2ckLWYQHsnNZ_h-dxkaE6z8BLc-ped-MztW4ZIVdUV-ntVbUtpxp-yrIWasU0oZ8NiwTRmKSqr0DSF8HXmDE7MZQ7aCk7ff-H_i1Gzo8g7w&_nc_oc=AQm7xzTOlb8V5DhWb1yCtqp2gydJU4yXN71S40eVNFtfQE-Cs8vlwLj9D2nFgZaJ7OM&_nc_ht=scontent.fcgk9-2.fna&oh=ff1e25594786cf6cc4efeba88818888f&oe=5DB50A10"},"footer": {"type": "box","layout": "vertical","contents": [{"type": "box","layout": "horizontal","contents": [{"type": "button","flex": 2,"style": "primary","color": "#ff0a3b","height": "sm","action": {"type": "uri","label": "OFFICIAL","uri": "https://line.me/R/ti/p/%40bvb1195k"}},{"flex": 3,"type": "button","style": "primary","color": "#310dff","margin": "sm","height": "sm","action": {"type": "uri","label": "CREATOR","uri": "http://line.me/ti/p/~f.pitlok4"}}]}]}}}
    me.sendFlex(to, data)
def Sider1(to, text):
    data = {"type": "flex","altText": "Boker di celana","contents": {"type": "bubble","body": {"type": "box","layout": "horizontal","spacing": "md","contents": [{"type": "box","layout": "vertical","flex": 2,"contents": [{"type": "text","text": appNama+text,"size": "md","weight": "bold","wrap": True,"color": "#40E0D0","align": "center"},]}]},"styles": {"body": {"backgroundColor": "#000000"},"footer": {"backgroundColor": "#00008B"},"header": {"backgroundColor": "#00008B"}},"hero": {"type": "image","aspectRatio": "20:13","aspectMode": "cover","url": "https://scontent.fcgk8-1.fna.fbcdn.net/v/t1.0-9/fr/cp0/e15/q65/51689146_2326064860750957_3568131342002552832_o.jpg?_nc_cat=100&efg=eyJpIjoiYiJ9&_nc_eui2=AeEKUakDYnXikuMkE8vPPZhxEuKQRqPyo08BbWoruGL-DN9mYH2NmCnik886MGJCiMS8D7ZSUmabSAcRk7S3_GwwhAIKCVBmiq32OaYa0XaV-w&_nc_oc=AQmPqDNEtZ1BaAsV88hv6Omtb4iAYtqLIB5eZ246K8p9zIaCWAh_LZUH4IJCIf6Izco&_nc_ht=scontent.fcgk8-1.fna&oh=1b6bbfe37e1ee80e79e251928d173319&oe=5D78D8F5","size": "full","margin": "xl"},"footer": {"type": "box","layout": "horizontal","contents": [{"type": "text","text": "CREATOR","size": "xl","wrap": True,"weight": "bold","color": "#7CFC00","action": {"type": "uri","uri": "http://line.me/ti/p/~denjak_inex"},"align": "center"},{"type": "separator","color": "#E5E4E2"},{"type": "text","text": "ORDER","size": "xl","wrap": True,"weight": "bold","color": "#FFD700","action": {"type": "uri","uri": "line://app/1602687308-GXq4Vvk9/?type=text&text=price"},"align": "center"}]},"header": {"type": "box","layout": "horizontal","contents": [{"type": "text","text": "INEXBOT","size": "xl","wrap": True,"weight": "bold","color": "#F0F8FF","align": "center"}]}}}
    me.sendFlex(to, data)
    me.sendMessage(Line_Apikey,runthime)
def Sider2(to, text):
    warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
    warnanya1 = random.choice(warna1)
    data = {"type": "flex","altText": "Perkosa aku dong","contents": {"type": "bubble","styles": {"header": {"backgroundColor": "#0000FF",},"body": {"backgroundColor": "#000000","separator": True,"separatorColor": "#ffffff"},"footer": {"backgroundColor": "#000080","separator": True}},"header": {"type": "box","layout": "horizontal","contents": [{"type": "text","text": "🅸🅽🅴🆇🅱🅾🆃🆂","weight": "bold","color": warnanya1,"size": "md"}]},"hero": {"type": "image","url": "https://scontent.fcgk8-1.fna.fbcdn.net/v/t1.0-9/fr/cp0/e15/q65/51835843_2326067974083979_5266191763927728128_o.jpg?_nc_cat=108&efg=eyJpIjoiYiJ9&_nc_eui2=AeFDU4lcYDFco8MPKFdjadDZwGM-OaoU1OpdoEy5tbG_pgtK7-Qi0FKAnO5XYb0n84IH8UT1COwUMMZQtL6MZqzsB5nU9xrCFuWJwMS292zLew&_nc_oc=AQn1Bz_w6PRzflVaoNFmOwDK7FvrMRt9CMMBI719V6o55j2L5KBZr0wDB_pa_IZqf6E&_nc_ht=scontent.fcgk8-1.fna&oh=30aa3c7acb664e7e3e273d0c4052e603&oe=5DE71341","size": "full","aspectRatio": "20:13","aspectMode": "cover","action": {"type": "uri","uri": "https://line.me/ti/p/~f.pitlok4"}},"type": "bubble","body": {"type": "box","layout": "horizontal","contents": [{"type": "text","text": appNama+text,"wrap": True,"color": warnanya1,"align": "center"}]},"footer": {"type": "box","layout": "vertical","spacing": "sm","contents": [{"type": "button","style": "primary","color": warnanya1,"height": "sm","action": {"type": "uri","label": "ADD MY LINE","uri": "https://line.me/ti/p/"+me.getUserTicket().id}},{"type": "spacer","size": "sm",}],"flex": 0}}}
    me.sendFlex(to, data)
    me.sendMessage(Line_Apikey,runthime)
def Sider3(to, text):
    contact = me.getContact(op.param2)
    favoritelist = me.getFavoriteMids()
    grouplist = me.getGroupIdsJoined()
    contactlist = me.getAllContactIds()
    blockedlist = me.getBlockedContactIds()
    data = {"type": "flex","altText": "Lagi nyari janda","contents": {"styles": {"body": {"backgroundColor": "#000000"},"footer": {"backgroundColor": "#000000"}},"type": "bubble","body": {"contents": [{"contents":[{"text": "BIO DATA\n❀ NAMA: {}".format(me.getContact(rank.param2).displayName)+"\n❀ GROUP: {}".format(str(len(grouplist)))+"\n❀ FRIEND : {}".format(str(len(contactlist)))+"\n❀ FAFORITE : {}".format(str(len(favoritelist)))+"\n❀ BLOCKED : {}".format(str(len(blockedlist)))+"\nBio: {}".format(me.getContact(rank.param2).statusMessage),"size": "sm","color": "#FF3366","wrap": True,"type": "text","align": "center"},{"type": "separator","color": "#FF0000"},{"url": "https://obs.line-scdn.net/{}".format(me.getContact(rank.param2).pictureStatus),"type": "image","size": "full"}],"type": "box","spacing": "md","layout": "horizontal"},{"type": "separator","color": "#FF0000"},{"contents": [{"contents": [{"size": "xxl","type": "icon","url": "https://obs.line-scdn.net/{}".format(me.getContact(meM).pictureStatus)},{"text": text,"size": "sm","margin": "none","color": "#00FF00","wrap": True,"weight": "regular","type": "text","align": "center"}],"type": "box","layout": "baseline"}],"type": "box","layout": "horizontal"}],"type": "box","spacing": "md","layout": "vertical"},"footer": {"type": "box","layout": "vertical","contents": [{"type": "box","layout": "horizontal","flex": 2,"contents": [{"type": "button","style": "secondary","color": "#00FF00","height": "sm","action": {"type": "uri","label": "CREATOR","uri": "http://line.me/ti/p/~f.pitlok4"}}]}]}}}
    me.sendFlex(to, data)
def atend1():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict1, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
Helpgrup = """♡   (\   (\
     (>ㅅ< )  ♡
┏━━∪∪━━━━━━┓
ɢʀᴜᴘʟɪsᴛ
ɢɴᴀᴍᴇ: [ᴛᴇxᴛ]
ᴍᴇᴍʙᴇʀʟɪsᴛ
ᴍᴇᴍʙᴇʀᴘɪᴄᴛ
ᴄʀᴇᴀᴛᴏʀ ɢʀᴜᴘ
ɢɪɴғᴏ
ᴘᴇɴᴅɪɴɢʟɪsᴛ
ɢɪᴅ
ɢᴜʀʟ
ᴏᴘᴇɴ-ᴄʟᴏsᴇ
ᴘʀᴏʟɪsᴛ
ᴀᴅᴍɪɴʟɪsᴛ
┗━━━━━♡━━━━┛"""
Helps = """╭━──────────────━╮
xᴛᴄ ᴍᴇɴᴜ
╰━──────────────━╯
╭━──────────────━╮
ᴍᴇ
ᴍɪᴅ
ɢᴇᴛᴍɪᴅ
ᴍʏʙᴏᴛ
ʀᴇʙᴏᴏᴛ
ʀᴜɴᴛɪᴍᴇ
ɪɴᴇx
ᴘʀɪᴄᴇ
sᴛᴀᴛᴜs
ᴘᴍ ᴏɴ/ᴏғғ
sᴘᴇᴇᴅ-sᴘ
sᴏʀʏ @
ʙᴀɴʟɪsᴛ
ᴄʟᴇᴀʀʙᴀɴ
ᴀᴅᴍɪɴᴀᴅᴅ @/ ᴀᴅᴍɪɴᴅᴇʟʟ @
ʀᴇᴍᴏᴠᴇ ᴄʜᴀᴛ
╰━──────────────━╯
╭━──────────────━╮
├━────[Creator]───━
│➢  WE ARE INEXBOTS
╰━──────────────━╯"""
HelpMedia = """ ┏━━━━━ ♡ ━━━━━┓
Youtube [Judul]
Musik [Judul]
Televisi
Tanggal: [12-05-1945]
Movie [text]
Xvideo [text]
Cakcak
Id line
Call
Instagram [ID]
Smule [ID]
┗━━━━━ ♡ ━━━━━┛"""
Helpbot = """ ☆ ∩∩
 （   •  •）☆
┏━∪∪━━━━━━━━┓
░★ ʙᴏᴛ ᴏɴ-ᴏғғ
░★ ᴍʏ ᴘɪᴄᴛ
░★ ᴊs ᴘɪᴄᴛ
░★ ᴍʏɴᴀᴍᴇ: [ᴛᴇxᴛ]
░★ ᴊsɴᴀᴍᴇ: [ᴛᴇxᴛ]
░★ ᴊs ɪɴ-ᴏᴜᴛ
░★ sᴛᴀʏ - [ . ]-[ , ]
░★ ᴊsɴᴀᴍᴇ: [ᴛᴇxᴛ]
░★ ʙᴏᴛ ɪɴғᴏ
░★ ᴀᴅᴅ @
┗━━━━━━━━━━━┛"""
Help_OnOff = """╔═════════════════╗
║░★ x ᴏɴ-ᴏғғ
║░★ sᴛɪᴄᴋᴇʀ ᴏɴ-ᴏғғ
║░★ sᴛɪᴄᴋᴇʀʙɪɢ ᴏɴ-ᴏғғ
║░★ ᴡᴇʟᴄᴏᴍᴇ ᴏɴ-ᴏғғ
║░★ ᴀᴜᴛᴏᴊᴏɪɴ ᴏɴ-ᴏғғ
║░★ ᴀᴜᴛᴏʟᴇᴀᴠᴇ ᴏɴ-ᴏғғ
║░★ ᴀᴜᴛᴏᴀᴅᴅ ᴏɴ-ᴏғғ
║░★ ʀᴇᴀᴅ ᴏɴ-ᴏғғ
║░★ ᴜɴsᴇɴᴅ ᴏɴ-ᴏғғ
║░★ sʜᴀʀᴇᴅ ᴏɴ-ᴏғғ
║░★ ᴘᴍ ᴏɴ-ᴏғғ
║░★ ʀ1 ᴏɴ-ᴏғғ
║░★ sᴇᴛᴛ ᴏɴ-ᴏғғ
║ {\__/}         
║(   • - •)                 
║/つ つ✎_ _ _ _ _ _ _ _ _ _ _ _
╚═════════════════╝
"""
def SqL_R(text):
    R_SQL = text.lower()
    if InexBots["key"] == True:
        if R_SQL.startswith(InexBots["text"]):
            InexBotsList = R_SQL.replace(InexBots["text"],"")
        else:
            InexBotsList = "Undefined command"
    else:
        InexBotsList = text.lower()
    return InexBotsList
def serviceX(rank):
    global groupParam
    Rumahku = rank.param1
    Musuhku = rank.param2
    Temanku = rank.param3
    try:
        if rank.type == 0:
            return
        if rank.type == 11:
            print ("PRO QR")
            if Rumahku in pro["Pintu"]:
                if Musuhku in InexWars or Musuhku in Owner or Musuhku in Import_Server or Musuhku in Admin or Musuhku in meM:pass
                else:
                    Z = me.getGroup(Rumahku)
                    if Z.preventedJoinByTicket == False:
                        Z.preventedJoinByTicket = True
                        me.updateGroup(Z)
                        me.kickoutFromGroup(Rumahku,[Musuhku])
                        InexBots["blacklist"][Musuhku] = True
                    else:
                        jss.acceptGroupInvitation(Rumahku)
                        Z = jss.getGroup(Rumahku)
                        Z.preventedJoinByTicket = True
                        jss.updateGroup(Z)
                        jss.sendMessage(Rumahku, "Dont open qr")
                        jss.kickoutFromGroup(Rumahku,[Musuhku])
                        jss.leaveGroup(Rumahku)
                        me.inviteIntoGroup(Rumahku,[Antijs])
            if Musuhku in InexBots["blacklist"]:
                Z = me.getGroup(Rumahku)
                if Z.preventedJoinByTicket == False:
                    Z.preventedJoinByTicket = True
                    me.updateGroup(Z)
                    me.kickoutFromGroup(Rumahku,[Musuhku])
                else:
                    jss.acceptGroupInvitation(Rumahku)
                    Z = jss.getGroup(Rumahku)
                    Z.preventedJoinByTicket = True
                    jss.updateGroup(Z)
                    jss.sendMessage(Rumahku, "Dont open qr")
                    jss.kickoutFromGroup(Rumahku,[Musuhku])
                    jss.leaveGroup(Rumahku)
                    me.inviteIntoGroup(Rumahku,[Antijs])
                
        if rank.type == 19:
            print ("PRO AJS")
            try:
                if Rumahku in pro["Penyelamat"]:
                  if Temanku in meM:
                    if Musuhku not in InexWars and Musuhku not in Owner and Musuhku not in meM and Musuhku not in Import_Server and Musuhku not in Admin:
                        jss.acceptGroupInvitation(Rumahku)
                        G = jss.getGroup(Rumahku)
                        G.preventedJoinByTicket = False
                        jss.updateGroup(G)
                        Terbuka = jss.reissueGroupTicket(Rumahku)
                        me.acceptGroupInvitationByTicket(Rumahku,Terbuka)
                        jss.kickoutFromGroup(Rumahku,[Musuhku])
                        G.preventedJoinByTicket = True
                        jss.updateGroup(G)
                        InexBots["blacklist"][Musuhku] = True
                        jss.leaveGroup(Rumahku)
                        me.inviteIntoGroup(Rumahku,[Antijs])
                        me.inviteIntoGroup(Rumahku,[Owner])
                    else:
                        pass
                if Temanku in Antijs:
                    if Musuhku not in InexWars and Musuhku not in Owner and Musuhku not in meM and Musuhku not in Import_Server and Musuhku not in Admin:
                        try:
                            me.kickoutFromGroup(Rumahku,[Musuhku])
                            me.findAndAddContactsByMid(Temanku)
                            me.inviteIntoGroup(Rumahku,[Temanku])
                        except:
                            me.kickoutFromGroup(Rumahku,[Musuhku])
                            me.findAndAddContactsByMid(Temanku)
                            me.inviteIntoGroup(Rumahku,[Temanku])
                if Musuhku not in InexWars and Musuhku not in Owner and Musuhku not in meM and Musuhku not in Import_Server and Musuhku not in Admin:
                    if Temanku in Owner:
                        if Rumahku in pro["Penyelamat"]:
                            InexBots["blacklist"][Musuhku] = True
                            me.kickoutFromGroup(Rumahku,[Musuhku])
                            me.findAndAddContactsByMid(Temanku)
                            me.inviteIntoGroup(Rumahku,[Temanku])
                else:
                    pass
            except:
                pass
        if rank.type == 32:
            print ("PRO JOIN")
            if Rumahku in pro["Pencuri"]:
                if Musuhku not in InexWars and Musuhku not in Owner and Musuhku not in meM and Musuhku not in Import_Server and Musuhku not in Admin:
                    InexBots["blacklist"][Musuhku] = True
                    try:
                        if Temanku not in InexBots["blacklist"]:
                            me.kickoutFromGroup(Rumahku,[Musuhku])
                    except:
                        pass
                return
        if rank.type == 13:
            print ("PRO INVITE")
            if Rumahku in pro["Penghasut"]:
                if Musuhku not in InexWars and Musuhku not in Owner and Musuhku not in meM and Musuhku not in Import_Server and Musuhku not in Admin:
                    InexBots["blacklist"][Musuhku] = True
                    try:
                        if Temanku not in InexBots["blacklist"]:
                            group = me.getGroup(Rumahku)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                me.cancelGroupInvitation(Rumahku,[_mid])
                                me.kickoutFromGroup(Rumahku,[Musuhku])
                    except:
                        pass

        if rank.type == 17:
            print ("PRO KICK")
            if Rumahku in pro["Maling"]:
                if Musuhku not in InexWars and Musuhku not in Owner and Musuhku not in meM:
                    InexBots["blacklist"][Musuhku] = True
                    try:
                        if Temanku not in InexBots["blacklist"]:
                        	me.kickoutFromGroup(Rumahku,[Musuhku])
                    except:
                        pass

        if rank.type == 19 or rank.type == 32:
            print ("INDUK DI KICK")
            if meM in Temanku:
                if Musuhku in InexWars:
                    pass
                else:
                    InexBots["blacklist"][Musuhku] = True
                    print ("AJS BANTU INDUK")
                    try:
                        jss.acceptGroupInvitation(Rumahku)
                        jss.inviteIntoGroup(Rumahku,[Temanku])
                        jss.kickoutFromGroup(Rumahku,[Musuhku])
                        me.acceptGroupInvitation(Rumahku)
                    except:
                        jss.acceptGroupInvitation(Rumahku)
                        Z = jss.getGroup(Rumahku)
                        Z.preventedJoinByTicket = False
                        jss.updateGroup(Z)
                        Terbuka = jss.reissueGroupTicket(Rumahku)
                        me.acceptGroupInvitationByTicket(Rumahku,Terbuka)
                        me.kickoutFromGroup(Rumahku,[Musuhku])
                        jss.leaveGroup(Rumahku)
                        Z = me.getGroup(Rumahku)
                        Z.preventedJoinByTicket = True
                        me.updateGroup(Z)
                        me.inviteIntoGroup(Rumahku,[Antijs])
        if rank.type == 19 or rank.type == 32:
            print ("AJS DI KICK")
            if Antijs in Temanku:
                if Musuhku in InexWars:
                    pass
                else:
                    InexBots["blacklist"][Musuhku] = True
                    print ("INDUK BANTU AJS")
                    try:
                        me.inviteIntoGroup(Rumahku,[Antijs])
                        me.kickoutFromGroup(Rumahku,[Musuhku])
                    except:
                        Z = me.getGroup(Rumahku)
                        Z.preventedJoinByTicket = False
                        me.updateGroup(Z)
                        Terbuka = me.reissueGroupTicket(Rumahku)
                        jss.acceptGroupInvitationByTicket(Rumahku,Terbuka)
                        jss.kickoutFromGroup(Rumahku,[Musuhku])
                        jss.leaveGroup(Rumahku)
                        Z = me.getGroup(Rumahku)
                        Z.preventedJoinByTicket = True
                        me.updateGroup(Z)
                        me.inviteIntoGroup(Rumahku,[Antijs])

        if rank.type == 19 or rank.type == 32:
            print ("OWNER DI KICK")
            if Owner in Temanku:
                if Musuhku in InexWars:
                    pass
                else:
                    InexBots["blacklist"][Musuhku] = True
                    try:
                        me.findAndAddContactsByMid(Rumahku,Owner)
                        me.inviteIntoGroup(Rumahku,Owner)
                        me.kickoutFromGroup(Rumahku,[Musuhku])
                    except:
                        jss.acceptGroupInvitation(Rumahku)
                        jss.findAndAddContactsByMid(Rumahku,Owner)
                        jss.inviteIntoGroup(Rumahku,Owner)
                        jss.kickoutFromGroup(Rumahku,[Musuhku])
        if rank.type == 17:
            print ("MUSUH TERBLACKLIST KENA KICK")
            if Musuhku in InexBots["blacklist"]:
                if Musuhku not in Owner and Musuhku not in meM:
                    try:
                        me.kickoutFromGroup(Rumahku,[Musuhku])
                    except:
                        jss.kickoutFromGroup(Rumahku,[Musuhku])
            else:pass
        if rank.type == 13:
            print ("MUSUH TERBLACKLIST DI PENDINGAN CANCLE")
            if Musuhku in InexBots["blacklist"]:
                if Temanku not in Owner and Temanku not in meM:
                    try:
                        me.cancelGroupInvitation(Rumahku,[Temanku])
                    except:
                        jss.cancelGroupInvitation(Rumahku,[Temanku])
            if Temanku in InexBots["blacklist"]:
                if Musuhku not in Owner and Musuhku not in meM:
                    try:
                        me.cancelGroupInvitation(Rumahku,[Temanku])
                    except:
                        jss.cancelGroupInvitation(Rumahku,[Temanku])
                else:pass
            if Temanku in InexBots["blacklist"]:
                if Musuhku not in Owner and Musuhku not in meM:
                    try:
                        me.cancelGroupInvitation(Rumahku,[Temanku])
                        me.kickoutFromGroup(Rumahku,[Musuhku])
                        me.sendMessage(Rumahku, "Blacklist True")
                    except:
                        pass
        if rank.type == 13:
            print ("AUTO LEAVE")
            if meM in Temanku:
                if InexBots["autoLeave"] == True:
                    if Musuhku not in Owner and Musuhku not in meM and Musuhku not in InexWars:
                        me.acceptGroupInvitation(Rumahku)
                        ginfo = me.getGroup(Rumahku)
                        sendTextTemplate1(Rumahku,"Maaf fams "+str(ginfo.name)+" saya pamit lagi ya.")
                        me.leaveGroup(Rumahku)
                    else:
                        me.acceptGroupInvitation(Rumahku)
                        ginfo = me.getGroup(Rumahku)
                        me.sendMessage(Rumahku,str(ginfo.name))

        if rank.type == 13:
            print ("AUTO JOIN")
            if meM in Temanku:
                if InexBots["autoJoin"] == True:
                    if Musuhku not in Owner and Musuhku not in meM and Musuhku not in InexWars:
                        me.acceptGroupInvitation(Rumahku)
                        ginfo = me.getGroup(Rumahku)
                        sendTextTemplate1(Rumahku,"Terimakasih kak yg udah undang saya di room "+str(ginfo.name))
                    else:
                        me.acceptGroupInvitation(Rumahku)
                        ginfo = me.getGroup(Rumahku)
                        sendTextTemplate1(Rumahku,"Terimakasih kak yg udah undang saya di room "+str(ginfo.name))

        if rank.type == 26 or rank.type == 25:
            msg = rank.message
            Keluarga = msg.id
            Pesan = msg.to
            Dari = msg._from
            Proses_message = msg.text
            if Proses_message == "Active" or Proses_message == "active":
                if Dari in Owner or Dari in meM:
                    InexBots["bot"] = True
                    me.sendMessage(Pesan,"Bot active")
                    me.sendMessage(Pesan,"Already Ok "+me.getContact(Dari).displayName)
                    InexBots["Conection"] = Pesan
                    Run_Xx()
                    
            if Proses_message == "Non active" or Proses_message == "non active":
                print ("NOTIF BOT NON ACTIVE")
                if Dari in Owner or Dari in meM:
                    InexBots["bot"] = False
                    me.sendMessage(Pesan,"Bot Non Active")
                    me.sendMessage(Pesan,"Ok I'am Turn down "+me.getContact(Dari).displayName)
                
        if rank.type == 25 or rank.type == 26:
          if InexBots["bot"] == True:
            msg = rank.message
            text = msg.text
            Keluarga = msg.id
            Pesan = msg.to
            Dari = msg._from
            Gr = Rumahku
            InexBotsLists = InexBots["text"].title()
            if InexBots["key"] == False:
                 InexBotsLists = ''
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if Dari != me.profile.mid:
                        to = Dari
                    else:
                        to = Pesan
                elif msg.toType == 1:
                    to = Pesan
                elif msg.toType == 2:
                    to = Pesan
                if msg.contentType == 0:
                    if text is None:
                        return
                    else:
                        InexBotsList = SqL_R(text)
                        if InexBotsList == "helps":
                          if Dari in Owner or Dari in meM:
                            Sider1(Pesan,Helps)
                        if InexBotsList == "helpsgrup":
                          if Dari in Owner or Dari in meM:
                            Sider1(Pesan,Helpgrup)
                        if InexBotsList == "helpbot":
                          if Dari in Owner or Dari in meM:
                            sendTextTemplate1(Pesan,Helpbot)
                        if InexBotsList == "helpmedia":
                          if Dari in Owner or Dari in meM:
                            Sider2(Pesan,HelpMedia)
                        if InexBotsList == "helpsaklar":
                          if Dari in Owner or Dari in meM:
                            sendTextTemplate1(Pesan,Help_OnOff)
                        if InexBotsList == "statust":
                          if Dari in Owner or Dari in meM:
                            Res= "╭━──────────────━╮\n│➢      xᴛᴄ ᴍᴇɴᴜ\n╰━──────────────━╯\n╭━──────────────━╮\n"
                            Res+= "├➢➢CHECK BOT\n├━──────────────━─\n"
                            if InexBots["Add"] == True: Res+= Stiles+" autoadd->『on』\n"
                            else: Res+= Stiles+" autoadd->『off』\n"
                            if InexBots["Shared"] == True: Res+= Stiles+" shared->『on』\n"
                            else: Res+= Stiles+" shared->『off』\n"
                            if InexBots["Join"] == True: Res+= Stiles+" autojoin->『on』\n"
                            else: Res+= Stiles+" autojoin->『off』\n"
                            if InexBots["Read"] == True: Res+= Stiles+" autoread->『on』\n"
                            else: Res+= Stiles+" autoread->『off』\n"
                            if InexBots["Unsend"] == True: Res+= Stiles+" unsend->『on』\n"
                            else: Res+= Stiles+" unsend->『off』\n"
                            if Welcome == True: Res+= Stiles+" welcome->『on』\n"
                            else: Res+= Stiles+" welcome->『off』\n"
                            if InexBots["Respon"] == True: Res+= Stiles+" respon->『on』\n"
                            else: Res+= Stiles+" respon->『off』\n"
                            if InexBots["arespon"] == True: Res+= Stiles+" respon pm->『on』\n"
                            else: Res+= Stiles+" respon pm->『off』\n"
                            Res+= "╰━──────────────━╯\n╭━──────────────━╮\n│➢      xᴛᴄ ᴍᴇɴᴜ\n╰━──────────────━╯\n╭━──────────────━╮\n"
                            Res+= "├━────[SelfName]───━\n"+Stiles+meProfile.displayName+"\n"
                            sendTextTemplate1(Pesan, str(Res)+Stiles+" WE ARE INEXBOTS\n╰━──────────────━╯")
                        if InexBotsList == "me":
                            Nama = me.getContact(Dari)
                            cover = me.getProfileCoverURL(Dari)
                            me.reissueUserTicket()
                            data = {"type": "flex","altText": "{} Berak di celana".format(str(Nama.displayName)),"contents": {"type": "bubble","styles": {"header": {"backgroundColor": "#000000",},"body": {"backgroundColor": "#000000","separator": True,"separatorColor": "#000000"},"footer": {"backgroundColor": "#000000","separator": True}},"hero": {"type": "image","url": "https://os.line.naver.jp/os/p/{}".format(Dari),"size": "full","aspectRatio": "20:13","aspectMode": "cover","action": {"type": "uri","uri": "https://line.me/ti/p/~denjaka-inexx"}},"body": {"type": "box","layout": "vertical","spacing": "md","action": {"type": "uri","uri": "https://line.me/ti/p/~denjaka-inexx"},"contents": [{"type": "text","text": "🅸🅽🅴🆇🅱🅾🆃🆂","size": "md","color": "#0000FF"},{"type": "box","layout": "vertical","spacing": "sm","contents": [{"type": "box","layout": "baseline","contents": [{"type": "icon","url": "https://os.line.naver.jp/os/p/{}".format(Dari),"size": "5xl"},{"type": "text","text": " Name : ","weight": "bold","color": "#0000FF","margin": "sm","flex": 0},{"type": "text","text": Nama.displayName,"size": "sm","align": "end","color": "#0000FF"}]}]},{"type": "text","text": "_________________________________________________\nɬɧąŋƙʂ ɬơ ąƖƖąɧ \nɬɧąŋƙʂ ɬơ ℘ཞąŋƙცơɬʂ,\nąŋɖ ɬɧąŋƙʂ ɬơ ıŋɛҳ ɬɛąɱ.","wrap": True,"color": "#0000FF","size": "xxs"}]},"footer": {"type": "box","layout": "vertical","contents": [{"type": "spacer","size": "sm"},{"type": "button","style": "primary","color": "#0000FF","action": {"type": "uri","label": "CONTACT","uri": "https://line.me/ti/p/"+me.getUserTicket().id}}]}}}
                            me.sendFlex(Pesan, data)
                        if InexBotsList == "id line":
                          if Dari in Owner or Dari in meM:
                            me.reissueUserTicket()
                            My_Id = me.profile.displayName + "My id Line: http://line.me/ti/p/" + me.getUserTicket().id
                            sendTextTemplate(Pesan,My_Id)
                        if InexBotsList == "@pamit":
                          if Dari in Owner or Dari in meM:
                            me.leaveGroup(Pesan)
                        if InexBotsList == "my cover":
                          if Dari in Owner or Dari in meM:
                            h = me.getContact(Dari)
                            cpu = me.getProfileCoverURL(h)          
                            path = str(cpu)
                            me.sendImageWithURL(Pesan, path)
                            data = {"type": "template","altText": "{} sent a image".format(me.getContact(Dari).displayName),"template": {"type": "image_carousel","columns": [{"imageUrl": "{}".format(path),"size": "full", "action": {"type": "uri","uri": "http://line.me/ti/p/~denjaka_inex"}}]}}
                            me.sendFlex(to, data)
                        if InexBotsList == "televisi":
                          if Dari in Owner or Dari in meM:
                            data = {"type": "flex","altText": "Live","contents": {"styles": {"body": {"backgroundColor": "#000000"},"footer": {"backgroundColor": "#000000"}},"type": "bubble","hero": {"type": "image","url": "https://1.bp.blogspot.com/-i1zdSitCRW0/Vvf8oTMvzII/AAAAAAAAP7M/WZjC__380i8jqaZCTKRx8_XxfGvE6guaA/s1600/usee-tv.jpg","size": "full","aspectRatio": "20:13","aspectMode": "cover",},"body": {"contents": [{"contents": [{"url": "https://id.androidxyz.com/wp-content/uploads/2018/05/10-Aplikasi-Nonton-TV-Android-Offline-Tanpa-Kuota-dan-Internet-Terbaik-Indonesia.jpg","type": "image"},],"type": "box","spacing": "sm","layout": "vertical"},{"type": "separator","color": "#DC143C"},{"contents": [{"text": "TV ONLINE","size": "md","align": "center","color": "#FF0000","wrap": True,"weight": "bold","type": "text"}],"type": "box","spacing": "sm","layout": "vertical"},{"type": "separator","color": "#DC143C"},{"contents":[{"contents":[{"url": "https://mobile.facebook.com/photo.php?fbid=2326067967417313&id=100000423968592&set=a.119622271395238&source=56","type": "icon","size": "md"},{"text":"saluran tv streaming","size": "sm","margin": "none","color": "#6F4E37","wrap": True,"weight": "regular","type": "text"}],"type": "box","layout": "baseline"}],"type": "box","layout": "vertical"}],"type": "box","spacing": "md","layout": "vertical"},"footer": {"type": "box","layout": "vertical","spacing": "sm","contents": [{"type": "button","style": "link","height": "sm","action": {"type": "uri","label": "channel","uri": "line://app/1560739707-0YmQLW3W",}},{"type": "spacer","size": "sm",}],"flex": 0}}}
                            me.sendFlex(to, data)
                        if InexBotsList == "cakcak":
                          if Dari in Owner or Dari in meM:
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(InexBots["userAgent"])
                                r = web.get('http://api-1cak.herokuapp.com/random')
                                data = r.text
                                data = json.loads(data)
                                img = data["img"]
                                sendTextTemplate1(Pesan,"━═| Daftar cakcak |═━\n━═| Title: %s\n━═| Link: %s\n━═| Id: %s\n━═| Votes: %s\n━═| NSFW: %s\n━═| [ Finish ] |═━" %(str(data["title"].replace('FACEBOOK Comments', ' ')), str(data["url"]), str(data["id"]), str(data["votes"]), str(data["nsfw"])))
                        if InexBotsList.startswith("xvideo "):
                          if Dari in Owner or Dari in meM:
                            separate = text.split(" ")
                            kata = text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(InexBots["userAgent"])
                                try:
                                    r = web.get("https://api.redtube.com/?data=redtube.Videos.searchVideos&output=json&search={}".format(urllib.parse.quote(kata)))
                                    data = r.text
                                    data = json.loads(data)
                                    ret_ = "━═Bokep inimah"
                                    no = 1
                                    anu = data["videos"]
                                    if len(anu) >= 20:
                                        for s in range(20):
                                            hmm = anu[s]
                                            title = hmm['video']['title']
                                            duration = hmm['video']['duration']
                                            views = hmm['video']['views']
                                            link = hmm['video']['embed_url']
                                            ret_ += "\n━═ {}. \nTitle ━═ {}\nDurasi ━═ {}\nViews ━═ {}\nLink ━═ {}".format(str(no), str(title), str(duration), str(views), str(link))
                                            no += 1
                                    else:
                                        for s in anu:
                                            hmm = s
                                            title = hmm['video']['title']
                                            duration = hmm['video']['duration']
                                            views = hmm['video']['views']
                                            link = hmm['video']['embed_url']
                                            ret_ += "\n━═ {}. \nTitle ━═ {}\nDurasi ━═ {}\nViews ━═ {}\nLink ━═ {}".format(str(no), str(title), str(duration), str(views), str(link))
                                            no += 1
                                    sendTextTemplate1(Pesan, str(ret_))
                                except:
                                    sendTextTemplate1(Pesan, "Tidak ditemukan")
                        if InexBotsList.startswith("movie "):
                          if Dari in Owner or Dari in meM:
                            sep = text.split(" ")
                            title = text.replace(sep[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(InexBots["userAgent"])
                                r = web.get("http://www.omdbapi.com/?t="+title+"&y=&plot=full&apikey=4bdd1d70")
                                data=r.text
                                data=json.loads(data)
                                hasil = "╭━━═════[ Hasil pencarian film]"
                                hasil += "\n| Informasi : " +str(data["Title"])+ " (" +str(data["Year"])+ ")"
                                hasil += "\n| Plot : " +str(data["Plot"])
                                hasil += "\n| Director : " +str(data["Director"])
                                hasil += "\n| Actors : " +str(data["Actors"])
                                hasil += "\n| Release : " +str(data["Released"])
                                hasil += "\n| Genre : " +str(data["Genre"])
                                hasil += "\n| Timer : " +str(data["Runtime"])+"\n╰━──────────────━╯"
                                img = data["Poster"]
                                me.sendImageWithURL(Pesan,img)
                                sendTextTemplate1(Pesan,hasil)
                        if InexBotsList.startswith("add "):
                          if Dari in Owner or Dari in meM:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]                
                            mmid = me.getContact(key1)
                            me.findAndAddContactsByMid(key1)
                            sendTextTemplate(Pesan, "teman di tambahkan")
                        if InexBotsList == "reboot":
                          if Dari in Owner or Dari in meM:
                            sendTextTemplate(Pesan, "Selesai.!!")
                            InexBots["Conection"] = Pesan
                            Run_Xp()
                        if InexBotsList == "runtime":
                          if Dari in Owner or Dari in meM:
                            timeNow = time.time()
                            rantime = timeNow - botStart
                            runtime = format_timespan(rantime)
                            sendTextTemplate(Pesan, "☣️RUNTIME BOTS☣️\n☣️[ {}".format(str(runtime)))
                        if InexBotsList == "help":
                          if Dari in Owner or Dari in meM:
                            me.sendFlex(Pesan, plate["helpgrup"])
                        if InexBotsList == "price":
                          if Dari in Owner or Dari in meM:
                            me.sendFlex(Pesan, plate["pricelist"])
                        if InexBotsList == "speed":
                          if Dari in Owner or Dari in meM:
                            start = time.time()
                            elapsed_time = time.time() - start
                            gambar = ("https://media1.tenor.com/images/f93a0ca129d8cf2403de969c0a4a249d/tenor.gif?itemid=9218951","https://i.pinimg.com/originals/03/b6/77/03b67753372dc432953fef2a4d89959d.gif","https://steamuserimages-a.akamaihd.net/ugc/848214635663113729/072EA7E5479C89B54E95EBD2B6540841C7BD7A1E/")
                            gambarnya = random.choice(gambar)
                            data = {"type": "flex","altText": "Apollo lewat","contents": {"styles": {"body": {"backgroundColor": "#000000"},"footer": {"backgroundColor": "#000000"}},"type": "bubble","hero": {"type": "image","url": gambarnya,"size": "full","aspectRatio": "3:4","aspectMode": "cover",},"body": {"contents": [{"contents": [{"text": "{} Detik".format(str(elapsed_time)),"size": "md","align": "center","wrap": True,"weight": "regular","type": "text"}],"type": "box","layout": "baseline"}],"type": "box","layout": "vertical"}}}
                            me.sendFlex(Pesan, data)
                        if InexBotsList == "mid":
                            h = me.getContact(Dari)
                            me.sendMessage(Pesan,h.mid)
                        if InexBotsList == "memberpict":
                          if Dari in Owner or Dari in meM:
                            kontak = me.getGroup(Pesan)
                            group = kontak.members
                            picall = []
                            for ids in group:
                              if len(picall) >= 400:
                                pass
                              else:
                                picall.append({"imageUrl": "https://os.line.naver.jp/os/p/{}".format(ids.mid),"action": {"type": "uri","uri": "http://line.me/ti/p/~denjaka-inexx"}})
                            k = len(picall)//10
                            for aa in range(k+1):
                              data = {"type": "template","altText": "Poto artis semua","template": {"type": "image_carousel","columns": picall[aa*10 : (aa+1)*10]}}
                              me.sendFlex(Pesan, data)
                        if InexBotsList == "myprofil":
                          if Dari in Owner or Dari in meM:
                            contact = me.getContact(Dari)
                            cover = me.getProfileCoverURL(Dari)
                            me.reissueUserTicket()
                            result = "╔══[ Details Profile ]"
                            result += "\n╠ Display Name : {}".format(contact.displayName)
                            result += "\n╠ Mid : {}".format(contact.mid)
                            result += "\n╠ Status Message : {}".format(contact.statusMessage)
                            result += "\n╠ Picture Profile : http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                            result += "\n╠ Cover : {}".format(str(cover))
                            result += "\n╚══[ Finish ]"
                            sendTextTemplate1(Pesan, str(result))
                            try:
                              poto = "https://os.line.naver.jp/os/p/{}".format(Dari)
                            except:
                              poto = "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQcNdUbC8kEeVWqgR9qMX66lQ_hQPM8ScNY30x4nqpYaKY2jt02"
                            dax = {"type": "template","altText": "berak di celana","template": {"type": "image_carousel","columns": [{"imageUrl": poto,"layout": "horizontal","action": {"type": "uri","label": "PROFILE","uri": poto,"area": {"x": 447,"y": 356,"width": 1040,"height": 1040}}},{"imageUrl": cover,"layout": "horizontal","action": {"type": "uri","label": "COVER","uri": cover,"area": {"x": 447,"y": 356,"width": 1040,"height": 1040}}},{"imageUrl": "https://qr-official.line.me/L/"+me.getUserTicket().id+".png","layout": "horizontal","action": {"type": "uri","label": "CONTACT","uri": "https://line.me/ti/p/"+me.getUserTicket().id,"area": {"x": 447,"y": 356,"width": 1040,"height": 1040}}}]}}
                            me.sendFlex(Pesan, dax)
                        if InexBotsList.startswith("getmid "):
                          if Dari in Owner or Dari in meM:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                ret_ = ""
                                for ls in lists:
                                    ret_ += "{}".format(str(ls))
                                me.sendMessage(Pesan, str(ret_))
                        if InexBotsList.startswith("youtube "):
                          if Dari in Owner or Dari in meM:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = InexBotsList.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    mee = best.url
                                    data = {"type": "flex","altText": "YOUTUBE","contents": {"styles": {"body": {"backgroundColor": "#FFFFFF"},"footer": {"backgroundColor": "#FF0000"}},"type": "bubble","body": {"contents": [{"contents": [{"url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSgekIeIdfny8Bgr-WBIhhZgecUBZKyE89-u_SdB6Z2P-XNPdaVXhrSL1o","type": "image"},{"type": "separator","color": "#C0C0C0"},{"text": "YOUTUBE\nVIDEOS\nLOADING.\nPLAY","size": "sm","color": "#000000","wrap": True,"weight": "bold","type": "text"}],"type": "box","spacing": "md","layout": "horizontal"},{"type": "separator","color": "#C0C0C0"},{"contents": [{"text": "JUDUL\n " + vid.title + " ?","size": "xs","align": "center","color": "#000000","wrap": True,"weight": "bold","type": "text"}],"type": "box","spacing": "md","layout": "vertical"},{"type": "separator","color": "#C0C0C0"},{"contents": [{"contents": [{"url": "https://media2.giphy.com/media/13Nc3xlO1kGg3S/100.webp?cid=19f5b51a5c7364c358654a44730cc489","type": "icon","size": "md"},{"text": "Author : " + str(vid.author),"size": "sm","margin": "none","color": "#6F00FF","wrap": True,"weight": "regular","type": "text"}],"type": "box","layout": "baseline"},{"contents": [{"url": "https://media2.giphy.com/media/13Nc3xlO1kGg3S/100.webp?cid=19f5b51a5c7364c358654a44730cc489","type": "icon","size": "md"},{"text": "Duration : " + str(vid.duration),"size": "sm","margin": "none","color": "#6F00FF","wrap": True,"weight": "regular","type": "text"}],"type": "box","layout": "baseline"},{"contents": [{"url": "https://media2.giphy.com/media/13Nc3xlO1kGg3S/100.webp?cid=19f5b51a5c7364c358654a44730cc489","type": "icon","size": "md"},{"text": "Likes : " + str(vid.likes),"size": "sm","margin": "none","color": "#6F00FF","wrap": True,"weight": "regular","type": "text"}],"type": "box","layout": "baseline"},{"contents": [{"url": "https://media2.giphy.com/media/13Nc3xlO1kGg3S/100.webp?cid=19f5b51a5c7364c358654a44730cc489","type": "icon","size": "md"},{"text": "Rating : " + str(vid.rating),"size": "sm","margin": "none","color": "#6F00FF","wrap": True,"weight": "regular","type": "text"}],"type": "box","layout": "baseline"}],"type": "box","layout": "vertical"}],"type": "box","spacing": "md","layout": "vertical"},"footer":{"type": "box","layout": "vertical","contents": [{"type": "box","layout": "horizontal","contents": [{"type": "button","flex": 2,"style": "primary","color": "#800000","height": "sm","action": {"type": "uri","label": "OFFICIAL","uri": "https://line.me/R/ti/p/%40bvb1195k"}},{"flex": 3,"type": "button","style": "primary","color": "#800000","margin": "sm","height": "sm","action": {"type": "uri","label": "YOUTUBE","uri": search_url}}]}]}}}
                                    me.sendFlex(Pesan, data)
                                me.sendVideoWithURL(Pesan, mee)
                            except Exception as error:
                                return False
                        if InexBotsList.startswith("Tanggal: "):
                          if Dari in Owner or Dari in meM:
                            try:
                                sep = msg.text.split(" ")
                                tanggal = msg.text.replace(sep[0] + " ","")
                                r = requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                                data=r.text
                                data=json.loads(data)
                                ret_ = "╭━━━━════[Tanggal,Lahir]"
                                ret_ += "\n┣═Tanggal lahir : {}".format(str(data["data"]["lahir"]))
                                ret_ += "\n┣═Umur : {}".format(str(data["data"]["usia"]))
                                ret_ += "\n┣═Tanggal ultah : {}".format(str(data["data"]["ultah"]))
                                ret_ += "\n┣═Zodiak : {}".format(str(data["data"]["zodiak"]))
                                ret_ += "\n╰━━═════[INEXBOTS]"
                                sendTextTemplate1(Pesan, str(ret_))
                            except Exception as error:
                                return False
                        if InexBotsList.startswith("instagram "):
                          if Dari in Owner or Dari in meM:
                            sep = text.split(" ")
                            instagram = text.replace(sep[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(InexBots["userAgent"])
                                html = web.get("https://www.instagram.com/" + instagram + "/")
                                soup = BeautifulSoup(html.text, 'html5lib')
                                data = soup.find_all('meta', attrs={'property':'og:description'})
                                text = data[0].get('content').split()
                                data1 = soup.find_all('meta', attrs={'property':'og:image'})
                                text1 = data1[0].get('content').split()
                                user = "Name: " + text[-2] + "\n"
                                user1 = "Username: " + text[-1] + "\n"
                                followers = "Followers: " + text[0] + "\n"
                                following = "Following: " + text[2] + "\n"
                                post = "Post: " + text[4] + "\n"
                                link = "Link: " + "https://instagram.com/" + instagram
                                me.sendImageWithURL(Pesan, text1[0])
                                Sider1(Pesan, user + user1 + followers + following + post + link)
                                print("[Notif] Search Instagram Sucess")
                        if InexBotsList.startswith("smule "):
                          if Dari in Owner or Dari in meM:
                            proses = text.split(" ")
                            urutan = text.replace(proses[0] + " ","")
                            count = urutan.split("-")
                            search = str(count[0])
                            r = requests.get("https://www.smule.com/"+search+"/performances/json")
                            data = json.loads(r.text)
                            if len(count) == 1:
                                no = 0
                                ret_ = "DAFTAR OC\n"
                                for aa in data["list"]:
                                    no += 1
                                    ret_ += "\n" + str(no) + ". " + str(aa["title"])
                                ret_ += "\n\nSelanjutnya ketik: smule {}-nomor\nuntuk melihat detailnya. ".format(str(search))
                                sendTextTemplate1(Pesan,ret_)
                            elif len(count) == 2:
                                try:
                                    num = int(count[1])
                                    b = data["list"][num - 1]
                                    smule = str(b["web_url"])
                                    c = "Judul Oc: "+str(b["title"])
                                    c += "\nPembuat: "+str(b["owner"]["handle"])
                                    c += "\nTotal like: "+str(b["stats"]["total_loves"])+" like"
                                    c += "\nTotal comment: "+str(b["stats"]["total_comments"])+" comment"
                                    c += "\nStatus VIP: "+str(b["owner"]["is_vip"])
                                    c += "\nStatus Oc: "+str(b["message"])
                                    c += "\nCreated Oc: {}".format(b["created_at"][:10])
                                    c += "\nDidengarkan: {}".format(b["stats"]["total_listens"])+" orang"
                                    hasil = "Detail Record\n\n"+str(c)
                                    dl = str(b["cover_url"])
                                    sendTextTemplate1(Pesan,dl)
                                    sendTextTemplate(Pesan, hasil, {'AGENT_NAME': ' URL Smule','AGENT_LINK': 'https://www.smule.com/{}'.format(str(b['owner']['handle'])),'AGENT_ICON': 'https://png.icons8.com/color/50/000000/speaker.png' })
                                    with requests.session() as s:
                                        s.headers['user-agent'] = 'Mozilla/5.0'
                                        r = s.get("https://sing.salon/smule-downloader/?url=https://www.smule.com{}".format(urllib.parse.quote(smule)))
                                        data = BeautifulSoup(r.content, 'html5lib')
                                        get = data.select("a[href*=https://www.smule.com/redir?]")[0]
                                        title = data.findAll('h2')[0].text
                                        imag = data.select("img[src*=https://www.smule.com/redir?]")[0]
                                        if 'Smule.m4a' in get['download']:
                                            sendTextTemplate(Pesan,"Type: Audio\n\nPlease wait for audio...")
                                            me.sendAudioWithURL(Pesan, get['href'])
                                        else:
                                            sendTextTemplate(Pesan,"Type: Video\n\nPlease wait for video...")
                                            cl.sendVideoWithURL(Pesan, get['href'])
                                except Exception as error:
                                    return False
                        if InexBotsList.startswith("musik "):
                            try:
                                proses = text.split(" ")
                                urutan = text.replace(proses[0] + " ","")
                                r = requests.get("http://api.zicor.ooo/joox.php?song={}".format(str(urllib.parse.quote(urutan))))
                                data = r.text
                                data = json.loads(data)
                                b = data
                                c = str(b["title"])
                                d = str(b["singer"])
                                e = str(b["url"])
                                g = str(b["image"])
                                hasil = "Penyanyi: "+str(d)
                                hasil += "\nJudul : "+str(c)
                                data = {"type": "flex","altText": "Musik","contents": {"styles": {"body": {"backgroundColor": "#0000FF"},"footer": {"backgroundColor": "#7FFF00"}},"type": "bubble","body": {"contents": [{"contents": [{"url": g,"type": "image"},{"type": "separator","color": "#F8F8FF"},{"text": "INEX TEAM\n\nMP3\nSONG ALBUM","size": "xs","color": "#00FF00","wrap": True,"weight": "bold","type": "text"}],"type": "box","spacing": "md","layout": "horizontal"},{"type": "separator","color": "#FF0000"},{"contents": [{"contents": [{"text": hasil,"size": "sm","margin": "none","color": "#FFFF00","wrap": True,"weight": "regular","type": "text"}],"type": "box","layout": "baseline"}],"type": "box","layout": "vertical"}],"type": "box","spacing": "md","layout": "vertical"},"hero": {"type": "image","aspectRatio": "20:13","aspectMode": "cover","url": g,"size": "full","margin": "xl"},"footer": {"type": "box","layout": "vertical","contents": [{"type": "box","layout": "horizontal","contents": [{"type": "button","flex": 2,"style": "primary","color": "#660000","height": "sm","action": {"type": "uri","label": "URL","uri": e}},{"flex": 3,"type": "button","style": "primary","color": "#800000","margin": "sm","height": "sm","action": {"type": "uri","label": "ORDER","uri": "line://app/1602687308-GXq4Vvk9/?type=text&text=price"}}]}]}}}
                                me.sendFlex(Pesan, data)
                                me.sendAudioWithURL(Pesan,e)
                            except Exception as error:
                                sendTextTemplate(Pesan, "error\n" + str(error))
                                ErrorX(error)
                        if InexBotsList.startswith("gname: "):
                          if Dari in Owner or Dari in meM:
                            if msg.toType == 2:
                                X = me.getGroup(Pesan)
                                sep = msg.text.split(" ")
                                X.name = msg.text.replace(sep[0] + " ","")
                                me.updateGroup(X)
                        if InexBotsList == "clear chat":
                          if Dari in Owner or Dari in meM:
                            me.removeAllMessages(Musuhku)
                            sendTextTemplate(Pesan, "Chat deleted")
                        if InexBotsList.startswith("bcast: "):
                          if Dari in Owner or Dari in meM:
                            sep = text.split(" ")
                            txt = text.replace(sep[0] + " ","")
                            groups = me.getGroupIdsJoined()
                            for group in groups:
                                sendTextTemplate1(group, "╭━━━╦BroadCast by Inex╦━━━╮\n{}".format(str(txt)))
                            sendTextTemplate(Pesan, "Berhasil broadcast ke {} group".format(str(len(groups))))
                        if InexBotsList == "gruplist":
                          if Dari in Owner or Dari in meM:
                            groups = me.getGroupIdsJoined()
                            ret_ = "╭━━━━══[ Group List ]══━━━━╮"
                            no = 0 + 1
                            for gid in groups:
                                group = me.getGroup(gid)
                                ret_ += "\n┣═ {}. {} \n┣═Member: {}".format(str(no), str(group.name), str(len(group.members)))
                                no += 1
                            ret_ += "\n╰━━━━━══[ Total {} Groups ]══━━━━━".format(str(len(groups)))
                            sendTextTemplate1(Pesan, str(ret_))
                        if InexBotsList == "friendlist":
                          if Dari in Owner or Dari in meM:
                            contactlist = me.getAllContactIds()
                            kontak = me.getContacts(contactlist)
                            num=1
                            msgs="╭━━══[ Friend List ]══━━╮"
                            for ids in kontak:
                                msgs+="\n[%i] %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n━━━══[ Friend Result ]══━━━\nTotal : %i" % len(kontak)
                            me.sendMessage(Pesan, msgs)
                        if InexBotsList == "blocklist":
                          if Dari in Owner or Dari in meM:
                            blockedlist = me.getBlockedContactIds()
                            kontak = me.getContacts(blockedlist)
                            num=1
                            msgs="╭━━━━══[ Friend Block ]══━━━━╮"
                            for ids in kontak:
                                msgs+="\n[%i] %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n ━━━━══[ Block Result ]══━━━━\nBlock Total : %i" % len(kontak)
                            sendTextTemplate1(Pesan, msgs)
                        if InexBotsList == "creator grup":
                          if Dari in Owner or Dari in meM:
                            sendTextTemplate(Pesan, "━═[Pembuat Grup]═━")
                            group = me.getGroup(Pesan)
                            GS = group.creator.mid
                            me.sendContact(Pesan, GS)
                        if InexBotsList == "memberlist":
                          if Dari in Owner or Dari in meM:
                            if Dari in meM:
                                if msg.toType == 2:
                                    group = me.getGroup(Pesan)
                                    ret_ = "╭━━━══[ Member List ]"
                                    no = 0 + 1
                                    for mem in group.members:
                                        ret_ += "\n┣═ {}. {}".format(str(no), str(mem.displayName))
                                        no += 1
                                    ret_ += "\n╰━━━══[ Total {} member]".format(str(len(group.members)))
                                    sendTextTemplate1(Pesan, str(ret_))
                        if InexBotsList == "pendinglist":
                          if Dari in Owner or Dari in meM:
                            if Dari in meM:
                                if msg.toType == 2:
                                    group = me.getGroup(Pesan)
                                    ret_ = "╭━━━══[ Pending List ]"
                                    no = 0 + 1
                                    if group.invitee is None or group.invitee == []:
                                        me.sendMessage(Pesan, "Tidak ada pendingan")
                                        return
                                    else:
                                        for pen in group.invitee:
                                            ret_ += "\n┣═ {}. {}".format(str(no), str(pen.displayName))
                                            no += 1
                                        ret_ += "\n╰━━━══[ Total {} tertunda]".format(str(len(group.invitee)))
                                        sendTextTemplate1(Pesan, str(ret_))
                        if InexBotsList == "ginfo":
                            if Dari in Owner or Dari in meM:
                                group = me.getGroup(Pesan)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "Closed"
                                    gTicket = "Qr tidak tersedia karna di tutup"
                                else:
                                    gQr = "Open"
                                    gTicket = "https://me.me/R/ti/g/{}".format(str(me.reissueGroupTicket(group.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(group.createdTime) / 1000)))
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                ret_ = "[ Group Info ]"
                                ret_ += "\nNama Group : {}".format(str(group.name))
                                ret_ += "\nWaktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\nID Group : {}".format(group.id)
                                ret_ += "\nPembuat : {}".format(str(gCreator))
                                ret_ += "\nJumlah Member : {}".format(str(len(group.members)))
                                ret_ += "\nJumlah Pending : {}".format(gPending)
                                ret_ += "\n═━━━Kode Qr/Link━━━═"
                                ret_ += "\nGroup Ticket : {}".format(gTicket)
                                ret_ += "\nGroup Qr : {}".format(gQr)
                                ret_ += "\n[ INEXBOT_TEAM]"
                                warna = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
                                warnanya = random.choice(warna)
                                data = {"type": "flex","altText": "Info grup","contents": {"type": "bubble","body": {"type": "box","layout": "horizontal","spacing": "md","contents": [{"type": "box","layout": "vertical","flex": 2,"contents": [{"type": "text","text": str(ret_),"size": "md","weight": "bold","wrap": True,"color": warnanya,"align": "center"},]}]},"styles": {"body": {"backgroundColor": "#000000"},"footer": {"backgroundColor": "#00FFFF"},"header": {"backgroundColor": "#00FFFF"}},"hero": {"type": "image","aspectRatio": "20:13","aspectMode": "cover","url": "https://obs.line-scdn.net/{}".format(group.pictureStatus),"size": "full","margin": "xl"},"footer": {"type": "box","layout": "vertical","contents": [{"type": "box","layout": "horizontal","contents": [{"type": "button","flex": 2,"style": "primary","color": "#006400","height": "sm","action": {"type": "uri","label": "OFFICIAL","uri": "https://line.me/R/ti/p/%40bvb1195k"}},{"flex": 3,"type": "button","style": "primary","color": "#800000","margin": "sm","height": "sm","action": {"type": "uri","label": "CREATOR","uri": "http://line.me/ti/p/~denjaka-inexx"}}]}]}}}
                                me.sendFlex(Pesan, data)
                        if InexBotsList == "gid":
                          if Dari in Owner or Dari in meM:
                            gid = me.getGroup(Pesan)
                            sendTextTemplate(Pesan,gid.id)
                        if InexBotsList == "gurl":
                          if Dari in Owner or Dari in meM:
                            if msg.toType == 2:
                                group = me.getGroup(Pesan)
                                if group.preventedJoinByTicket == False:
                                    ticket = me.reissueGroupTicket(Pesan)
                                    me.sendMessage(Pesan, "https://me.me/R/ti/g/{}".format(str(ticket)))
                                else:
                                    group.preventedJoinByTicket = False
                                    me.updateGroup(group)
                                    me.sendMessage(Pesan, "https://me.me/R/ti/g/{}".format(str(ticket)))
                        if InexBotsList == "open":
                          if Dari in Owner or Dari in meM:
                            if msg.toType == 2:
                                group = me.getGroup(Pesan)
                                if group.preventedJoinByTicket == False:
                                    sendTextTemplate(Pesan, "Sudah terbuka")
                                else:
                                    group.preventedJoinByTicket = False
                                    me.updateGroup(group)
                                    sendTextTemplate(Pesan, "Berhasil membuka Qr")
                        if InexBotsList == "close":
                          if Dari in Owner or Dari in meM:
                            if msg.toType == 2:
                                group = me.getGroup(Pesan)
                                if group.preventedJoinByTicket == True:
                                    sendTextTemplate(Pesan, "Sudah tertutup")
                                else:
                                    group.preventedJoinByTicket = True
                                    me.updateGroup(group)
                                    sendTextTemplate(Pesan, "Berhasil menutup Qr")
                        if InexBotsList == "autoadd on":
                          if Dari in Owner or Dari in meM:
                            InexBots["Add"] = True
                            sendTextTemplate(Pesan, "Auto add di aktifkan")
                        if InexBotsList == "autoadd off":
                          if Dari in Owner or Dari in meM:
                            InexBots["Add"] = False
                            sendTextTemplate(Pesan, "Auto add di nonaktifkan")
                        if InexBotsList == "join on":
                          if Dari in Owner or Dari in meM:
                            InexBots["Join"] = True
                            sendTextTemplate(Pesan, "Auto join di aktifkan")
                        if InexBotsList == "join off":
                          if Dari in Owner or Dari in meM:
                            InexBots["Join"] = False
                            sendTextTemplate(Pesan, "Auto join di nonaktifkan")
                        if InexBotsList == "read on":
                          if Dari in Owner or Dari in meM:
                            InexBots["Read"] = True
                            sendTextTemplate(Pesan, "Autoread on")
                        if InexBotsList == "read off":
                          if Dari in Owner or Dari in meM:
                            InexBots["Read"] = False
                            sendTextTemplate(Pesan, "Autoread off")
                        if InexBotsList == "unsend on":
                          if Dari in Owner or Dari in meM:
                            InexBots["Unsend"] = True
                            sendTextTemplate(Pesan, "Unsend di aktifkan")
                        if InexBotsList == "unsend off":
                          if Dari in Owner or Dari in meM:
                            InexBots["Unsend"] = False
                            sendTextTemplate(Pesan, "Unsend di nonaktifkan")
                        if InexBotsList == "shared on":
                          if Dari in Owner or Dari in meM:
                            InexBots["Shared"] = True
                            sendTextTemplate(Pesan, "Already on")
                        if InexBotsList == "shared off":
                          if Dari in Owner or Dari in meM:
                            InexBots["Shared"] = False
                            sendTextTemplate(Pesan, "Already off")
                        if InexBotsList == "r1 on":
                          if Dari in Owner or Dari in meM:
                            InexBots["Respon"] = True
                            sendTextTemplate(Pesan, "Respon Already on")
                        if InexBotsList == "r1 off":
                          if Dari in Owner or Dari in meM:
                            InexBots["Respon"] = False
                            sendTextTemplate(Pesan, "Respon Already off")
                        if InexBotsList == "contact on":
                          if Dari in Owner or Dari in meM:
                            InexBots["contact"] = True
                            sendTextTemplate(Pesan, "detect contact Already on")
                        if InexBotsList == "contact off":
                          if Dari in Owner or Dari in meM:
                            InexBots["contact"] = False
                            sendTextTemplate(Pesan, "detect contact Already off")
                        if InexBotsList == "x on":
                          if Dari in Owner or Dari in meM:
                                try:
                                    del Sid['Red'][Pesan]
                                    del Sid['Reason'][Pesan]
                                    del Sid['Tar'][Pesan]
                                except:
                                    pass
                                Sid['Red'][Pesan] = Keluarga
                                Sid['Reason'][Pesan] = ""
                                Sid['Tar'][Pesan]=True
                                me.sendMessage(Pesan, "inex")
                        if InexBotsList == "x off":
                          if Dari in Owner or Dari in meM:
                            if Pesan in Sid['Red']:
                                Sid['Tar'][Pesan]=False
                                sendTextTemplate(Pesan, "Daftar yang terlihat\n"+Sid['Reason'][Pesan])
                                sendTextTemplate(Pesan, "Already off")
                            else:
                                sendTextTemplate(Pesan, "aktifkan dulu coy sidernya")
                        if InexBotsList == "sticker on":
                         if Dari in Owner or Dari in Import_Server or Dari in meM:
                            InexBots["sticker"] = True
                            sendTextTemplate(Pesan,"Deteksi sticker diaktifkan")

                        if InexBotsList == "sticker off":
                         if Dari in Owner or Dari in Import_Server or Dari in meM:
                            InexBots["sticker"] = False
                            sendTextTemplate(Pesan,"Deteksi sticker dinonaktifkan")

                        if InexBotsList == "stickerbig on":
                         if Dari in Owner or Dari in Import_Server or Dari in meM:
                            InexBots["stickerbig"] = True
                            sendTextTemplate(Pesan,"Deteksi stickerbig diaktifkan")

                        if InexBotsList == "stickerbig off":
                         if Dari in Owner or Dari in Import_Server or Dari in meM:
                            InexBots["stickerbig"] = False
                            sendTextTemplate(Pesan,"Deteksi stickerbig dinonaktifkan")
                        if InexBotsList == "inex":
                         if Dari in Owner or Dari in Import_Server or Dari in meM:
                          Group = me.getGroup(Pesan)
                          Rmem = [contact.mid for contact in Group.members]
                          Dmem = len(Rmem)//20
                          try:                          	
                              for mentionMembers in range(Dmem+1):
                                  no = 0
                                  ret_ = "╭━─────────────────━╮\n│ MEMBER GORUP\n╰━─────────────────━╯\n╭━─────────────────━╮"
                                  dataMid = []
                                  for dataMention in Group.members[mentionMembers*20 : (mentionMembers+1)*20]:
                                      dataMid.append(dataMention.mid)
                                      no += 1
                                      ret_ += "\n│ @! ".format(str(no))
                                  ret_ += "\n╰━─────────────────━╯".format(str(len(dataMid)))
                                  sendMeention(Pesan, ret_, dataMid)
                          except Exception as error:
                              return False
                        if InexBotsList == "sett on":
                          if Dari in Owner or Dari in meM:
                            try:
                                InexBots["Shared"] = True
                                InexBots["Add"] = True
                                InexBots["Join"] = True
                                InexBots["Read"] = True
                                InexBots["Unsend"] = True
                            except:sendTextTemplate(Pesan,"SETTING ALL IN ONLINE")
                        if InexBotsList == "sett off":
                          if Dari in Owner or Dari in meM:
                            try:
                                InexBots["Shared"] = False
                                InexBots["Add"] = False
                                InexBots["Join"] = False
                                InexBots["Read"] = False
                                InexBots["Unsend"] = False
                            except:sendTextTemplate(Pesan,"SETTING ALL IN OFFLINE")
                        if InexBotsList == "mybot" or InexBotsList == "my bot":
                          if Dari in Owner or Dari in meM:
                              me.sendContact(Pesan,Antijs)
                        if InexBotsList == "banlist":
                          if Dari in Owner or Dari in meM:
                            if InexBots["blacklist"] == {}:
                                sendTextTemplate(Pesan,"Tidak ada blacklist")
                            else:
                                sendTextTemplate(Pesan,"⪨⪩─┅❇͜͡[BLACKLIST]࿐")
                                h = ""
                                for i in InexBots["blacklist"]:
                                  h = me.getContact(i)
                                  me.sendContact(Pesan,i)
                        if InexBotsList == "clearban" or InexBotsList == "Clearban":
                          if Dari in Owner or Dari in Import_Server or Dari in meM:
                            sendTextTemplate(Pesan, "Berhasil menghapus {} user blacklist".format(str(len(InexBots["blacklist"]))))
                            InexBots["blacklist"] = {}
                        if InexBotsList == "js in" or InexBotsList == "ajs in":
                          if Dari in Owner or Dari in meM:
                            gg = me.getGroup(Pesan)
                            gg.preventedJoinByTicket = False
                            me.updateGroup(gg)
                            grup = me.reissueGroupTicket(Pesan)
                            jss.acceptGroupInvitationByTicket(Pesan, grup)
                            gg.preventedJoinByTicket = True
                            jss.updateGroup(gg)
                        if InexBotsList == "js out" or InexBotsList == "ajs out":
                          if Dari in Owner or Dari in meM:
                            gg = me.getGroup(Pesan)
                            jss.leaveGroup(Pesan)
                        if InexBotsList == "stay" or InexBotsList == ".":
                          if Dari in Owner or Dari in meM:
                              try:
                                  ginfo = me.getGroup(Pesan)
                                  jss.leaveGroup(Pesan)
                                  me.inviteIntoGroup(Pesan, [Antijs])
                              except:
                                  try:
                                      ginfo = me.getGroup(Pesan)
                                      me.inviteIntoGroup(Pesan, [Antijs])
                                  except:
                                      pass
                        if InexBotsList == "prolist" or InexBotsList == "protectlist":
                          if Dari in Owner or Dari in meM:
                            ma = ""
                            mb = ""
                            mc = ""
                            md = ""
                            mi = ""
                            mf = ""
                            mg = ""
                            a = 0
                            b = 0
                            c = 0
                            d = 0
                            i = 0
                            f = 0
                            g = 0
                            gid = pro["Pintu"]
                            for group in gid:
                                a = a + 1
                                end = '\n'
                                ma += str(a) + ". " +me.getGroup(group).name + "\n"
                            gid = pro["Pembunuh"]
                            for group in gid:
                                b = b + 1
                                end = '\n'
                                mb += str(b) + ". " +me.getGroup(group).name + "\n"
                            gid = pro["Maling"]
                            for group in gid:
                                c = c + 1
                                end = '\n'
                                mc += str(c) + ". " +me.getGroup(group).name + "\n"
                            gid = pro["Penghasut"]
                            for group in gid:
                                d = d + 1
                                end = '\n'
                                md += str(d) + ". " +me.getGroup(group).name + "\n"
                            gid = pro["Pencuri"]
                            for group in gid:
                                i = i + 1
                                end = '\n'
                                mi += str(i) + ". " +me.getGroup(group).name + "\n"
                            gid = pro["Penyelamat"]
                            for group in gid:
                                f = f + 1
                                end = '\n'
                                mf += str(f) + ". " +me.getGroup(group).name + "\n"
                            gid = pro["Kuntilanak"]
                            for group in gid:
                                g = g + 1
                                end = '\n'
                                mg += str(g) + ". " +me.getGroup(group).name + "\n"
                            sendTextTemplate1(Pesan,"☠•➤Protection\n\n☠•➤PROTECT URL :\n"+ma+"\n☠•➤PROTECT KICK :\n"+mb+"\n☠•➤PROTECT INVITE :\n"+mc+"\n☠•➤PROTECT JOIN :\n"+md+"\n☠•➤PROTECT CANCEL:\n"+mi+"\n☠•➤PROTECT ANTIJS:\n"+mf+"\n☠•➤PROTECT GHOST:\n"+mg+"\nTotal「%s」Grup yg dijaga" %(str(len(pro["Pintu"])+len(pro["Pembunuh"])+len(pro["Maling"])+len(pro["Penghasut"])+len(pro["Pencuri"])+len(pro["Penyelamat"])+len(pro["Kuntilanak"]))))
                        if InexBotsList == "," or InexBotsList == "pulang":
                          if Dari in Owner or Dari in meM:
                            try:
                                ginfo = me.getGroup(Pesan)
                                jss.leaveGroup(Pesan)
                            except:
                                try:
                                    ginfo = me.getGroup(Pesan)
                                    jss.acceptGroupInvitation(Pesan)
                                    jss.leaveGroup(Pesan)
                                except:
                                    ginfo = me.getGroup(Pesan)
                                    me.cancelGroupInvitation(Pesan, [Antijs])
                        if InexBotsList == "cek" or InexBotsList == "skill":
                          if Dari in Owner or Dari in Import_Server or Dari in meM:
                            try:me.inviteIntoGroup(Pesan, ["u69215ed58462ef80fd637a0c7207f230"]);has = "OK"
                            except:has = "NOT"
                            try:me.kickoutFromGroup(Pesan, ["u69215ed58462ef80fd637a0c7207f230"]);has1 = "OK"
                            except:has1 = "NOT"
                            try:me.cancelGroupInvitation(Pesan, ["u69215ed58462ef80fd637a0c7207f230"]);has2 = "OK"
                            except:has2 = "NOT"
                            if has == "OK":sil = "🅱🅰🅳🅰🅽 🆂🅴🅷🅰🆃"
                            else:sil = "🆃🅾🅻🅾🅽🅶 🅰🅺🆄"
                            if has1 == "OK":sil1 = "https://2.bp.blogspot.com/-4Yr8ckT8tgs/U_ZiZFWPewI/AAAAAAAACDo/GUcjJOT1lrE/s1600/senamsehat.gif"
                            else:sil1 = "https://1.bp.blogspot.com/-GhAAjmcghVc/WDQHbLNi7bI/AAAAAAAAAGg/-wIouq5Hu3EEnwdx2jr-DFN9r0Vn5f3IgCLcB/s1600/Infectieziekten%2B%25281%2529.gif"
                            if has2 == "OK":sil2 = "https://www.isostar.com/share/sport/img_anime_rub/1.gif"
                            else:sil2 = "https://www.gambaranimasi.org/data/media/511/animasi-bergerak-kubur-0025.gif"
                            data = {"type": "flex","altText": "Cek kesehatan","contents": {"styles": {"body": {"backgroundColor": "#000000"},"footer": {"backgroundColor": "#000000"}},"type": "bubble","hero": {"type": "image","url": "{}".format(sil1),"size": "full","aspectRatio": "20:13","aspectMode": "cover",},"body": {"contents": [{"contents": [{"url": "{}".format(sil2),"type": "image"},],"type": "box","spacing": "sm","layout": "vertical"},{"type": "separator","color": "#ECF0F1"},{"contents": [{"text": "{}".format(sil),"size": "md","align": "center","wrap": True,"weight": "regular","type": "text"}],"type": "box","layout": "baseline"}],"type": "box","layout": "vertical"}}}
                            me.sendFlex(Pesan, data)
                        if InexBotsList == "cek js" or InexBotsList == "skill js":
                          if Dari in Owner or Dari in meM:
                            try:jss.inviteIntoGroup(Pesan, ["u69215ed58462ef80fd637a0c7207f230"]);has = "OK"
                            except:has = "NOT"
                            try:jss.kickoutFromGroup(Pesan, ["u69215ed58462ef80fd637a0c7207f230"]);has1 = "OK"
                            except:has1 = "NOT"
                            if has == "OK":sil = "ś̵̢̨͕̋̽͛̇̿̚e̷̗͍̩͚͚̗͔̾ḩ̴̛̞̬̝̟̘̭̾̊͑́͛̒̓̈́͒ͅȃ̴̞͇̗̭̪͖̦̜̫̞͗͑́̈́̀͘t̶̮͕͉̂̉̐̀́͜"
                            else:sil = "ֆǟӄɨȶ"
                            if has1 == "OK":sil1 = "ś̵̢̨͕̋̽͛̇̿̚e̷̗͍̩͚͚̗͔̾ḩ̴̛̞̬̝̟̘̭̾̊͑́͛̒̓̈́͒ͅȃ̴̞͇̗̭̪͖̦̜̫̞͗͑́̈́̀͘t̶̮͕͉̂̉̐̀́͜"
                            else:sil1 = "ֆǟӄɨȶ"
                            jss.sendMessage(Pesan, "🄺🄸🄲🄺 : {} \n🄸🄽🅅🄸🅃🄴 : {}".format(sil1,sil))
                        if InexBotsList.startswith("sory "):
                          if Dari in Owner or Dari in meM:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                              names = re.findall(r'@(\w+)', text)
                              mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                              mentionees = mention['MENTIONEES']
                              lists = []
                              for mention in mentionees:
                                  if mention["M"] not in lists:
                                      lists.append(mention["M"])
                              for ls in lists:
                                  try:
                                      me.kickoutFromGroup(Pesan,[ls])
                                      print (Pesan,[ls])
                                  except:
                                      pass
                        if ("Maaf " in InexBotsList):
                          if Dari in Owner or Dari in meM:
                            key = eval(msg.contentMetadata["MENTION"])
                            key["MENTIONEES"][0]["M"]
                            targets = []
                            for x in key["MENTIONEES"]:
                                 targets.append(x["M"])
                            for target in targets:
                                if target not in Bots:
                                    try:
                                        Gz = me.getGroup(Pesan)
                                        Gz.preventedJoinByTicket = False
                                        me.updateGroup(Gz)
                                        invsend = 0
                                        Ticket = me.reissueGroupTicket(Pesan)
                                        jss.acceptGroupInvitationByTicket(Pesan,Ticket)
                                        jss.kickoutFromGroup(Pesan, [target])
                                        jss.leaveGroup(Pesan)
                                        X = Denjaka.getGroup(Pesan)
                                        X.preventedJoinByTicket = True
                                        me.updateGroup(X)
                                    except:
                                        pass
                        if InexBotsList.startswith("myname: "):
                          if Dari in Owner or Dari in meM:
                              separate = InexBotsList.split(" ")
                              string = InexBotsList.replace(separate[0] + " ","")
                              if len(string) <= 10000000000:
                                  profile = me.getProfile()
                                  profile.displayName = string
                                  me.updateProfile(profile)
                                  sendTextTemplate(Pesan,"Nama diganti jadi " + string + "")
                        if InexBotsList.startswith("jsname: "):
                          if Dari in Owner or Dari in meM:
                              separate = InexBotsList.split(" ")
                              string = InexBotsList.replace(separate[0] + " ","")
                              if len(string) <= 10000000000:
                                  profile = jss.getProfile()
                                  profile.displayName = string
                                  jss.updateProfile(profile)
                                  jss.sendMessage(Pesan,"Nama diganti jadi " + string + "")
                        if InexBotsList == "bot info":
                          if Dari in Owner or Dari in meM:
                            RunTheRun(Pesan, Dari, "[_______[RESULT]______]\n")
                            """
                            BOT WAR
                            VERSION : INEXBOTS
                            REVISION : VPS
                            """
        if rank.type == 25:
          """
          BOT WAR
          VERSION : INEXBOTS
          REVISION : VPS
          """
          if InexBots["bot"] == True:
            war = rank.message
            Denwar = war.text
            Keluarga = war.id
            Pesan = war.to
            Dari = war._from
            if Denwar == "autojoin on":
              if Dari in Owner or Dari in meM:
                  InexBots["autoJoin"] = True
                  sendTextTemplate(Pesan,"join d aktifkan.....")
            if Denwar == "autojoin off":
              if Dari in Owner or Dari in meM:
                  InexBots["autoJoin"] = False
                  sendTextTemplate(Pesan,"join d non aktifkan.....")
            if Denwar == "pm on" or Denwar == "Pm on":
              if Dari in Owner or Dari in meM:
                  InexBots["arespon"] = True
                  sendTextTemplate(Pesan,"Respon pm d aktifkan.....")
            if Denwar == "pm off" or Denwar == "Pm off":
              if Dari in Owner or Dari in meM:
                  InexBots["arespon"] = False
                  sendTextTemplate(Pesan,"Respon pm d nonaktifkan.....")
            if Denwar == "autoleave on" or Denwar == "Autoleave on":
              if Dari in Owner or Dari in meM:
                  InexBots["autoLeave"] = True
                  sendTextTemplate(Pesan,"Leave d aktifkan.....")
            if Denwar == "autoleave off" or Denwar == "Autoleave off":
              if Dari in Owner or Dari in meM:
                  InexBots["autoLeave"] = False
                  sendTextTemplate(Pesan,"Leave d non aktifkan.....")
            if Denwar == "admin on" or Denwar == "Admin on":
              if Dari in Owner or Dari in meM:
                  InexBots["addOwner"] = True
                  sendTextTemplate(Pesan,"Kirim kontaknya...")
            if Denwar == "admin off" or Denwar == "Admin off":
              if Dari in Owner or Dari in meM:
                  InexBots["dellOwner"] = True
                  sendTextTemplate(Pesan,"Kirim kontaknya...")
            if Denwar == "my pict":
              if Dari in Owner or Dari in meM:
                  InexBots["Xfoto"][meM] = True
                  sendTextTemplate(Pesan,"Kirim fotonya.....")
            if Denwar == "bot pict" or Denwar == "Botpict":
              if Dari in Owner or Dari in meM:
                  InexBots["Xfoto"][Antijs] = True
                  sendTextTemplate(Pesan,"Kirim fotonya.....")
            if Denwar == "adminlist" or Denwar == "Adminlist":
              if Dari in Owner or Dari in meM:
                  ma = ""
                  a = 0
                  for m_id in Owner:
                      a = a + 1
                      end = '\n'
                      ma += str(a) + ". " +me.getContact(m_id).displayName + "\n"
                  sendTextTemplate1(Pesan,"☠•RANGGERLIST\n\n☠•Creator InexBots :\n"+ma+"\nTotal「%s」 InexBots" %(str(len(meM)+len(Owner))))
            if 'Welcome ' in msg.text:
              if Dari in Owner or Dari in meM:
                  spl = Denwar.replace('Welcome ','')
                  if spl == 'on':
                      if Pesan in pro["Pintu"]:
                           msgs = ""
                      else:
                           Welcome.append(Pesan)
                           ginfo = me.getGroup(Pesan)
                           msgs = "Welcome Msg diaktifkan\nDi Group : " +str(ginfo.name)
                      sendTextTemplate(Pesan, "「Diaktifkan」\n" + msgs)
                  if spl == 'off':
                        if Pesan in Welcome:
                             Welcome.remove(Pesan)
                             ginfo = me.getGroup(Pesan)
                             msgs = "Welcome Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                        else:
                             msgs = "Welcome Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                        sendTextTemplate(Pesan, "「Dinonaktifkan」\n" + msgs)
            if 'Pro ' in Denwar:
              if Dari in Owner or Dari in meM:
                  spl = Denwar.replace('Pro ','')
                  if spl == 'on':
                      if Pesan in pro["Pintu"]:
                           msgs = ""
                      else:
                           pro["Pintu"].append(Pesan)
                      if Pesan in pro["Pembunuh"]:
                          msgs = ""
                      else:
                          pro["Pembunuh"].append(Pesan)
                      if Pesan in pro["Maling"]:
                          msgs = ""
                      else:
                          pro["Maling"].append(Pesan)
                      if Pesan in pro["Penghasut"]:
                          msgs = ""
                      else:
                          pro["Penghasut"].append(Pesan)
                      if Pesan in pro["Pencuri"]:
                          msgs = ""
                      else:
                          pro["Pencuri"].append(Pesan)
                      if Pesan in pro["Kuntilanak"]:
                          msgs = ""
                      else:
                          pro["Kuntilanak"].append(Pesan)
                      if Pesan in pro["Penyelamat"]:
                          ginfo = me.getGroup(Pesan)
                          msgs = "Semua protect sudah on\nDi Group : " +str(ginfo.name)
                      else:
                          pro["Penyelamat"].append(Pesan)
                          ginfo = me.getGroup(Pesan)
                          msgs = "Berhasil mengaktifkan semua protect\nDi Group : " +str(ginfo.name)
                      sendTextTemplate(Pesan, "「Diaktifkan」\n" + msgs)
                  if spl == 'off':
                        if Pesan in pro["Pintu"]:
                             pro["Pintu"].remove(Pesan)
                        else:
                             msgs = ""
                        if Pesan in pro["Pembunuh"]:
                             pro["Pembunuh"].remove(Pesan)
                        else:
                             msgs = ""
                        if Pesan in pro["Maling"]:
                             pro["Maling"].remove(Pesan)
                        else:
                             msgs = ""
                        if Pesan in pro["Penghasut"]:
                             pro["Penghasut"].remove(Pesan)
                        else:
                             msgs = ""
                        if Pesan in pro["Pencuri"]:
                             pro["Pencuri"].remove(Pesan)
                        else:
                             msgs = ""
                        if Pesan in pro["Kuntilanak"]:
                             pro["Kuntilanak"].remove(Pesan)
                        else:
                             msgs = ""
                        if Pesan in pro["Penyelamat"]:
                             pro["Penyelamat"].remove(Pesan)
                             ginfo = me.getGroup(Pesan)
                             msgs = "Berhasil menonaktifkan semua protect\nDi Group : " +str(ginfo.name)
                        else:
                             ginfo = me.getGroup(Pesan)
                             msgs = "Semua protect sudah off\nDi Group : " +str(ginfo.name)
                        sendTextTemplate(Pesan, "「Dinonaktifkan」\n" + msgs)
            if ("Adminadd " in Denwar):
              if Dari in Owner or Dari in meM:
                 key = eval(msg.contentMetadata["MENTION"])
                 key["MENTIONEES"][0]["M"]
                 targets = []
                 for x in key["MENTIONEES"]:
                      targets.append(x["M"])
                 for target in targets:
                     if target not in InexWars:
                         try:
                             Owner.append(target)
                             sendTextTemplate(Pesan,"Berhasil menambahkan admin")
                         except:
                             pass
            if ("Admindell " in Denwar):
              if Dari in Owner or Dari in meM:
                 key = eval(msg.contentMetadata["MENTION"])
                 key["MENTIONEES"][0]["M"]
                 targets = []
                 for x in key["MENTIONEES"]:
                      targets.append(x["M"])
                 for target in targets:
                     if target not in InexWars:
                         try:
                             Owner.remove(target)
                             sendTextTemplate(Pesan,"Berhasil menghapus admin")
                         except:
                             pass

        if rank.type == 26:
          if InexBots["bot"] == True:
            msg = rank.message
            text = msg.text
            Id = msg.id
            R = msg.to
            D = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = D
                elif msg.toType == 2:
                    to = R
                if InexBots["Read"] == True:
                    me.sendChatChecked(R, Id)
                if msg.contentType == 0:
                    if text is None:
                        return
                if msg.contentType == 16:
                        if InexBots["Shared"] == True:
                            try:
                                ret_ = "╔══[ Details Post ]"
                                if msg.contentMetadata["serviceType"] == "GB":
                                    contact = me.getContact(D)
                                    auth = "\n╠ Penulis : {}".format(str(contact.displayName))
                                else:
                                    auth = "\n╠ Penulis : {}".format(str(msg.contentMetadata["serviceName"]))
                                purl = "\n╠ URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://me.me/R/"))
                                ret_ += auth
                                ret_ += purl
                                if "mediaOid" in msg.contentMetadata:
                                    object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                    if msg.contentMetadata["mediaType"] == "V":
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            murl = "\n╠ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                            murl = "\n╠ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                        ret_ += murl
                                    else:
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                    ret_ += ourl
                                if "stickerId" in msg.contentMetadata:
                                    stck = "\n╠ Stiker : https://me.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                    ret_ += stck
                                if "text" in msg.contentMetadata:
                                    text = "\n╠ Tulisan : {}".format(str(msg.contentMetadata["text"]))
                                    ret_ += text
                                ret_ += "\n╚══[ Finish ]"
                                sendTextTemplate1(R, str(ret_))
                            except Exception as error:
                                traceback.print_tb(error.__traceback__)
                if msg.contentType == 0 and D not in meM and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mid in mention["M"]:
                                if InexBots["Respon"] == True:
                                    contact = me.getContact(D)
                                    cover = me.getProfileCoverURL(D)
                                    path = "http://dl.profile.line.naver.jp/"+ contact.pictureStatus
                                    try:
                                      poto = "https://os.line.naver.jp/os/p/{}".format(D)
                                    except:
                                      poto = "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQcNdUbC8kEeVWqgR9qMX66lQ_hQPM8ScNY30x4nqpYaKY2jt02"
                                    data = {"type": "flex","altText": "TOOOOLLLOOOOOOOOONGGG...","contents": {"type": "bubble","body": {"type": "box","layout": "horizontal","spacing": "md","contents":[{"type": "box","layout": "vertical","flex": 2,"contents":[{"type": "text","text": "{} \n".format(me.getContact(D).displayName)+str(respontags["Auto_text"]),"size": "sm","weight": "bold","wrap": True,"color": "#40ff00"}]}]},"styles": {"body": {"backgroundColor": "#000000"},"footer":{"backgroundColor": "#03f5f1"},"header": {"backgroundColor": "#03f5f1"}},"hero": {"type": "image","aspectRatio": "20:13","aspectMode": "cover","url": poto,"size": "full","margin": "xl"},"footer": {"type": "box","layout": "vertical","contents": [{"type": "box","layout": "horizontal","contents": [{"type": "button","flex": 2,"style": "primary","color": "#ff0a3b","height": "sm","action": {"type": "uri","label": "OFFICIAL","uri": "https://line.me/R/ti/p/%40bvb1195k"}},{"flex": 3,"type": "button","style": "primary","color": "#310dff","margin": "sm","height": "sm","action": {"type": "uri","label": "CREATOR","uri": "http://line.me/ti/p/~denjaka_inex"}}]}]}}}
                                    me.sendFlex(R, data)
                                break
                if msg.contentType == 0 and D not in meM and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if meM in mention["M"]:
                                if InexBots["arespon"] == True:
                                    contact = me.getContact(D)
                                    sendMention(D, "@! ᴊᴀɴɢᴀɴ ᴛᴀɢ ᴅ ɢʀᴏᴜᴘ ᴋᴀᴋ ʙᴀʜᴀʏᴀ...", [D])
                                    warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
                                    warnanya1 = random.choice(warna1)
                                    data = {"type":"flex","altText":"{} Cieeeee... Kang tag".format(me.getContact(D).displayName),"contents": {"type": "bubble","styles": {"header":{"backgroundColor": "#0000FF",},"body": {"backgroundColor": "#000000","separator": True,"separatorColor": "#ffffff"},"footer": {"backgroundColor": "#000080","separator": True}},"header":{"type": "box","layout": "horizontal","contents": [{"type": "text","text": "{}".format(me.getContact(D).displayName),"weight": "bold","color": warnanya1,"size": "md"}]},"hero": {"type": "image","url": "https://obs.line-scdn.net/{}".format(me.getContact(D).pictureStatus),"size": "full","aspectRatio": "20:13","aspectMode": "cover","action":{"type": "uri","uri": "https://line.me/ti/p/~denjaka_inex"}},"type": "bubble","body": {"type": "box","layout": "horizontal","contents": [{"type": "text","text": "{} \n".format(me.getContact(D).displayName)+str(respontags["Auto_pM"]),"wrap": True,"color": warnanya1,"align": "center"}]},"footer": {"type": "box","layout": "vertical","spacing": "sm","contents": [{"type": "button","style": "primary","color": warnanya1,"height": "sm","action": {"type": "uri","label": "ADD MY LINE","uri": "https://line.me/ti/p/"+me.getUserTicket().id}},{"type": "spacer","size": "sm",}],"flex": 0}}}
                                    me.sendFlex(D, data)
                                    break
        if rank.type == 25 or rank.type == 26:
            msg = rank.message
            text = msg.text
            Id = msg.id
            R = msg.to
            D = msg._from            
            if msg.contentType == 13:
                 if InexBots["contact"] == True:
                    msg.contentType = 0
                    me.sendMessage(R,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = me.getContact(msg.contentMetadata["mid"])
                        path = me.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        sendTextTemplate(R,"☠•➤Nama : " + msg.contentMetadata["displayName"] + "\n☠•➤MID : " + msg.contentMetadata["mid"] + "\n☠•➤Status Msg : " + contact.statusMessage + "\n☠•➤Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        me.sendImageWithURL(R, image)
            if msg.contentType == 7:
                 if InexBots["sticker"] == True:
                    msg.contentType = 0
                    sendTextTemplate(R,"「Cek ID Sticker」\n☠•➤STKID : " + msg.contentMetadata["STKID"] + "\n☠•➤STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n☠•➤STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
            if msg.contentType == 7:
                 if InexBots["stickerbig"] == True:
                    msg.contentType = 0
                    masuk = me.getContact(D)
                    nama = me.getContact(D).displayName
                    stk_id = msg.contentMetadata["STKID"]
                    stc = "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker.png".format(stk_id)
                    data = {"type": "template","altText": "{} sent a sticker".format(nama),"template": {"type": "image_carousel","columns": [{"imageUrl": "{}".format(stc),"size": "full","action": {"type": "uri","uri": "http://line.me/ti/p/~denjaka_inex"}}]}}
                    me.sendFlex(R, data)
            if msg.contentType == 1:
                    if meM in InexBots["Xfoto"]:
                         path = me.downloadObjectMsg(R)
                         del InexBots["Xfoto"][meM]
                         me.updateProfilePicture(path)
                         sendTextTemplate(R,"Foto berhasil dirubah")
            if msg.contentType == 1:
                    if Antijs in InexBots["Xfoto"]:
                         path = jss.downloadObjectMsg(R)
                         del InexBots["Xfoto"][Antijs]
                         jss.updateProfilePicture(path)
                         jss.sendMessage(R,"Foto berhasil dirubah")
        if rank.type == 13:
            print ("NOTIFIED MEMBER OR SELF JOIN GROUP")
            Gr = Rumahku
            if InexBots["Join"] == True:
                me.acceptGroupInvitation(Gr)
            else:
                pass
            if InexBots["addOwner"] == True:
              if msg.contentMetadata["mid"] in Owner:
                  sendTextTemplate(R,"Contact itu sudah jadi admin")
                  InexBots["addOwner"] = True
              else:
                  Owner.append(msg.contentMetadata["mid"])
                  InexBots["addOwner"] = True
                  sendTextTemplate(R,"Berhasil menambahkan ke admin")
            if InexBots["dellOwner"] == True:
              if msg.contentMetadata["mid"] in Owner:
                  Owner.remove(msg.contentMetadata["mid"])
                  sendTextTemplate(R,"Berhasil menghapus dari admin")
              else:
                  InexBots["dellOwner"] = True
                  sendTextTemplate(R,"Contact itu bukan admin")
        if rank.type == 5:
            print ("NOTIFIED ADD CONTACT SELF")
            if InexBots["Add"] == True:
              if Musuhku not in InexWar and Musuhku not in Owner and Musuhku not in meM:
                me.findAndAddContactsByMid(Rumahku)
                if (respontags["message"] in [" "," ","\n",None]):
                    pass
                else:
                    me.sendMessage(Rumahku, respontags["message"])
                    me.sendFlex(Rumahku, plate["pricelist"])
        if rank.type == 15:
            print ("NOTIFIED CONTACT MEMBER LEAVE TO GROUP")
            if Rumahku in Welcome:
                ginfo = me.getGroup(Rumahku)
                Contact = me.getContact(Musuhku).picturePath
                data = {"type": "flex","altText": "kickall","contents": {"type": "bubble","styles": {"header": {"backgroundColor": "#000080",},"body": {"backgroundColor": "#0000FF","separator": True,"separatorColor": "#ffffff"},"footer": {"backgroundColor": "#000080","separator": True}},"header": {"type": "box","layout": "horizontal","contents": [{"type": "text","text": "{} LEAVE".format(me.getContact(Musuhku).displayName),"weight": "bold","color": "#FF0000","size": "xxl"}]},"hero": {"type": "image","url": "https://obs.line-scdn.net/{}".format(me.getContact(Musuhku).pictureStatus),"size": "full","aspectRatio": "20:13","aspectMode": "cover","action": {"type": "uri","uri": "https://line.me/ti/p/~denjaka-inexx"}},"type": "bubble","body": {"type": "box","layout": "horizontal","contents": [{"type": "text","text": "Selamat jalan,,, semoga d luar gak kdinginan","wrap": True,"color": "#00FF00","align": "center"}]},"footer": {"type": "box","layout": "vertical","spacing": "sm","contents": [{"type": "button","style": "primary","color": "#00FF00","height": "sm","action": {"type": "uri","label": "ADD MY LINE","uri": "https://line.me/ti/p/"+me.getUserTicket().id}},{"type": "spacer","size": "sm",}],"flex": 0}}}
                me.sendFlex(Rumahku, data)
        if rank.type == 17:
            print ("NOTIFIED CONTACT MEMBER JOIN TO GROUP")
            if Rumahku in Welcome:
                ginfo = me.getGroup(Rumahku)
                Contact = me.getContact(Musuhku)
                data = {"type": "flex","altText": "JANGAN KABUR DARI GRUP KAK","contents": {"type": "bubble","styles": {"header": {"backgroundColor": "#000080",},"body": {"backgroundColor": "#0000FF","separator": True,"separatorColor": "#ffffff"},"footer": {"backgroundColor": "#000080","separator": True}},"header": {"type": "box","layout": "horizontal","contents": [{"type": "text","text": "{} WELCOME".format(me.getContact(Musuhku).displayName),"weight": "bold","color": "#FF0000","size": "xxl"}]},"hero": {"type": "image","url": "https://obs.line-scdn.net/{}".format(me.getContact(Musuhku).pictureStatus),"size": "full","aspectRatio": "20:13","aspectMode": "cover","action": {"type": "uri","uri": "https://line.me/ti/p/~denjaka-inexx"}},"type": "bubble","body": {"type": "box","layout": "horizontal","contents": [{"type": "text","text": "Selamat bergabung,,, semoga betah kak","wrap": True,"color": "#00FF00","align": "center"}]},"footer": {"type": "box","layout": "vertical","spacing": "sm","contents": [{"type": "button","style": "primary","color": "#00FF00","height": "sm","action": {"type": "uri","label": "ADD MY LINE","uri": "https://line.me/ti/p/"+me.getUserTicket().id}},{"type": "spacer","size": "sm",}],"flex": 0}}}
                me.sendFlex(Rumahku, data)
        if rank.type == 65:
            print ("UNSEND MESSAGE UNSENDER FROM MY SELF")
            if InexBots["Unsend"] == True:
                Geting = Rumahku
                Text_in_Destroy = Musuhku
                if Text_in_Destroy in msg_dict:
                    Timer = time.time()
                    Target_Text = me.getContact(msg_dict[Text_in_Destroy]["from"])
                    if "text" in msg_dict[Text_in_Destroy]:
                        StartTimer = Timer - msg_dict[Text_in_Destroy]["waktu"]
                        StartTimer = format_timespan(StartTimer)
                        rat_ = "Timer unsend: {} WIB".format(StartTimer)
                        rat_ += "Text Unsend\n{}".format(msg_dict[Text_in_Destroy]["text"])
                        sendMention(Geting, Target_Text.mid, "Sorry\nMy Resend your Message\n\n", str(rat_))
                        del msg_dict[Text_in_Destroy]
                else:
                    me.sendMessage(Geting,"Detected Unsend")
        if rank.type == 55:
            Gr = Rumahku
            try:
                if Sid['Tar'][Gr]==True:
                        if Gr in Sid['Red']:
                            Name = me.getContact(Musuhku).displayName
                            Np = me.getContact(Musuhku).pictureStatus
                            if Name in Sid['Reason'][Gr]:
                                pass
                            else:
                                Sid['Reason'][Gr] += "\n||[ " + Name + " ]||"
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        data = {"type": "flex","altText": "menghapus anda dari grup","contents": {"type": "bubble","body": {"type": "box","layout": "horizontal","spacing": "md","contents": [{"type": "box","layout": "vertical","flex": 2,"contents": [{"type": "text","text": "{} Ngintip terus colok matane..".format(Name),"size": "md","weight": "bold","wrap": True,"color": "#40E0D0","align": "center"},]}]},"styles": {"body": {"backgroundColor": "#000000"},"footer": {"backgroundColor": "#00008B"},"header": {"backgroundColor": "#00008B"}},"hero": {"type": "image","aspectRatio": "20:13","aspectMode": "cover","url": "https://obs.line-scdn.net/{}".format(me.getContact(Musuhku).pictureStatus),"size": "full","margin": "xl"},"footer": {"type": "box","layout": "horizontal","contents": [{"type": "text","text": "CREATOR","size": "xl","wrap": True,"weight": "bold","color": "#7CFC00","action": {"type": "uri","uri": "http://line.me/ti/p/~denjak_inex"},"align": "center"},{"type": "separator","color": "#E5E4E2"},{"type": "text","text": "ORDER","size": "xl","wrap": True,"weight": "bold","color": "#FFD700","action": {"type": "uri","uri": "line://app/1602687308-GXq4Vvk9/?type=text&text=price"},"align": "center"}]},"header": {"type": "box","layout": "horizontal","contents": [{"type": "text","text": "INEXBOT","size": "xl","wrap": True,"weight": "bold","color": "#F0F8FF","align": "center"}]}}}
                                        me.sendFlex(Gr, data)
                                    else:
                                        me.sendMessage(Gr, "Hallo.. " + " " + nick[1] + " " + "\nJangan ngintip.. . . .\nMasuk  ayox... ")
                                        data = {"type": "template","altText": "{} sent fhoto jones".format(me.getContact(Musuhku).displayName),"template": {"type": "image_carousel","columns": [{"imageUrl": "https://obs.line-scdn.net/{}".format(me.getContact(Musuhku).pictureStatus),"size": "full", "action": {"type": "uri","uri": "http://line.me/ti/p/~denjaka_inex"}}]}}
                                        me.sendFlex(Gr, data)
                                else:
                                    warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
                                    warnanya1 = random.choice(warna1)
                                    data = {"type": "flex","altText": "Congkel matanya ","contents": {"type": "bubble","styles": {"header": {"backgroundColor": "#0000FF",},"body": {"backgroundColor": "#000000","separator": True,"separatorColor": "#ffffff"},"footer": {"backgroundColor": "#000080","separator": True}},"header": {"type": "box","layout": "horizontal","contents": [{"type": "text","text": "Nama : {}".format(me.getContact(Musuhku).displayName),"weight": "bold","color": warnanya1,"size": "md"}]},"hero": {"type": "image","url": "https://obs.line-scdn.net/{}".format(me.getContact(Musuhku).pictureStatus),"size": "full","aspectRatio": "20:13","aspectMode": "cover","action": {"type": "uri","uri": "https://line.me/ti/p/~denjaka_inex"}},"type": "bubble","body": {"type": "box","layout": "horizontal","contents": [{"type": "text","text": "{}".format(me.getContact(Musuhku).displayName)+" Hayoooooooh,,, ngapain ngintip bae","wrap": True,"color": warnanya1,"align": "center"}]},"footer": {"type": "box","layout": "vertical","spacing": "sm","contents": [{"type": "button","style": "primary","color": warnanya1,"height": "sm","action": {"type": "uri","label": "ADD MY LINE","uri": "https://line.me/ti/p/"+me.getUserTicket().id}},{"type": "spacer","size": "sm",}],"flex": 0}}}
                                    me.sendFlex(Gr, data)
                        else:
                            pass
                else:
                    pass
            except:
                pass
        else:
            pass
    except Exception as error:
        return False
        if rank.type == 59:
            print(rank)
while True:
    try:
      ops=oepoll.singleTrace(count=50)
      if ops != None:
        for rank in ops: 
          serviceX(rank)
          oepoll.setRevision(rank.revision)
    except Exception as e:
        me.log("RESPONSE: " + str(e))
