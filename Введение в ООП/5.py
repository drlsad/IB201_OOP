class BigBell:
    def __init__(self):
        self._is_ding = True  

    def sound(self):
        if self._is_ding:
            print("ding")
            self._is_ding = False  
        else:
            print("dong")
            self._is_ding = True   

bell = BigBell()
bell.sound()  # Вывод: ding
bell.sound()  # Вывод: dong
bell.sound()  # Вывод: ding
