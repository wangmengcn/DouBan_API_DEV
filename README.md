# DouBan_API_DEV
使用豆瓣提供的[API](https://developers.douban.com/wiki/?title=api_v2)获取包括电影、图书和音乐等信息，以JSON格式返回数据，可以直接把这些数据丢给MonogDB存储。
# 代码结构
- tag_collection.py 用以通过tags中html文件获取标签信息
- spider_rule.py 按照豆瓣官方要求对不同类型数据执行不同的抓取规则
- db_manager.py 用以连接MongoDB
- run.py 运行此文件开始抓取数据

# 使用方法
通过修改run.py中get_info()的参数来获取不同的数据。
- movie 获取包括电影数据
- music 获取音乐信息
- book 获取图书信息
