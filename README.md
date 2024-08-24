# Minecraft Rcon Website
一個可以透過網站管理多個minecraft伺服器的專案

## .env
RCON_PASSWORD = 你的Minecraft伺服器rcon密碼(server.properties中的rcon-password) <br>
DCTOKEN = Discord機器人的token <br>
DCSECRET = Discord應用程式的secret <br>
REDIRECT_URI = 重新導向連結，需要同時於Discord應用程式中的OAuth URI新增 <br>
CLIENT_ID = Discord應用程式的ID <br>

## servers.py
從第11行開始新增伺服器 <br>
Ex:Servers["lobby"] = Server("mc-lobby", 25576, password) <br>
其中:
* Servers["lobby"]中的lobby可任意改為自己的伺服器名稱
* Server("mc-lobby", 25576, password)中的mc-lobby需改成伺服器的IP
* 25576須改為在server.properties中的rcon-port (**注意** 每個伺服器的port不可以相同)
* password等同於.env中的RCON_PASSWORD，也可將其分別改為不同伺服器的rcon-password

## check_user.py
本專案透過Discord OAuth辨別身分 <br>
在第一行 admins 列表中新增所有可以使用指令功能的Discord用戶名稱 <br>
Ex:admin = ["e04._.40e", "a.uuu"] <br>
其中e04._.40e和a.uuu兩位使用者在登入後可以進入指令面板

## 其他
* 未登入狀態皆會被重新導向至Discord登入畫面
* 本專案需要先於Discord developer Portal新增應用程式，並將資訊填入.env檔才能使用
* Go to server底下需填入在servers.py中新增的伺服器名稱來快速前往Rcon指令區
* 傳送指令也可以手動透過連結:"/send/伺服器名稱/指令"，Ex:https://rcon.ckcsc.net/mod/list
* 若不是在check_user.py中的管理員列表，進入"/rcon/伺服器名稱"和使用"/send/伺服器名稱/指令"時，會被403
* 可以透過連結"/logout"登出，Ex:https://rcon.ckcsc.net/logout