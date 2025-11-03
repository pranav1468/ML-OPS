import numpy as np

def gradient_descent(x,y):
    m_cur=b_cur=0
    iter=1000
    n=len(x)
    Lr=0.08
    for i in range(iter):
        yp = m_cur*x+b_cur
        cost=(1/n)*sum([val**2 for val in (y-yp)])
        md=-(2/n)*sum(x*(y-yp))
        bd=-(2/n)*sum(y-yp)
        m_cur=m_cur-Lr * md
        b_cur=b_cur-Lr*bd
        print("m {}, b {}, cost{} iteration {}".format(m_cur,b_cur,cost,i))
    pass    
x=np.array([1,2,3,6,5])
y=np.array([5,7,9,15,13])

gradient_descent(x,y)
