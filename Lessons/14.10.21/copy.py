chunk = 10000

with open("image.jpg", "rb") as donor:
    with open("image-copy.jpg", "wb") as receiver:
        while True:
            cc = donor.read(chunk)
            if not cc:
                break
            receiver.write(cc)