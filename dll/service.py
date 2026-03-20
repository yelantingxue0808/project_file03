from multiprocessing import Pool, Manager
from concurrent.futures import ThreadPoolExecutor, wait
from utils import utils
from save_data import dao

# 多进程获取所有的url
def get_url(num, lis):
    if num == 0:
        for url in range(1, 30):
            url = f'https://www.zyctd.com/jiage/1-0-0-{url}.html'
            lis.append(url)
    elif num == 1:
        for url in range(30, 60):
            url = f'https://www.zyctd.com/jiage/1-0-0-{url}.html'
            lis.append(url)
    elif num == 2:
        for url in range(60, 90):
            url = f'https://www.zyctd.com/jiage/1-0-0-{url}.html'
            lis.append(url)
    else:
        for url in range(90, 123):
            url = f'https://www.zyctd.com/jiage/1-0-0-{url}.html'
            lis.append(url)


# 执行多进程和多线程并返回任务
def execute_task():
    # 创建一个列表对象
    lis = Manager().list()
    # 创建4个进程池来收集122页html的url,作为生产者
    pool = Pool(4)
    for i in range(4):
        pool.apply_async(func=get_url, args=(i, lis))
    # 关闭进程池
    pool.close()
    # 等待所有子进程完成
    pool.join()
    # print('主进程的列表', lis)
    # 创建12个线程来请求url获取数据
    thread_pool = ThreadPoolExecutor(12)
    tasks = [thread_pool.submit(utils.send_url, url_html) for url_html in lis]
    # 等待所有子线程完成
    wait(tasks)
    dao.save_data(tasks)
