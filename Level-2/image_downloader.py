# 实现一个并发下载系统：
# 1. 创建一个图片下载器，支持并发下载多个URL的图片
# 2. 要求：
#    - 使用线程池控制并发数
#    - 实现进度条显示总体下载进度
#    - 正确处理GIL，对于I/O密集型任务优化性能
#    - 实现超时和重试机制
#    - 使用异步回调通知下载完成

from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
import threading
import requests
import time
import multiprocessing

# 多线程版本
class ImageDownloader:
    def __init__(self, max_workers=4):
        # 实现并发下载器
        self.max_workers = max_workers
        pass

    def download_one_image(self, url, filename):
        pass

    def download(self, urls, filenames):
        # 下载图片
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [executor.submit(self.download_one_image, url, filename) for url, filename in zip(urls, filenames)]
            for future in concurrent.futures.as_completed(futures):
                try:
                    result = future.result()
                    if result:
                        print(f"下载成功：{result}")
                except Exception as e:
                    print(f"下载失败：{e}")

# 多进程版本 
class ImageDownloader1:
    def __init__(self, max_workers=4):
        # 实现并发下载器
        self.max_workers = max_workers
        pass

    def download_one_image(self, url, filename):
        pass

    def download(self, urls, filenames):
        # 下载图片
        with multiprocessing.Pool(process=3) as pool:
            results = pool.map(self.download_one_image, urls, filenames)
            print(results)


