import subprocess
import win32clipboard as w
import win32con
import time
import sys

count = 0

while True:
    if time.localtime().tm_mon == 6:
        while True:
            msg = '儿童节快乐'
            # 将消息导入粘贴板
            w.OpenClipboard()
            w.EmptyClipboard()
            w.SetClipboardData(win32con.CF_UNICODETEXT, msg)
            w.CloseClipboard()
            subprocess.call('cscript autosend.vbs')
            count = count + 1
            if count == 61:
                sys.exit()

