# 全局变量在函数内赋值需先用global关键字进行声明

start_flag = True # 全局变量
knn = 3 # 全局变量


def func():
    """
    全局变量可以在函数中多次引用，但如果要对全局变量在函数中赋值，
    则需要先用global关键字在函数内对全局变量进行声明
    """
    # global start_flag
    print(start_flag)
    print('aaa'* knn)
    # for _ in range(10):
    #     if start_flag: # 如果上面不声明，这里默认是局部变量
    #         print('开始')
    #         start_flag = False
    #     print('测试')
    print([11]*knn)
    


if __name__ == '__main__':
    func()