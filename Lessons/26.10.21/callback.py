import time, threading

# time.sleep(5)
# print("after sleep")

def show_promo():
    print("buy me!")

def start_promo(promo):
    promo()
    time.sleep(5)
    start_promo(promo)
    
def call():
    print("sdfgdjhkgfxdfgjhkljhdfgsghjkljhgdfsghjklhgfdsfghjkljhgfdhjkl!")
    threading.Timer(5, call).start()
    for i in range(100000000):
        print(i)

call()