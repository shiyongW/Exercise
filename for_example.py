#coding=utf-8

def demo(*p):
    avg=sum(p)/len(p);
    g=[i for i in p if i>avg];#列表推导式
    print(g);
    return (avg,)+tuple(g);

print(demo(1,2,3))
