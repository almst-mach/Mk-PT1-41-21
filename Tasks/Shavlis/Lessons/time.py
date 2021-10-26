import time

# time.sleep()

def show_promo():
    print('buy me!')

def start_promo(promo):
    while True:
        promo()
        time.sleep(5)

start_promo(show_promo)
