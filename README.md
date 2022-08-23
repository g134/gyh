# 每日早安推送给别人家的女朋友[自用版]


公众号模板

```text
 {{text_date.DATA}}
 {{city.DATA}}{{weather.DATA}}
 空气质量：{{air_level.DATA}}  湿度：{{humidity.DATA}}
 {{air_tips.DATA}}
 最低温度：{{low.DATA}}℃
 最高温度：{{high.DATA}}℃
 今天是我们结婚：{{love_days.DATA}}天
 小甜甜出生第：{{yutian_days.DATA}}天
 距离你的生日还有{{birthday_left.DATA}}天
 
 {{words.DATA}}
```
github变量
```text
APP_ID
APP_SECRET
TEMPLATE_ID
USER_ID
START_DATE
BIRTHDAY
CITY
YUTIANDAY
ll_KEY
```
变量说明
`TEMPLATE_ID` 为模板ID
`USER_ID` 多个可以用`,`隔开
`YUTIANDAY` 为宝宝出生日期，格式参照纪念日格式
`ll_KEY` 为农历API接口Key

ps. 有一些注意事项在此补充

1. 第一次登录微信公众平台测试号给的 app secret 是错误的，刷新一下页面即可
2. 生日的日期格式是：`05-20`，纪念日的格式是 `2022-08-09`，请注意区分。城市请写到地级市，比如：`北京`，`广州`，`承德`
3. 变量中粘贴的各种英文字符串不要有空格，不要有换行，除了模板之外都没有换行
4. Github Actions 的定时任务，在 workflow 的定义是 `0 0 * * *`，是 UTC 时间的零点，北京时间的八点。但是由于 Github 同一时间任务太多，因此会有延迟

