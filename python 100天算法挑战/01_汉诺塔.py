'''
如果我们要将最大的圆盘移动到最右边的柱子上。我们需要把除此圆盘的其他圆盘先移动到中间的柱子上。
因此这个问题就变成了如何将 N-1 个圆盘移动到中间的柱子上。
很容易我们就想到了递归的方法。

将 N 个圆盘从左边柱子移动到右边柱子：

[递归的]将 N-1 个圆盘从左边柱子移动到中间柱子。
将最大的圆盘从左边柱子移动到右边柱子。
[递归的]将 N-1 个圆盘从中间柱子移动到右边柱子。
'''
def hannoi(height,left='left',right='right',middle='middle'):
    if height:
        hannoi(height - 1,left,middle,right)
        print(left,'=>',right)
        hannoi(height - 1,middle,right,left)

hannoi(3)