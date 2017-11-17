# depth first
def depth_tree(tree_node):
	if tree_node is not None:
		print(tree_node._data)
		if tree_node._left is not None:
			return depth_tree(tree_node._left)
		if tree_node._right is not None:
			return depth_tree(tree_node._right)

# width first
def level_queue(root):
	if root is None:
		return
	my_queue = []
	node = root
	my_queue.append(node)
	while my_queue:
		node = my_queue.pop(0)
		print(node.elem)
		if node.lchild is not None:
			my_queue.append(node.lchild)
		if node.rchild is not None:
			my_queue.append(node.rchild)


"""
8 bit=1 byte
最大数字为255
GB2312两个字节表示一个汉字，偏的可以用3或4个
unicode用8位和16位统一所有编码
unicode兼容ascii，前面加0；两个字节表示所有
为了解决空间问题，出现utf-8，英文1个字节，汉语三个字节，特别生僻的编程4-6个字节

"""

"""
进入虚拟环境，安装scrapyd

"""
"""
python单例模式

"""
class Singleton(object):
	def __new__(cls, *args, **kwargs):
		if not hasattr(cls, '_instance'):
			orig = super(Singleton, cls)
			cls._instance = orig.__new__(cls, *args, **kwargs)

		return cls._instance


class Borg(object):
	_state = {}
	def __new__(cls, *args, **kwargs):
		ob = super(Borg, cls).__new__(cls, *args, **kwargs)
		cls.__dict__ = ob._state
		return ob


"""
斐波那契数列
"""
def fib(n):
	a, b = 0, 1
	for x in range(n):
		a, b = b, a + b
		yield b

y = fib(9)
for sa in y:
	print(sa)





