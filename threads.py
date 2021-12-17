from server.exc_thread import ExcThread
from server.parser import SpringsToCodeParser

# Thread 'sda'
def thread1():
    d = 4
    if d == d:
            print('d =', d)
        print('d =', d)


results = ''
threads = []
thread = ExcThread(name='1. sda', target=thread1)
threads.append(thread)
thread.start()
[thread.join() for thread in threads]


for thread in threads:
    results += thread.status()
with open(SpringsToCodeParser.RESULT_FILE_PATH, "w+") as file:
    file.write(results)