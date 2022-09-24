import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import os
 
if __name__ == "__main__":
    # 対象ディレクトリ
    DIR_WATCH = './save_img'
    # 対象ファイル名のパターン
    PATTERNS = ['*.jpg']

    def on_modified(event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        print('%s changed' % filename)

    # event_handler = LoggingEventHandler()
    event_handler = PatternMatchingEventHandler(PATTERNS)
    event_handler.on_modified = on_modified
    
    observer = Observer()
    observer.schedule(event_handler, DIR_WATCH, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()