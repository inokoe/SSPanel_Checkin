## SSPanel_Checkin
[![SSPanel_Checkin](https://github.com/inokoe/SSPanel_Checkin/actions/workflows/main.yml/badge.svg)](https://github.com/inokoe/SSPanel_Checkin/actions/workflows/main.yml)

This is a dish chicken script for automatic check-in of sspanel for GitHub action,
It is only applicable when there is no verification code protection and cloudflare protection, and there is no more perfect exception handling and push.
 
这是一个用于GitHub action 的 sspanel 自动签到的菜鸡脚本,
仅仅适用于没有验证码保护，没有cloudflare保护的情况下，没有做更完善的异常处理和推送。
 
## How to use

 First,Fork, set secrets [AIRPORTURL] [USERNAME] [USERPASSWD]  
 Then start action file.  
 If your secrets is right , the action will running successful.  
 And Multi URL split with &&.
 
 首先，您需要Fork , 并在Secrets中增加 [AIRPORTURL] [USERNAME] [USERPASSWD] 三个值。  
 最后启用Action files,如果Secrets设置正确的值，脚本将会正常运行。  
 支持多个机场签到，多个值使用&&分割。  


## Example

AIRPORTURL https://github.com

USERNAME LoginName

USERPASSWD LoginPassword

OR

AIRPORTURL https://github.com&&https://github.com

USERNAME LoginNameA&&LoginNameB

USERPASSWD LoginPasswordA&&LoginPasswordB

This use case shows that AIRPORTURL[0] USERNAME[0] USERPASSWD[0] these three attributes are a set of Web Login data.  
Note that the URL must be a string with HTTP (HTTPS), such as https://github.com , he must end with a domain name

此用例显示 AIRPORTURL[0] USERNAME[0] USERPASSWD[0] 这三个属性是一组Web登录数据。  
注意，URL必须是一个带Http（Https）的字符串，如https://github.com，他必须以域名结尾。  
## IMAGE
![image](https://user-images.githubusercontent.com/45820630/133551741-f836b3f8-b9f5-42c5-bb41-c09f4dcb7f59.png)

## Stargazers over time

[![Stargazers over time](https://starchart.cc/inokoe/SSPanel_Checkin.svg)](https://starchart.cc/inokoe/SSPanel_Checkin)

