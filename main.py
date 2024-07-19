import threading

def print_number():
    for i in range(1, 6):
        print(i)

def print_letters():
    for letter in ['A', 'B', 'B', 'D', 'E']:
        print(letter)

thread1 = threading.Thread(target=print_number)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Done")

print_number()
print_letters()
