from lxml import etree

# xpath 解析方式 1.本地 2.网络

tree = etree.parse("bs4_base.html")

# 路径查询
# / 查子节点
# // 查深层次节点
li_list = tree.xpath('//body//li')
# also ok
# li_list = tree.xpath('//body/ul/li')
print(len(li_list))

# 谓词查询 [@id]
# 查找所有有id属性的li标签
id_list = tree.xpath('//ul/li[@id]')
print(len(id_list))

# 获取标签内容
id_list_content = tree.xpath('//ul/li[@id]/text()')
print(id_list_content)

# 找到id为l1的li标签值 注意内双引号
id_list_l1 = tree.xpath('//ul/li[@id="l1"]/text()')
print(id_list_l1)

# 查询标签为l1的标签的class属性值
id_list_l1_class = tree.xpath('//ul/li[@id="l1"]/@class')
print(id_list_l1_class)

# 模糊查询
# 包含
id_list_like = tree.xpath('//ul/li[contains(@id, "l")]/text()')
# 同前缀
id_list_like_prefix = tree.xpath('//ul/li[starts-with(@id, "l")]/text()')
print(id_list_like)
print(id_list_like_prefix)

# 内容查询
content = tree.xpath('//ul/li/text()')
print(content)

# 逻辑运算
id_and_class = tree.xpath('//ul/li[@id="l1" and @class = "c1"]/text()')
id_or = tree.xpath('//ul/li[@id="l1"]/text() | //ul/li[@id="l2"]/text()')
print(id_and_class)
print(id_or)
