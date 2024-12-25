
import datetime
import warnings

import pyautogui
import pytesseract
from PIL import Image, ImageFilter, ImageEnhance, ImageOps
import cv2
import numpy as np


class coordinate:
    def __init__(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.region = (self.left, self.top, self.width, self.height)
    
    def get_position(self):
        # Capture the screenshot
        screenshot = pyautogui.screenshot(region=self.region)
        screenshot.save('roi_screenshot_origin.png')  # Save original screenshot

        # # Convert PIL Image to OpenCV format
        # img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # # Resize the image to enhance OCR accuracy
        # img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        # cv2.imwrite('step0_resized.png', img)

        # # Convert to grayscale
        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # cv2.imwrite('step1_grayscale.png', gray)

        # # Increase contrast
        # pil_img = Image.fromarray(gray)
        # enhancer = ImageEnhance.Contrast(pil_img)
        # pil_img = enhancer.enhance(2.5)  # Adjust contrast factor if needed
        # gray = np.array(pil_img)
        # cv2.imwrite('step2_contrast.png', gray)

        # # Apply sharpening filter
        # kernel_sharpening = np.array([[-1,-1,-1],
        #                               [-1, 9,-1],
        #                               [-1,-1,-1]])
        # sharpened = cv2.filter2D(gray, -1, kernel_sharpening)
        # cv2.imwrite('step3_sharpened.png', sharpened)

        # # Apply thresholding
        # _, thresh = cv2.threshold(sharpened, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        # cv2.imwrite('step4_threshold.png', thresh)

        # # Apply dilation to enhance characters
        # kernel = np.ones((2,2), np.uint8)
        # dilated = cv2.dilate(thresh, kernel, iterations=1)
        # cv2.imwrite('step5_dilated.png', dilated)

        # # Save the preprocessed image
        # preprocessed_image_path = 'preprocessed_screenshot.png'
        # cv2.imwrite(preprocessed_image_path, dilated)

        # # Convert back to PIL Image for pytesseract
        # processed_image = Image.fromarray(dilated)

        # Suppress specific warnings
        warnings.filterwarnings(
            "ignore",
            message="32-bit application should be automated using 32-bit Python (you use 64-bit Python)"
        )

        # Configure pytesseract (remove character whitelist temporarily)
        custom_config = r'--oem 3 --psm 6  -c tessedit_char_whitelist=0123456789:'

        # Perform OCR
        extracted_text = pytesseract.image_to_string(
            screenshot,
            lang='eng',
            config=custom_config
        )

        print(f"Extracted Text: {extracted_text.strip()}")
        return extracted_text.strip()


    # def get_position(self):
    #     # Capture the screenshot
    #     screenshot = pyautogui.screenshot(region=self.region)
    #     screenshot.save('roi_screenshot_origin.png')  # Save original screenshot

    #     # Convert PIL Image to OpenCV format
    #     img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    #     # Resize the image to enhance OCR accuracy
    #     img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    #     cv2.imwrite('step0_resized.png', img)

    #     # Convert to grayscale
    #     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #     cv2.imwrite('step1_grayscale.png', gray)

    #     # Increase contrast
    #     pil_img = Image.fromarray(gray)
    #     enhancer = ImageEnhance.Contrast(pil_img)
    #     pil_img = enhancer.enhance(2.0)  # Increase contrast factor if needed
    #     gray = np.array(pil_img)
    #     cv2.imwrite('step2_contrast.png', gray)

    #     # Apply sharpening filter
    #     kernel_sharpening = np.array([[-1,-1,-1],
    #                                   [-1, 9,-1],
    #                                   [-1,-1,-1]])
    #     sharpened = cv2.filter2D(gray, -1, kernel_sharpening)
    #     cv2.imwrite('step3_sharpened.png', sharpened)

    #     # Apply thresholding
    #     _, thresh = cv2.threshold(sharpened, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    #     cv2.imwrite('step4_threshold.png', thresh)

    #     # Save the preprocessed image
    #     preprocessed_image_path = 'preprocessed_screenshot.png'
    #     cv2.imwrite(preprocessed_image_path, thresh)

    #     # Convert back to PIL Image for pytesseract
    #     processed_image = Image.fromarray(thresh)

        # Suppress specific warnings
        # warnings.filterwarnings(
        #     "ignore",
        #     message="32-bit application should be automated using 32-bit Python (you use 64-bit Python)"
        # )

        # # Configure pytesseract to recognize digits and colon
        # custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789:'
        # extracted_text = pytesseract.image_to_string(
        #     processed_image,
        #     lang='eng',
        #     config=custom_config
        # )

        # print(f"Extracted Text: {extracted_text.strip()}")
        # return extracted_text.strip()


    # def get_position(self):
    #     # Capture the screenshot
    #     screenshot = pyautogui.screenshot(region=self.region)
    #     screenshot.save('roi_screenshot_origin.png')  # Save original screenshot

    #     # Convert PIL Image to OpenCV format
    #     img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    #     # Optional: Resize the image to enhance OCR accuracy
    #     img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    #     cv2.imwrite('step0_resized.png', img)

    #     # Convert to grayscale
    #     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #     cv2.imwrite('step1_grayscale.png', gray)

    #     # Apply Gaussian Blur (optional, can be skipped)
    #     # blur = cv2.GaussianBlur(gray, (1, 1), 0)
    #     # cv2.imwrite('step2_blur.png', blur)
    #     # Use 'gray' directly if skipping blur
    #     blur = gray

    #     # Apply Thresholding
    #     # Use Otsu's thresholding
    #     _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    #     cv2.imwrite('step3_threshold.png', thresh)

    #     # Apply Morphological Operations (optional)
    #     # Adjust kernel size as needed
    #     kernel = np.ones((2, 2), np.uint8)
    #     # Comment out the morphology if it's causing issues
    #     # morph = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    #     # cv2.imwrite('step4_morph.png', morph)
    #     # Use 'thresh' directly if skipping morphology
    #     morph = thresh

    #     # Save the preprocessed image
    #     cv2.imwrite('preprocessed_screenshot.png', morph)

    #     # Convert back to PIL Image for pytesseract
    #     processed_image = Image.fromarray(morph)

    #     # Suppress specific warnings
    #     warnings.filterwarnings(
    #         "ignore",
    #         message="32-bit application should be automated using 32-bit Python (you use 64-bit Python)"
    #     )

    #     # Configure pytesseract to recognize digits and colon
    #     custom_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789:'
    #     extracted_text = pytesseract.image_to_string(
    #         processed_image,
    #         lang='eng',
    #         config=custom_config
    #     )

    #     print(f"Extracted Text: {extracted_text.strip()}")
    #     return extracted_text.strip()


    # def get_position(self):
    #     # Capture the screenshot
    #     screenshot = pyautogui.screenshot(region=self.region)
    #     # Save the original screenshot (optional)
    #     screenshot.save('roi_screenshot_origin.png')

    #     # Convert PIL Image to OpenCV format
    #     img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    #     # Convert to grayscale
    #     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #     # Apply Gaussian Blur to reduce noise
    #     blur = cv2.GaussianBlur(gray, (3, 3), 0)

    #     # Apply Adaptive Thresholding
    #     thresh = cv2.adaptiveThreshold(
    #         blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    #         cv2.THRESH_BINARY_INV, 15, 4
    #     )

    #     # Apply Morphological Operations to retain the colon
    #     kernel = np.ones((2, 2), np.uint8)
    #     morph = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

    #     # Save the preprocessed image (optional)
    #     cv2.imwrite('preprocessed_screenshot.png', morph)

    #     # Convert back to PIL Image for pytesseract
    #     processed_image = Image.fromarray(morph)

    #     # Suppress specific warnings
    #     warnings.filterwarnings(
    #         "ignore",
    #         message="32-bit application should be automated using 32-bit Python (you use 64-bit Python)"
    #     )

    #     # Configure pytesseract to recognize digits and colon
    #     custom_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789:'
    #     extracted_text = pytesseract.image_to_string(
    #         processed_image,
    #         lang='eng',
    #         config=custom_config
    #     )

    #     print(f"Extracted Text: {extracted_text.strip()}")
    #     return extracted_text.strip()
    # def get_position(self):
    #         screenshot = pyautogui.screenshot(region=self.region)
            
    #         # Preprocess the image
    #         screenshot = screenshot.convert('L')  # Convert to grayscale
    #         screenshot = screenshot.resize((screenshot.width * 2, screenshot.height * 2), Image.Resampling.LANCZOS)  # Resize image
    #         # screenshot = ImageOps.invert(screenshot)  # Remove inversion if not necessary
    #         screenshot = screenshot.filter(ImageFilter.MedianFilter())  # Remove noise
    #         screenshot = screenshot.filter(ImageFilter.SHARPEN)  # Sharpen image
    #         screenshot = screenshot.filter(ImageFilter.GaussianBlur(1))  # Apply slight blur to reduce noise
    #         enhancer = ImageEnhance.Contrast(screenshot)
    #         screenshot = enhancer.enhance(2)  # Increase contrast
    #         screenshot = ImageOps.autocontrast(screenshot)  # Auto contrast
    #         screenshot = screenshot.rotate(-1, expand=True)  # Deskew image if needed
    #         screenshot = screenshot.point(lambda x: 0 if x < 160 else 255, '1')  # Apply binary threshold with higher value

    #         screenshot.save('roi_screenshot_' + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + '.png')
    #         # Save the preprocessed image (optional for debugging)
    #         # screenshot.save('preprocessed_screenshot.png')
            
    #         warnings.filterwarnings("ignore", message="32-bit application should be automated using 32-bit Python (you use 64-bit Python)")
            
    #         # Configure pytesseract to recognize only digits with adjusted PSM
    #         custom_config = r'--oem 3 --psm 8 -c tessedit_char_whitelist=0123456789'
    #         extracted_text = pytesseract.image_to_string(screenshot, lang='eng', config=custom_config)
            
    #         print(extracted_text)
    #         return extracted_text


    # def get_position(self):
    #     # Capture the screenshot
    #     screenshot = pyautogui.screenshot(region=self.region)
    #     screenshot.save('roi_screenshot_origin.png')  # Optional: Save original screenshot

    #     # Convert PIL Image to OpenCV format
    #     img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    #     # Convert to grayscale
    #     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #     # Apply Gaussian Blur to reduce noise
    #     blur = cv2.GaussianBlur(gray, (5, 5), 0)

    #     # Apply Adaptive Thresholding
    #     thresh = cv2.adaptiveThreshold(
    #         blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
    #         cv2.THRESH_BINARY_INV, 11, 2
    #     )

    #     # Apply Morphological Operations to enhance digits
    #     kernel = np.ones((3,3), np.uint8)
    #     morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    #     # Optional: Dilate to make digits more prominent
    #     morph = cv2.dilate(morph, kernel, iterations=1)

    #     # Save the preprocessed image for debugging
    #     cv2.imwrite('preprocessed_screenshot.png', morph)

    #     # Convert back to PIL Image for pytesseract
    #     processed_image = Image.fromarray(morph)

    #     # Suppress specific warnings
    #     warnings.filterwarnings(
    #         "ignore", 
    #         message="32-bit application should be automated using 32-bit Python (you use 64-bit Python)"
    #     )

    #     # Configure pytesseract to recognize only digits
    #     custom_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789'
    #     extracted_text = pytesseract.image_to_string(
    #         processed_image, 
    #         lang='eng', 
    #         config=custom_config
    #     )

    #     print(f"Extracted Text: {extracted_text.strip()}")
    #     return extracted_text.strip()

    # def get_position(self):
    #     screenshot = pyautogui.screenshot(region=self.region)
        
    #     # Preprocess the image
    #     screenshot = screenshot.convert('L')  # Convert to grayscale
    #     screenshot = screenshot.resize((screenshot.width * 2, screenshot.height * 2), Image.Resampling.LANCZOS)  # Resize image
    #     # screenshot = ImageOps.invert(screenshot)  # Remove inversion if not necessary
    #     screenshot = screenshot.filter(ImageFilter.MedianFilter())  # Remove noise
    #     screenshot = screenshot.filter(ImageFilter.SHARPEN)  # Sharpen image
    #     screenshot = screenshot.filter(ImageFilter.GaussianBlur(1))  # Apply slight blur to reduce noise
    #     enhancer = ImageEnhance.Contrast(screenshot)
    #     screenshot = enhancer.enhance(2)  # Increase contrast
    #     screenshot = ImageOps.autocontrast(screenshot)  # Auto contrast
    #     screenshot = screenshot.rotate(-1, expand=True)  # Deskew image if needed
    #     screenshot = screenshot.point(lambda x: 0 if x < 160 else 255, '1')  # Apply binary threshold with higher value

    #     screenshot.save('roi_screenshot_' + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + '.png')
    #     # Save the preprocessed image (optional for debugging)
    #     # screenshot.save('preprocessed_screenshot.png')
        
    #     warnings.filterwarnings("ignore", message="32-bit application should be automated using 32-bit Python (you use 64-bit Python)")
        
    #     # Configure pytesseract to recognize only digits with adjusted PSM
    #     custom_config = r'--oem 3 --psm 8 -c tessedit_char_whitelist=0123456789'
    #     extracted_text = pytesseract.image_to_string(screenshot, lang='eng', config=custom_config)
        
    #     print(extracted_text)
    #     return extracted_text

    # def get_position(self):
        # screenshot = pyautogui.screenshot(region=self.region)
        # screenshot.save('roi_screenshot_origin.png')
        
        # # Convert PIL image to OpenCV format
        # img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        
        # # Convert to grayscale
        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # # Apply Gaussian Blur
        # gray = cv2.GaussianBlur(gray, (5, 5), 0)
        
        # # Apply adaptive thresholding
        # thresh = cv2.adaptiveThreshold(
        #     gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        #     cv2.THRESH_BINARY_INV, 11, 2
        # )
        
        # # Apply morphological operations
        # kernel = np.ones((3,3), np.uint8)
        # thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        
        # # Save the preprocessed image for debugging
        # cv2.imwrite('preprocessed_screenshot.png', thresh)
        
        # # Use PIL Image for pytesseract
        # screenshot = Image.fromarray(thresh)
        # screenshot.save('roi_screenshot_' + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + '.png')
        
        # warnings.filterwarnings("ignore", message="32-bit application should be automated using 32-bit Python (you use 64-bit Python)")
        
        # # Configure pytesseract
        # custom_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789'
        # extracted_text = pytesseract.image_to_string(screenshot, lang='eng', config=custom_config)
        
        # print(extracted_text)
        # return extracted_text


    # def get_position(self):
    #     screenshot = pyautogui.screenshot(region=self.region)
    #     screenshot.save('roi_screenshot_origin.png')
        
    #     # Preprocess the image
    #     screenshot = screenshot.convert('L')  # Convert to grayscale
    #     screenshot = screenshot.resize(
    #         (screenshot.width * 2, screenshot.height * 2), 
    #         Image.Resampling.LANCZOS
    #     )  # Resize image
        
    #     screenshot = screenshot.filter(ImageFilter.MedianFilter(size=3))  # Increased kernel size to remove more noise
    #     screenshot = screenshot.filter(ImageFilter.GaussianBlur(1.5))  # Increased blur radius
        
    #     enhancer = ImageEnhance.Contrast(screenshot)
    #     screenshot = enhancer.enhance(3)  # Increased contrast
        
    #     screenshot = ImageOps.autocontrast(screenshot)  # Auto contrast
        
    #     # Optional: Remove rotation if not necessary
    #     # screenshot = screenshot.rotate(-1, expand=True)  # Deskew image if needed
        
    #     # Apply Otsu's thresholding
    #     threshold = self.otsu_threshold(screenshot)
    #     screenshot = screenshot.point(lambda x: 0 if x < threshold else 255, '1')  # Apply binary threshold
        
    #     screenshot.save('roi_screenshot_' + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + '.png')
    #     # Save the preprocessed image (optional for debugging)
    #     # screenshot.save('preprocessed_screenshot.png')
        
    #     warnings.filterwarnings("ignore", message="32-bit application should be automated using 32-bit Python (you use 64-bit Python)")
        
    #     # Configure pytesseract to recognize only digits with optimized PSM
    #     custom_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789'
    #     extracted_text = pytesseract.image_to_string(screenshot, lang='eng', config=custom_config)
        
    #     print(extracted_text)
    #     return extracted_text

    def otsu_threshold(self, image):
        """Calculate Otsu's threshold for a grayscale image."""
        histogram = image.histogram()
        total = sum(histogram)
        
        sum_total = 0
        for i in range(256):
            sum_total += i * histogram[i]
        
        sum_b = 0
        w_b = 0
        w_f = 0
        
        max_variance = 0
        threshold = 0
        
        for i in range(256):
            w_b += histogram[i]
            if w_b == 0:
                continue
            w_f = total - w_b
            if w_f == 0:
                break
            sum_b += i * histogram[i]
            m_b = sum_b / w_b
            m_f = (sum_total - sum_b) / w_f
            variance = w_b * w_f * (m_b - m_f) ** 2
            if variance > max_variance:
                max_variance = variance
                threshold = i
        return threshold


    # def get_position(self):
    #         screenshot = pyautogui.screenshot(region=self.region)
            
            # Preprocess the image
            # screenshot = screenshot.convert('L')  # Convert to grayscale
            # screenshot = screenshot.resize((screenshot.width * 2, screenshot.height * 2), Image.Resampling.LANCZOS)  # Resize image  # Resize image
            # screenshot = ImageOps.invert(screenshot)  # Invert colors if necessary
            # screenshot = screenshot.filter(ImageFilter.MedianFilter())  # Remove noise
            # enhancer = ImageEnhance.Contrast(screenshot)
            # screenshot = enhancer.enhance(2)  # Increase contrast
            # screenshot = ImageOps.autocontrast(screenshot)  # Auto contrast
            # screenshot = screenshot.rotate(-1, expand=True)  # Deskew image if needed
            # screenshot = screenshot.point(lambda x: 0 if x < 140 else 255, '1')  # Apply binary threshold

            

            # screenshot = screenshot.convert('L')  # Convert to grayscale
            # screenshot = screenshot.resize((screenshot.width * 2, screenshot.height * 2), Image.Resampling.LANCZOS)  # Resize image
            # # screenshot = ImageOps.invert(screenshot)  # Remove inversion if not necessary
            # screenshot = screenshot.filter(ImageFilter.MedianFilter())  # Remove noise
            # enhancer = ImageEnhance.Contrast(screenshot)
            # screenshot = enhancer.enhance(2)  # Increase contrast
            # screenshot = ImageOps.autocontrast(screenshot)  # Auto contrast
            # screenshot = screenshot.rotate(-1, expand=True)  # Deskew image if needed
            # screenshot = screenshot.point(lambda x: 0 if x < 160 else 255, '1')  # Apply binary threshold with higher value


            # screenshot.save('roi_screenshot_' + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + '.png')
            # # Save the preprocessed image (optional for debugging)
            # # screenshot.save('preprocessed_screenshot.png')
            
            # warnings.filterwarnings("ignore", message="32-bit application should be automated using 32-bit Python (you use 64-bit Python)")
            
            # # Configure pytesseract to recognize only digits
            # custom_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789'
            # extracted_text = pytesseract.image_to_string(screenshot, lang='eng', config=custom_config)
            
            # print(extracted_text)
            # return extracted_text


    # def get_position(self):
    #     # Using pywinauto to get the window handle
    #     screenshot = pyautogui.screenshot(region=self.region)
        
    #     # Preprocess the image
    #     screenshot = screenshot.convert('L')  # Convert to grayscale
    #     screenshot = screenshot.filter(ImageFilter.MedianFilter())
    #     enhancer = ImageEnhance.Contrast(screenshot)
    #     screenshot = enhancer.enhance(2)
    #     screenshot = screenshot.point(lambda x: 0 if x < 160 else 255, '1')  # Apply binary threshold
    #     screenshot.save('roi_screenshot_' + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + '.png')
        
    #     # Save the preprocessed image (optional for debugging)
    #     # screenshot.save('preprocessed_screenshot.png')
        
    #     warnings.filterwarnings("ignore", message="32-bit application should be automated using 32-bit Python (you use 64-bit Python)")
        
    #     # Configure pytesseract to recognize only digits
    #     custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789'
    #     extracted_text = pytesseract.image_to_string(screenshot, lang='eng', config=custom_config)
        
    #     print(extracted_text)
    #     return extracted_text
    
    # def get_position(self):
    #     # Using pywinauto to get the window handle
    #     # region=(self.left, self.top, self.width, self.height)
    #     screenshot = pyautogui.screenshot(region=self.region)
    #     # screenshot.save('roi_screenshot.png')
    #     screenshot.save('roi_screenshot_' + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + '.png')

    #     warnings.filterwarnings("ignore", message="32-bit application should be automated using 32-bit Python (you use 64-bit Python)")
    #     # extracted_text = pytesseract.image_to_string(cropped_image, lang='chi_sim')  # Specify language if needed
        
    #     extracted_text = pytesseract.image_to_string(screenshot, lang='eng')  # Specify language and whitelist
    #     print(extracted_text)
    #     return extracted_text

    