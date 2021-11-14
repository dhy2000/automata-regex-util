import regex
from automata import Automata

# 注意：以下多组被注释的输出语句只能选择一组取消注释以查看输出

'''
Example 1: DFA
'''
# start = '0' # 定义起始状态，状态名称可以是整数或字符串
# finish = ('3', )    # 定义终止状态集（以元组、列表等形式给出）
# trans = [   # 定义状态转移边，每条边为一个三元组，元素依次为：源状态，目标状态，引起状态转移的输入
#     ['0', '1', 'a'],
#     ['0', '2', 'b'],
#     ['1', '2', 'b'],
#     ['2', '1', 'a'],
#     ['1', '3', 'a'],
#     ['2', '3', 'b'],
#     ['3', '3', 'a'],
#     ['3', '3', 'b'],
# ]
# # 约束：起始状态、终止状态必须出现在状态转移当中
# dfa = Automata(start, finish, trans) # 构造 Automata 类，参数依次为起始状态，终止状态集，转移规则集
# dfa.print_trans_table() # 在 stdout 打印该状态机的状态转移矩阵
# dfa.show() # 用 graphviz 库输出该状态机的状态图


'''
Example 2: NFA
'''
# start = 1   # 可以用整数或字符串来表示状态
# finish = (4, )
# trans = [
#     [1, 2, 'a'],
#     [1, 3, 'a'],
#     [2, 2, 'a'],
#     [2, 4, 'b'],
#     [3, 3, 'c'],
#     [3, 4, 'c'],
#     [1, 4, '']
# ]
# # 构造 NFA 以及将 NFA 转化成 DFA

# nfa = Automata(start, finish, trans)
# assert not nfa.is_deterministic() # is_deterministic(): 判断该自动机是否是 DFA, 这里显然不是
# # ---- 取消注释以查看 NFA ----
# # nfa.print_trans_table() # 打印 NFA 的状态转移矩阵
# # nfa.show() # 显示 NFA 的状态图

# dfa = nfa.to_deterministic() # 将 NFA 转成 DFA, 会在 stdout 输出转换过程
# assert dfa.is_deterministic() # 转化后的自动机是 DFA
# # ---- 取消注释以查看 DFA ----
# # dfa.print_trans_table() # 打印 DFA 的状态转移矩阵
# # dfa.show() # 显示 DFA 的状态图

'''
Example 3: DFA 最小化
'''
# start = 1
# finish = (5, 6, 7)
# trans = [
#     [1, 6, 'a'], [1, 3, 'b'],
#     [2, 7, 'a'], [2, 3, 'b'],
#     [3, 1, 'a'], [3, 5, 'b'],
#     [4, 4, 'a'], [4, 6, 'b'],
#     [5, 7, 'a'], [5, 3, 'b'],
#     [6, 4, 'a'], [6, 1, 'b'],
#     [7, 4, 'a'], [7, 2, 'b'],
# ]

# dfa = Automata(start, finish, trans)
# assert dfa.is_deterministic() # 是一个 DFA
# # ---- 取消注释以输出非最简的 DFA ----
# # dfa.print_trans_table()
# # dfa.show()

# min_dfa = dfa.minify() # 将 DFA 最小化，在 stdout 输出最小化 DFA 的过程，即将状态进行 "分区" 的表格（注意，这里分区号没有按从 1 开始递增的顺序）
# # ---- 取消注释以输出最简的 DFA ----
# # min_dfa.print_trans_table()
# # min_dfa.show()

'''
Example 4: 正则表达式转自动机
'''
nfa = regex.regexToAutomata(r'1(1010*|1(010)*1)*0')
# ---- 取消注释以输出 NFA ----
# nfa.print_trans_table()
# nfa.show()

dfa = nfa.to_deterministic() # NFA to DFA
# ---- 取消注释以输出 DFA ----
# dfa.print_trans_table()
# dfa.show()

min_dfa = dfa.minify() # 最小化 DFA
# ---- 取消注释以输出最简 DFA ----
min_dfa.print_trans_table()
min_dfa.show()
