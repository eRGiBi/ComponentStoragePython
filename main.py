import Controller

try:
    Controller.start()

except FileNotFoundError:
    print("File not found!")