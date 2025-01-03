import os
import threading
import time
from pygetwindow import getWindowsWithTitle
import pywinauto
import pyautogui
import pytesseract
from PIL import Image
# ...existing code...
import warnings

from move import player_move
from node import astar
from position import coordinate
import threading
import time
import pyautogui
import pygetwindow as gw
import win32con
import win32api
import win32gui

from read_map_file import read_header


# ...existing code...
# app = pywinauto.application.Application().connect(path='D:\部落传奇\部落冲突20241214\部落冲突.exe')

# Assuming you know the title of the window
window_list = getWindowsWithTitle('部落冲突二区')
if window_list:
    window = window_list[0]
    roi_left = window.left + 60
    roi_top = window.top + 775
    roi_width = window.width - 970
    roi_height = window.height - 778

    # screen size is 1030*797
    # 4 quandrant of the screen
    # 1st quandrant point 

    # print(f"Window found: {window.title}")
    print(f"Window top-left corner: ({window.left}, {window.top}) Window size: {window.width} x {window.height} middle point: {window.left + window.width//2} x {window.top + window.height//2+150}")
else:
    print("Window not found")
    
sleep_time = 10

# middle_x = window.left + window.width//2
# middle_y = window.top + window.height//2+150

# top_left_x, top_left_y = (middle_x - 150, middle_y-300)  
# top_right_x, top_right_y = (middle_x+150, middle_y - 300)  
# bottom_left_x, bottom_left_y = ( middle_x- 150, middle_y+20)  
# bottom_right_x, bottom_right_y = ( middle_x+150, middle_y+20)  

# top_x, top_y = ( middle_x, middle_y - 300)  
# bottom_x, bottom_y = ( middle_x, middle_y)  
# left_x, left_y = ( middle_x - 50, middle_y-220)  
# right_x, right_y = ( middle_x + 150, middle_y-250)  

def test_move():
    pyautogui.moveTo(443,241)
    pyautogui.mouseDown(button='right')
    time.sleep(sleep_time)
    pyautogui.mouseUp(button='right')



def press_key(key, duration=0.1):
    """
    Press a single key.
    
    :param key: The key to press (e.g., 'w', 'a', 's', 'd')
    :param duration: How long to hold the key down (in seconds)
    """
    print(f"Pressing key: {key}")
    # window.set_focus()  # Activate the window
    pyautogui.keyDown(key)
    time.sleep(duration)
    pyautogui.keyUp(key)

# ... (existing code to set up window and positions)
    
# co = coordinate(roi_left, roi_top, roi_width, roi_height)
# mv = player_move(
#     top_left_x, top_left_y, 
#     top_right_x, top_right_y, 
#     bottom_left_x, bottom_left_y, 
#     bottom_right_x, bottom_right_y, 
#     top_x, top_y, 
#     bottom_x, bottom_y, 
#     left_x, left_y, 
#     right_x, right_y, 
#     1  # Adjust sleep_time as needed
# )

# Define obstacles as a set of positions
obstacles = {
    (435, 468), 
    (499, 483), 
    (498, 484),  # Example obstacles
    # Add more obstacle positions as needed
}

# # Get current position
# current_pos = co.get_position()
# # Convert the extracted text to coordinates
# #if current_pos is 6 digits use the first 3 digits as x and the last 3 digits as y
# #if current_pos is other digits move to next position then get the position again

# if len(current_pos) == 6:
#     x_str = current_pos[:3]
#     y_str = current_pos[3:]
# else:
#     # mv.move_bottom()
#     current_pos = co.get_position()
#     # if current_pos contains : then split the string

#     if ":" in current_pos:
#         x_str, y_str = current_pos.split(':')
#     else:
#         x_str = current_pos[:3]
#         y_str = current_pos[3:]


# # x_str, y_str = current_pos.split(':')
# # start_pos = (int(x_str), int(y_str))

# # Define the goal position
# goal_pos = (417,567)  # Replace with your target position

# # Get the path using A* algorithm
# # path = astar(start_pos, goal_pos, obstacles)

def press_key_in_window(window, key, duration=0.1):
    window.set_focus()
    time.sleep(0.5)  
    pyautogui.keyDown(key)
    time.sleep(duration)
    pyautogui.keyUp(key)

def press_key_async(window, key, duration=0.1):
    t = threading.Thread(target=press_key_in_window, args=(window, key, duration))
    t.start()

