import Controller

if __name__ == '__main__':

    try:
        ctrller = Controller.Controller()
        ctrller.start()

    except FileNotFoundError:
        print("File not found!")

