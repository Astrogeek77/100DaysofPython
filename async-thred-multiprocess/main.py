import requests
import multiprocessing
import threading
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import asyncio

curr_path = "C:\\Coding\\Python\\100DaysofCode\\async-thred-multiprocess"

# '''AsyncIO'''


async def function1():
    print("func 1")
    URL = "https://wallpaperaccess.in/public/uploads/preview/1920x1200-desktop-background-ultra-hd-wallpaper-wiki-desktop-wallpaper-4k-.jpg"
    response = requests.get(URL)
    open("instagram.ico", "wb").write(response.content)

    return "Harry"


async def function2():
    print("func 2")
    URL = "https://p4.wallpaperbetter.com/wallpaper/490/433/199/nature-2560x1440-tree-snow-wallpaper-preview.jpg"
    response = requests.get(URL)
    open("instagram2.jpg", "wb").write(response.content)


async def function3():
    print("func 3")
    URL = "https://c4.wallpaperflare.com/wallpaper/622/676/943/3d-hd-wikipedia-3d-wallpaper-preview.jpg"
    response = requests.get(URL)
    open("instagram3.ico", "wb").write(response.content)


async def main():
    # await function1()
    # await function2()
    # await function3()
    # return 3
    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
    print(L)
    # task = asyncio.create_task(function1())
    # # await function1()
    # await function2()
    # await function3()

# asyncio.run(main())

# Indicates some task being done

# '''Threading'''


def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds


def main():
    time1 = time.perf_counter()
    # Normal Code
    # func(4)
    # func(2)
    # func(1)

    # Same code using Threads
    t1 = threading.Thread(target=func, args=[4])
    t2 = threading.Thread(target=func, args=[2])
    t3 = threading.Thread(target=func, args=[1])
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    # Calculating Time
    time2 = time.perf_counter()
    print(time2 - time1)


def poolingDemo():
    with ThreadPoolExecutor() as executor:
        # future1 = executor.submit(func, 3)
        # future2 = executor.submit(func, 2)
        # future3 = executor.submit(func, 4)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())
        l = [3, 5, 1, 2]
        results = executor.map(func, l)
        for result in results:
            print(result)


# poolingDemo()
# main()

# '''Multi-Processing'''


def downloadFile(url, name):
    print(f"Started Downloading {name}")
    response = requests.get(url)
    open(f"{curr_path}\\files\\file-{name}.jpg", "wb").write(response.content)
    print(f"Finished Downloading {name}")


def main1():
    # url = "https://picsum.photos/1920/1080"
    url = "https://source.unsplash.com/1600x900/?space"
    pros = []
    for i in range(1, 5):
        # downloadFile(url, i)
        p = multiprocessing.Process(target=downloadFile, args=[url, i+1])
        p.start()
        pros.append(p)

    for p in pros:
        p.join()


def main2():
    url = "https://picsum.photos/2000/3000"
    with ProcessPoolExecutor() as executor:
        l1 = [url for i in range(60)]
        l2 = [i for i in range(60)]
        results = executor.map(downloadFile, l1, l2)
        for r in results:
            print(r)


if __name__ == "__main__":
    main1()
    # main2()
