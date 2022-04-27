import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

class Main:
    home_page = ''
    project_name = ''
    DOMAIN_NAME = ''
    queue_file = ''
    crawled_file = ''
    number_of_threads= 8
    queue = Queue()

    def __init__(self, home_page):
        Main.home_page=home_page
        Main.project_name="siteCrawled/"+get_project_name(home_page)
        Main.domain_name=get_domain_name(home_page)
        Main.queue_file=Main.project_name+'/queue.txt'
        Main.crawled_file=Main.project_name+'/crawled.txt'
        Spider(Main.project_name, Main.home_page, Main.domain_name)
        
    # Create worker threads (will die when main exits)
    @staticmethod
    def create_workers():
        for _ in range(Main.number_of_threads):
            t = threading.Thread(target=Main.work)
            t.daemon = True
            t.start()


    # Do the next job in the queue
    @staticmethod
    def work():
        while True:
            url = Main.queue.get()
            Spider.crawl_page(threading.current_thread().name, url)
            Main.queue.task_done()


    # Each queued link is a new job
    @staticmethod
    def create_jobs():
        for link in file_to_set(Main.queue_file):
            Main.queue.put(link)
        Main.queue.join()
        Main.crawl()


    # Check if there are items in the queue, if so crawl them
    @staticmethod
    def crawl():
        queued_links = file_to_set(Main.queue_file)
        if len(queued_links) > 0:
            print(str(len(queued_links)) + ' links in the queue')
            Main.create_jobs()