def move_to_target():
    if path:
        for position in path:
            x, y = position
            print(f"Moving to position: {x}, {y}")
            # Translate game map coordinates to screen coordinates if needed
            # screen_x, screen_y = map_to_screen(x, y, window)
            # pyautogui.moveTo(screen_x, screen_y)
            # pyautogui.mouseDown(button='right')
            # time.sleep(0.5)
            # pyautogui.mouseUp(button='right')
            # time.sleep(1)  # Wait for the character to reach the position
    else:
        print("No path found to the goal")

def press_key_loop(window,key, duration=0.1, interval=1.0):
    """
    Continuously press a key in a separate thread.
    
    :param key: The key to press
    :param duration: How long to hold the key
    :param interval: Wait time between presses
    """
    def loop_press(window):
        while True:
            # window.set_focus()
            pyautogui.keyDown(key)
            time.sleep(duration)
            pyautogui.keyUp(key)
            time.sleep(interval)
    
    t = threading.Thread(target=loop_press,args=(window,), daemon=True)
    t.start()


def main():
    #read all the files in the dirctory :C:\Users\along-PC\Desktop\mir\Map\
    directory = r'C:\Users\along-PC\Desktop\mir\Map'    
    # List all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Check if it's a file
        if os.path.isfile(file_path):
            print(f"Reading header for file: {file_path}")
            read_header(file_path)



    # read_header(r"0.map")
    # test_move()
    # window.set_focus()  # Activate the window
    # mv.move_bottom()
    # press_key_loop(window,'f2', 0.5, 15)
    # try:
    #     while True:
    #         # press_key('f2', 0.5)
    #         # press_key_async(window, 'f2', 0.5)
    #         print("Press end...")
    #         time.sleep(10)  # Small delay between key presses
    # except KeyboardInterrupt:
    #     print("\nProgram interrupted by user. Exiting gracefully...")
    #     # Perform any necessary cleanup here
    #     # For example, releasing keys, closing files, etc.
    # finally:
    #     # Optional: Code here will run regardless of whether an exception occurred
    #     print("Cleanup complete.")



# def map_to_screen(x, y, window):
    # Implement the conversion from game map coordinates to screen coordinates
    # This depends on how the game displays positions
    # Example (needs adjustment based on actual game scaling):
    # screen_x = window.left + (x / 597) * window.width
    # screen_y = window.top + (y / 597) * window.height
    # return int(screen_x), int(screen_y)



#target = (411, 564)
if __name__ == "__main__":
    main()
    # co = coordinate(roi_left, roi_top, roi_width, roi_height)
    
    # mv = player_move(top_left_x, top_left_y, 
    #                  top_right_x, top_right_y, 
    #                  bottom_left_x, bottom_left_y, 
    #                  bottom_right_x, bottom_right_y, 
    #                  top_x, top_y, 
    #                  bottom_x, bottom_y, 
    #                  left_x, left_y, 
    #                  right_x, right_y, 1)
    # for i in range(1):
    #     mv.move_left()
    #     co.get_position()
    #     mv.move_bottom()
    #     co.get_position()
        # mv.move_bottom()
        # print mouse position
        # move_top_right()
        # move_top_left()
        # move_bottom_left()
        # move_bottom_right()
        # move_top()
        # move_bottom()
        # move_right()
        # move_left()


    # tesseract each image in the current position psm6/ psm7/ and psm8/ directory parameter should  --oem 3 --psm 7 -l eng 
    # for i in range(6,9):
    #     directory = f"psm{i}/"
    #     print(f"Processing {directory}")
    #     pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe'
        
    #     # List all files in the directory
    #     for filename in os.listdir(directory):
    #         if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
    #             image_path = os.path.join(directory, filename)
    #             image = Image.open(image_path)
    #             print(f"Processing file: {filename}")
    #             text = pytesseract.image_to_string(image, config=f'--oem 3 --psm 6 -l eng  -c tessedit_char_whitelist=0123456789:')
    #             print(f"Extracted {image_path} Text: {text.strip()} psm 6\n")
    #             text = pytesseract.image_to_string(image, config=f'--oem 3 --psm 7 -l eng  -c tessedit_char_whitelist=0123456789:')
    #             print(f"Extracted {image_path} Text: {text.strip()} psm 7\n")
    #             text = pytesseract.image_to_string(image, config=f'--oem 3 --psm 8 -l eng  -c tessedit_char_whitelist=0123456789:')
    #             print(f"Extracted {image_path} Text: {text.strip()} psm 8\n")
                


        # # list all the files in the directory psm{i}/ then tesseract each image
        # print(f"Processing psm{i}/")
        # pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe'
        # image = Image.open(f"psm{i}/1.png")
        # print(pytesseract.image_to_string(image, config='--oem 3 --psm 7 -l eng'))




    

        
        # receive the command from the 
        #move_top_right()
    # print
    # releae the mouse
print("Done")