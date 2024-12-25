
import time
import pyautogui


class player_move:
    def __init__(self, x, y, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, sleep_time):
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
        self.x5 = x5
        self.y5 = y5
        self.x6 = x6
        self.y6 = y6
        self.x7 = x7
        self.y7 = y7
        self.sleep_time = sleep_time

    def move_top_left(self):
        print("Moving to top left position: ", self.x, self.y)
        pyautogui.moveTo(self.x, self.y)
        pyautogui.mouseDown(button='right')
        time.sleep(self.sleep_time)
        pyautogui.mouseUp(button='right')

    def move_top_right(self):
        print("Moving to top right position: ", self.x1, self.y1)
        pyautogui.moveTo(self.x1, self.y1)
        pyautogui.mouseDown(button='right')
        time.sleep(self.sleep_time)
        pyautogui.mouseUp(button='right')

    def move_bottom_left(self):
        print("Moving to bottom left position: ", self.x2, self.y2)
        pyautogui.moveTo(self.x2, self.y2)
        pyautogui.mouseDown(button='right')
        time.sleep(self.sleep_time)
        pyautogui.mouseUp(button='right')

    def move_bottom_right(self):
        print("Moving to bottom right position: ", self.x3, self.y3)
        pyautogui.moveTo(self.x3, self.y3)
        pyautogui.mouseDown(button='right')
        time.sleep(self.sleep_time)
        pyautogui.mouseUp(button='right')

    def move_top(self):
        print("Moving to top position: ", self.x4, self.y4, self.x5, self.y5)
        pyautogui.moveTo(self.x4, self.y4)
        pyautogui.mouseDown(button='right')
        time.sleep(self.sleep_time)
        pyautogui.mouseUp(button='right')
    
    def move_bottom(self):
        print("Moving to bottom position: ", self.x5, self.y5, self.x6, self.y6)
        pyautogui.moveTo(self.x5, self.y5)
        pyautogui.mouseDown(button='right')
        time.sleep(self.sleep_time)
        pyautogui.mouseUp(button='right')
    
    def move_left(self):
        print("Moving to left position: ", self.x6, self.y6, self.x7, self.y7)
        pyautogui.moveTo(self.x6, self.y6)
        pyautogui.mouseDown(button='right')
        time.sleep(self.sleep_time)
        pyautogui.mouseUp(button='right')

    def move_right(self):
        print("Moving to right position: ", self.x7, self.y7, self.x, self.y)
        pyautogui.moveTo(self.x7, self.y7)
        pyautogui.mouseDown(button='right')
        time.sleep(self.sleep_time)
        pyautogui.mouseUp(button='right')

    





# def move_top_left():
#     print("Moving to top left position: ", top_left_x, top_left_y, middle_x , middle_y)
#     pyautogui.moveTo(top_left_x, top_left_y)
#     pyautogui.mouseDown(button='right')
#     time.sleep(sleep_time)
#     pyautogui.mouseUp(button='right')


# def move_top_right():
#     print("Moving to top right position: ", top_right_x, top_right_y, middle_x , middle_y)
#     pyautogui.moveTo(top_right_x, top_right_y)
#     pyautogui.mouseDown(button='right')
#     time.sleep(sleep_time)
#     pyautogui.mouseUp(button='right')

# def move_bottom_left():
#     print("Moving to bottom left position: ", bottom_left_x, bottom_left_y, middle_x , middle_y)
#     pyautogui.moveTo(bottom_left_x, bottom_left_y)
#     pyautogui.mouseDown(button='right')
#     time.sleep(sleep_time)
#     pyautogui.mouseUp(button='right')

# def move_bottom_right():
#     print("Moving to bottom right position: ", bottom_right_x, bottom_right_y, middle_x , middle_y)
#     pyautogui.moveTo(bottom_right_x, bottom_right_y)
#     pyautogui.mouseDown(button='right')
#     time.sleep(sleep_time)
#     pyautogui.mouseUp(button='right')

# def move_top():
#     print("Moving to top position: ", top_x, top_y, middle_x , middle_y)
#     pyautogui.moveTo(top_x, top_y)
#     pyautogui.mouseDown(button='right')
#     time.sleep(sleep_time)
#     pyautogui.mouseUp(button='right')

# def move_bottom():
#     print("Moving to bottom position: ", bottom_x, bottom_y, middle_x , middle_y)
#     pyautogui.moveTo(bottom_x, bottom_y)
#     pyautogui.mouseDown(button='right')
#     time.sleep(sleep_time)
#     pyautogui.mouseUp(button='right')

# def move_left():
#     print("Moving to left position: ", left_x, left_y, middle_x , middle_y)
#     pyautogui.moveTo(left_x, left_y)
#     pyautogui.mouseDown(button='right')
#     time.sleep(sleep_time)
#     pyautogui.mouseUp(button='right')

# def move_right():
#     print("Moving to right position: ", right_x, right_y, middle_x , middle_y)
#     pyautogui.moveTo(right_x, right_y)
#     pyautogui.mouseDown(button='right')
#     time.sleep(sleep_time)
#     pyautogui.mouseUp(button='right')




