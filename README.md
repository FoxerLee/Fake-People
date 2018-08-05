# Fake-People
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://github.com/FoxerLee/Fake-People/blob/master/LICENSE)

中国大陆人物信息生成，包括人名、电话、邮箱、地址。

## 人名
抓取网页上随机生成的人名，每次刷新更新100个人名。
- 源代码：[FakeName.py](https://github.com/FoxerLee/Fake-People/blob/master/FakeName.py)
- 数据来源：http://www.gaoshukai.com/lab/0014/cn.php

## 电话
首先随机选取中国移动、中国联通、中国电信的前3位电话段，后9位则通过随机数生成(0, 99999999)的int变量，利用0补全不足的位数。
- 源代码 [RandomPhone.py](https://github.com/FoxerLee/Fake-People/blob/master/RandomPhone.py)

## 邮箱
暂代补充

## 地址
利用该 [Repository](https://github.com/modood/Administrative-divisions-of-China) 获取到的中华人民共和国行政区划代码、统计用区划和城乡划分代码，根据其划分代码将区划构建成完整的地址。

- ⚠️：代码中的address精确到区、乡镇一级，如果street则精确到街道一级，street需要利用address获取到的地址。
- ⚠️：如需获取最新原始地址，请前往 [Repository](https://github.com/modood/Administrative-divisions-of-China)。
- 源代码 [Address.py](https://github.com/FoxerLee/Fake-People/blob/master/Address.py)
- 数据来源：https://github.com/modood/Administrative-divisions-of-China

## 综合
获取到前3种数据后，随机组合后获得一个“虚拟“🇨🇳人。
- 源代码 [FakePeople.py](https://github.com/FoxerLee/Fake-People/blob/master/FakePeople.py)
