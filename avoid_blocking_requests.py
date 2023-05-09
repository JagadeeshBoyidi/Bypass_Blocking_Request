import threading
from queue import Queue

def get_raw_positions(client):
    
    '''assuming get positions returns current day all the positons'''
    
    try:
        return client.get_positions() 
    except:
        pass
        

def make_request_with_retry(client):
    response_queue = Queue()
    response = 'j'
    
    for i in range(3):
        thread = threading.Thread(target=lambda: response_queue.put(get_raw_positions(client)))
        thread.start()
        thread.join(timeout=3)
        if thread.is_alive():
            print(f"Thread {thread.ident} timed out on try {i+1}")
        else:
            response = response_queue.get()
            break
    return response


'''pass the client object as a parameter to get the day positions'''

client = "client"

positions =  make_request_with_retry(client)