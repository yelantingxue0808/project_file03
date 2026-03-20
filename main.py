"""
多进程加多线程并发爬取中药材天地网的市场价格数据

"""
from dll import service


# 执行多进程和多线程
def run():
    service.execute_task()


if __name__ == '__main__':
    run()
