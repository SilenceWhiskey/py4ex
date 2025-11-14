# list是一种有序的集合，可以随时添加、删除其中的元素
# tuple定义后无法修改
# 追加使用append，插入具体位置使用insert，删除末尾pop，删除具体位置pop(i)
# list 中的元素类型可以不同
classmate_list = ['李华', '小明', '小红']
classmate_tuple = ('李华', '小明', '小红')
list_example = ['123', classmate_list, 2]

# classmate_tuple.append('小刚') 这样会报错AttributeError: 'tuple' object has no attribute 'append'

print('classmate_list里面包含', classmate_list)
classmate_list.insert(1, '小白')
print('修改后为', classmate_list)
