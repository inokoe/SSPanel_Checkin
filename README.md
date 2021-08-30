# SSPanel_Checkin
[![SSPanel_Checkin](https://github.com/inokoe/SSPanel_Checkin/actions/workflows/main.yml/badge.svg)](https://github.com/inokoe/SSPanel_Checkin/actions/workflows/main.yml)

This is a dish chicken script for automatic check-in of sspanel for GitHub action,
It is only applicable when there is no verification code protection and cloudflare protection, and there is no more perfect exception handling and push.
 
这是一个用于GitHub action 的 sspanel 自动签到的菜鸡脚本,
仅仅适用于没有验证码保护，没有cloudflare保护的情况下，没有做更完善的异常处理和推送。
 
# How to use

 Add secrets
 在Secrets中增加

 AIRPORTUR、USERNAME、USERPASSWD

 spilt with &&
 以&&作为分割

# Example

AIRPORTUR https://github.com
USERNAME 123
USERPASSWD 456

OR

AIRPORTUR https://github.com&&https://github.com
USERNAME 123&&123
USERPASSWD 456&&456

