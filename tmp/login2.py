# -*- coding: utf-8 -*-
# Built-in libraries
#from CHRLINE import CHRLINE
import os
import sys
import time
import string
import re
import ast
import platform
import threading
#from threading import Timer
import colorama
import random
import subprocess
import atexit
import codecs
import urllib
import pytz
from urllib.parse import quote
from genericpath import isdir
from datetime import datetime, timedelta, date
from time import sleep
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest

# Third-party libraries
from apscheduler.schedulers.background import BackgroundScheduler
import requests
from bs4 import BeautifulSoup
import yt_dlp

# Custom libraries
from akad.ttypes import *
from linepy import *

# Others
import json
import traceback
from linebot.models import TextSendMessage
import shutil


####################################################
ts = time.time()
# 記錄每個群組的通話開始時間
call_start_time = {}
#星期幾
week_list = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
#yt列表
search_results_map = {}
####################################################
cl = LINE("47tvrqqdr@jxp.shenyin-linebot.com", "a2329921")
#ShenYin_Change_cover=CHRLINE(cl.authToken,device="DESKTOPMAC",encType=0)
# cl = LINE("u75c284891d577706523bf2c77b6659db:aWF0OiA5ODkzMzQ4ODYyMAo=..F+iT6ywljgxspIVgUFmqsQA1VdQ=", appName="IOS\t10.1.1\tIOS\t13.3.1")#ST登入
Backstage = "login2"# 檔案名稱
msg_dict, msg_read = {}, {}
#####
####################################################
proset =  {
    "rafww":False,
    "changePictureProfile":False,
    "changea":False,
    "changeb":False,
    "changeall":False,
    "changevp":False
}
wait = {
    "contactve": False,
    "game": {},
    "banbe": False,
    "unbanbe": False,
    "cvp": False,
    "5image": False,
    "5video": False,
    'pcms': True,  # 私聊監控系統
    'Speak_remotely': {},
    'gbc': {},
    "xin": "",
    "squiredab": False,
    "broadcast": {}
}
wait3 = {
    'readPoint': {},
    'readMember': {},
    'setTime': {},
    'ROM': {}
}
beihong = []
####################################################
oepoll = OEPoll(cl)
####################################################
clMID = cl.profile.mid
profile = cl.getProfile()
clProfile = cl.getProfile()
####################################################
cl.log(clMID)
####################################################
mulai = time.time()
bots =[cl]
botwww = random.choice(bots)
####################################################
ban = json.load(codecs.open("ban.json", "r", "utf-8"))
rpy = json.load(codecs.open("reply.json", "r", "utf-8"))
ig = json.load(codecs.open("ig.json","r","utf-8"))
timess = json.load(codecs.open("timexss.json", "r", "utf-8"))
haohao = "cc6f53fea5ea9faa95a6ecf90cb2cf368"
ggg = "cc6f53fea5ea9faa95a6ecf90cb2cf368"
gom = ["ue1d1762de95bc0fd9b9e4e309436353f", clMID]
####################################################
boom = """








"""
boom2 = "ণاعနัゆीՁşัढे囟ֆ₤❂Ǥª₦🔝"
boom3 = ".1.2.3.4.5.6.7.8.9.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0."
boom4 = "జ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞా"
boom5 = "1.0.S.1.0.S.1.0.S.1.0.S."
if clMID not in ban["owners"]:
    ban["owners"].append(clMID)
highest = ["ue1d1762de95bc0fd9b9e4e309436353f","u11f5f40c5e835e916188ea1c85f50832","u7802bdacd6da582773ebff53257a8f95"]
for x in highest:
    if x not in ban["admin"]:
        ban["admin"].append(x)
    if x not in ban["owners"]:
        ban["owners"].append(x)
logintime = str(time.time() - ts)
loginmsg = "登入完成"
loginmsg += f"\n登錄時間:{logintime[0:8]}"
if os.path.isdir('./user_data'):
    try:
        os.makedirs('./user_data')
    except OSError:
        pass
try:
    cl.sendMessage(ggg, str(loginmsg))
except:
    pass
####################################################時間到自動改名
def auto_run():
    while True:
        current_time = datetime.now().strftime("%H:%M")
        new_name = "hao helper " + " (" + current_time + ")"
        c = cl.getProfile()
        c.displayName = new_name
        cl.updateProfile(c)
        time.sleep(900)  # 等待十五分鐘（900秒）後再次執行
# 建立執行緒並運行自動運行函式
auto_run_thread = threading.Thread(target=auto_run)
auto_run_thread.start()
####################################################後台儲存
def count_files(directory):
    return sum(len(files) for _, _, files in os.walk(directory))
####################################################帳號資料 伺服器資料 內存訊息
def get_system_information(mid_information=False, use_flex=False):
    system_info = "【帳號資訊】"
    
    # 获取群组和邀请数量
    group_ids_joined = cl.getGroupIdsJoined()
    group_ids_invited = cl.getGroupIdsInvited()
    system_info += f"\n群組數量：{len(group_ids_joined)}"
    system_info += f"\n邀請數量：{len(group_ids_invited)}"
    
    # 获取隐私设置信息
    src = cl.getSettings().privacySearchByUserid
    seal = cl.getSettings().e2eeEnable
    fil = cl.getSettings().privacyReceiveMessagesFromNotFriend
    alid = "開放line ID加入 : 開啟" if src else "開放line ID加入 : 關閉"
    letsel = "Letter Sealing : 開啟" if seal else "Letter Sealing : 關閉"
    fpes = "阻擋非好友訊息 : 關閉" if fil else "阻擋非好友訊息 : 開啟"
    system_info += f"\n{alid}"
    system_info += f"\n{fpes}"
    system_info += f"\n{letsel}"
    
    # 获取关于服务器的信息
    system_info += "\n\n【關於伺服器】"
    
    # 获取操作系统信息
    try:
        os_info = subprocess.getoutput('lsb_release -a')
        for line in os_info.splitlines():
            if 'Description:' in line:
                os_description = line.split('Description:')[1].replace('     ', '')
                system_info += f"\nOS: {os_description}"
    except:
        os_description = "Ubuntu 18.04.5 LTS"
        system_info += f"\nOS: {os_description}"
    
    # 获取Python信息
    python_imp = platform.python_implementation()
    python_ver = platform.python_version()
    system_info += f"\nLang: {python_imp}"
    system_info += f"\nVer: {python_ver}"
    
    # 获取CPU信息
    cpu_info = subprocess.getoutput('lscpu')
    core_count = subprocess.getoutput('grep -c ^processor /proc/cpuinfo')
    for line in cpu_info.splitlines():
        if 'Architecture:' in line:
            architecture = line.split('Architecture:')[1].replace(' ', '')
            system_info += f"\nArchitecture: {architecture}"
    system_info += f"\nCPU Core: {core_count}"
    
    # 获取内存信息
    memory_info = subprocess.getoutput('cat /proc/meminfo')
    for line in memory_info.splitlines():
        if 'MemTotal:' in line:
            mem_total = line.split('MemTotal:')[1].replace(' ', '')
        if 'MemFree:' in line:
            mem_free = line.split('MemFree:')[1].replace(' ', '')
    system_info += f"\nMemory: {mem_total}"
    system_info += f"\nFree: {mem_free}"

    system_info += "\n\n【全群功能】"
    if mid_information:
        system_info += "\n友資偵測開啟✅"
    else:
        system_info += "\n友資偵測關閉❌"
    if use_flex:
        system_info += "\n模板開啟✅"
    else:
        system_info += "\n模板關閉❌"
    
    return system_info
####################################################錯誤訊息
def logError(e):
    cl.log("[ ERROR ] " + str(e))
    cl.log("[ ERROR DETAIL ] " + str(traceback.format_exc()))

def ismid(mid):
    try:
        cl.getContact(mid)
        return True
    except:
        return False

def find_between_r(s, first, last):
    try:
        start = s.rindex(first) + len(first)
        end = s.rindex(last, start)
        return s[start:end]
    except ValueError:
        return ""
####################################################重啟存檔
def print_colored(text):
    color_codes = [
        colorama.Fore.RED,
        colorama.Fore.GREEN,
        colorama.Fore.YELLOW,
        colorama.Fore.BLUE,
        colorama.Fore.MAGENTA,
        colorama.Fore.CYAN
    ]
    random_color = random.choice(color_codes)
    colored_text = random_color + text + colorama.Style.RESET_ALL
    print(colored_text)

# 初始化colorama
colorama.init()

def restartBot():
    print_colored(" [ 訊息 ] 機器重啟 " )
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
####################################################speed測速發圖
def speedImage(to):
    res = []
    string="speedtest-cli --share"
    p = subprocess.Popen(string, shell=True, stdout=subprocess.PIPE, universal_newlines=True) # 在shell中运行命令并捕获输出
    p.wait()
    result_lines = p.stdout.readlines()   # 从子进程的输出中读取行
    result = ""
    for line in result_lines:
        print(line.strip()) 
        result += line.strip()
        result += "\n"
    #x = result.split("s:")
    u = find_between_r(result, "result/", ".png") # 从结果中提取图像的URL
    cl.sendImageWithURL(to,"http://www.speedtest.net/result/"+str(u)+".png") # 使用cl.sendImageWithURL函数将图像发送到指定的目标
####################################################yt_dlp
def tiny_url(url):
    apiurl = "http://tinyurl.com/api-create.php?url="
    try:
        tinyurl = urllib.request.urlopen(apiurl + url).read()
        return tinyurl.decode("utf-8")
    except urllib.error.HTTPError as e:
        error_message = f"URL轉換失敗：{e.code} {e.reason}"
        return error_message
