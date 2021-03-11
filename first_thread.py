from threading import Thread
import time


def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))


def main():
    try:
        thread_list = []
        for i in range(1,3):
            thread = Thread(target=print_time, args=("Thread-" + str(i), i * 2))
            thread_list.append(thread)
            thread.start()
    except Exception as ex:
        print(ex)

    for thread in thread_list:
        thread.join()

    print("Done")


if __name__ == "__main__":
    main()
