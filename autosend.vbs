' 指定执行过程中出错的处理方式
On Error Resume Next

' 创建一个操作对象
Set Wshshell=WScript.CreateObject("WScript.Shell")

' 停顿一秒
WScript.Sleep 10

' 打开桌面应用程序（聊天窗口的桌面快捷方式，如图6，需要在路径中的双引号之前加一个"）
WshShell.run"""C:\Program Files (x86)\Tencent\QQ\Bin\QQScLauncher.exe"" /uin:1377875184 /quicklunch:8EFE6291DD6F36EFBAA84D900DAFAD85A41C7427692597C62033AD0E48B8D682A2B4FAC3133A4F04"

WScript.Sleep 10

' 将粘贴板的内容粘贴
WshShell.SendKeys"^v"

WScript.Sleep 10

' 发送
WshShell.SendKeys "%s"
