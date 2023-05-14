from akad.ttypes import ApplicationType
import re, json, requests, urllib
class Config(object):
    LINE_HOST_DOMAIN            = 'https://legy-jp-addr-long.line.naver.jp'
    LINE_OBS_DOMAIN             = 'https://obs-sg.line-apps.com' #https://xcdn-cn-shp.line-apps.com
    LINE_TIMELINE_API           = 'https://legy-jp-addr-long.line.naver.jp/mh/api'
    LINE_TIMELINE_MH            = 'https://legy-jp-addr-long.line.naver.jp/mh'
    LINE_LOGIN_QUERY_PATH       = '/api/v4p/rs'
    LINE_PERMISSION_API         = 'https://access.line.me/dialog/api/permissions'
    LINE_AUTH_QUERY_PATH        = '/api/v4/TalkService.do'
    LINE_API_QUERY_PATH_FIR     = '/S4'
    LINE_POLL_QUERY_PATH_FIR    = '/P4'
    LINE_CALL_QUERY_PATH        = '/V4'
    LINE_CERTIFICATE_PATH       = '/Q'
    LINE_CHAN_QUERY_PATH        = '/CH4'
    LINE_SQUARE_QUERY_PATH      = '/SQS1'
    LINE_SHOP_QUERY_PATH        = '/SHOP4'
    LINE_LIFF_QUERY_PATH        = '/LIFF1'
    CHANNEL_ID = {
        'HELLO_WORLD': '1602289196',
        'LINE_TIMELINE': '1341209850',
        'LINE_WEBTOON': '1401600689',
        'LINE_TODAY': '1518712866',
        'LINE_STORE': '1376922440',
        'LINE_MUSIC': '1381425814',
        'LINE_SERVICES': '1459630796'
    }
    APP_TYPE    = ApplicationType._VALUES_TO_NAMES[384]
    APP_VER     = '7.5.0'
    CARRIER     = '51089, 1-0'
    SYSTEM_NAME = 'HAO_BOT'
    SYSTEM_VER  = '11.2.5'
    IP_ADDR     = '8.8.8.8'
    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

    def __init__(self, appType=None): 
        self.APP_NAME = 'DESKTOPMAC\t7.5.0\tDESKTOPMAC\t11.2.5'
        self.USER_AGENT = 'Line/7.5.0'