def ytdl(url):
    try:
        ydl_opts = {
            'outtmpl': 'moe.mp4',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return True
    except Exception as e:
        print("下载失败:", str(e))
        return False

def download(url):
    try:
        ydl_opts = {
            'outtmpl': '%(id)s.%(ext)s',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return True
    except Exception as e:
        print("下载失败:", str(e))
        return False

def ytdlwwwe(to, url):
    try:
        ydl_opts = {
            'outtmpl': 'test.mp3',
            'format': 'bestaudio/best',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        cl.sendAudio(to, "test.mp3")
        os.remove("test.mp3")
    except Exception as e:
        print("下载失败:", str(e))
def ytdlwww(to, url):
    try:
        ydl_opts = {
            'outtmpl': 'test.mp4',
            'merge_output_format': 'mp4',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        cl.sendVideo(to, "test.mp4")
        os.remove("test.mp4")
    except Exception as e:
        print("下载失败:", str(e))

def ytdl_cover(to, url):
    try:
        ydl_opts = {
            'outtmpl': 'test',
            'writethumbnail': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            thumbnail_filename = "test.webp" if os.path.exists("test.webp") else "test.jpg"
        cl.sendImage(to, thumbnail_filename)
        if os.path.exists("test.jpg"):
            os.remove("test.jpg")
        if os.path.exists("test.webm"):
            os.remove("test.webm")
        if os.path.exists("test.webp"):
            os.remove("test.webp")
    except Exception as e:
        print("下载失败:", str(e))

def ytdl_combined(to, url):
    try:
        # 下載影片
        print("開始下載影片...")
        ydl_opts = {
            'outtmpl': 'test.mp4',
            'merge_output_format': 'mp4',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        cl.sendVideo(to, "test.mp4")
        print("影片下載完成並傳送.")

        # 下載封面
        print("開始下載封面...")
        ydl_opts = {
            'outtmpl': 'test',
            'writethumbnail': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            thumbnail_filename = "test.webp" if os.path.exists("test.webp") else "test.jpg"
        cl.sendImage(to, thumbnail_filename)
        print("封面下載完成並傳送.")
        
        # 刪除本地檔案
        print("開始清理本地檔案...")
        os.remove("test.mp4")
        if os.path.exists("test.jpg"):
            os.remove("test.jpg")
        if os.path.exists("test.webm"):
            os.remove("test.webm")
        if os.path.exists("test.webp"):
            os.remove("test.webp")
        print("本地檔案清理完成.")
    except Exception as e:
        print("下载失败:", str(e))

def isgid(gid):
    try:
        cl.getGroupWithoutMembers(gid)
        return True
    except:
        return False
####################################################自動儲存文字訊息(包含私訊 群組)
def write_to_daily_file(sender_name, sender_mid, message_text, send_location, send_time):
    current_date = datetime.now().strftime("%Y-%m-%d")
    filename = f"{current_date}.txt"

    with open(filename, "a", encoding="UTF-8") as f:
        f.write(f"發送者名稱: {sender_name}\n")
        f.write(f"發送者MID: {sender_mid}\n")
        f.write(f"發送位置: {send_location}\n")
        f.write(f"發送內容: {message_text}\n")
        f.write(f"發送時間: {send_time.strftime('%Y年%m月%d日%H點%M分%S秒')}\n")
        f.write("-----------------------\n")

def send_daily_file():#每天晚上23:59:59分自動傳送該檔案
    target_mid = "cc6f53fea5ea9faa95a6ecf90cb2cf368"
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"{today}.txt"

    if not os.path.isfile(filename):
        print(f"File {filename} does not exist. Skipping.")
        return

    # 傳送檔案
    cl.sendFile(to=target_mid, path=filename)

    # 刪除檔案
    if os.path.isfile(filename):
        os.remove(filename)
# 建立背景排程器
scheduler = BackgroundScheduler()
scheduler.add_job(send_daily_file, 'cron', hour=23, minute=59, second=50)#如果是晚上8點 5分5秒就是 20 5 5
scheduler.start()
# 在程式結束前，確保排程器可以清理它的資源
atexit.register(lambda: scheduler.shutdown())
###########################################################################
def backupData():
    data = {
        'ban': ban,
        'reply': rpy,
        'timexss': timess,
        'ig': ig
    }
    try:
        with codecs.open('backup.json', 'w', 'utf-8') as file:
            json.dump(data, file, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False

def helptest():
    f = open('helptest.txt', 'r', encoding="UTF-8")
    return f.read()

def helpbot():
    f = open('help0.txt', 'r', encoding="UTF-8")
    return f.read()


def help1():
    f = open('help1.txt', 'r', encoding="UTF-8")
    return f.read()


def help2():
    f = open('help2.txt', 'r', encoding="UTF-8")
    return f.read()


def help3():
    f = open('help3.txt', 'r', encoding="UTF-8")
    return f.read()


def help4():
    f = open('help4.txt', 'r', encoding="UTF-8")
    return f.read()

def help5():
    f = open('help5.txt', 'r', encoding="UTF-8")
    return f.read()
###################################################
def Runtime(secs):
    mins, secs = divmod(secs, 60)
    hours, mins = divmod(mins, 60)
    days, hours = divmod(hours, 24)
    return '%02d 天 %02d 時 %02d 鐘 %02d 秒' % (days, hours, mins, secs)

def timeChange(secs):
    mins, secs = divmod(secs, 60)
    hours, mins = divmod(mins, 60)
    days, hours = divmod(hours, 24)
    weeks, days = divmod(days, 7)
    months, weeks = divmod(weeks, 4)
    text = ""
    if months != 0:
        text += "%2d 月" % (months)
    if weeks != 0:
        text += " %2d 周" % (weeks)
    if days != 0:
        text += " %2d 天" % (days)
    if hours != 0:
        text += "%2d 時" % (hours)
    if mins != 0:
        text += " %2d 分" % (mins)
    if secs != 0:
        text += " %2d 秒" % (secs)
    if text[0] == " ":
        text = text[1:]
    return text
####################################################
#自動重啟
def job_bot():
    # Backup data
    backupData()
    # Send a message to the group before restarting
    groupId = ggg
    cl.sendMessage(groupId, '晚上12點囉\n機器正在自動重啟...')
    # Restart the application
    python = sys.executable
    os.execl(python, python, *sys.argv)

scheduler = BackgroundScheduler()
scheduler.add_job(job_bot, 'cron', hour=0, minute=0, second=0) # 定时任务每天凌晨12点执行
scheduler.start()  # 启动调度器

# Now your program can continue running and your job_bot will run in the background at the specified time
def sendflex(to, data):
    n1 = LiffChatContext(to)
    n2 = LiffContext(chat=n1)
    view = LiffViewRequest('1657024923-2r46WKKN', n2)
    token = cl.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@tinghaobo "
    if mids == []:
        raise Exception("Invaliod mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S': str(slen), 'E': str(elen - 4), 'M': mid}
            arr.append(arrData)
            textx += mention
            textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S': str(slen), 'E': str(elen - 4), 'M': mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    cl.sendMessage(to, textx, {'MENTION': str(
        '{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
#油價查詢
def oil_price():
    target_url = 'https://gas.goodlife.tw/'
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    res.encoding = 'utf-8'  # 設定文字編碼為 utf-8
    soup = BeautifulSoup(res.text, 'html.parser')
    title = soup.select('#main')[0].text.replace('\n', '').split('(')[0]
    gas_price = soup.select('#gas-price')[0].text.replace('\n\n\n', '').replace(' ', '')
    cpc = soup.select('#cpc')[0].text.replace(' ', '')
    content = '{}\n{}{}'.format(title, gas_price, cpc)
    return content

####################################################
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 1:
            print_colored("更新配置文件")
        if op.type == 5:
            sendMention(ggg, "[ 加友通知 ]\n@!	此人加我好友", [op.param1])
            cl.sendContact(ggg, str(op.param1))  # 丟出加好友人的友資
            #cl.findAndAddContactsByMid(op.param1)
            #try:
            #    cl.sendMessage(op.param1, ban["text"])
            #    time.sleep(5)
            #except:
            #    pass
            #try:
            #    cl.sendImage(op.param1, "Private_message_image.jpg")
            #    time.sleep(5)
            #except:
            #    pass
            #try:
            #    cl.sendVideo(op.param1, "Private_message_video.mp4")
            #except:
            #    pass
            if ban["autoblock"] == True:
                cl.blockContact(op.param1)
                cl.sendMessage(op.param1, "自動封鎖已開啟")
        if op.type == 30:
            if ban["announcement"][op.param1] == True:
                if op.param3 == 'c':
                    print(f"[{op.type}]:{op.param3}")
                    ac = cl.getChatRoomAnnouncements(op.param1)[0]
                    sendMention(
                        op.param1, f"member: @!  設置了公告\n公告內容:{ac.contents.text}\n設置時間:{time.strftime('%m-%d %H:%M:%S',time.localtime(int(round(ac.createdTime/1000))))}", [ac.creatorMid])
                if op.param3 == 'd':
                    print(f"[{op.type}]:{op.param3}")
        if op.type == 11 or op.type == 122:
            pass
        if op.type == 13 or op.type == 124:
            group = cl.getGroup(op.param1)
            contact1 = cl.getContact(op.param2)
            #cl.sendMessage(ggg,"通知邀請群組\n群組名稱:"+ str(group.name)+"\n群組ID:\n"+ str(group.id)+"\n邀請者:"+contact1.displayName +"\nMID:"+contact1.mid)
            if clMID in op.param3:
                if op.param2 in ban["owners"]:
                    cl.acceptGroupInvitation(op.param1)
                    ban["announcement"][op.param1] = False
                    ban["groupcall"][op.param1] = False
                    ban["reply"][op.param1] = False
                    backupData()
                    data = {
    "type": "template",
    "altText": "hao bot",
    "template": {
        "type": "carousel",
        "actions": [],
        "columns": 
        [
            {
                "thumbnailImageUrl": "https://p2.bahamut.com.tw/B/2KU/50/b1ff50c8207de9fd13145177651lbdy5.JPG",
                "imageBackgroundColor": "#002727",
                "title": "本機器為測試用機器人",
                "text": "不開放私自邀請",
                "defaultAction": {
                    "type": "uri",
                    "uri": "line://ti/p/~none"
                },
                "actions": [
                    {
                        "type": "uri",
                        "label": "我的網站",
                        "uri": "https://haoline.fans.link/hhline"
                    },
                    {
                        "type": "uri",
                        "label": "我的主人",
                        "uri": "https://line.me/ti/p/oYpVwkXSlp"
                    }
                ]
            }
        ]
    }
}
                    sendflex(op.param1, data)
                    #cl.sendMessage(op.param1, "感謝偉大的作者邀請我入群")
                else:
                    cl.acceptGroupInvitation(op.param1)
                    data = {
    "type": "template",
    "altText": "hao bot",
    "template": {
        "type": "carousel",
        "actions": [],
        "columns": 
        [
            {
                "thumbnailImageUrl": "https://p2.bahamut.com.tw/B/2KU/50/b1ff50c8207de9fd13145177651lbdy5.JPG",
                "imageBackgroundColor": "#002727",
                "title": "本機器為測試用機器人",
                "text": "不開放私自邀請",
                "defaultAction": {
                    "type": "uri",
                    "uri": "line://ti/p/~none"
                },
                "actions": [
                    {
                        "type": "uri",
                        "label": "我的網站",
                        "uri": "https://haoline.fans.link/hhline"
                    },
                    {
                        "type": "uri",
                        "label": "我的主人",
                        "uri": "https://line.me/ti/p/oYpVwkXSlp"
                    }
                ]
            }
        ]
    }
}
                    sendflex(op.param1, data)
                    #sendMention(
                    #    op.param1, "@! 你沒權限.\n請找作者ヽ(✿ﾟ▽ﾟ)ノ", [op.param2])
                    cl.sendContact(
                        op.param1, "ue1d1762de95bc0fd9b9e4e309436353f")
                    cl.leaveGroup(op.param1)
        if op.type == 15 or op.type == 128:
            if op.param1 in ban["gcgid"]:
                if op.param1 not in timess['gc']:
                    sender = op.param2
                    if sender in gom:
                        pass
                    else:
                        try:
                            arrData = ""
                            text = "%s " % ('掰掰')
                            arr = []
                            mention = "@hao "
                            slen = str(len(text))
                            elen = str(len(text) + len(mention) - 1)
                            arrData = {'S': slen, 'E': elen, 'M': op.param2}
                            arr.append(arrData)
                            text += mention + '此人退出群組'
                            cl.sendMessage(op.param1, text, {'MENTION': str(
                                '{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                            # cl.sendContact(op.param1,str(op.param2)) #退群友資
                        except Exception as error:
                            print(error)
                else:
                    sender = op.param2
                    if sender in gom:
                        pass
                    else:
                        cl.sendMessage(op.param1, "@hao" + timess['gc'][op.param1], contentMetadata={
                                       'MENTION': '{"MENTIONEES":['+'{"S":"0","E":"4","M":'+json.dumps(sender)+'}'+']}'})
        if op.type == 17 or op.type == 130:
            if op.param1 in ban["wcgid"]:
                if op.param1 not in timess['wc']:
                    sender = op.param2
                    if sender in gom:
                        pass
                    else:
                        try:
                            arrData = ""
                            text = "%s " % ('你好')
                            arr = []
                            mention = "@hao "
                            slen = str(len(text))
                            elen = str(len(text) + len(mention) - 1)
                            arrData = {'S': slen, 'E': elen, 'M': op.param2}
                            arr.append(arrData)
                            text += mention + '歡迎加入群組'
                            cl.sendMessage(op.param1, text, {'MENTION': str(
                                '{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                            # cl.sendContact(op.param1,str(op.param2)) #入群友資
                        except Exception as error:
                            print(error)
                else:
                    sender = op.param2
                    if sender in gom:
                        pass
                    else:
                        cl.sendMessage(op.param1, "@hao" + timess['wc'][op.param1], contentMetadata={
                                       'MENTION': '{"MENTIONEES":['+'{"S":"0","E":"4","M":'+json.dumps(sender)+'}'+']}'})
        if op.type == 19 or op.type == 133:
            pass
        if op.type == 32 or op.type == 126:
            pass
        if op.type == 26 or op.type == 25:
            msg, text, msg_id, receiver, sender = op.message, op.message.text, op.message.id, op.message.to , op.message._from
            if msg.toType == 0:
                if sender not in clMID:to = sender
                else:to = receiver
            else:to = receiver
            if msg.toType != 0 and ban['autoRead']:
                try:cl.sendChatChecked(to,msg_id)
                except Exception as e:print(e)
            if msg.toType != 0:msg_read[msg_id] = {}
            if sender not in clMID:
                if msg.contentType == 0:
                    msg_dict[msg_id] = {"from": sender, "text": text, "createdTime": msg.createdTime, "optype": msg.toType}
                    sender_name = cl.getContact(sender).displayName
                    send_time = datetime.fromtimestamp(msg.createdTime/1000)  # assuming createdTime is in milliseconds
                    if msg.toType == 0:
                        send_location = '私人訊息'
                    elif msg.toType == 1:
                        send_location = '副本'
                    elif msg.toType == 2:
                        group_id = msg.to
                        group_name = cl.getGroup(group_id).name
                        send_location = f'群組名稱 {group_name}'
                    else:
                        send_location = '未知'
                    write_to_daily_file(sender_name, sender, text, send_location, send_time)
                    if msg.toType == 0:
                        cl.log(f"[{sender}]--->訊息來源:私訊\n訊息內容:{text}")
                        if cl.getContact(sender).attributes == 0:
                            if ban["pcms"] and ban["pcmsrd"]:
                                cl.sendChatChecked(to, msg_id)
                            if ban["pcms"]:
                                sendMention(ban["dio"], f"[私訊監控系統]\n發送者: @!\n發送者MID:\n{sender}\n發送內容:\n{text}", [sender])
                    elif msg.toType == 1:
                        cl.log(f"[{sender}]--->訊息來源:副本\n訊息內容:{text}")
                    elif msg.toType == 2:
                        cl.log(f"[{sender}]--->訊息來源:群組\n訊息內容:{text}")
                elif msg.contentType == 1:
                    image = cl.downloadObjectMsg(msg_id, saveAs=f"allsave/image/{msg.createdTime}-jpg.jpg")
                    msg_dict[msg_id] = {"from":sender,"image":image,"createdTime":msg.createdTime, "optype":msg.toType}
                    imagesave = sum(len(files) for _, _, files in os.walk(r'/root/login2/allsave/image'))
                    if msg.toType == 0:
                        cl.log(f"[{sender}]--->訊息來源:私訊\n訊息內容(圖片):Picture")
                        if cl.getContact(sender).attributes == 0:
                            if ban["pcms"] and ban["pcmsrd"]:cl.sendChatChecked(to,msg_id)
                            if ban["pcms"]:sendMention(ban["dio"],f"[私訊監控系統]\n發送者: @!\n發送者MID:\n{sender}\n發送了一張圖片",[sender]);cl.sendImage(ban["dio"],image)
                    elif msg.toType == 1:cl.log(f"[{sender}]--->訊息來源:副本\n訊息內容(圖片):Picture")
                    elif msg.toType == 2:cl.log(f"[{sender}]--->訊息來源:群組\n訊息內容(圖片):Picture")
                    if imagesave > 1000:
                        cl.sendMessage(ban["dio"],"圖片已達1000張 將自動清理圖片後台")
                        try:
                            shutil.rmtree(f'/root/login2/allsave/image')
                            os.makedirs(f'/root/login2/allsave/image')
                            cl.sendMessage(ban["dio"],"圖片後台清理成功")
                        except Exception as e:cl.sendMessage(ban["dio"],f"圖片後臺清理失敗 原因:{e}")
                elif msg.contentType == 2:
                    def svideo(createdTime):
                        try:
                            print("開始下載影片")
                            Video = cl.downloadObjectMsg(msg_id, saveAs=f"allsave/video/{createdTime}-Video.mp4")
                            msg_dict[msg_id] = {"from":msg._from,"Video":Video,"createdTime":createdTime, "optype":msg.toType}
                            #cl.sendMessage(ban["dio"],f"Video:{Video}")
                            if msg.toType == 0 and ban["pcms"]:cl.sendVideo(ban["dio"],Video);print(f"[私訊影片]發送{Video}成功")
                        except Exception as e:print(f"download video failed:{e}")
                    threading.Thread(target=svideo, args=(msg.createdTime,)).start()
                    videosave = sum(len(files) for _, _, files in os.walk(r'/root/login2/allsave/video'))
                    if msg.toType == 0:
                        cl.log(f"[{sender}]--->訊息來源:私訊\n訊息內容(影片):Video")
                        if cl.getContact(sender).attributes == 0:
                            if ban["pcms"] and ban["pcmsrd"]:cl.sendChatChecked(to,msg_id)
                            if ban["pcms"]:sendMention(ban["dio"],f"[私訊監控系統]\n發送者: @!\n發送者MID:\n{sender}\n發送了一個影片",[sender])
                    elif msg.toType == 1:cl.log(f"[{sender}]--->訊息來源:副本\n訊息內容(影片):Video")
                    elif msg.toType == 2:cl.log(f"[{sender}]--->訊息來源:群組\n訊息內容(影片):Video")
                    if videosave > 100:
                        cl.sendMessage(ban["dio"],"影片已達100部 將自動清理影片後台")
                        try:
                            shutil.rmtree(f'/root/login2/allsave/video')
                            os.makedirs(f'/root/login2/allsave/video')
                            cl.sendMessage(ban["dio"],"影片後台清理成功")
                        except Exception as e:cl.sendMessage(ban["dio"],f"影片後臺清理失敗 原因:{e}")
                elif msg.contentType == 3:
                    sound = cl.downloadObjectMsg(msg_id, saveAs=f"allsave/sound/{msg.createdTime}-sound.mp3")
                    msg_dict[msg_id] = {"from":msg._from,"sound":sound,"createdTime":msg.createdTime, "optype":msg.toType}
                    soundsave = sum(len(files) for _, _, files in os.walk(r'/root/login2/allsave/sound'))
                    if msg.toType == 0:
                        cl.log(f"[{sender}]--->訊息來源:私訊\n訊息內容(語音):Sound")
                        if cl.getContact(sender).attributes == 0:
                            if ban["pcms"] and ban["pcmsrd"]:cl.sendChatChecked(to,msg_id)
                            if ban["pcms"]:sendMention(ban["dio"],f"[私訊監控系統]\n發送者: @!\n發送者MID:\n{sender}\n發送了一個錄音檔",[sender]);cl.sendAudio(ban["dio"],sound)
                    elif msg.toType == 1:cl.log(f"[{sender}]--->訊息來源:副本\n訊息內容(語音):Sound")
                    elif msg.toType == 2:cl.log(f"[{sender}]--->訊息來源:群組\n訊息內容(語音):Sound")
                    if soundsave > 100:
                        cl.sendMessage(ban["dio"],"音檔已達100個 將自動清理音檔後台")
                        try:
                            shutil.rmtree(f'/root/login2/allsave/sound')
                            os.makedirs(f'/root/login2/allsave/sound')
                            cl.sendMessage(ban["dio"],"音檔後台清理成功")
                        except Exception as e:cl.sendMessage(ban["dio"],f"音檔後臺清理失敗 原因:{e}")
                elif msg.contentType == 7:
                    msg_dict[msg_id] = {"from":msg._from,"id":msg.contentMetadata['STKID'],"createdTime":msg.createdTime, "optype":msg.toType}
                    if msg.toType == 0:
                        cl.log(f"[{sender}]--->訊息來源:私訊\n訊息內容(貼圖):{msg.contentMetadata['STKID']}")
                        if cl.getContact(sender).attributes == 0:
                            if ban["pcms"] and ban["pcmsrd"]:cl.sendChatChecked(to,msg_id)
                            if ban["pcms"]:sendMention(ban["dio"],f"[私訊監控系統]\n發送者: @!\n發送者MID:\n{sender}\n發送了一個貼圖",[sender])
                    elif msg.toType == 1:cl.log(f"[{sender}]--->訊息來源:副本\n訊息內容(貼圖):{msg.contentMetadata['STKID']}")
                    elif msg.toType == 2:cl.log(f"[{sender}]--->訊息來源:群組\n訊息內容(貼圖):{msg.contentMetadata['STKID']}")
                elif msg.contentType == 13:
                    msg_dict[msg_id] = {"from":msg._from,"mid":msg.contentMetadata["mid"],"createdTime":msg.createdTime, "optype":msg.toType}
                    if ban["midInformation"] == True:
                        try:
                            contact = cl.getContact(msg.contentMetadata["mid"])
                            cover = cl.getProfileCoverURL(msg.contentMetadata["mid"])
                            ret_ = "• 名片資訊"
                            ret_ += "\n• 暱稱: {}".format(str(contact.displayName))
                            ret_ += "\n• 狀態 : {}".format(str(contact.statusMessage))
                            ret_ += "\n• 辨識碼: {}".format(str(msg.contentMetadata["mid"]))
                            ret_ += "\n• 名片頭貼 : http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                            ret_ += "\n• 名片封面 : {}".format(str(cover))
                            cl.sendMessage(to, str(ret_))
                            cl.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus)))
                        except:
                            cl.sendMessage(to, "Kontak tidak valid")
                    if msg.toType == 0:
                        try:cl.log(f"[{sender}]--->訊息來源:私訊\n訊息內容(友資):{msg.contentMetadata['displayName']} {msg.contentMetadata['mid']}")
                        except:cl.log(f"[{sender}]--->訊息來源:私訊\n訊息內容(友資): {msg.contentMetadata['mid']}")
                        if cl.getContact(sender).attributes == 0:
                            if ban["pcms"] and ban["pcmsrd"]:cl.sendChatChecked(to,msg_id)
                            if ban["pcms"]:sendMention(ban["dio"],f"[私訊監控系統]\n發送者: @!\n發送者MID:\n{sender}\n發送了一個友資",[sender]);cl.sendMessage(ban["dio"], None, contentMetadata={'mid': msg.contentMetadata["mid"]}, contentType=13) 
                    elif msg.toType == 1:
                        try:cl.log(f"[{sender}]--->訊息來源:副本\n訊息內容(友資):{msg.contentMetadata['displayName']} {msg.contentMetadata['mid']}")
                        except:cl.log(f"[{sender}]--->訊息來源:副本\n訊息內容(友資): {msg.contentMetadata['mid']}")
                    elif msg.toType == 2:
                        try:cl.log(f"[{sender}]--->訊息來源:群組\n訊息內容(友資):{msg.contentMetadata['displayName']} {msg.contentMetadata['mid']}")
                        except:cl.log(f"[{sender}]--->訊息來源:群組\n訊息內容(友資): {msg.contentMetadata['mid']}")
                elif msg.contentType == 6:
                    if msg.toType == 2:
                        group_name = cl.getGroup(msg.to).name
                        if msg.contentMetadata.get("GC_EVT_TYPE") == "E":
                            cl.log(f"[{sender}]--->訊息來源:群組\n群組名稱：{group_name}\n訊息內容：群通結束")
                        elif msg.contentMetadata.get("GC_EVT_TYPE") == "S":
                            cl.log(f"[{sender}]--->訊息來源:群組\n群組名稱：{group_name}\n訊息內容：群通開始")
                elif msg.contentType == 14:
                    def sfile(createdTime):
                        try:
                            print("開始下載檔案")
                            file = cl.downloadObjectMsg(msg_id, saveAs=f"allsave/file/{createdTime}-{msg.contentMetadata['FILE_NAME']}")
                            msg_dict[msg_id] = {"from":sender,"file":file,"createdTime":createdTime, "optype":msg.toType}
                            #cl.sendMessage(ban["dio"],f"File:{msg.contentMetadata['FILE_NAME']}")
                            if msg.toType == 0 and ban["pcms"]:cl.sendFile(ban["dio"],file);print(f"[私訊檔案]發送{file}成功")
                        except Exception as e:print(f"download file failed:{e}")
                    threading.Thread(target=sfile, args=(msg.createdTime,)).start()
                    filesave = sum(len(files) for _, _, files in os.walk(r'/root/login2/allsave/file'))
                    if msg.toType == 0:
                        cl.log(f"[{sender}]--->訊息來源:私訊\n訊息內容(檔案):{msg.contentMetadata['FILE_NAME']}")
                        if cl.getContact(sender).attributes == 0:
                            if ban["pcms"] and ban["pcmsrd"]:cl.sendChatChecked(to,msg_id)
                            if ban["pcms"]:sendMention(ban["dio"],f"[私訊監控系統]\n發送者: @!\n發送者MID:\n{sender}\n發送了一個檔案",[sender])
                    elif msg.toType == 1:cl.log(f"[{sender}]--->訊息來源:副本\n訊息內容(檔案):{msg.contentMetadata['FILE_NAME']}")
                    elif msg.toType == 2:cl.log(f"[{sender}]--->訊息來源:群組\n訊息內容(檔案):{msg.contentMetadata['FILE_NAME']}")
                    if filesave > 100:
                        cl.sendMessage(ban["dio"],"檔案已達100個 將自動清理檔案後台")
                        try:
                            shutil.rmtree(f'/root/login2/allsave/file')
                            os.makedirs(f'/root/login2/allsave/file')
                            cl.sendMessage(ban["dio"],"檔案後台清理成功")
                        except Exception as e:cl.sendMessage(ban["dio"],f"檔案後臺清理失敗 原因:{e}")
                elif msg.contentType == 15:  # Location
                    location_info = msg.location
                    reply = (
                        f"地址: {location_info.address}\n"
                        f"緯度: {location_info.latitude}\n"
                        f"經度: {location_info.longitude}"
                    )
                    cl.sendMessage(to, reply)
                    print(location_info)  # Print it out to see what's inside   
                elif msg.contentType == 16:  # 
                    print(vars(msg))
                else:
                    msg_dict[msg_id] = {"from":msg._from,"createdTime":msg.createdTime, "optype":msg.toType}
                    if msg.toType == 0:
                        cl.log(f"[{sender}]--->訊息來源:私訊\n訊息Type:{msg.contentType}\n訊息內容(未知):{msg.contentMetadata}")
                        if cl.getContact(sender).attributes == 0:
                            if ban["pcms"] and ban["pcmsrd"]:cl.sendChatChecked(to,msg_id)
                            if ban["pcms"]:sendMention(ban["dio"],f"[私訊監控系統]\n發送者: @!\n發送者MID:\n{sender}\n基於某些原因讀取失敗了",[sender])
                    elif msg.toType == 1:cl.log(f"[{sender}]--->訊息來源:副本\n訊息Type:{msg.contentType}\n訊息內容(未知):{msg.contentMetadata}")
                    elif msg.toType == 2:cl.log(f"[{sender}]--->訊息來源:群組\n訊息Type:{msg.contentType}\n訊息內容(未知):{msg.contentMetadata}")
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if text is not None and text.lower() == "mid":
                    contact = cl.getContact(sender)
                    cl.relatedMessage(to, str(sender), op.message.id)
                if msg.text is not None and msg.text.lower().startswith("mid "):
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(
                            msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            aa = '{"S":"0","E":"5","M":'+json.dumps(ls)+'}'
                            cl.relatedMessage(to, str(ls), op.message.id)
                elif text is not None and text.lower() == '指令':#指令表文字
                    if ban["useflex"] == False:
                        cl.relatedMessage(to, helpbot(), msg_id)
                    else:
                        data = {
                            "type": "flex",
                            "altText": "hao bot",
                            "contents":{
"type": "bubble",
"body": {
"type": "box",
"layout": "vertical",
"contents": [
  {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "hao hleper",
        "align": "center",
        "size": "xxs",
        "color": "#888888"
      },
      {
        "type": "text",
        "text": "指令表",
        "align": "center",
        "size": "lg",
        "weight": "bold",
        "color": "#ff0000",
        "decoration": "underline"
      }
    ],
    "offsetBottom": "sm"
  },
  {
    "type": "separator",
    "color": "#000000"
  },
  {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": helpbot(),
        "color": "#0000cc",
        "align": "center",
        "wrap": True
      }
    ],
    "offsetTop": "sm"
  }
]
},
"size": "kilo"
}
                        }
                        sendflex(to, data)
                elif text is not None and text.lower() == '油價':
                    content = oil_price()
                    cl.sendMessage(to, content)

                elif text is not None and text.lower() == '我':#音樂名片
                    aa = ["https://anonfiles.com/K2maL3r9z8","https://anonfiles.com/97s2L1r2zf","https://anonfiles.com/O1s0Lfr8z0"]
                    music = str(BeautifulSoup(requests.get(random.choice(aa)).text, "html.parser").find("a", id="download-url")['href'])
                    cl.sendMessage(msg.to, text=cl.getContact(msg._from).displayName + "\n", contentMetadata={
            'previewUrl': 'http://dl.profile.line-cdn.net/' + cl.getContact(msg._from).pictureStatus, 
            'i-installUrl': 'line://nv/profilePopup/mid=' + msg._from,
            'ORGCONTP': 'MUSIC',
            'type': 'mt',
            'subText': cl.getContact(msg._from).statusMessage, 
            'a-installUrl': 'https://www.google.com.tw',
            'a-packageName': '音樂友資><',
            'playUrl': music,
            'countryCode': 'TW', 
            'a-linkUri': 'line://nv/profilePopup/mid=' + msg._from,
            'i-linkUri': 'line://nv/profilePopup/mid=' + msg._from,
            'text': cl.getContact(msg._from).displayName,
            'id': 'mt000000000a6b79f9',
            'linkUri': 'line://nv/profilePopup/mid=' + msg._from},
            contentType=19)
                elif text is not None and text.lower() == 'mp':
                    me = cl.getContact(sender)
                    contact = cl.getContact(sender)
                    cl.sendMessage(to, " 傳送了影片", contentMetadata={"DOWNLOAD_URL": "http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus), "PREVIEW_URL": "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)}, contentType = 2)
                elif text is not None and text.lower() == '繳費指令':  # 繳費指令 help
                    cl.relatedMessage(to, help5(), msg_id)
                if text is not None and text.lower().startswith("tt "):
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ", "")
                    # 在这里执行你的操作，例如调用 tiny_url() 函数
                    result = tiny_url(search)
                    cl.sendMessage(to, result)  # 使用 cl.sendMessage 发送结果
            if msg.contentType == 0:
                if text is None:
                    return
                else:
                    cmd = text.lower()
            if msg.contentType == 1:
                if "sender" in wait["broadcast"] and wait["broadcast"]["sender"] == sender and wait["broadcast"]["content"] == "pic" and wait["broadcast"]["to"] == msg.to:
                    image = cl.downloadObjectMsg(msg_id, saveAs="cvp.jpg")
                    if wait["broadcast"]["type"] == 2:
                        t = cl.getGroupIdsJoined()
                    if wait["broadcast"]["type"] == 0:
                        t = cl.getAllContactIds()
                    aa = 0
                    for manusia in t:
                        aa += 1
                        cl.sendImage(manusia, image)
                        time.sleep(2)
                    cl.sendMessage(to, "廣播完成 共廣播"+str(aa)+"群")
                if wait["squiredab"] == True:
                    if sender in beihong:
                        ooowwwoooo = wait["xin"]
                        jjjj = cl.downloadObjectMsg(
                            msg_id, saveAs="/root/"+Backstage+"/picsave/"+ooowwwoooo)
                        wait["xin"] = ""
                        wait["squiredab"] = False
                        beihong.clear()
                        cl.sendMessage(msg.to, "圖片回覆新增完成")
                if sender in wait['gbc'] and wait['gbc'][sender]['type'] == 'pic':
                    image = cl.downloadObjectMsg(msg.id)
                    n = cl.getGroupIdsJoined()
                    g = 0
                    for manusia in n:
                        group = cl.getGroup(manusia)
                        nama = [contact.mid for contact in group.members]
                        if len(nama) > int(wait['gbc'][sender]['over']):
                            cl.sendMessage(
                                manusia, "群組廣播 圖片\n" + wait['gbc'][sender]['text'])
                            cl.sendImage(manusia, image)
                            g += 1
                        else:
                            pass
                    cl.sendMessage(to, "群組廣播 分享《{}》個群組".format(str(g)))
                    cl.deleteFile(image)
                    del wait['gbc'][sender]
                if wait["5image"] == True:
                    if sender in highest:
                        wait["5image"] = False
                        cl.sendMessage(to, "開始下載圖片...")
                        path1 = cl.downloadObjectMsg(
                            msg.id, saveAs="Private_message_image.jpg")
                        cl.sendMessage(to, "圖片下載完成\n私訊圖片更改完成")
                if text is None:
                    return
                else:
                    cmd = text.lower()
            if msg.contentType == 2:
                if "sender" in wait["broadcast"] and wait["broadcast"]["sender"] == sender and wait["broadcast"]["content"] == "video" and wait["broadcast"]["to"] == msg.to:
                    image = cl.downloadObjectMsg(msg_id, saveAs="video.mp4")
                    if wait["broadcast"]["type"] == 2:
                        t = cl.getGroupIdsJoined()
                    if wait["broadcast"]["type"] == 0:
                        t = cl.getAllContactIds()
                    aa = 0
                    for manusia in t:
                        aa += 1
                        cl.sendVideo(manusia, image)
                        time.sleep(2)
                    cl.sendMessage(to, "廣播完成 共廣播"+str(aa)+"群")
                if wait["5video"] == True:
                    if sender in highest:
                        wait["5video"] = False
                        cl.sendMessage(to, "開始下載影片...")
                        path1 = cl.downloadObjectMsg(
                            msg.id, saveAs="Private_message_video.mp4")
                        cl.sendMessage(to, "影片下載完成\n私訊影片更改完成")
                if text is None:
                    return
                else:
                    cmd = text.lower()
            if msg.contentType == 3:
                if "sender" in wait["broadcast"] and wait["broadcast"]["sender"] == sender and wait["broadcast"]["content"] == "sound" and wait["broadcast"]["to"] == msg.to:
                    image = cl.downloadObjectMsg(msg_id, saveAs="sound.mp3")
                    if wait["broadcast"]["type"] == 2:
                        t = cl.getGroupIdsJoined()
                    if wait["broadcast"]["type"] == 0:
                        t = cl.getAllContactIds()
                    aa = 0
                    for manusia in t:
                        aa += 1
                        cl.sendVideo(manusia, image)
                        time.sleep(2)
                    cl.sendMessage(to, "廣播完成 共廣播"+str(aa)+"群")
                if text is None:
                    return
                else:
                    cmd = text.lower()
            if msg.contentType == 6 and to in ban['groupcall'] and ban['groupcall'][to] == True:
                if msg.contentMetadata['GC_EVT_TYPE'] == 'S':
                    # 記錄通話開始時間
                    call_start_time[to] = time.time()
                    start_time = datetime.today().strftime("%Y-%m-%d %I:%M:%S %p") + " " + "\n" + week_list[datetime.today().weekday()]
                    return sendMention(msg.contentMetadata['GC_CHAT_MID'],
                               f'成員 @! \n開啟了群組通話\n群通類別：{"群組語音通話" if msg.contentMetadata["GC_MEDIA_TYPE"] == "AUDIO" else "群組視訊通話"}\n群通開啟時間：\n{start_time}',
                               [sender])
                elif msg.contentMetadata['GC_EVT_TYPE'] == 'E':
                    # 計算通話時間
                    call_duration = time.time() - call_start_time.get(to, 0)
                    call_duration_str = time.strftime('%H時%M分%S秒', time.gmtime(call_duration))
                    # 重設通話開始時間
                    call_start_time[to] = 0
                    end_time = datetime.today().strftime("%Y-%m-%d %I:%M:%S %p") + " " + "\n" + week_list[datetime.today().weekday()]
                    return sendMention(msg.contentMetadata['GC_CHAT_MID'],
                               f'成員 @! \n結束了群組通話\n群通類別：{"群組語音通話" if msg.contentMetadata["GC_MEDIA_TYPE"] == "AUDIO" else "群組視訊通話"}\n群通結束時間：\n{end_time}\n通話時間：{call_duration_str}',
                               [sender])   
            if msg.contentType == 7:
                if text is None:
                    return
                else:
                    cmd = text.lower()
            if msg.contentType == 13:
                if "sender" in wait["broadcast"] and wait["broadcast"]["sender"] == sender and wait["broadcast"]["content"] == "contact" and wait["broadcast"]["to"] == msg.to:
                    if wait["broadcast"]["type"] == 2:
                        t = cl.getGroupIdsJoined()
                    if wait["broadcast"]["type"] == 0:
                        t = cl.getAllContactIds()
                    aa = 0
                    for manusia in t:
                        aa += 1
                        cl.sendContact(manusia, msg.contentMetadata["mid"])
                        time.sleep(2)
                    cl.sendMessage(to, "廣播完成 共廣播"+str(aa)+"群")
            else:
                if text is None:
                    return
                else:
                    cmd = text.lower()
            if sender in sender:
                if ban["reply"][to] == True:
                    if text.lower() in rpy['pic']:
                        if sender not in clMID:
                            cl.sendImage(to, "/root/"+Backstage +"/picsave/"+str(rpy['pic'][text.lower()]))
                if ban["reply"][to] == True:    
                    if text.lower() in ban['video']:
                        if sender not in clMID:
                            cl.sendAudio(to, "/root/"+Backstage +"/soundsave/"+str(ban['video'][text.lower()]))
            if sender in highest:  # 最大權限 最大指令
                if text and text.lower() == '速度':
                    sendMention(to, "———【測速開始】———\n@!\n"+str(timeit.timeit(
                        '"-".join(str(n) for n in range(100))', number=1000)) + "\n——【標註測速完畢】——", [sender])
                    backupData
                elif text and text.lower() == '更改頭貼':
                    cl.sendMessage(to,"• 更換頭貼功能\n請直接輸入數字\n[1] 直接上傳頭貼\n[2] 上傳頭貼加影片\n[3] 保留影片只換頭貼\n[4] +:網址 保留頭貼只換影片\n[5] 取消更換頭貼")
                    proset["changeall"] = True
                elif text and text.lower() == '1' and proset["changeall"] == True:
                    wait["cvp"] = True
                    cl.relatedMessage(to, "請發送要更改的圖片",op.message.id)
                    proset["changeall"] = False
                elif text and text.lower() == '2' and proset["changeall"] == True:
                    proset["changevp"] = True
                    time.sleep(0.5)
                    cl.sendMessage(to, "請發送影片連結")
                    proset["changeall"] = False
                elif text and text.lower() == '3' and proset["changeall"] == True:
                    proset["changea"] = True
                    contact = cl.getContact(clMID)
                    try:
                        os.remove(clMID + ".mp4")
                    except:
                        pass
                    finally:
                        urllib.request.urlretrieve("http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus), clMID + ".mp4")
                        time.sleep(0.5)
                        cl.sendMessage(to,"請發送要更改的圖片")
                        proset["changeall"] = False
                elif text is not None and text.lower().startswith("4:") and proset["changeall"] == True:
                    search = msg.text.replace("4:","")
                    contact = cl.getContact(clMID)
                    cl.sendMessage(to, "類型: Profile\n • 動作: Change video url\n • 狀態: Download...")
                    ytdl(search)
                    cl.sendMessage(msg.to, "影片下載成功 獲取個人圖片中")
                    pic = "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                    pict = cl.downloadFileURL(pic)
                    cl.sendMessage(msg.to, "圖片下載成功 開始更改動態頭貼")
                    time.sleep(2)
                    cl.changeVideoAndPictureProfile(pict, "moe.mp4")
                    cl.sendMessage(to, "類型: Profile\n • 動作: Change video url\n • 狀態: Prefect")
                    os.remove("moe.mp4")
                    proset["changeall"] = False
                elif text and text.lower() == '5' and proset["changeall"] == True:
                    proset["changevp"] = False
                    proset["changeb"] = False
                    proset["changea"] = False
                    proset["changePictureProfile"] = False
                    time.sleep(0.5)
                    cl.sendMessage(to,"已取消動作")
                    proset["changeall"] = False
                elif text and text.lower() == "logout":
                    backupData()
                    os._exit(0) 
                    return
                if text is not None and text.lower().startswith('回覆群組:'):
                    for x in text[5:].split():
                        if x not in ban['reply']:
                            ban['reply'][x] = False
                            backupData()
                if text and text.lower() == '確認回覆群組':
                    if not ban["reply"]:
                        cl.sendMessage(to, "没有群组")
                    else:
                        noo = 0
                        mc = "名單："
                        invalid_groups = []
                        for group_id, status in ban["reply"].items():
                            try:
                                group_name = cl.getGroup(group_id).name
                                noo += 1
                                mc += f"\n{noo}. Group ID: {group_id}, Name: {group_name}, Status: {'開啟' if status else '關閉'}"
                            except Exception as e:
                                print(f"Error when getting group info: {e}")
                                invalid_groups.append(group_id)
                        cl.sendMessage(to, mc)
                        for group_id in invalid_groups:
                            del ban["reply"][group_id]
                        backupData()
                    cl.relatedMessage(to, "完成", op.message.id)
                if text and text.lower() == '群組網址':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = cl.reissueGroupTicket(to)
                            cl.relatedMessage(to, "• 群組網址:\nhttps://line.me/R/ti/g/{}".format(str(ticket)),op.message.id)
                if text and text.lower() == '開網址':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            cl.relatedMessage(to, "群組網址本來就沒關",op.message.id)
                        else:
                            group.preventedJoinByTicket = False
                            cl.updateGroup(group)
                            cl.relatedMessage(to, "群組網址已開啟",op.message.id)
                if text and text.lower() == '關網址':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            cl.relatedMessage(to, "群組網址本來就沒開",op.message.id)
                        else:
                            group.preventedJoinByTicket = True
                            cl.updateGroup(group)
                            cl.relatedMessage(to, "群組網址已關閉",op.message.id)
                elif text and text.lower() == '特殊登入':
                    cl.sendMessage(to,"login..")
                elif text and text.lower() == '特殊重啟':
                    cl.sendMessage(to,"準備重啟..")
                elif text and text.lower() == '特殊測速':
                    cl.sendMessage(to,"sptest")
                if text is not None and text.lower().startswith("爽邀通 "):
                    if msg.toType == 2:
                        sep = msg.text.split(" ")
                        resp = msg.text.replace(sep[0] + " ","")
                        num = int(resp)
                    try:
                        cl.sendReplyMessage(msg.id,to,"開始動作....")
                    except:
                        pass
                    for var in range(num):
                        group = cl.getGroup(msg.to)
                        members = [mem.mid for mem in group.members]
                        cl.acquireGroupCallRoute(msg.to)
                        cl.inviteIntoGroupCall(msg.to, contactIds=members)
                        time.sleep(1)
                    cl.sendReplyMessage(msg.id,to,"完成囉")
                if text is not None and text.lower().startswith("call"):
                    call_ = msg.text.split(":")
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    x = call_[2]
                    z = int(call_[1])
                    start = time.time()
                    cl.relatedMessage(to,"開始動作...",op.message.id)
                    if (z > 30):
                        z = 30
                        cl.sendMessage(to, "最多30次")
                        for z in range(z):
                            botwww.inviteIntoGroupCall(to, [inkey])
                            time.sleep(1)
                    else:
                        for z in range(z):
                            botwww.inviteIntoGroupCall(to, [inkey])
                            time.sleep(1)
                    elapsed_time = time.time() - start
                    cl.relatedMessage(to,"成功邀請通話{}次".format(z+1)+"\n花費了 {} 秒".format(str(elapsed_time)),op.message.id)
                # ----rebot
                if text is not None and text.lower().startswith("reb "):
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(
                            msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        if clMID in lists:
                            contact1 = cl.getContact(sender)
                            group = cl.getGroup(to)
                            backupData()
                            # cl.sendMessage(ggg, "【"+contact1.displayName + "】重啟了機器\n群組名稱: " + str(
                            # group.name) + "\n群組MID: " + str(group.id) + "\n重啟者MID: " + contact1.mid)
                            cl.relatedMessage(
                                msg.to, "重新啟動中...", op.message.id)
                            restartBot()
                        else:
                            pass
                elif text and text.lower() == '無視列表':#無視名單
                    if not ig["ig"]:cl.relatedMessage(to,"沒有人被無視",msg_id) 
                    else:
                        no = 1;mc = "無視名單如下：";dm = []
                        for i,mi_d in enumerate(ig["ig"]):
                            try:mc +=f"\n{i+1}.{cl.getContact(mi_d).displayName}\n({mi_d})"
                            except:mc+=f"\n{i+1}.此人砍帳了\n({mi_d})";dm.append(mi_d)
                        cl.relatedMessage(to,mc,msg_id)
                        if dm:
                            for x in dm:ig["ig"].remove(x)
                            json.dump(ig,codecs.open("ig.json","w","utf-8"), sort_keys=True, indent=4, ensure_ascii=False)
                            cl.sendMessage(ban["dio"],"砍帳名單刪除完畢")
                if text is not None and text.lower().startswith("無視 ") and 'MENTION' in msg.contentMetadata.keys()!= None:#標記增加無視
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    list1 = [];list2 = [];ret_ = "〖無視新增成功〗";rat_ = "\n〖無視新增失敗〗";a = 1;b = 1
                    for x in MENTION['MENTIONEES']:
                        if x["M"] not in ig["ig"]:ig["ig"].append(x["M"]);list1.append(x["M"])
                        else:list2.append(x["M"])
                    json.dump(ig,codecs.open("ig.json","w","utf-8"), sort_keys=True, indent=4, ensure_ascii=False)
                    if not list1:ret_ += "\n• 無"
                    else:
                        for c in list1:ret_ +=f"\n{a}.{cl.getContact(c).displayName}";a += 1
                    if list2:rat_ += "\n• 無"
                    else:
                        for d in list2:rat_ +=f"\n{b}.{cl.getContact(d).displayName}";b += 1
                    cl.sendMessage(to,str(ret_)+str(rat_))
                if text is not None and text.lower().startswith("刪無視 "):#標記刪除無視
                    if msg.contentMetadata:
                        MENTION = eval(msg.contentMetadata['MENTION'])
                        list1 = [];list2 = [];ret_ = "〖無視刪除成功〗";rat_ = "\n〖無視刪除失敗〗";a = 1;b = 1
                        for x in MENTION['MENTIONEES']:
                            if x["M"] in highest or x["M"] in ban["owners"]:list2.append(x["M"])
                            elif x["M"] in ig["ig"]:ig["ig"].remove(x["M"]);list1.append(x["M"])
                            else:list2.append(x["M"])
                        json.dump(ig,codecs.open("ig.json","w","utf-8"), sort_keys=True, indent=4, ensure_ascii=False)
                        if not list1:ret_ += "\n• 無"
                        else:
                            for c in list1:ret_ +=f"\n{a}.{cl.getContact(c).displayName}";a += 1
                        if not list2:rat_ += "\n• 無"
                        else:
                            for d in list2:rat_ +=f"\n{b}.{cl.getContact(d).displayName}";b += 1
                        cl.sendMessage(to,str(ret_)+str(rat_))
                    else:
                        separate = text.split(" ")
                        input1 = text.replace(separate[0] + " ","")
                        sep = input1.split(" ")
                        newcancellist = sorted(sep)
                        canceldata = []
                        for x in newcancellist:
                            try:middata = ig["ig"][(int(x)-1)];canceldata.append(middata)
                            except:cl.sendMessage(to, "刪除失敗")
                        for c in canceldata:
                            if c in highest:cl.sendMessage(to, "此人為最大權限 無法刪除")
                            else:
                                ig["ig"].remove(c)
                                try:gn = cl.getContact(c).displayName
                                except:gn="此人已砍帳"
                                cl.relatedMessage(to,f"已刪除:{gn}\nMID:{c}",msg_id)
                        json.dump(ig, codecs.open('ig.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False)
                if text is not None and text.lower().startswith("抽籤 "):
                    inputs = msg.text.split(" ")
                    if len(inputs) < 3:
                        cl.sendMessage(to, "格式錯誤，請輸入「抽籤 獎品 抽獎人1 抽獎人2 ...」")
                    else:
                        prize = inputs[1]
                        contestants = inputs[2:]
                        winner = random.choice(contestants)
                        result = "獎品: {}\n抽到的人: {}".format(prize, winner)
                        cl.sendMessage(to, result)
                elif text and text.lower() == '儲存':
                    backupData()
                    cl.relatedMessage(to, "儲存設定成功!", op.message.id)
                    #後台檔案
                elif text and text.lower() == '後台儲存':
                    ret_ = "【 伺服器存檔 】"
                    base_path = '/root/login2/allsave'
                    categories = {'image': '張圖片', 'sound': '則語音', 'file': '個檔案', 'video': '部影片'}
                    for category, unit in categories.items():
                        count = count_files(os.path.join(base_path, category))
                        ret_ += f"\n{category.capitalize()}儲存數量：{count} {unit}"
                    cl.relatedMessage(to, str(ret_), op.message.id) 
                elif text and text.lower() == 'data':#data抓資訊
                    if msg.relatedMessageId:
                        try:
                            for x in cl.getRecentMessagesV2(to,1000):
                                if x.id == msg.relatedMessageId:
                                    cl.relatedMessage(to,str(x),msg_id)
                                    break
                        except:
                            cl.relatedMessage(to,"查詢失敗",msg_id)
                    else:
                        cl.relatedMessage(to,"需回覆訊息來查詢",msg_id)
                elif text and text.lower() == "退下":  # 退當前群組
                    try:
                        cl.leaveGroup(to)
                    except:
                        pass
                elif text and text.lower() == '清群1':
                    group_ids = cl.getGroupIdsJoined()
                    if set(group_ids) == {ggg}:
                        cl.sendMessage(to, "沒有其他群組需要退出")
                        return
                    for x in group_ids:
                        if x != ggg:
                            group_name = cl.getGroupWithoutMembers(x).name
                            cl.leaveGroup(x)
                            cl.sendMessage(to, "已退出:"+ group_name)
                            time.sleep(2)
                    cl.sendMessage(to, "已退出完畢")
                elif text is not None and text.lower().startswith("退:"):#搜尋群組 當低於不包含自動退群 範例 退:5 會退1234個字的群
                    if text[2:].isdigit():
                        for group in cl.getGroups(cl.getGroupIdsJoined()):
                            if len(group.members) < int(text[2:]):
                                cl.leaveGroup(group.id)
                                cl.sendMessage(to, f'退出{group.name}成功')
                                time.sleep(10)
                        cl.relatedMessage(to,"ok.",op.message.id)
                elif text is not None and text.lower().startswith("離:"):#搜尋群組 當等於數字自動退群 範例 離:5 會退12345個字的群
                    if text[2:].isdigit():
                        for group in cl.getGroups(cl.getGroupIdsJoined()):
                            if len(group.members) <= int(text[2:]):
                                cl.leaveGroup(group.id)
                                cl.sendMessage(to, f'退出{group.name}成功')
                                time.sleep(10)
                        cl.relatedMessage(to,"ok.",op.message.id)
                elif text and text.lower() == '清邀請':
                    gid = cl.getGroupIdsInvited()

                    if not gid:
                        cl.sendMessage(to, "沒有群組邀請需要取消")
                        return
                    num_accepted = 0
                    start_time = time.time()
                    cl.sendMessage(to, f"開始清理邀請群組..\n目前邀請群組數量: {len(gid)}")
                    # List to store the names of the groups
                    group_names = []
                    for i, group_id in enumerate(gid, start=1):
                        cl.acceptGroupInvitation(group_id)
                        # Get group info and store its name
                        group_info = cl.getGroup(group_id)
                        group_names.append(group_info.name)
                        time.sleep(1)
                        cl.leaveGroup(group_id)
                        num_accepted += 1
                        # Take a break after accepting 50 invitations
                        if i % 50 == 0:
                            print("Taking a break...")
                            time.sleep(60)
                            print("Resuming operation...")
                    # Convert the list of group names into a string to include in the message
                    group_names_str = "\n".join(f"{i}. {name}" for i, name in enumerate(group_names, start=1))
                    cl.sendMessage(to, f"已成功取消 {num_accepted} 個群組邀請\n取消的群組有:\n{group_names_str}\n")
                    print("結束")
                elif text is not None and text.lower().startswith("退出:"):
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(
                            msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        if clMID in lists:
                            separate = text.split(":")
                            name = text.replace(separate[0] + ":", "")
                            sep = name.split("_")
                            try:
                                middata = cl.getGroupIdsJoined()[int(sep[0])-1]
                                cl.leaveGroup(middata)
                                gn = cl.getGroup(middata).name
                                cl.sendMessage(
                                    op.message.to, "已退出群組\n群組名稱:\n"+gn)
                            except Exception as e:
                                cl.relatedMessage(
                                    receiver, "退出群組失敗\n失敗原因：\n"+str(e), op.message.id)
                elif text and text.lower() == '監控 開':
                    ban["pcmsrd"] = True
                    cl.relatedMessage(to, "私聊監控已開啟", op.message.id)
                elif text and text.lower() == '監控 關':
                    ban["pcmsrd"] = False
                    cl.relatedMessage(to, "私聊監控已關閉", op.message.id)
                elif text and text.lower() == '同步好友群組':
                    cl.sendMessage(
                        to, "https://line.me/R/manualrepair/?category=friendsandgroups&closeModals=false")
                elif text and text.lower() == '同步檔案設定':
                    cl.sendMessage(
                        to, "https://line.me/R/manualrepair/?category=profilesandettingsandconfigs&closeModals=false")
                elif text and text.lower() == '資料':
                    system_info = get_system_information(ban["midInformation"], ban["useflex"])
                    cl.relatedMessage(to, system_info, op.message.id) 
                elif text and text.lower() == "#資料":
                    x = cl.getProfile()
                    cl.sendMessage(receiver,"【簡介信息】\n名稱：%s\n辨識碼：%s\n用戶id：%s\nPhone Number：%s\nE-Mail：%s\nRegion Code：%s\nThumbnail Url：%s\nAllow Search By Userid：%s\nAllow Search By Email：%s\nPicture Url：\nhttps://profile.line-scdn.net%s\nMusic Profile：%s\nVideo Profile：%s" % (x.displayName, x.mid, x.userid, x.phone, x.email, x.regionCode, x.thumbnailUrl, x.allowSearchByUserid, x.allowSearchByEmail, x.picturePath, x.musicProfile, x.videoProfile))
                elif text is not None and text.lower().startswith("標記 "):
                    x = text.split(' ')
                    for c in range(int(x[1])):
                        cl.sendMessage(to, "@All ", contentMetadata={'NOTIFICATION_DISABLED': 'null', 'MENTION': '{"MENTIONEES":[{"S":"0","E":"4","A":"1"}]}', 'app_extension_type': 'null', 'PREVIEW_URL_ENABLED': 'true', 'app_version_code': '121410255'}, contentType=0)
                        time.sleep(1)
                elif text and text.lower() == '標記':
                    cl.sendMessage(to, "@All ", contentMetadata={'NOTIFICATION_DISABLED': 'null', 'MENTION': '{"MENTIONEES":[{"S":"0","E":"4","A":"1"}]}', 'app_extension_type': 'null', 'PREVIEW_URL_ENABLED': 'true', 'app_version_code': '121410255'}, contentType=0)
                #偵測到關鍵字就會標記
                #elif "標記" in msg.text:
                    #cl.sendMessage(to, "@All ", contentMetadata={'NOTIFICATION_DISABLED': 'null', 'MENTION': '{"MENTIONEES":[{"S":"0","E":"4","A":"1"}]}', 'app_extension_type': 'null', 'PREVIEW_URL_ENABLED': 'true', 'app_version_code': '121410255'}, contentType=0)
                elif text and text.lower() == '狀態':
                    ret_="規制查詢"
                    try:cl.kickoutFromGroup(to, ["Fuck you"])
                    except Exception as e:
                        if e.reason == "request blocked":ret_ += "\n• 踢人狀態 : 規制中\n• 邀請狀態 : 規制中"
                        else:ret_ += "\n• 踢人狀態 : 可以執行\n• 邀請狀態 : 可以執行"
                    try:cl.cancelGroupInvitation(to, ["Fuck you"])
                    except Exception as e:
                        if e.reason == "request blocked":ret_ += "\n• 取消狀態 : 規制中"
                        else:ret_ += "\n• 取消狀態 : 可以執行"
                    try:cl.findAndAddContactsByMid("ue1d1762de95bc0fd9b9e4e309436353f");ret_ += "\n• 加友狀態 : 可以執行"
                    except Exception as e:
                        if e.reason == "request blocked":ret_ += "\n• 加友狀態 : 規制中"
                    cl.relatedMessage(to, ret_,msg_id)
                elif msg.text and msg.text.lower().startswith("封鎖 "):
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(
                            msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            cl.blockContact(ls)
                        cl.sendMessage(to, "已封鎖")
                elif msg.text and msg.text.lower().startswith("解封鎖:"):
                    targets = msg.text.lower().replace("解封鎖:", "").split(",")
                    unblocked_users = []
                    for target in targets:
                        contacts = cl.getContacts([target])
                        if contacts:
                            cl.unblockContact(target)
                            unblocked_users.append(contacts[0].displayName)
                    if unblocked_users:
                        cl.sendMessage(to, "已解除封鎖 {}".format(", ".join(unblocked_users)))
                elif msg.text and msg.text.lower().startswith("封鎖:"):
                    targets = msg.text.lower().replace("封鎖:", "").split(",")
                    blocked_users = []
                    for target in targets:
                        contacts = cl.getContacts([target])
                        if contacts:
                            cl.blockContact(target)
                            blocked_users.append(contacts[0].displayName)
                    if blocked_users:
                        cl.sendMessage(to, "已封鎖 {}".format(", ".join(blocked_users)))
                elif msg.text and msg.text.lower().startswith("刪除好友:"):
                    targets = msg.text.lower().replace("刪除好友:", "").split(",")
                    removed_friends = []
                    for target in targets:
                        cl.deleteContact(target)
                        user = cl.getContact(target)
                        removed_friends.append(user.displayName)
                    cl.sendMessage(to, "已刪除好友 {}".format(", ".join(removed_friends)))
                elif text is not None and text.lower().startswith("xx:"):
                    anlian = cl
                    sep = msg.text.split(":")
                    query = msg.text.replace(sep[0] + ":", "")
                    cond = query.split("|")
                    search = str(cond[0])
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        r = s.get(
                            "https://www.xvideos.com/?k={}".format(str(search)))
                        soup = BeautifulSoup(r.content, 'html5lib')
                        data = soup.findAll('div', attrs={'class': 'thumb'})
                        if len(cond) == 1:
                            num = 0
                            ret_ = "• 搜索結果"
                            for a in data:
                                num += 1
                                link = "\nhttps://www.xvideos.com" + \
                                    a.find('a')['href']
                                ret_ += "\n• {}. {}".format(str(num),
                                                            str(link))
                            ret_ += "\n總共推薦 {} 個影片".format(str(len(data)))
                            anlian.sendMessage(to, str(ret_))

                elif text and text.lower() == '好友名單':  # 好友列表顯示MID
                    allmid = cl.getAllContactIds()
                    contactlist = cl.getContacts(allmid)
                    ret = "好友列表如下:"
                    count = 0
                    no = 1
                    for g in contactlist:
                        ret += "\n" + \
                            str(no) + ":" + cl.getContact(g.mid).displayName + \
                            "\n" + str(g.mid)
                        count += 1
                        no += 1
                        if count == 100:
                            cl.sendMessage(to, ret)
                            ret = "好友列表如下:"
                            count = 0
                    cl.sendMessage(to, ret)

                elif text and text.lower() == 'v備份好友v':  # 好友列表顯示MID
                    allmid = cl.getAllContactIds()
                    contactlist = cl.getContacts(allmid)
                    ret = "好友列表如下:"
                    count = 0
                    no = 1
                    for g in contactlist:
                        ret += "\n" + \
                            str(no) + ":" + cl.getContact(g.mid).displayName + \
                            "\n" + str(g.mid)
                        count += 1
                        no += 1
                        if count == 100:
                            cl.sendMessage(to, ret)
                            ret = "好友列表如下:"
                            count = 0
                    cl.sendMessage(to, ret)
                    # 创建好友名单备份文本文件
                    file_name = cl.profile.displayName + "的好友名單備份.txt"
                    with open(file_name, "w", encoding="utf-8") as file:
                        for g in contactlist:
                            file.write(cl.getContact(g.mid).displayName + "\n" + str(g.mid) + "\n")
                    # 发送好友名单备份文本文件
                    cl.sendFile(to, file_name)
                    # 删除备份文本文件
                    os.remove(file_name)

                elif text and text.lower() == 'v群組備份v':
                    groups = cl.getGroupIdsJoined()
                    mc = "• 群組列表"
                    count = 0
                    no = 0
                    for gid in groups:
                        group = cl.getGroup(gid)
                        no += 1
                        count += 1
                        mc += "\n{}. {} ( {} 人) [GID: {}]".format(str(no), str(group.name), str(len(group.members)),str(group.id))
                        if count == 100:
                            cl.sendMessage(msg.to, mc)
                            count = 0
                    cl.relatedMessage(to, mc + "\n總計 {} 個群組".format(str(len(groups))), op.message.id)
                    # 创建群组名单备份文本文件
                    file_name = cl.profile.displayName + "的群組名單備份.txt"
                    with open(file_name, "w", encoding="utf-8") as file:
                        for gid in groups:
                            group = cl.getGroup(gid)
                            file.write("{} ( {} 人) [GID: {}]\n".format(group.name, len(group.members), gid))
                    # 发送群组名单备份文本文件
                    cl.sendFile(to, file_name)
                    # 删除备份文本文件
                    os.remove(file_name)

                elif text is not None and text.lower().startswith("備份:"):
                    gid = text[3:]  # 提取群组ID
                    group = cl.getGroup(gid)
                    # 备份群组成员
                    member_file = group.name + "_成員名單.txt"
                    with open(member_file, "w", encoding="utf-8") as file:
                        file.write("【 {}的成员名单 】\n".format(group.name))
                        if group.members is not None:
                            for num, member in enumerate(group.members, 1):
                                file.write("{}. {}\n{}\n".format(num, member.displayName, member.mid))
                    # 备份邀请成员
                    invitee_file = group.name + "_邀请名单.txt"
                    with open(invitee_file, "w", encoding="utf-8") as file:
                        file.write("【 {}的邀请名单 】\n".format(group.name))
                        if group.invitee is not None:
                            for num, invitee in enumerate(group.invitee, 1):
                                file.write("{}. {}\n{}\n".format(num, invitee.displayName, invitee.mid))
                    # 发送备份文件
                    cl.sendFile(to, member_file)
                    cl.sendFile(to, invitee_file)
                    # 删除备份文件
                    os.remove(member_file)
                    os.remove(invitee_file)

                elif text and text.lower() == '封鎖名單':
                    blocked_ids = cl.getBlockedContactIds()
                    if len(blocked_ids) == 0:
                        cl.sendMessage(to, "封鎖名單為空")
                    else:
                        blocked_list = cl.getContacts(blocked_ids)
                        ret = "封鎖名單如下:"
                        count = 0
                        no = 1
                        for contact in blocked_list:
                            ret += "\n" + str(no) + ": " + contact.displayName + "\n" + contact.mid
                            count += 1
                            no += 1
                            if count == 100:
                                cl.sendMessage(to, ret)
                                ret = "封鎖名單如下:"
                                count = 0
                        cl.sendMessage(to, ret)
                elif text is not None and text.lower().startswith('搜好友:'):
                    keyword = text[4:].strip()  # 取得關鍵字
                    allmid = cl.getAllContactIds()
                    contactlist = cl.getContacts(allmid)
                    ret = f"搜尋結果如下: \n找不到符合關鍵字 「{keyword}」 的好友。"
                    count = 0
                    no = 1
                    found = False  # 標記是否找到相符的好友
                    for g in contactlist:
                        if keyword.lower() in cl.getContact(g.mid).displayName.lower():
                            if not found:
                                ret = f"搜尋結果如下: \n找到符合關鍵字 「{keyword}」 的好友："
                                found = True  # 找到相符的好友
                            ret += "\n" + str(no) + ":" + cl.getContact(g.mid).displayName + "\n" + str(g.mid)
                            count += 1
                            no += 1
                            if count == 100:
                                cl.sendMessage(to, ret)
                                ret = f"搜尋結果如下: \n找不到符合關鍵字 「{keyword}」 的好友。"
                                count = 0
                    cl.sendMessage(to, ret)
                elif text is not None and text.lower().startswith("加三級 ") and "MENTION" in op.message.contentMetadata:
                    key = eval(msg.contentMetadata["MENTION"])
                    yi = "【成功新增權限】"
                    ono = 0
                    fuck = 0
                    greg = "\n【新增權限失敗】"
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        if x["M"] not in ban["owners"]:
                            ban["owners"].append(x["M"])
                            ono += 1
                            yi += "\n"+str(ono)+"." + \
                                cl.getContact(x["M"]).displayName
                        else:
                            fuck += 1
                            greg += "\n"+str(fuck)+"." + \
                                cl.getContact(x["M"]).displayName
                    if ono == 0:
                        yi += "\n • 無名單"
                    if fuck == 0:
                        greg += "\n • 無名單"
                    mc = yi+greg
                    cl.sendMessage(to, mc)
                    json.dump(ban, codecs.open('ban.json', 'w', 'utf-8'),
                              sort_keys=True, indent=4, ensure_ascii=False)
                elif text is not None and text.lower().startswith("刪三級 "):
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        inkey = key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            if x["M"] in ban["owners"]:
                                ban["owners"].remove(x["M"])
                                cl.relatedMessage(to, "已取消權限！", op.message.id)
                            else:
                                cl.relatedMessage(to, "本來就沒權限", op.message.id)
                        json.dump(ban, codecs.open('ban.json', 'w', 'utf-8'),
                                  sort_keys=True, indent=4, ensure_ascii=False)
                elif text is not None and text.lower().startswith("刪除三級 "):
                    input1 = op.message.text.replace("刪除三級 ", "")
                    sep = input1.split(" ")
                    newcancellist = sorted(sep)
                    canceldata = []
                    for x in newcancellist:
                        try:
                            middata = ban["owners"][(int(x)-1)]
                            canceldata.append(middata)
                        except:
                            cl.sendMessage(op.message.to, "刪除失敗")
                    for c in canceldata:
                        ban["owners"].remove(c)
                        gn = cl.getContact(c).displayName
                        cl.sendMessage(op.message.to, "已刪除✘" +
                                       gn + "\n" + middata)
                        backupData()
                elif text is not None and text.lower().startswith("加二級 ") and "MENTION" in op.message.contentMetadata:
                    key = eval(msg.contentMetadata["MENTION"])
                    yi = "【成功新增權限】"
                    ono = 0
                    fuck = 0
                    greg = "\n【新增權限失敗】"
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        if x["M"] not in ban["admin"]:
                            ban["admin"].append(x["M"])
                            ono += 1
                            yi += "\n"+str(ono)+"." + \
                                cl.getContact(x["M"]).displayName
                        else:
                            fuck += 1
                            greg += "\n"+str(fuck)+"." + \
                                cl.getContact(x["M"]).displayName
                    if ono == 0:
                        yi += "\n • 無名單"
                    if fuck == 0:
                        greg += "\n • 無名單"
                    mc = yi+greg
                    cl.sendMessage(to, mc)
                    json.dump(ban, codecs.open('ban.json', 'w', 'utf-8'),
                              sort_keys=True, indent=4, ensure_ascii=False)
                elif text is not None and text.lower().startswith("刪二級 "):
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        inkey = key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            if x["M"] in ban["admin"]:
                                ban["admin"].remove(x["M"])
                                cl.relatedMessage(to, "已取消權限！", op.message.id)
                            else:
                                cl.relatedMessage(to, "本來就沒權限", op.message.id)
                        json.dump(ban, codecs.open('ban.json', 'w', 'utf-8'),
                                  sort_keys=True, indent=4, ensure_ascii=False)
                elif text is not None and text.lower().startswith("刪除二級 "):
                    input1 = op.message.text.replace("刪除二級 ", "")
                    sep = input1.split(" ")
                    newcancellist = sorted(sep)
                    canceldata = []
                    for x in newcancellist:
                        try:
                            middata = ban["admin"][(int(x)-1)]
                            canceldata.append(middata)
                        except:
                            cl.sendMessage(op.message.to, "刪除失敗")
                    for c in canceldata:
                        ban["admin"].remove(c)
                        gn = cl.getContact(c).displayName
                        cl.sendMessage(op.message.to, "已刪除✘" +
                                       gn + "\n" + middata)
                        backupData()
                elif text and text.lower() == '收':
                    if hasattr(msg, 'relatedMessageId') and msg.relatedMessageId is not None:
                        cl.unsendMessage(msg.relatedMessageId)
                elif text is not None and text.lower().startswith('un'):  # 收回指定數量訊息
                    try:
                        args = text.split(' ')
                        mes = 0
                        try:
                            mes = int(args[1])
                        except:
                            mes = 1
                        M = cl.getRecentMessagesV2(to, 1001)
                        MId = []
                        for ind, i in enumerate(M):
                            if ind == 0:
                                pass
                            else:
                                if i._from == clMID:
                                    MId.append(i.id)
                                    if len(MId) == mes:
                                        break
                        def unsMes(id):
                            cl.unsendMessage(id)
                        for i in MId:
                            thread1 = threading.Thread(
                                target=unsMes, args=(i,))
                            thread1.start()
                            thread1.join()
                    except:
                        pass
                elif text is not None and text.lower().startswith("改名:"):
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(
                            msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        if clMID in lists:
                            separate = text.split(":")
                            string = text.replace(separate[0] + ":", "")
                            name = string.split("_")
                            c = cl.getProfile()
                            c.displayName = name[0]
                            cl.updateProfile(c)
                            cl.sendMessage(to, "名稱已更改為 :	 \n" + name[0])
                elif text is not None and text.lower().startswith("改簽名:"):
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(
                            msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        if clMID in lists:
                            separate = text.split(":")
                            name = text.replace(separate[0] + ":", "")
                            sep = name.split("_")
                            try:
                                c = cl.getProfile()
                                c.statusMessage = sep[0]
                                cl.updateProfile(c)
                                cl.sendMessage(to, "個簽成功更改為：\n"+str(sep[0]))
                            except Exception as e:
                                cl.relatedMessage(
                                    receiver, "更改個簽失敗\n失敗原因：\n"+str(e), op.message.id)
                elif text and text.lower() == '自動鎖 開':
                    ban["autoblock"] = True
                    cl.relatedMessage(to, "自動封鎖已開啟 ✔",op.message.id)  
                elif text and text.lower() == '自動鎖 關':
                    ban["autoblock"] = False
                    cl.relatedMessage(to, "自動封鎖已關閉 ✘",op.message.id)
                elif text is not None and text.lower().startswith("1cgni "):
                    lg = msg.text.replace("cgni ","")
                    cl.sendMessage(to,"處理中...")
                    aa = cl.getGroupIdsByNameFrominv(lg)
                    mes = "\n取消的群組名稱\n"
                    no = 0
                    for x in aa:
                        mes += cl.getGroup(x).name+"\n"
                    cl.sendMessage(to,"總共有" + str(len(aa)) + "個群符合要求")
                    cl.sendMessage(to,"取消這些群組邀請中...")
                    for x in aa:
                        cl.acceptGroupInvitation(x)
                        time.sleep(1)
                        cl.leaveGroup(x)
                        time.sleep(1)
                        no += 1
                        if no == 50:
                            print("Cool Time")
                            time.sleep(60)
                            no = 0
                            print("動作繼續")
                    cl.sendMessage(to,"成功取消這些群組\n"+ mes)
                elif text is not None and text.lower().startswith("1tgni "):
                    lg = msg.text.replace("tgni ","")
                    cl.sendMessage(to,"處理中...")
                    aa = cl.getGroupIdsByName(lg)
                    mes = "\n退出的群組名稱\n"
                    for x in aa:
                        mes += cl.getGroup(x).name+"\n"
                    cl.sendMessage(to,"總共有" + str(len(aa)) + "個群符合要求")
                    cl.sendMessage(to,"退出這些群組中...")
                    for x in aa:
                        cl.sendMessage(x,'收到退群指令...')
                        cl.leaveGroup(x)
                    cl.sendMessage(to,"成功退出這些群組囉\n"+ mes)
                elif text is not None and text.lower().startswith("設定 "):
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(
                            msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        if clMID in lists:
                            ban["announcement"][to] = False
                            ban["groupcall"][op.param1] = False
                            cl.sendMessage(to, "群組資料初始化完成")
                elif text is not None and text.lower().startswith("deltext:"):
                    G = cl.getGroup(to)
                    rep = text.replace("deltext:", "")
                    if rep in rpy["orgrpy"]:
                        reply = rpy["orgrpy"]["{}".format(rep)]
                        del rpy["orgrpy"]["{}".format(rep)]
                        cl.sendMessage(
                            to, "此回覆已刪除\n偵測：{}\n回覆：{}".format(rep, reply))
                        backupData()
                    else:
                        cl.sendMessage(to, "沒有這個關鍵字回覆呢")
                elif text is not None and text.lower().startswith("delpic:"):
                    ieggm = op.message.text.replace("delpic:", "")
                    if ieggm == "":
                        cl.sendMessage(to, "請輸入移除圖片關鍵字")
                    elif ieggm not in rpy["pic"]:
                        cl.sendMessage(to, "找不到此關鍵字回復圖片")
                    else:
                        del rpy["pic"][ieggm.lower()]
                        ddddd = ieggm+".jpg"
                        os.remove("/root/"+Backstage+"/picsave/"+ddddd)
                        cl.sendMessage(to, "回復圖片刪除完成")
                if text is not None and text.lower().startswith("delcot:"):
                    con = text.replace("delcot:", "")
                    try:
                        conrpy = rpy["contact"]["{}".format(con)]
                        cl.sendMessage(to, "此回覆友資已刪除\n{}".format(con))
                        cl.sendContact(to, str(conrpy))
                        del rpy["contact"]["{}".format(con)]
                        backupData()
                    except:
                        cl.sendMessage(to, "沒有這個友資回覆呢...")
                elif text is not None and text.lower().startswith("群組"):
                    if msg.contentMetadata:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(
                            msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        if clMID in lists:
                            groups = cl.getGroupIdsJoined()
                            #cl.relatedMessage(msg.to, "以下是群組列表", op.message.id)
                            mc = "【 群組列表 】"
                            count = 0
                            no = 0
                            for gid in groups:
                                group = cl.getGroup(gid)
                                no += 1
                                count += 1
                                mc += "\n{}. {} ( {} 人)\n群組ID:{}\n".format(str(no), str(
                                    group.name), str(len(group.members)), str(group.id))
                                if count == 100:
                                    cl.sendMessage(msg.to, mc)
                                    count = 0
                                    mc = "【 群組列表 】"
                            cl.relatedMessage(
                                to, mc + "\n【 總計 {} 個群組 】".format(str(len(groups))), op.message.id)
                elif text is not None and text.lower().startswith("搜群組:"):
                    keyword = text[4:].strip()
                    groups = cl.getGroupIdsJoined()
                    count = 0
                    result = "以下是群組列表 (含有 '{}' )\n".format(keyword)
                    for gid in groups:
                        group = cl.getGroup(gid)
                        if keyword in group.name:
                            count += 1
                            result += "{}. {} ({} 人)\n".format(str(count), group.name, len(group.members))
                            if count == 100:
                                cl.sendMessage(msg.to, result)
                                count = 0
                                result = ""
                    if count > 0:
                        result += "總計 {} 個群組".format(str(count))
                    else:
                        result = "找不到符合的群組"
                    cl.relatedMessage(msg.to, result, op.message.id)
                elif text is not None and text.lower().startswith("換封面 "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    home = cl.getProfileDetail(inkey)
                    objectId = home["result"]["objectId"]
                    cl.updateProfileCoverById(objectId)
                    cl.relatedMessage(to, "更換封面成功", op.message.id)
                elif text is not None and text.lower().startswith("換封面:"):
                    home = cl.getProfileDetail(text[4:])
                    objectId = home["result"]["objectId"]
                    cl.updateProfileCoverById(objectId)
                    cl.relatedMessage(to, "更換封面成功", op.message.id)
                elif text and text.lower() == '最大指令':  # 最大指令 help
                    if ban["useflex"] == False:
                        cl.relatedMessage(to, help4(), msg_id)
                    else:
                        data = {
                            "type": "flex",
                            "altText": "hao bot",
                            "contents":{
"type": "bubble",
"body": {
"type": "box",
"layout": "vertical",
"contents": [
  {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "hao hleper",
        "align": "center",
        "size": "xxs",
        "color": "#888888"
      },
      {
        "type": "text",
        "text": "指令表",
        "align": "center",
        "size": "lg",
        "weight": "bold",
        "color": "#ff0000",
        "decoration": "underline"
      }
    ],
    "offsetBottom": "sm"
  },
  {
    "type": "separator",
    "color": "#000000"
  },
  {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": help4(),
        "color": "#0000cc",
        "align": "center",
        "wrap": True
      }
    ],
    "offsetTop": "sm"
  }
]
},
"size": "kilo"
}
                        }
                        sendflex(to, data)
                elif text and text.lower() == '..':
                        data = {
                            "type": "flex",
                            "altText": "hao bot",
                            "contents":{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "kilo",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.pinimg.com/564x/4a/f7/7a/4af77acd31f23ef79cfcd5ca0cca1d4a.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "哈囉",
                    "size": "xxl",
                    "color": "#e31bcc",
                    "weight": "bold",
                    "align": "center"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "--",
                    "align": "center",
                    "color": "#e31bcc"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "text",
                        "text": "案我沒東西",
                        "color": "#e31bcc",
                        "flex": 0,
                        "offsetTop": "-2px"
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "spacing": "sm"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "borderWidth": "1px",
                "cornerRadius": "4px",
                "spacing": "sm",
                "borderColor": "#e31bcc",
                "margin": "xxl",
                "height": "40px",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "line://app/1657024923-2r46WKKN?auto=yes&type=text&text=%E6%88%91%E6%98%AF%E5%82%BB%E9%80%BC"
                }
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
            "backgroundColor": "#ede9f7cc",
            "paddingAll": "20px",
            "paddingTop": "18px"
          }
        ],
        "paddingAll": "0px"
      }
    },
    {
      "type": "bubble",
      "size": "kilo",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.pinimg.com/564x/e2/6d/7f/e26d7f3ca65709a180d523e679bd9b39.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "網站",
                    "size": "xxl",
                    "color": "#e31bcc",
                    "weight": "bold",
                    "align": "center"
                  }
                ]
              },
              {
                "type": "text",
                "text": "--",
                "align": "center",
                "color": "#ede9f7"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "text",
                        "text": "點我去網站",
                        "color": "#e31bcc",
                        "flex": 0,
                        "offsetTop": "-2px"
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "spacing": "sm"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "borderWidth": "1px",
                "cornerRadius": "4px",
                "spacing": "sm",
                "borderColor": "#e31bcc",
                "margin": "xxl",
                "height": "40px",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://haoline.fans.link/hhline"
                  #"uri": "line://app/1657024923-2r46WKKN?auto=yes&type=text&text=編碼"
                }
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
            "backgroundColor": "#ede9f7cc",
            "paddingAll": "20px",
            "paddingTop": "18px"
          }
        ],
        "paddingAll": "0px"
      }
    }
  ]
}
                        }
                        sendflex(to, data)
                elif text is not None and text.lower().startswith("yt "):
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q={}&type=video&key=AIzaSyBKgLzhgkpoa0e7sKYJOVlTIejJLVyKclg".format(str(search)))
                    data = r.text
                    a = json.loads(data)
                    if 'items' in a:
                        if a["items"] != []:
                            ret_ = []
                            yt = []
                            for music in a["items"]:
                                ret_.append({
                                        "type": "bubble",
                                          "hero": {
                                            "type": "image",
                                            "url": "https://i.ytimg.com/vi/{}/maxresdefault.jpg".format(music['id']['videoId']),
                                            "size": "full",
                                            "aspectRatio": "20:13",
                                            "aspectMode": "cover",
                                            "action": {
                                              "type": "uri",
                                              "uri": "https://www.youtube.com/watch?v=%s" % music['id']['videoId']
                                            }
                                          },
                                          "body": {
                                            "type": "box",
                                            "layout": "vertical",
                                            "spacing": "xs",
                                            "contents": [
                                              {
                                                "type": "text",
                                                "text": "「 影片名稱 」",
                                                "wrap": True,
                                                "weight": "bold",
                                                "color": "#000000",
                                                "align": "center",
                                                "size": "md",
                                                "flex": 2
                                              },
                                              {
                                                "type": "separator",
                                                "color": "#000000"
                                              },
                                              {
                                                "type": "text", 
                                                "text": "%s" % music['snippet']['title'],
                                                "color": "#000000",
                                                "wrap": True,
                                                "weight": "bold",
                                                "align": "center",
                                                "size": "xs",
                                                "action": {
                                                  "type": "uri",
                                                  "uri":  "https://www.youtube.com/watch?v=%s" % music['id']['videoId']
                                                }
                                              }
                                            ]
                                          },
                                          "styles": {"body": {"backgroundColor": "#ffffffcc"},
                                        }
                                    }
                                )
                                yt.append('https://www.youtube.com/watch?v=' +music['id']['videoId'])
                            k = len(ret_)//10
                            for aa in range(k+1):
                                data = {
                                    "type": "flex",
                                    "altText": "hao bot",
                                    "contents": {
                                        "type": "carousel",
                                        "contents": ret_[aa*10 : (aa+1)*10]
                                    }
                                }
                                sendflex(to, data)  
                    else:
                        print("Items not found in data: ", a)

                elif text is not None:
                    lower_text = text.lower()
                    if lower_text.startswith("搜yt "):
                        search = lower_text.replace("搜yt ", "", 1)
                        url = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q={}&type=video&key=AIzaSyBKgLzhgkpoa0e7sKYJOVlTIejJLVyKclg".format(search))
                        data = url.json()
                        videos = data["items"]
                        search_results_map[to] = videos

                        result = "• Youtube Search\n"
                        for i, video in enumerate(videos):
                            result += "\n• {}. {}\n".format(i+1, video["snippet"]["title"])
                        result += "\n• 總共 {} 個影片".format(len(videos))
                        cl.sendMessage(to, result)

                        threading.Timer(10.0, lambda: search_results_map.pop(to, None)).start()
                        print("10秒到了沒有選擇 自動關閉選項功能")

                    elif lower_text.isdigit():
                        num = int(lower_text)
                        if to in search_results_map and 1 <= num <= len(search_results_map[to]):
                            video = search_results_map[to][num - 1]
                            video_id = video["id"]["videoId"]
                            url = requests.get("https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&id={}&key=AIzaSyBKgLzhgkpoa0e7sKYJOVlTIejJLVyKclg".format(video_id))
                            details = url.json()
                            if "items" in details:
                                video_details = details["items"][0]
                                ret_ = "• Youtube Video Info"
                                ret_ += "\n• 影片網址:https://www.youtube.com/watch?v={} ".format(video_id)
                                ret_ += "\n• 發布者: {}".format(str(video_details["snippet"]["channelTitle"]))
                                ret_ += "\n• 影片名稱: {}".format(str(video_details["snippet"]["title"]))
                                ret_ += "\n• 發布日期: {}".format(str(video_details["snippet"]["publishedAt"]))
                                ret_ += "\n• 觀看次數: {}".format(str(video_details["statistics"].get("viewCount", "N/A")))
                                ret_ += "\n• 案喜歡的人: {}".format(str(video_details["statistics"].get("likeCount", "N/A")))
                                ret_ += "\n• 不喜歡的人: {}".format(str(video_details["statistics"].get("dislikeCount", "N/A")))
                                ret_ += "\n• 說明: {}".format(str(video_details["snippet"]["description"]))
                                cl.sendMessage(to, str(ret_))
                                cl.sendImageWithURL(to, str(video_details["snippet"]["thumbnails"]["high"]["url"]))#yt影片封面
                            # Set a timer to delete the search result after 30 seconds
                            threading.Timer(3.0, lambda: search_results_map.pop(to, None)).start()
                            print("3秒到了沒有選擇 自動關閉選項功能")

                elif text is not None and text.lower().startswith("說 "):
                    x = text.split(' ')
                    if len(x) == 2:
                        cl.relatedMessage(to,x[1],op.message.id)
                    elif len(x) == 3:
                        try:
                            c = int(x[2])
                            for c in range(c):
                                cl.sendMessage(to,x[1])
                        except:
                            cl.sendMessage(to,"無法正確執行此指令")

                elif text is not None and text.lower().startswith("system:"):
                    separate = text.split(":")
                    string = text.replace(separate[0] + ":", "")
                    res = []
                    p = subprocess.Popen(
                        string, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
                    p.wait()
                    result_lines = p.stdout.readlines()	  # 从子进程 p 的标准输出中读取所有行，并储存在一个list对象中
                    result = ""
                    for line in result_lines:
                        print(line.strip())
                        result += line.strip()
                        result += "\n"
                    cl.sendMessage(to, result)
                if text.lower().startswith("py "):
                    try:exec(text.replace(f"{text.split(' ')[0]} ", "")); return
                    except Exception as e:cl.relatedMessgae(to,str(e))
                elif text is not None and text.lower().startswith("群組文字廣播:"):
                    bctxt = text.split(':')
                    string = text.replace(bctxt[0] + ":", "")
                    aa = 0
                    for manusia in cl.getGroupIdsJoined():
                        aa += 1
                        cl.sendMessage(manusia, str(string))
                        time.sleep(2)
                    cl.sendMessage(to, "廣播完成 共廣播"+str(aa)+"群")
                elif text is not None and text.lower().startswith("rp "):
                    if msg.relatedMessageId:
                        try:
                            for x in cl.getRecentMessagesV2(to, 1000):
                                if x.id == msg.relatedMessageId and x._from == clMID and x.text.lower().startswith("[私訊監控系統]"):
                                    MENTION = eval(
                                        x.contentMetadata['MENTION'])
                                    for x in MENTION['MENTIONEES']:
                                        cl.sendMessage(x["M"], text[3:])
                                        cl.sendMessage(
                                            to, "已發送訊息給\n【"+cl.getContact(x["M"]).displayName+"】\n內容:"+text[3:])
                                    break
                        except:
                            pass
                    else:
                        pass
                elif text and text.lower() == "rpp":
                    if msg.relatedMessageId:
                        try:
                            for x in cl.getRecentMessagesV2(to, 1000):
                                if x.id == msg.relatedMessageId and x._from == clMID and x.text.lower().startswith("[私訊監控系統]"):
                                    MENTION = eval(
                                        x.contentMetadata['MENTION'])
                                    for x in MENTION['MENTIONEES']:
                                        wait["Speak_remotely"] = {}
                                        wait["Speak_remotely"][to] = {}
                                        wait["Speak_remotely"][to]["mode"] = "pic"
                                        wait["Speak_remotely"][to]["sender"] = sender
                                        wait["Speak_remotely"][to]["msgto"] = "0"
                                        wait["Speak_remotely"][to]["location"] = x["M"]
                                        cl.relatedMessage(
                                            to, "請發送圖片", op.message.id)
                                    break
                        except:
                            pass
                    else:
                        pass
                elif text and text.lower() == "rpv":
                    if msg.relatedMessageId:
                        try:
                            for x in cl.getRecentMessagesV2(to, 1000):
                                if x.id == msg.relatedMessageId and x._from == clMID and x.text.lower().startswith("[私訊監控系統]"):
                                    MENTION = eval(
                                        x.contentMetadata['MENTION'])
                                    for x in MENTION['MENTIONEES']:
                                        wait["Speak_remotely"] = {}
                                        wait["Speak_remotely"][to] = {}
                                        wait["Speak_remotely"][to]["mode"] = "video"
                                        wait["Speak_remotely"][to]["sender"] = sender
                                        wait["Speak_remotely"][to]["msgto"] = "0"
                                        wait["Speak_remotely"][to]["location"] = x["M"]
                                        cl.relatedMessage(
                                            to, "請發送影片", op.message.id)
                                    break
                        except:
                            pass
                    else:
                        pass
                elif text and text.lower() == "rpc":
                    if msg.relatedMessageId:
                        try:
                            for x in cl.getRecentMessagesV2(to, 1000):
                                if x.id == msg.relatedMessageId and x._from == clMID and x.text.lower().startswith("[私訊監控系統]"):
                                    MENTION = eval(
                                        x.contentMetadata['MENTION'])
                                    for x in MENTION['MENTIONEES']:
                                        wait["Speak_remotely"] = {}
                                        wait["Speak_remotely"][to] = {}
                                        wait["Speak_remotely"][to]["mode"] = "contact"
                                        wait["Speak_remotely"][to]["sender"] = sender
                                        wait["Speak_remotely"][to]["msgto"] = "0"
                                        wait["Speak_remotely"][to]["location"] = x["M"]
                                        cl.relatedMessage(
                                            to, "請發送友資", op.message.id)
                                    break
                        except:
                            pass
                    else:
                        pass
                elif text is not None and text.lower().startswith('sendto:'):
                    x = text.split(":")
                    if len(x) >= 2:
                        if isgid(x[1]):
                            if x[1] in cl.getGroupIdsJoined():
                                try:
                                    cl.sendMessage(x[1], text[41:])
                                    cl.relatedMessage(to, "成功發送訊息至\n群組名稱：【{}】\n發送內容：{}".format(
                                        cl.getGroupWithoutMembers(x[1]).name, text[41:]), op.message.id)
                                except Exception as e:
                                    cl.sendMessage(to, str(e))
                            else:
                                cl.relatedMessage(
                                    to, "機器不在群 無法發送", op.message.id)
                        elif ismid(x[1]):
                            try:
                                if x[1] not in cl.getAllContactIds():
                                    cl.findAndAddContactsByMid(x[1])
                                cl.sendMessage(x[1], text[41:])
                                cl.relatedMessage(to, "成功發送訊息給\n【{}】\n發送內容：{}".format(
                                    cl.getContact(x[1]).displayName, text[41:]), op.message.id)
                            except Exception as e:
                                cl.sendMessage(to, str(e))
                        else:
                            cl.relatedMessage(
                                to, "你輸入的似乎不是GID/MID...", op.message.id)
                    else:
                        cl.relatedMessage(to, "格式錯誤 請重新輸入", op.message.id)
                elif text is not None and text.lower().startswith("sendp:"):
                    gidtext = text[6:]
                    if isgid(gidtext):
                        try:
                            gMembMids = [
                                contact.mid for contact in cl.getGroup(gidtext).members]
                        except:
                            gMembMids = []
                        if clMID in gMembMids:
                            wait["Speak_remotely"] = {}
                            wait["Speak_remotely"][to] = {}
                            wait["Speak_remotely"][to]["mode"] = "pic"
                            wait["Speak_remotely"][to]["sender"] = sender
                            wait["Speak_remotely"][to]["msgto"] = "2"
                            wait["Speak_remotely"][to]["location"] = gidtext
                            cl.relatedMessage(to, "請發送圖片", op.message.id)
                        else:
                            cl.relatedMessage(to, "機器不在群 無法發送", op.message.id)
                    elif ismid(gidtext):
                        if gidtext not in cl.getAllContactIds():
                            try:
                                cl.findAndAddContactsByMid(gidtext)
                            except:
                                cl.relatedMessage(
                                    to, "目前處於 加友規制中", op.message.id)
                        if gidtext in cl.getAllContactIds():
                            wait["Speak_remotely"] = {}
                            wait["Speak_remotely"][to] = {}
                            wait["Speak_remotely"][to]["mode"] = "pic"
                            wait["Speak_remotely"][to]["sender"] = sender
                            wait["Speak_remotely"][to]["msgto"] = "0"
                            wait["Speak_remotely"][to]["location"] = gidtext
                            cl.relatedMessage(to, "請發送圖片", op.message.id)
                        else:
                            cl.relatedMessage(to, "無法發送", op.message.id)
                    else:
                        cl.relatedMessage(
                            to, "你輸入的似乎不是GID/MID...", op.message.id)
                elif text is not None and text.lower().startswith("sendc:"):
                    gidtext = text[6:]
                    if isgid(gidtext):
                        try:
                            gMembMids = [
                                contact.mid for contact in cl.getGroup(gidtext).members]
                        except:
                            gMembMids = []
                        if clMID in gMembMids:
                            wait["Speak_remotely"] = {}
                            wait["Speak_remotely"][to] = {}
                            wait["Speak_remotely"][to]["mode"] = "contact"
                            wait["Speak_remotely"][to]["sender"] = sender
                            wait["Speak_remotely"][to]["msgto"] = "2"
                            wait["Speak_remotely"][to]["location"] = gidtext
                            cl.relatedMessage(to, "請發送友資", op.message.id)
                        else:
                            cl.relatedMessage(to, "機器不在群 無法發送", op.message.id)
                    elif ismid(gidtext):
                        if gidtext not in cl.getAllContactIds():
                            try:
                                cl.findAndAddContactsByMid(gidtext)
                            except:
                                cl.relatedMessage(
                                    to, "目前處於 加友規制中", op.message.id)
                        if gidtext in cl.getAllContactIds():
                            wait["Speak_remotely"] = {}
                            wait["Speak_remotely"][to] = {}
                            wait["Speak_remotely"][to]["mode"] = "contact"
                            wait["Speak_remotely"][to]["sender"] = sender
                            wait["Speak_remotely"][to]["msgto"] = "0"
                            wait["Speak_remotely"][to]["location"] = gidtext
                            cl.relatedMessage(to, "請發送友資", op.message.id)
                        else:
                            cl.relatedMessage(to, "無法發送", op.message.id)
                    else:
                        cl.relatedMessage(
                            to, "你輸入的似乎不是GID/MID...", op.message.id)
                elif text is not None and text.lower().startswith("sendv:"):
                    gidtext = text[6:]
                    if isgid(gidtext):
                        try:
                            gMembMids = [
                                contact.mid for contact in cl.getGroup(gidtext).members]
                        except:
                            gMembMids = []
                        if clMID in gMembMids:
                            wait["Speak_remotely"] = {}
                            wait["Speak_remotely"][to] = {}
                            wait["Speak_remotely"][to]["mode"] = "video"
                            wait["Speak_remotely"][to]["sender"] = sender
                            wait["Speak_remotely"][to]["msgto"] = "2"
                            wait["Speak_remotely"][to]["location"] = gidtext
                            cl.relatedMessage(to, "請發送影片", op.message.id)
                        else:
                            cl.relatedMessage(to, "機器不在群 無法發送", op.message.id)
                    elif ismid(gidtext):
                        if gidtext not in cl.getAllContactIds():
                            try:
                                cl.findAndAddContactsByMid(gidtext)
                            except:
                                cl.relatedMessage(
                                    to, "目前處於 加友規制中", op.message.id)
                        if gidtext in cl.getAllContactIds():
                            wait["Speak_remotely"] = {}
                            wait["Speak_remotely"][to] = {}
                            wait["Speak_remotely"][to]["mode"] = "video"
                            wait["Speak_remotely"][to]["sender"] = sender
                            wait["Speak_remotely"][to]["msgto"] = "0"
                            wait["Speak_remotely"][to]["location"] = gidtext
                            cl.relatedMessage(to, "請發送影片", op.message.id)
                        else:
                            cl.relatedMessage(to, "無法發送", op.message.id)
                    else:
                        cl.relatedMessage(
                            to, "你輸入的似乎不是GID/MID...", op.message.id)
                elif text and text.lower() == '群組圖片廣播':
                    wait["broadcast"]["content"] = "pic"
                    wait["broadcast"]["type"] = 2
                    wait["broadcast"]["sender"] = sender
                    wait["broadcast"]["to"] = to
                    cl.sendMessage(to, "請發送圖片")
                elif text and text.lower() == '群組語音廣播':
                    wait["broadcast"]["content"] = "sound"
                    wait["broadcast"]["type"] = 2
                    wait["broadcast"]["sender"] = sender
                    wait["broadcast"]["to"] = to
                    cl.sendMessage(to, "請發送語音")
                elif text and text.lower() == '群組影片廣播':
                    wait["broadcast"]["content"] = "video"
                    wait["broadcast"]["type"] = 2
                    wait["broadcast"]["sender"] = sender
                    wait["broadcast"]["to"] = to
                    cl.sendMessage(to, "請發送影片")
                elif text and text.lower() == '群組友資廣播':
                    wait["broadcast"]["content"] = "contact"
                    wait["broadcast"]["type"] = 2
                    wait["broadcast"]["sender"] = sender
                    wait["broadcast"]["to"] = to
                    cl.sendMessage(to, "請發送友資")
                elif msg.text and msg.text.lower().startswith('改私訊文字:'):
                    ban["text"] = text.replace("改私訊文字:", "")
                    cl.sendMessage(to, "更改私訊發話完成\n更改內容：\n\n"+str(ban["text"]))
                elif msg.text and msg.text.lower().startswith('改已讀文字:'):
                    ban["text1"] = text.replace("改已讀文字:", "")
                    cl.sendMessage(to, "更改已讀發話完成\n更改內容：\n\n"+str(ban["text1"]))
                    backupData()
                elif text and text.lower() == '改私訊圖片':
                    wait["5image"] = True
                    cl.relatedMessage(to, "請發送圖片", op.message.id)
                elif text and text.lower() == '改私訊影片':
                    wait["5video"] = True
                    cl.relatedMessage(to, "請發送影片", op.message.id)
                #elif text and text.lower() == '改頭貼':
                #    wait["cvp"] = True
                #    cl.relatedMessage(to, "請發送圖片", op.message.id)
            if msg.contentType == 0:
                if text.lower() is None:
                    return
                else:
                    pass
                if text is None:
                    return
                else:
                    pass
            if msg.contentType == 1:
                if to in wait["Speak_remotely"] and sender == wait["Speak_remotely"][to]["sender"] and wait["Speak_remotely"][to]["mode"] == "pic":
                    if wait["Speak_remotely"][to]["msgto"] == "0":
                        try:
                            image = cl.downloadObjectMsg(
                                msg_id, saveAs="send.jpg")
                            cl.sendImage(wait["Speak_remotely"]
                                         [to]["location"], image)
                            cl.sendMessage(
                                to, "已發送圖片給\n【"+str(cl.getContact(wait["Speak_remotely"][to]["location"]).displayName)+"】")
                            os.remove("send.jpg")
                            wait["Speak_remotely"] = {}
                        except Exception as error:
                            wait["Speak_remotely"] = {}
                            cl.sendMessage(to, str(error))
                    if wait["Speak_remotely"][to]["msgto"] == "2":
                        try:
                            gMembMids = [contact.mid for contact in cl.getGroup(
                                wait["Speak_remotely"][to]["location"]).members]
                        except:
                            gMembMids = []
                        if clMID in gMembMids:
                            try:
                                image = cl.downloadObjectMsg(
                                    msg_id, saveAs="send.jpg")
                                cl.sendImage(
                                    wait["Speak_remotely"][to]["location"], image)
                                cl.sendMessage(to, "已發送圖片到\n【"+str(cl.getGroupWithoutMembers(
                                    wait["Speak_remotely"][to]["location"]).name)+"】")
                                os.remove("send.jpg")
                                wait["Speak_remotely"] = {}
                            except Exception as error:
                                wait["Speak_remotely"] = {}
                                cl.sendMessage(to, str(error))
                        else:
                            wait["Speak_remotely"] = {}
                            cl.sendMessage(to, "機器不在群組內")
            if msg.contentType == 2:
                if to in wait["Speak_remotely"] and sender == wait["Speak_remotely"][to]["sender"] and wait["Speak_remotely"][to]["mode"] == "video":
                    if wait["Speak_remotely"][to]["msgto"] == "0":
                        try:
                            image = cl.downloadObjectMsg(
                                msg_id, saveAs="send.mp4")
                            cl.sendVideo(wait["Speak_remotely"]
                                         [to]["location"], image)
                            cl.sendMessage(
                                to, "已發送影片給\n【"+str(cl.getContact(wait["Speak_remotely"][to]["location"]).displayName)+"】")
                            os.remove("send.mp4")
                            wait["Speak_remotely"] = {}
                        except Exception as error:
                            wait["Speak_remotely"] = {}
                            cl.sendMessage(to, str(error))
                    if wait["Speak_remotely"][to]["msgto"] == "2":
                        try:
                            gMembMids = [contact.mid for contact in cl.getGroup(
                                wait["Speak_remotely"][to]["location"]).members]
                        except:
                            gMembMids = []
                        if clMID in gMembMids:
                            try:
                                image = cl.downloadObjectMsg(
                                    msg_id, saveAs="send.mp4")
                                cl.sendVideo(
                                    wait["Speak_remotely"][to]["location"], image)
                                cl.sendMessage(to, "已發送影片到\n【"+str(cl.getGroupWithoutMembers(
                                    wait["Speak_remotely"][to]["location"]).name)+"】")
                                os.remove("send.mp4")
                                wait["Speak_remotely"] = {}
                            except Exception as error:
                                wait["Speak_remotely"] = {}
                                cl.sendMessage(to, str(error))
                        else:
                            wait["Speak_remotely"] = {}
                            cl.sendMessage(to, "機器不在群組內")
                if text is None:
                    return
                else:
                    cmd = text.lower()
            if msg.contentType == 13:
                if to in wait["Speak_remotely"] and sender == wait["Speak_remotely"][to]["sender"] and wait["Speak_remotely"][to]["mode"] == "contact":
                    if wait["Speak_remotely"][to]["msgto"] == "0":
                        try:
                            cl.sendContact(
                                wait["Speak_remotely"][to]["location"], msg.contentMetadata["mid"])
                            cl.sendMessage(
                                to, "已發送友資給\n【"+str(cl.getContact(wait["Speak_remotely"][to]["location"]).displayName)+"】")
                            wait["Speak_remotely"] = {}
                        except Exception as error:
                            wait["Speak_remotely"] = {}
                            cl.sendMessage(to, str(error))
                    if wait["Speak_remotely"][to]["msgto"] == "2":
                        try:
                            gMembMids = [contact.mid for contact in cl.getGroup(
                                wait["Speak_remotely"][to]["location"]).members]
                        except:
                            gMembMids = []
                        if clMID in gMembMids:
                            try:
                                cl.sendContact(
                                    wait["Speak_remotely"][to]["location"], msg.contentMetadata["mid"])
                                cl.sendMessage(to, "已發送友資到\n【"+str(cl.getGroupWithoutMembers(
                                    wait["Speak_remotely"][to]["location"]).name)+"】")
                                wait["Speak_remotely"] = {}
                            except Exception as error:
                                wait["Speak_remotely"] = {}
                                cl.sendMessage(to, str(error))
                        else:
                            wait["Speak_remotely"] = {}
                            cl.sendMessage(to, "機器不再該群組內")
            if sender in ban["owners"] or sender in gom:  # 3級權限3級權限3級權限3級權限3級權限
                if text and text.lower() == '三級名單':
                    if ban["owners"] == []:
                        cl.sendMessage(to, "沒有權限者")
                    else:
                        noo = 0
                        mc = "三級清單："
                        pip = []
                        for mi_d in ban["owners"]:
                            try:
                                noo += 1
                                mc += "\n"+str(noo)+".* " + \
                                    cl.getContact(mi_d).displayName
                            except:
                                mc += "\n"+str(noo)+".* 已經砍帳ㄌ"
                                pip.append(mi_d)
                        cl.sendMessage(to, mc)
                        if pip == []:
                            pass
                        else:
                            for j in pip:
                                ban["owners"].remove(j)
                            cl.sendMessage(to, "砍帳名單清理完畢")
                elif text and text.lower() == '最大名單':
                    if highest == []:
                        cl.relatedMessage(msg.to, "沒有權限者", op.message.id)
                    else:
                        mc = "我的主人\n"
                        num = 0
                        pp = 0
                        for mi_d in highest:
                            num += 1
                            pp += 1
                            try:
                                mc += "{}->".format(num) + cl.getContact(
                                    mi_d).displayName + "\n"+mi_d + "\n"
                            except:
                                mc += "{}->已經砍帳號了\n".format(num)
                            if pp == 100:
                                cl.sendMessage(to, mc)
                                pp = 0
                                mc = "我的主人\n"
                        cl.sendMessage(to, mc)
                elif text and text.lower() == '二級名單':
                    if ban["admin"] == []:
                        cl.sendMessage(to, "沒有權限者")
                    else:
                        noo = 0
                        mc = "二級清單："
                        pip = []
                        for mi_d in ban["admin"]:
                            try:
                                noo += 1
                                mc += "\n"+str(noo)+".* " + \
                                    cl.getContact(mi_d).displayName
                            except:
                                mc += "\n"+str(noo)+".* 已經砍帳ㄌ"
                                pip.append(mi_d)
                        cl.sendMessage(to, mc)
                        if pip == []:
                            pass
                        else:
                            for j in pip:
                                ban["admin"].remove(j)
                            cl.sendMessage(to, "砍帳名單清理完畢")
                elif text and text.lower() == '指令3':
                    if ban["useflex"] == False:
                        cl.relatedMessage(to, help3(), msg_id)
                    else:
                        data = {
                            "type": "flex",
                            "altText": "hao bot",
                            "contents":{
"type": "bubble",
"body": {
"type": "box",
"layout": "vertical",
"contents": [
  {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "hao hleper",
        "align": "center",
        "size": "xxs",
        "color": "#888888"
      },
      {
        "type": "text",
        "text": "指令表",
        "align": "center",
        "size": "lg",
        "weight": "bold",
        "color": "#ff0000",
        "decoration": "underline"
      }
    ],
    "offsetBottom": "sm"
  },
  {
    "type": "separator",
    "color": "#000000"
  },
  {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": help2(),
        "color": "#0000cc",
        "align": "center",
        "wrap": True
      }
    ],
    "offsetTop": "sm"
  }
]
},
"size": "kilo"
}
                        }
                        sendflex(to, data)
                elif text and text.lower() == '指令2':
                    if ban["useflex"] == False:
                        cl.relatedMessage(to, help2(), msg_id)
                    else:
                        data = {
                            "type": "flex",
                            "altText": "hao bot",
                            "contents":{
"type": "bubble",
"body": {
"type": "box",
"layout": "vertical",
"contents": [
  {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "hao hleper",
        "align": "center",
        "size": "xxs",
        "color": "#888888"
      },
      {
        "type": "text",
        "text": "指令表",
        "align": "center",
        "size": "lg",
        "weight": "bold",
        "color": "#ff0000",
        "decoration": "underline"
      }
    ],
    "offsetBottom": "sm"
  },
  {
    "type": "separator",
    "color": "#000000"
  },
  {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": help3(),
        "color": "#0000cc",
        "align": "center",
        "wrap": True
      }
    ],
    "offsetTop": "sm"
  }
]
},
"size": "kilo"
}
                        }
                        sendflex(to, data)
                elif text and text.lower() == '運行':
                    timeNow = time.time()
                    runtime = timeNow - mulai
                    runtime = timeChange(runtime)
                    cl.relatedMessage(to, "目前機器運行時間\n時間:【{}】".format(
                        str(runtime)), op.message.id)
                elif msg.text and msg.text.lower().startswith("mp "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            cl.sendMessage(to, " 傳送了影片", contentMetadata={"DOWNLOAD_URL": "http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus), "PREVIEW_URL": "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)}, contentType = 2)
                elif text and text.lower() == "群組主人":
                    try:
                        group = cl.getGroup(receiver)
                        GS = group.creator.mid
                        cl.sendMessageWithMention(receiver, '', [GS])
                        cl.sendContact(receiver, GS)
                    except:
                        W = group.members[0].mid
                        cl.sendMessageWithMention(
                            receiver, '群組創建者已刪除帳號\n這是繼承的群組創建者\n', [W])
                        cl.sendContact(receiver, W)
                elif text and text.lower() == 'gid':  # 查群GID
                    group = cl.getGroup(to)
                    cl.relatedMessage(to, "{}".format(group.id), op.message.id)
                elif text is not None and text.lower().startswith("友資:"):
                    midd = msg.text.replace("友資:", "")
                    if msg.toType == 0:
                        cl.sendContact(msg._from, (midd))
                    if msg.toType == 2:
                        # cl.sendMessage(to,"test")
                        cl.sendContact(msg.to, (midd))
                elif text is not None and text.lower().startswith("查人:"):
                    gid = msg.text.replace("查人:", "")
                    group = cl.getGroup(gid)
                    mc = "【 "+group.name + "的成員名單 】"
                    mv = "【 "+group.name + "的邀請名單 】"
                    count = 0
                    num = 0
                    count1 = 0
                    num1 = 0
                    if group.members:
                        for contact in group.members:
                            num += 1
                            count += 1
                            mc += "\n{}. {}\n{}".format(num,
                                                        contact.displayName, contact.mid)
                            if count == 100:
                                cl.sendMessage(msg.to, mc)
                                count = 0
                                mc = "【 "+group.name + "的成員名單 】"
                                time.sleep(1)
                        cl.sendMessage(msg.to, mc)
                    if group.invitee:
                        for contact in group.invitee:
                            num1 += 1
                            count1 += 1
                            mv += "\n{}. {}\n{}".format(num1,
                                                        contact.displayName, contact.mid)
                            if count1 == 100:
                                cl.sendMessage(msg.to, mv)
                                count1 = 0
                                mv = "【 "+group.name + "的邀請名單 】"
                                time.sleep(1)
                        cl.sendMessage(msg.to, mv)
                elif text is not None and text.lower().startswith("查:"):
                    gid = msg.text.replace("查:", "")
                    group = cl.getGroup(gid)
                    mc = "【 "+group.name + "的成員名單 】"
                    mv = "【 "+group.name + "的邀請名單 】"
                    count = 0
                    num = 0
                    count1 = 0
                    num1 = 0
                    if group.members:
                        for contact in group.members:
                            num += 1
                            count += 1
                            mc += "\n{}. {}\n{}".format(num,
                                                        contact.displayName, contact.mid)
                            if count == 100:
                                cl.sendMessage(msg.to, mc)
                                count = 0
                                mc = "【 "+group.name + "的成員名單 】"
                                time.sleep(1)
                        cl.sendMessage(msg.to, mc)
                    if group.invitee:
                        for contact in group.invitee:
                            num1 += 1
                            count1 += 1
                            mv += "\n{}. {}　　　{}".format(num1,
                                                        contact.displayName, contact.mid)
                            if count1 == 100:
                                cl.sendMessage(msg.to, mv)
                                count1 = 0
                                mv = "【 "+group.name + "的邀請名單 】"
                                time.sleep(1)
                        cl.sendMessage(msg.to, mv)
                elif text is not None and text.lower().startswith("查成員:"):
                    gid = msg.text.replace("查成員:", "")
                    group = cl.getGroup(gid)
                    mc = "【 "+group.name + "的成員名單 】"
                    count = 0
                    num = 0
                    if group.members:
                        for contact in group.members:
                            num += 1
                            count += 1
                            mc += "\n{}. {}\n{}".format(num,
                                                        contact.displayName, contact.mid)
                            if count == 100:
                                cl.sendMessage(msg.to, mc)
                                count = 0
                                mc = "【 "+group.name + "的成員名單 】"
                                time.sleep(1)
                        cl.sendMessage(msg.to, mc)
                    else:
                        cl.sendMessage(to, "沒有成員")
                elif text is not None and text.lower().startswith("查邀請:"):
                    gid = msg.text.replace("查邀請:", "")
                    group = cl.getGroup(gid)
                    mc = "【 "+group.name + "的邀請名單 】"
                    count = 0
                    num = 0
                    if group.invitee:
                        for contact in group.invitee:
                            num += 1
                            count += 1
                            mc += "\n{}. {}\n{}".format(num,
                                                        contact.displayName, contact.mid)
                            if count == 100:
                                cl.sendMessage(msg.to, mc)
                                count = 0
                                mc = "【 "+group.name + "的邀請名單 】"
                                time.sleep(1)
                        cl.sendMessage(msg.to, mc)
                    else:
                        cl.sendMessage(to, "沒有成員")
                elif text is not None and text.lower().startswith("群內友資:"):
                    gid = msg.text.replace("群內友資:", "")
                    group = cl.getGroup(gid)
                    if group.members:
                        cl.sendMessage(to, "以下是群內友資名片")
                        time.sleep(1)
                        for contact in group.members:
                            x = contact.mid
                            cl.sendContact(to, x)
                            time.sleep(1.0)
                        cl.relatedMessage(to, "完成", op.message.id)
                    else:
                        cl.sendMessage(to, "沒有成員")
                elif text is not None and text.lower().startswith("群內名片:"):
                    gid = msg.text.replace("群內名片:", "")
                    group = cl.getGroup(gid)
                    if group.members:
                        cl.sendMessage(to, "以下是群內友資名片")
                        time.sleep(1)
                        count = 0  # 初始化好友数量为 0
                        for contact in group.members:
                            x = contact.mid
                            cl.sendContact(to, x)
                            time.sleep(1.0)
                            count += 1  # 每循环一次，好友数量加 1
                        cl.relatedMessage(to, "完成，共发了 {} 个友资".format(count), op.message.id)  # 发送包含好友数量的消息
                    else:
                        cl.sendMessage(to, "沒有成員")
                elif text is not None and text.lower().startswith("卡邀友資:"):
                    gid = msg.text.replace("卡邀友資:", "")
                    group = cl.getGroup(gid)
                    if group.invitee:
                        cl.sendMessage(to, "以下是卡邀友資名片")
                        time.sleep(1)
                        for contact in group.invitee:
                            x = contact.mid
                            cl.sendContact(to, x)
                            time.sleep(1.0)
                        cl.relatedMessage(to, "完成", op.message.id)
                    else:
                        cl.sendMessage(to, "沒有成員")
                elif text is not None and text.lower().startswith("查群:") and text[3:] != "":
                    group = cl.getGroup(text[3:])
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = len(group.invitee)
                    ret_ = "查詢的群組資料"
                    ret_ += f"\n名稱:{group.name}"
                    ret_ += f"\nGID:{group.id}"
                    ret_ += f"\n成員數量:{len(group.members)}"
                    ret_ += f"\n邀請數量:{gPending}"
                    ret_ += "\n[ 查完了 ]"
                    cl.sendMessage(to, str(ret_))
                elif text is not None and text.lower().startswith("addpic:"):
                    separate = text.split(":")
                    iggm = text.replace(separate[0] + ":", "")
                    if iggm == "":
                        cl.sendMessage(to, "請輸入偵測圖片關鍵字")
                    elif iggm in rpy["pic"]:
                        cl.sendMessage(to, "已有此關鍵字回覆的圖片")
                    else:
                        ooowwwooo = iggm+".jpg"
                        wait["xin"] = ooowwwooo
                        rpy["pic"][iggm.lower()] = ooowwwooo
                        wait["squiredab"] = True
                        beihong.append(sender)
                        cl.sendMessage(to, "請發送關鍵字\n【"+str(iggm)+"】\n要回覆的圖片")
                elif text and text.lower() == 'piclist':
                    if rpy['pic'] == {}:
                        cl.sendMessage(to, "沒有圖片回復")
                    else:
                        mc = "[圖片回覆列表]"
                        no = 1
                        for iii in rpy['pic']:
                            mc += "\n"+str(no)+"."+iii
                            no += 1
                        mc += "\n[總共 {} 個回覆]".format(str(no-1))
                        cl.relatedMessage(to, str(mc), op.message.id)
                # 全群回復
                elif text is not None and text.lower().startswith("addtext"):
                    error = find_between_r(msg.text, "addtext", "*")
                    rep = find_between_r(msg.text, "*", "_")
                    reply = find_between_r(msg.text, "_", "")
                    if rep == "" or reply == "":
                        cl.sendMessage(to, "請重新輸入")
                    else:
                        rpy["orgrpy"]["{}".format(rep)] = reply
                        cl.sendMessage(to, "新增回覆\n關鍵字：{}\n回覆：{}".format(
                            str(rep), str(reply)))
                        backupData()
                # 回覆列表
                elif text and text.lower() == 'textlist':
                    if rpy["orgrpy"] == {}:
                        cl.sendMessage(to, "沒有文字回覆")
                    else:
                        mc = "[ 回覆列表 ]\n"
                        no = 0
                        pp = 0
                        for rep in rpy["orgrpy"]:
                            reply = rpy["orgrpy"]["{}".format(rep)]
                            no += 1
                            pp += 1
                            try:
                                mc += "{}.\n關鍵字:{}\n回覆內容:{}\n".format(
                                    str(no), str(rep), str(reply))
                            except:
                                mc += " "
                            if pp == 50:
                                cl.sendMessage(to, mc)
                                pp = 0
                                mc = "[ 回覆列表 ]\n"
                        cl.sendMessage(to, mc)
                elif text and text.lower() == 'conlist':
                    if rpy["contact"] == {}:
                        cl.sendMessage(to, "沒有友資回覆")
                    else:
                        mc = "[ 友資回覆列表 ]\n"
                        no = 0
                        pp = 0
                        for con in rpy["contact"]:
                            conrpy = rpy["contact"]["{}".format(con)]
                            no += 1
                            pp += 1
                            try:
                                mc += "{}.\n關鍵字:{}\n友資名稱:{}\n".format(str(no), str(
                                    con), str(cl.getContact(conrpy).displayName))
                            except:
                                mc += "{}.\n關鍵字:{}\n友資名稱:已經砍帳號了\n".format(
                                    str(no), str(con))
                            if pp == 100:
                                cl.sendMessage(to, mc)
                                pp = 0
                                mc = "[ 友資回覆列表 ]\n"
                        cl.sendMessage(to, mc)
                # 友資新增
                elif text is not None and text.lower().startswith("cotadd"):
                    error = find_between_r(msg.text, "cotadd", ":")
                    con = find_between_r(msg.text, ":", "_")
                    conrpy = find_between_r(msg.text, "_", "")
                    if not ismid(con):
                        cl.sendMessage(to, "沒有輸入MID 或 位置錯誤 請重新設定")
                        pass
                    elif conrpy == "" or conrpy == " " or conrpy == "  ":
                        cl.sendMessage(to, "設定錯誤 請重新設定")
                        pass
                    elif conrpy in rpy["contact"]:
                        if sender in ["ue1d1762de95bc0fd9b9e4e309436353f"]:
                            rpy["contact"][conrpy] = con
                            backupData()
                            cl.sendMessage(to, "新增回覆\n關鍵字：{}\n友資名稱：{}".format(
                                str(conrpy), str(cl.getContact(con).displayName)))
                        else:
                            org = rpy["contact"][conrpy]
                            cl.sendMessage(to, "該回覆已有偵測友資!!")
                            # cl.sendMessage("ggg","【警告】有人試圖替換原本友資回復")
                            #sendMention("ggg", "欲替換者:@!\n偵測友資：{}\n原本友資：{}\n替換友資：{}".format(str(conrpy),str(cl.getContact(org).displayName),str(cl.getContact(con).displayName)),[sender])
                    else:
                        rpy["contact"][conrpy] = con
                        backupData()
                        cl.sendMessage(to, "新增回覆\n關鍵友資：{}\n友資名稱：{}".format(
                            str(conrpy), str(cl.getContact(con).displayName)))
            if sender in ban["admin"] or sender in ban["owners"] or sender in gom:  # 2級權限2級權限2級權限2級權限2級權限2級權限
                if text and text.lower() == '指令1':
                    if ban["useflex"] == False:
                        cl.relatedMessage(to, help1(), msg_id)
                    else:
                        data = {
                            "type": "flex",
                            "altText": "hao bot",
                            "contents":{
"type": "bubble",
"body": {
"type": "box",
"layout": "vertical",
"contents": [
  {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "hao hleper",
        "align": "center",
        "size": "xxs",
        "color": "#888888"
      },
      {
        "type": "text",
        "text": "指令表",
        "align": "center",
        "size": "lg",
        "weight": "bold",
        "color": "#ff0000",
        "decoration": "underline"
      }
    ],
    "offsetBottom": "sm"
  },
  {
    "type": "separator",
    "color": "#000000"
  },
  {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": help1(),
        "color": "#0000cc",
        "align": "center",
        "wrap": True
      }
    ],
    "offsetTop": "sm"
  }
]
},
"size": "kilo"
}
                        }
                        sendflex(to, data)
                #elif text and text.lower() == '12345':  # 跟蹤像素網址
                #    if sender in gom:
                #        me = cl.getContact(sender)
                #        contact = cl.getContact(sender)
                #        cl.sendMessage(to, " 傳送了影片", contentMetadata={"DOWNLOAD_URL": "https://02ip.ru/1IdyX{}/vp".format(
                #            contact.pictureStatus), "PREVIEW_URL": "https://02ip.ru/1IdyX".format(contact.pictureStatus)}, contentType=2)
                #elif text and text.lower() == '測試1':  # 位置追蹤器網址
                #    if sender in gom:
                #        me = cl.getContact(sender)
                #        contact = cl.getContact(sender)
                #        cl.sendMessage(to, " 傳送了影片", contentMetadata={"DOWNLOAD_URL": "https://02ip.ru/XIn4D{}/vp".format(
                #            contact.pictureStatus), "PREVIEW_URL": "https://02ip.ru/XIn4D".format(contact.pictureStatus)}, contentType=2)
                #elif text and text.lower() == '測試2':  # IP檢查網址
                #    if sender in gom:
                #        me = cl.getContact(sender)
                #        contact = cl.getContact(sender)
                #        cl.sendMessage(to, " 傳送了影片", contentMetadata={"DOWNLOAD_URL": "https://02ip.ru/Zv126{}/vp".format(
                #            contact.pictureStatus), "PREVIEW_URL": "https://02ip.ru/Zv126".format(contact.pictureStatus)}, contentType=2)
                elif text and text.lower() == '@@@@@@':  # 萊恩用
                    if sender in highest:
                        me = cl.getContact(sender)
                        contact = cl.getContact(sender)
                        cl.sendMessage(to, " 傳送了影片", contentMetadata={"DOWNLOAD_URL": "https://02ip.ru/ZmyQ2/{}/vp".format(
                            contact.pictureStatus), "PREVIEW_URL": "https://02ip.ru/ZmyQ2".format(contact.pictureStatus)}, contentType=2)
                elif text and text.lower() == '7776666':  # 萊恩用
                    if sender in highest:
                        me = cl.getContact(sender)
                        contact = cl.getContact(sender)
                        cl.sendMessage(to, " 傳送了影片", contentMetadata={"DOWNLOAD_URL": "https://02ip.ru/104hq1/{}/vp".format(
                            contact.pictureStatus), "PREVIEW_URL": "https://02ip.ru/104hq1".format(contact.pictureStatus)}, contentType=2)
                #elif text and text.lower() == '777':
                #    me = cl.getContact(sender)
                #    contact = cl.getContact(sender)
                #    cl.sendMessage(to, " 傳送了影片", contentMetadata={"DOWNLOAD_URL": "網址{}/vp".format(
                #        contact.pictureStatus), "PREVIEW_URL": "網址/".format(contact.pictureStatus)}, contentType=2)
                elif text and text.lower() == '123':  # 抓已讀
                    cl.sendMessage(msg.to, "開囉")
                    try:
                        del wait3['readPoint'][msg.to]
                        del wait3['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait3['readPoint'][msg.to] = msg.id
                    wait3['readMember'][msg.to] = ""
                    wait3['setTime'][msg.to] = datetime.strftime(now2, "%H:%M")
                    wait3['ROM'][msg.to] = {}
                elif text and text.lower() == '456':
                    cl.sendMessage(to, "關囉")
                    try:
                        del wait3['readPoint'][msg.to]
                        del wait3['readMember'][msg.to]
                        del wait3['setTime'][msg.to]
                    except:
                        pass
                elif text and text.lower() == '789':
                    cl.sendMessage(to, "腦殘 沒這功能")
                # 設置群組歡迎訊息
                elif msg.text and msg.text.lower().startswith("設定歡迎"):
                    wc_ = msg.text.split("#")
                    if to not in timess['wc']:
                        try:
                            timess['wc'][to] = wc_[1]
                            with open('timexss.json', 'w') as fp:
                                json.dump(timess, fp, sort_keys=True, indent=4)
                                cl.relatedMessage(
                                    to, "[歡迎通知]\n成功設置群組歡迎訊息\n歡迎訊息: " + wc_[1], op.message.id)
                        except:
                            cl.relatedMessage(
                                to, "[錯誤通知]\n設置群組歡迎訊息失敗 ", op.message.id)
                    else:
                        cl.relatedMessage(
                            to, "[錯誤通知]\n群組歡迎訊息已存在!!!! ", op.message.id)
                # 更新群組歡迎訊息
                elif msg.text and msg.text.lower().startswith("更新歡迎"):
                    list_ = msg.text.split("#")
                    if to in timess['wc']:
                        try:
                            del timess['wc'][to]
                            timess['wc'][to] = list_[1]
                            with open('timexss.json', 'w') as fp:
                                json.dump(timess, fp, sort_keys=True, indent=4)
                                cl.sendMessage(
                                    to, "[歡迎通知]\n成功更新群組歡迎訊息\n目前歡迎訊息: " + list_[1])
                        except:
                            cl.sendMessage(to, "[錯誤通知]\n更新群組歡迎訊息失敗!!!")
                    else:
                        cl.sendMessage(to, "[錯誤通知]\n你正在更新不存在的歡迎訊息!!!")
                # 刪除歡迎訊息
                elif text and text.lower() == '刪除歡迎':
                    if to in timess['wc']:
                        try:
                            del timess['wc'][to]
                            with open('timexss.json', 'w') as fp:
                                json.dump(timess, fp, sort_keys=True, indent=4)
                                cl.relatedMessage(
                                    to, "[歡迎通知]\n成功刪除群組歡迎訊息", op.message.id)
                        except:
                            cl.relatedMessage(
                                to, "[錯誤通知]\n刪除群組歡迎訊息失敗!!!", op.message.id)
                    else:
                        cl.relatedMessage(
                            to, "[錯誤通知]\n你正在刪除不存在的歡迎訊息!!!", op.message.id)
                # 歡迎訊息wc
                elif text and text.lower() == '確認歡迎':
                    if to in timess['wc']:
                        cl.relatedMessage(
                            to, "[歡迎提示]\n歡迎訊息: "+timess['wc'][to], op.message.id)
                    else:
                        cl.relatedMessage(
                            to, "[歡迎提示]\n還沒設置歡迎詞\n使用預設群組歡迎訊息中!!!", op.message.id)
                # 設置群組退出訊息
                elif msg.text and msg.text.lower().startswith("設定退群"):
                    gc_ = msg.text.split("#")
                    if to not in timess['gc']:
                        try:
                            timess['gc'][to] = gc_[1]
                            with open('timexss.json', 'w') as fp:
                                json.dump(timess, fp, sort_keys=True, indent=4)
                                cl.relatedMessage(
                                    to, "[退出通知]\n成功設置群組退出訊息\n退出訊息: " + gc_[1], op.message.id)
                        except:
                            cl.relatedMessage(
                                to, "[錯誤通知]\n設置群組退出訊息失敗 ", op.message.id)
                    else:
                        cl.relatedMessage(
                            to, "[錯誤通知]\n群組退出訊息已存在!!!! ", op.message.id)
                # 更新群組退出訊息
                elif msg.text and msg.text.lower().startswith("更新退群"):
                    list_ = msg.text.split("#")
                    if to in timess['gc']:
                        try:
                            del timess['gc'][to]
                            timess['gc'][to] = list_[1]
                            with open('timexss.json', 'w') as fp:
                                json.dump(timess, fp, sort_keys=True, indent=4)
                                cl.sendMessage(
                                    to, "[歡迎通知]\n成功更新群組歡迎訊息\n目前歡迎訊息: " + list_[1])
                        except:
                            cl.sendMessage(to, "[錯誤通知]\n更新群組歡迎訊息失敗!!!")
                    else:
                        cl.sendMessage(to, "[錯誤通知]\n你正在更新不存在的歡迎訊息!!!")
                # 刪除退出訊息
                elif text and text.lower() == '刪除退群':
                    if to in timess['gc']:
                        try:
                            del timess['gc'][to]
                            with open('timexss.json', 'w') as fp:
                                json.dump(timess, fp, sort_keys=True, indent=4)
                                cl.relatedMessage(
                                    to, "[退出通知]\n成功刪除群組退出訊息", op.message.id)
                        except:
                            cl.relatedMessage(
                                to, "[錯誤通知]\n刪除群組退出訊息失敗!!!", op.message.id)
                    else:
                        cl.relatedMessage(
                            to, "[錯誤通知]\n你正在刪除不存在的退出訊息!!!", op.message.id)
                # 退出訊息wc
                elif text and text.lower() == '確認退群':
                    if to in timess['gc']:
                        cl.relatedMessage(
                            to, "[退出通知]\n退出訊息: "+timess['gc'][to], op.message.id)
                    else:
                        cl.relatedMessage(
                            to, "[退出通知]\n還沒設置退群詞\n使用預設群組退出訊息中!!!", op.message.id)
                elif text and text.lower() == '歡迎 開':  # 歡迎訊息
                    ban["wcgid"][to] = True
                    cl.relatedMessage(to, "歡迎訊息已開啟", op.message.id)
                    backupData()
                elif text and text.lower() == '歡迎 關':
                    del ban["wcgid"][to]
                    cl.relatedMessage(to, "歡迎訊息已關閉", op.message.id)
                    backupData()
                elif text and text.lower() == '退群 開':
                    ban["gcgid"][to] = True
                    cl.relatedMessage(to, "退群訊息已開啟", op.message.id)  # 退出訊息
                    backupData()
                elif text and text.lower() == '退群 關':
                    del ban["gcgid"][to]
                    cl.relatedMessage(to, "退群訊息已關閉", op.message.id)
                    backupData()
                elif text and text.lower() == '公告 開':  # 公告
                    ban["announcement"][to] = True
                    cl.relatedMessage(to, "公告通知已開啟", op.message.id)
                    backupData()
                    print("通知 : 公告通知開啟")
                elif text and text.lower() == '公告 關':  # 公告
                    ban["announcement"][to] = False
                    cl.relatedMessage(to, "公告通知已關閉", op.message.id)
                    backupData()
                    print("通知 : 公告通知關閉")
                elif text and text.lower() == '群通 開':  # 群通
                    ban["groupcall"][to] = True
                    cl.relatedMessage(to, "群通通知已開啟", op.message.id)
                    backupData()
                    print("通知 : 群通通知開啟")
                elif text and text.lower() == '群通 關':  # 群通
                    ban["groupcall"][to] = False
                    cl.relatedMessage(to, "群通通知已關閉", op.message.id)
                    backupData()
                    print("通知 : 群通通知關閉")
                elif text and text.lower() == '模板 開':
                    ban["useflex"] = True
                    backupData()
                    cl.sendMessage(to, "模板開啟")
                elif text and text.lower() == '模板 關':
                    ban["useflex"] = False
                    backupData()
                    cl.sendMessage(to, "模板關閉")
                elif text and text.lower() == '友資偵測 開':  # 友資偵測
                    ban["midInformation"] = True
                    cl.relatedMessage(to, "友資偵測開啟", op.message.id)
                    backupData()
                    print("通知 : 友資偵測開啟")
                elif text and text.lower() == '友資偵測 關':  # 友資偵測
                    ban["midInformation"] = False
                    cl.relatedMessage(to, "友資偵測關閉", op.message.id)
                    backupData()
                    print("通知 : 友資偵測關閉")
                elif text and text.lower() == '回覆 開':  # 回覆
                    ban["reply"][to] = True
                    cl.relatedMessage(to, "回覆已開啟", op.message.id)
                    backupData()
                    print("通知 : 回覆開啟")
                elif text and text.lower() == '回覆 關':  #回覆
                    ban["reply"][to] = False
                    cl.relatedMessage(to, "回覆已關閉", op.message.id)
                    backupData()
                    print("通知 : 回覆關閉")
                elif text and text.lower() == '群組設定':
                    G = cl.getGroup(msg.to)
                    group = cl.getGroup(to)
                    contact = cl.getContact(sender)
                    gtime = group.createdTime
                    gtimee = int(round(gtime/1000))
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    ret_ = "群組名稱 : {}".format(str(G.name))
                    ret_ += "\n成員數量 : "+(str(len(group.members)))+""
                    ret_ += "\n邀請數量 : "+(gPending)+""
                    ret_ += "\n群組GID"
                    ret_ += "\n{}".format(group.id)
                    ret_ += "\n創群時間 : {}".format(time.strftime(
                        '%Y-%m-%d %H:%M:%S', time.localtime(gtimee)))
                    ret_ += "\n\n•此群設定"
                    if msg.toType == 2:
                        if ban["announcement"][to] == True:
                            ret_ += "\n公告通知 : 開啟中✔"
                        else:
                            ret_ += "\n公告通知 : 關閉中❌"
                        if ban["groupcall"][to] == True:
                            ret_ += "\n群通通知 : 開啟中✔"
                        else:
                            ret_ += "\n群通通知 : 關閉中❌"
                    cl.relatedMessage(to, ret_, op.message.id)
                elif text == "群通資訊":
                    if cl.getGroupCall(to).online:
                        gcall = cl.getGroupCall(to)
                        call_ = "• 群通資訊　"
                        try:
                            call_ += f"\n• 群通開始成員：{cl.getContact(gcall.hostMids).displayName}"
                        except:
                            call_ += f"\n• 群通開始成員：此人已砍帳"
                        call_ += f"\n• 群通成員："
                        for n, x in enumerate(gcall.memberMids, start=1):
                            call_ += f"\n• {n}.{cl.getContact(x).displayName}"
                        call_ += "\n• 群通類型：群組"
                        if gcall.mediaType == 1:
                            call_ += "語音通話"
                        elif gcall.mediaType == 2:
                            call_ += "視訊通話"
                        elif gcall.mediaType == 3:
                            call_ += "Live直播"
                        call_ += f"\n• 群通開始時間：\n• {time.strftime('%m-%d %H:%M:%S', time.localtime(int(round(gcall.started/1000))))}"
                        duration = int(round((time.time() * 1000 - gcall.started) / 1000))
                        minutes, seconds = divmod(duration, 60)
                        hours, minutes = divmod(minutes, 60)
                        call_ += f"\n• 通話時間：{hours:02d}:{minutes:02d}:{seconds:02d}"
                        call_ += "\n• 查詢完畢　"
                        return cl.sendMessage(to, call_)
                    else:
                        cl.sendMessage(to, "沒有人在群通")
                elif text is not None and text.lower().startswith("查群通:"):
                    gid = text.split(":")[1]
                    if not cl.getGroupCall(gid).online:
                        cl.sendMessage(to, "該群組目前沒有通話。")
                    else:
                        gcall = cl.getGroupCall(gid)
                        call_info = f"• 群通資訊　\n• 群組名稱：{cl.getGroup(gid).name}"
                        try:
                            call_info += f"\n• 群通開始成員：{cl.getContact(gcall.hostMids).displayName}"
                        except:
                            call_info += f"\n• 群通開始成員：此人已砍帳"
                        call_info += f"\n• 群通成員："
                        for n, x in enumerate(gcall.memberMids, start=1):
                            call_info += f"\n• {n}.{cl.getContact(x).displayName}"
                        call_info += "\n• 群通類型：群組"
                        if gcall.mediaType == 1:
                            call_info += "語音通話"
                        elif gcall.mediaType == 2:
                            call_info += "視訊通話"
                        elif gcall.mediaType == 3:
                            call_info += "Live直播"
                        call_info += f"\n• 群通開始時間：\n• {time.strftime('%m-%d %H:%M:%S', time.localtime(int(round(gcall.started/1000))))}"
                        duration = int(round((time.time() * 1000 - gcall.started) / 1000))
                        minutes, seconds = divmod(duration, 60)
                        hours, minutes = divmod(minutes, 60)
                        call_info += f"\n• 通話時間：{hours:02d}:{minutes:02d}:{seconds:02d}"
                        call_info += "\n• 查詢完畢　"
                        cl.sendMessage(to, call_info)
                elif text and text.lower() == '起來嗨':
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//20
                    for aa in range(k+1):
                        if aa == 0:
                            dd = '「 點名 」'
                            no = aa
                        else:
                            dd = '「 點名 」'
                            no = aa*20
                        msgas = dd
                        for a in nama[aa*20:(aa+1)*20]:
                            no += 1
                            if no == len(nama):
                                msgas += '{}. @!'.format(no)
                            else:
                                msgas += '{}. @!'.format(no)
                        sendMention(to, msgas, nama[aa*20:(aa+1)*20])
                        time.sleep(0.5)
                    cl.sendMessage(to, "總共標記 {} 人".format(str(len(nama))))
                if text is not None and text.lower().startswith("yp3:"):
                    search = msg.text.replace("yp3:","")
                    threading.Thread(target=ytdlwwwe, args=(to,search,)).start()
                if text is not None and text.lower().startswith("yp4:"):
                    search = msg.text.replace("yp4:","")
                    threading.Thread(target=ytdlwww, args=(to,search,)).start()
                if text is not None and text.lower().startswith("ypc:"):
                    search = msg.text.replace("ypc:","")
                    threading.Thread(target=ytdl_cover, args=(to,search,)).start()
                if text is not None and text.lower().startswith("ypa:"):
                    search = msg.text.replace("ypa:","")
                    threading.Thread(target=ytdl_combined, args=(to,search,)).start()
                elif text == 'speedtest':
                    cl.sendMessage(msg.to,"測速測試中..請燒等")
                    threading.Thread(target=speedImage, args=(to,)).start()
        if op.type == 65 and op.param2 in msg_dict and msg_dict[op.param2]["from"] not in ig["ig"]:
            rereadtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(round(msg_dict[op.param2]["createdTime"]/1000))))
            newtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            msgop = msg_dict[op.param2]["optype"]
            rat_ = "@!\n"
            if msgop == 0:  rat_+=f"• 收回位置：私聊\n位置識別：\n{op.param1}"
            elif msgop == 1:rat_+=f"• 收回位置：副本\n位置識別：\n{op.param1}"
            elif msgop == 2:rat_+=f"• 收回位置：群組\n群組名稱：\n{cl.getGroupWithoutMembers(op.param1).name}\n• 群組GID：\n{op.param1}"
            rat_ +=f"\n• 名稱：{cl.getContact(msg_dict[op.param2]['from']).displayName}"
            rat_ +=f"\n• MID：{msg_dict[op.param2]['from']}"
            if 'text' in msg_dict[op.param2]:
                if boom in msg_dict[op.param2]["text"] or boom2 in msg_dict[op.param2]["text"] or boom3 in msg_dict[op.param2]["text"] or boom4 in msg_dict[op.param2]["text"] or boom5 in msg_dict[op.param2]["text"]:rat_ += "\n[收回訊息]\n<他收回了一個當機文>"
                else:rat_+=f"\n• 收回訊息\n{msg_dict[op.param2]['text']}\n• 發送時間\n{rereadtime}\n• 收回時間\n{newtime}"
            elif 'id'    in msg_dict[op.param2]:rat_+=f"\n• 收回貼圖\n• 發送時間\n{rereadtime}\n• 收回時間\n{newtime}"
            elif 'mid'   in msg_dict[op.param2]:rat_+=f"\n• 收回友資\n• 發送時間\n{rereadtime}\n• 收回時間\n{newtime}"
            elif 'sound' in msg_dict[op.param2]:rat_+=f"\n• 收回語音\n• 發送時間\n{rereadtime}\n• 收回時間\n{newtime}"
            elif 'file'  in msg_dict[op.param2]:rat_+=f"\n• 收回檔案\n• 發送時間\n{rereadtime}\n• 收回時間\n{newtime}"
            elif 'image' in msg_dict[op.param2]:rat_+=f"\n• 收回圖片\n• 發送時間\n{rereadtime}\n• 收回時間\n{newtime}"
            elif 'Video' in msg_dict[op.param2]:rat_+=f"\n• 收回影片\n• 發送時間\n{rereadtime}\n• 收回時間\n{newtime}"
            sendMention(ban["dio"],str(rat_),[msg_dict[op.param2]['from']])
            if 'id' in msg_dict[op.param2]:
                try:cl.sendImageWithURL(ban["dio"],f'https://stickershop.line-scdn.net/stickershop/v1/sticker/{msg_dict[op.param2]["id"]}/IOS/sticker_animation.png')
                except:cl.sendImageWithURL(ban["dio"],f'https://stickershop.line-scdn.net/stickershop/v1/sticker/{msg_dict[op.param2]["id"]}/ANDROID/sticker.png')
            elif 'mid' in msg_dict[op.param2]:cl.sendContact(ban["dio"],msg_dict[op.param2]["mid"])
            elif 'sound' in msg_dict[op.param2]:cl.sendAudio(ban["dio"],msg_dict[op.param2]["sound"])
            elif 'file'  in msg_dict[op.param2]:cl.sendFile(ban["dio"] ,msg_dict[op.param2]["file"])
            elif 'image' in msg_dict[op.param2]:cl.sendImage(ban["dio"],msg_dict[op.param2]["image"])
            elif 'Video' in msg_dict[op.param2]:cl.sendVideo(ban["dio"],msg_dict[op.param2]["Video"])
            del msg_dict[op.param2]
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if sender in sender:
                if msg.contentType == 1:
                    if wait["cvp"] == True:
                        if sender in highest:
                            path1 = cl.downloadObjectMsg(msg.id)
                            wait["cvp"] = False
                            cl.updateProfilePicture(path1)
                            cl.sendMessage(to, "圖片更換成功")
                            os.remove(path1)
                    if proset["changePictureProfile"] == True:
                        time.sleep(3)
                        cl.sendMessage(op.message.to, "成功取得圖片...")    
                        path = cl.downloadObjectMsg(msg_id)
                        proset["changePictureProfile"] = False
                        cl.updateProfilePicture(path)
                        cl.sendMessage(op.message.to, "頭貼更改成功")
                    if proset["changea"] == True:
                        try:
                            time.sleep(2)
                            path = cl.downloadObjectMsg(msg_id)
                            time.sleep(1.5)
                            cl.sendMessage(to, "成功取得圖片...\n開始執行更改頭貼程序")
                            proset["changea"] = False
                            cl.changeVideoAndPictureProfile(path,clMID+".mp4")
                            cl.sendMessage(to, "頭貼更改完成")
                            os.remove(clMID + ".mp4")
                        except Exception as error:
                            print (error)
                    if proset["rafww"] == True:
                        path = cl.downloadObjectMsg(msg_id)
                        cl.sendMessage(to, "成功取得圖片...\n開始執行更改頭貼程序")
                        proset["rafww"] = False
                        cl.changeVideoAndPictureProfile(path, "test.mp4")
                        cl.sendMessage(to, "影片頭貼更改完成")
                        os.remove("test.mp4")
                        cl.sendMessage(to,"上傳完成")
                if proset["changevp"]== True:
                    if "youtube.com/watch?v=" in msg.text.lower():
                        if "&list" in msg.text.lower():
                            cl.sendMessage(to,"這是歌單網址喔")
                        else:
                            try:
                                sep = text.split("=")
                                search = msg.text.replace(sep[0]+" ","")
                                name = search.replace("https://www.youtube.com/watch?v=","")
                                print(search)
                                cl.sendMessage(to,"偵測到影片連結開始下載影片...")
                                download(search)
                                os.rename(name+".mp4","test.mp4")
                                cl.sendMessage(to,"請發送想設定的圖片")
                                proset["rafww"]= True
                                proset["changevp"]= False
                                backupData()
                            except:
                                os.remove(test+".mp4")
                                os.rename(name+".mp4","test.mp4")
                                cl.sendMessage(to,"請發送圖片")
                                proset["rafww"]= True
                                proset["changevp"]= False
                                backupData()
                    if "youtu.be" in msg.text.lower():
                        try:
                            sep = text.split("/")
                            search = msg.text.replace(sep[0]+" ","")
                            name = search.replace("https://youtu.be/","")
                            print(search)
                            aa = cl.sendMessage(to,"偵測到影片連結開始下載影片...")
                            download(search)
                            os.rename(name+".mp4","test.mp4")
                            cl.sendMessage(to,"請發送想設定的圖片")
                            proset["rafww"]= True
                            proset["changevp"]= False
                            backupData()
                        except:
                            os.remove(test+".mp4")
                            os.rename(name+".mp4","test.mp4")
                            cl.sendMessage(to,"請發送圖片")
                            proset["rafww"]= True
                            proset["changevp"]= False
                            backupData()
                if ban["reply"][to] == True:
                    if text in rpy["orgrpy"]:
                        reply = rpy["orgrpy"][text]
                        cl.sendMessage(to, str(reply))
                    else:
                        pass
                    if text in rpy["contact"]:
                        G = cl.getGroup(to)
                        reply = rpy["contact"]["{}".format(text)]
                        cl.sendContact(to, str(reply))
                    else:
                        pass
        if op.type == 55:
            try:
                if op.param1 in wait3['readPoint']:
                    if op.param2 in wait3['readMember'][op.param1]:
                        pass
                    else:
                        wait3['readMember'][op.param1] += op.param2
                        sendMention(op.param1, ban["text1"], [op.param2])
                        time.sleep(0.5)
                    wait3['ROM'][op.param1][op.param2] = op.param2
                    wait3()
                else:
                    pass
            except:
                pass
    except Exception as e:
        logError(e)


print("作者LINE ID:tim0607. 販售者LINE ID:tim0607.\n系統開始執行~")
while True:
    try:
        ops = oepoll.singleTrace(count=30)
        if ops is not None:
            for op in ops:
                if op is not None:
                    lineBot(op)
                    oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)