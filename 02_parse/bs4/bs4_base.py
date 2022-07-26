from bs4 import BeautifulSoup

soup = BeautifulSoup(open('bs4_base.html', encoding="utf8"), 'lxml')

# 根据标签查找节点 找到的是第一个符合条件的数据
print(soup.a)

# 获取标签的属性和属性值
print(soup.a.attr)

# find
# 找到第一个符合条件的数据
print(soup.find('a'))

# 根据title值寻找标签对象
print(soup.find('a', title="a2"))

# class属性要带下划线
print(soup.find('a', class_="123"))

# 获取多个标签的数据
print(soup.find_all(['a', 'span']))

# limit限制找到前几个数据
print(soup.find_all('a', limit=2))

# select返回一个列表 包含多个数据
print(soup.select('a'))

# 通过 . 代替class，类选择器
print(soup.select('li.c1'))

# 属性选择器 通过属性来寻找对应的标签
print(soup.select('li[id]'))

# li标签中id为l2的标签
print(soup.select('li[id="l2"]'))

# 层级选择器 找到的是ul下的li
print(soup.select('ul li'))

# 子代选择球
print(soup.select('ul > li > a'))

# a标签和li标签的所有对象
print(soup.select('a,li'))

# 获取节点信息
obj = soup.select('#p1')[0]
print(obj.get_text())
