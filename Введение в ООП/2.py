class Button:
    def __init__(self):
        self._click_count = 0

    def click(self):
        self._click_count += 1

    def click_count(self):
        return self._click_count

    def reset(self):
        self._click_count = 0


button = Button()
button.click()
button.click()
print(button.click_count())  
button.click()
print(button.click_count()) 
