#coding=utf-8

def isValid(s,col):
    '''这个函数用来检查最后一个皇后的位置是否合法'''
    #当前皇后的行号
    row=len(s);
    #检查当前的皇后们是否有冲突
    for r,c in enumerate(s):
        #如果这一列已有皇后，后者某个皇后与当前皇后的水平与垂直距离相等就
        #表示当前皇后位置不合法，不允许放置
        if c==col or abs(row-r)==abs(col-c):
            return False;
    return True;

def queen(n,s=()):
    '''这个函数返回的结果是每个皇后所在的列号'''
    #已是最后一个皇后，保存本次结果
    if(len(s)==n):
        return [s];
    res=[];
    for col in range(n):
        if not isValid(s,col):
            continue;
        for r in queen(n,s+(col,)):
            res.append(r);
    return res;


def test():
    pass;

#形式转换，最终结果中包含每个皇后所在的行号和列号
result=[[(r,c) for r,c in enumerate(s)] for s in queen(8)];
#输出合法结果的数量
print(len(result));
#输出所有可能的结果，也就是皇后摆放的位置
#结果中的每个皇后的位置是一个元组，里面两个数分别是行号 和列号
for r in result:
    print(r);
