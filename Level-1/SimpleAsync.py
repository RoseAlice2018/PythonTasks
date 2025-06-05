import time
import asyncio

# 同步代码示例
def sync_task(name, delay):
    print(f"开始任务 {name}")
    time.sleep(delay)  # 阻塞等待
    print(f"完成任务 {name}")
    return f"结果 {name}"

# 异步代码示例
async def async_task(name, delay):
    print(f"开始任务 {name}")
    await asyncio.sleep(delay)  # 非阻塞等待
    print(f"完成任务 {name}")
    return f"结果 {name}"

def main():
    # 同步代码示例
    result1 = sync_task("同步任务1", 5)
    result2 = sync_task("同步任务2", 3)
    print(result1)
    print(result2)

    # 异步代码示例
    result3 = asyncio.create_task(async_task("异步任务1", 5))
    result4 = asyncio.create_task(async_task("异步任务2", 3))

main()