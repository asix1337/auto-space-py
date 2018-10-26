import random
import threading
import time
import winsound

import keyboard


def task():
    t = threading.currentThread()
    while getattr(t, 'do_run', True):
        keyboard.press('space')
        time.sleep(random.uniform(0.05, 0.1))
        keyboard.release('space')


def main():
    global thread
    global is_active
    is_active = False

    def x():
        global thread
        global is_active
        if not is_active:
            thread = threading.Thread(target=task)
            thread.start()
            print('Started with a interval between 0.05 and 0.1 seconds.')
        else:
            thread.do_run = False
            thread.join()
            del thread
            winsound.Beep(1500, 150)
            print('Stopped.')
        is_active = not is_active

    print('Press {0} key to start. Press {0} key again to stop. Press CTRL+C to Exit.'.format('DEL'))
    keyboard.add_hotkey('del', x)
    try:
        keyboard.wait()
    except KeyboardInterrupt:
        print('Exit.')


if __name__ == "__main__":
    main()
