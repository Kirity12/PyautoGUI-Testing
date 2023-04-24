import os
from pathlib import Path
import pyautogui
import pyperclip
import subprocess
import sys
import time

BASE_PATH = os.path.dirname(os.path.abspath(__file__)) 

def AppOpenTest(process_name):
    status = 0
    print ('----------------- Test Case 1: Check if application is executable -----------------')
    try:
        call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
        # use buildin check_output right away
        output = subprocess.check_output(call).decode()
        # check in last line for process name
        last_line = output.strip().split('\r\n')[-1]
        # because Fail message could be translated
        if last_line.lower().startswith(process_name.lower()):
            print('PASSED')
            status = 1
        else:
            print('FAILED')
            print('Reason: file not executable')
    except Exception as e:
        print('FAILED')
        print(e)
    print ('---------------------------------------------------------------------------------')
    return status


def CheckMainPage():
    print ('------------- Test Case 2: Check if Main Page of Application Opens --------------')
    status = 0
    try:
        test_image_path = os.path.join(BASE_PATH,'test_images','page1.PNG')
        location = pyautogui.locateOnScreen(test_image_path, confidence=0.9)
        if location == None:
            print('FAILED')
            print('Reason: Application Main Page did not open')
        else:
            status = 1
            print('PASSED')
    except Exception as e:
        print('FAILED')
        print(e)
    print ('---------------------------------------------------------------------------------')
    return status


def MoveFirst2SecondPage():
    print ('------------ Test Case 3: Check if Second page is visited from First ------------')
    status = 0

    test_image_path = os.path.join(BASE_PATH,'test_images','page1.PNG')
    location = pyautogui.locateOnScreen(test_image_path, confidence=0.9)

    if location == None:
        print('FAILED')
        print('Reason: Application did not find main page')
        print ('---------------------------------------------------------------------------------')
        return status

    pyautogui.click(location.left + 284, location.top + 458)

    try:
        test_image_path = os.path.join(BASE_PATH,'test_images','page2.PNG')
        location = pyautogui.locateOnScreen(test_image_path, confidence=0.9)
        if location == None:
            print('FAILED')
            print('Reason: Button not present or failed to flow from main page to second page did not happen')
        else:
            status = 1
            print('PASSED')
    except Exception as e:
        print('FAILED')
        print(e)
    print ('---------------------------------------------------------------------------------')
    pyautogui.click(location.left + 21, location.top + 55)
    return status


def MoveSecond2FirstPage():
    print ('------------ Test Case 4: Check if Main page is visited from Second ------------')
    status = 0

    test_image_path = os.path.join(BASE_PATH,'test_images','page1.PNG')
    location1 = pyautogui.locateOnScreen(test_image_path, confidence=0.9)

    if location1 == None:
        print('FAILED')
        print('Reason: Application did not find main page')
        print ('---------------------------------------------------------------------------------')
        return status
    else:
        pyautogui.click(location1.left + 120, location1.top + 55)

    pyautogui.click(location1.left + 292, location1.top + 838)

    try:
        test_image_path = os.path.join(BASE_PATH,'test_images','page1.PNG')
        location = pyautogui.locateOnScreen(test_image_path, confidence=0.9)
        if location == None:
            print('FAILED')
            print('Reason: Button not present or failed to flow from second page to main page did not happen')
        else:
            status = 1
            print('PASSED')
    except Exception as e:
        print('FAILED')
        print(e)
    print ('---------------------------------------------------------------------------------')
    pyautogui.click(location1.left + 21, location1.top + 55)
    return status


def MoveFirst2ThirdPage():
    print ('------------ Test Case 5: Check if Third page is visited from Main ------------')
    status = 0

    test_image_path = os.path.join(BASE_PATH,'test_images','page1.PNG')
    location1 = pyautogui.locateOnScreen(test_image_path, confidence=0.9)

    if location1 == None:
        print('FAILED')
        print('Reason: Application did not find main page')
        print ('---------------------------------------------------------------------------------')
        return status

    pyautogui.click(location1.left + 245, location1.top + 509)

    try:
        test_image_path = os.path.join(BASE_PATH,'test_images','page3.PNG')
        location = pyautogui.locateOnScreen(test_image_path, confidence=0.9)
        if location == None:
            print('FAILED')
            print('Reason: Button not present or failed to flow from main page to third page did not happen')
        else:
            status = 1
            print('PASSED')
    except Exception as e:
        print('FAILED')
        print(e)
    print ('---------------------------------------------------------------------------------')
    pyautogui.click(location1.left + 21, location1.top + 55)
    return status


def MoveThird2FirstPage():
    print ('------------ Test Case 6: Check if Main page is visited from Third ------------')
    status = 0

    test_image_path = os.path.join(BASE_PATH,'test_images','page1.PNG')
    location1 = pyautogui.locateOnScreen(test_image_path, confidence=0.9)

    if location1 == None:
        print('FAILED')
        print('Reason: Application did not find third page')
        print ('---------------------------------------------------------------------------------')
        return status
    else:
        pyautogui.click(location1.left + 205, location1.top + 55)
    pyautogui.click(location1.left + 297, location1.top + 744)
    try:
        test_image_path = os.path.join(BASE_PATH,'test_images','page1.PNG')
        location = pyautogui.locateOnScreen(test_image_path, confidence=0.9)
        if location == None:
            print('FAILED')
            print('Reason: Button not present or failed to flow from third page to main page did not happen')
        else:
            status = 1
            print('PASSED')
    except Exception as e:
        print('FAILED')
        print(e)
    print ('---------------------------------------------------------------------------------')
    pyautogui.click(location1.left + 21, location1.top + 55)
    return status

def VerifyMainPageText():
    print ('------------ Test Case 7: Verify Text Present on Main Page ----------------------')
    status = 0

    test_image_path = os.path.join(BASE_PATH,'test_images','page1.PNG')
    location = pyautogui.locateOnScreen(test_image_path, confidence=0.9)

    if location == None:
        print('FAILED')
        print('Reason: Application did not find main page')
        print ('---------------------------------------------------------------------------------')
        return status

    pyautogui.click(location.left + 230, location.top + 595)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    text = pyperclip.paste()
    pyautogui.click(location.left + 230, location.top + 595)
    text = ''.join(text.split('\n\n'))
    fact = "Adobe Inc. originally called Adobe Systems Incorporated, is an American multinational computer software company incorporated in Delaware and headquartered in San Jose, California."

    if text[:-2]!=fact:
        print('FAILED')
        print('Reason: Text on main page is incorrect')

    else:
        status = 1
        print('PASSED')
    print ('---------------------------------------------------------------------------------')
    return status


def VerifyDownloadFormat():
    print ('------------ Test Case 8: Verify RadioButtons to download images ----------------')
    status = 0

    test_image_path = os.path.join(BASE_PATH,'test_images','page1.PNG')
    location = pyautogui.locateOnScreen(test_image_path, confidence=0.9)
    if location == None:
        print('FAILED')
        print('Reason: Application did not find se3cond page')
        print ('---------------------------------------------------------------------------------')
        return status

    pyautogui.click(location.left + 120, location.top + 55)
    pyautogui.click(location.left + 50, location.top + 519)
    pyautogui.click(location.left + 328, location.top + 795)
    pyautogui.click(location.left + 300, location.top + 660)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    text = pyperclip.paste()
    pyautogui.click(location.left + 300, location.top + 660)
    pyautogui.click(location.left + 322, location.top + 840)
    fact = 'Images will be downloaded PNG format'
    if text[:-2]!=fact:
        print('FAILED')
        print('Reason: Text entry on second page for format config is incorrect')

    else:
        status = 1
        print('PASSED')
    print ('---------------------------------------------------------------------------------')
    pyautogui.click(location.left + 21, location.top + 55)
    return status


def VerifyClearConfig():
    print ('------------ Test Case 9: Verify Clear Button to reset configuration ---------------')
    status = 0

    test_image_path = os.path.join(BASE_PATH,'test_images','page1.PNG')
    location = pyautogui.locateOnScreen(test_image_path, confidence=0.9)
    if location == None:
        print('FAILED')
        print('Reason: Application did not find second page')
        print ('---------------------------------------------------------------------------------')
        return status

    pyautogui.click(location.left + 120, location.top + 55)
    pyautogui.click(location.left + 50, location.top + 519)
    pyautogui.click(location.left + 328, location.top + 795)
    pyautogui.click(location.left + 300, location.top + 660)
    pyautogui.click(location.left + 300, location.top + 600)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    text1 = pyperclip.paste()
    fact1 = ''
    if text1[:-2]!=fact1:
        print('FAILED')
        print('Reason: Clear Button did not work')

    else:
        pyautogui.click(location.left + 328, location.top + 795)
        pyautogui.click(location.left + 300, location.top + 660)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        text2 = pyperclip.paste()
        fact2 = 'Config not yet set'
        pyautogui.click(location.left + 300, location.top + 660)
        pyautogui.click(location.left + 322, location.top + 840)
        if text2[:-2]!=fact2:
            print('FAILED')
            print('Reason: Text entry on second page is incorrect for clear config')
        else:
            status = 1
            print('PASSED')
    print ('---------------------------------------------------------------------------------')
    pyautogui.click(location.left + 21, location.top + 55)
    return status

def VerifyAntiClockwiseImage():
    print ('----------- Test Case 10: Verify Slider rotates image anti-clockwise --------------')
    status = 0

    test_image_path = os.path.join(BASE_PATH,'test_images','page1.PNG')
    location = pyautogui.locateOnScreen(test_image_path, confidence=0.9)
    pyautogui.click(location.left + 205, location.top + 55)
    if location == None:
        print('FAILED')
        print('Reason: Application did not find main page')
        print ('---------------------------------------------------------------------------------')
        return status

    pyautogui.click(location.left + 104, location.top + 668)
    pyautogui.dragTo(location.left + 207, location.top + 668, 2,button='left')

    test_image_path = os.path.join(BASE_PATH,'test_images','page3_anticlockwise.PNG')
    arrow_location = pyautogui.locateOnScreen(test_image_path, confidence=0.95)
    pyautogui.dragTo(location.left + 104, location.top + 668, 2,button='left')
    pyautogui.click(location.left + 292, location.top + 747)
    if arrow_location and arrow_location.left-(location.left+293)<=3 and arrow_location.top==location.top+580:
        status = 1
        print('PASSED')
    else:
        print('FAILED')
        print('Reason: Slider did not rotate any image on page 3')

    print ('---------------------------------------------------------------------------------')
    pyautogui.click(location.left + 21, location.top + 55)
    return status


def VerifyClockwiseImage():
    print ('----------- Test Case 11: Verify Checkbox to rotate image clockwise --------------')
    status = 0

    test_image_path = os.path.join(BASE_PATH,'test_images','page1.PNG')
    location = pyautogui.locateOnScreen(test_image_path, confidence=0.9)
    pyautogui.click(location.left + 205, location.top + 55)

    if location == None:
        print('FAILED')
        print('Reason: Application did not find main page')
        print ('---------------------------------------------------------------------------------')
        return status

    pyautogui.click(location.left + 201, location.top + 542)
    pyautogui.click(location.left + 104, location.top + 668)
    pyautogui.dragTo(location.left + 207, location.top + 668, 2,button='left')

    test_image_path = os.path.join(BASE_PATH,'test_images','page3_clockwise.PNG')
    arrow_location = pyautogui.locateOnScreen(test_image_path, confidence=0.95)
    pyautogui.click(location.left + 296, location.top + 747)
    if arrow_location and arrow_location.left==location.left+295 and arrow_location.top==location.top+581:
        status = 1
        print('PASSED')
    else:
        print('FAILED')
        print('Reason: Slider did not rotate any image on page 3')

    print ('---------------------------------------------------------------------------------')
    pyautogui.click(location.left + 21, location.top + 55)
    return status

def ExitApplication(process_name):
    print ('-------------------- Test Case 12: Close the Application ------------------------')
    status = 0

    test_image_path = os.path.join(BASE_PATH,'test_images','page1.PNG')
    location = pyautogui.locateOnScreen(test_image_path, confidence=0.9)

    if location == None:
        print('FAILED')
        print('Reason: Application did not find main page')
        print ('---------------------------------------------------------------------------------')
        return status
    
    pyautogui.click(location.left + 595, location.top + 11)
    r = os.popen('tasklist /v').read().strip().split('\n')
    present = None
    for i in range(len(r)):
        if process_name in r[i]:
            present =  r[i]
            break
    
    if not present:
        status = 1
        print('PASSED')
    else:
        print('FAILED')
        print('Reason: Application not terminated sucessfully')

    print ('---------------------------------------------------------------------------------')
    pyautogui.click(location.left + 21, location.top + 55)
    return status


if __name__=='__main__':

    # complete_path = Path(r'C:\Users\ngaur5\Downloads\KirityProject\KirityProject\AppV1\build\exe.win-amd64-3.8\AppV1')
    complete_path = Path(sys.argv[1])
    
    dir_name = os.path.dirname(complete_path)
    app_name = os.path.basename(complete_path).split('/')[-1]+'.exe'
    os.chdir(dir_name)

    if not os.path.exists(complete_path) and not os.path.exists(dir_name):
        print('Files do not exist')
        print('0 test cases run')
        exit(0)
    
    os.system('start "" "' + app_name + '"')
    time.sleep(2)
    results = []

    results += [AppOpenTest(app_name) ]

    results += [CheckMainPage()]

    results += [MoveFirst2SecondPage()]

    results += [MoveSecond2FirstPage()]

    results += [MoveFirst2ThirdPage()]

    results += [MoveThird2FirstPage()]

    results += [VerifyMainPageText()]

    results += [VerifyDownloadFormat()]

    results += [VerifyClearConfig()]

    results += [VerifyAntiClockwiseImage()]

    results += [VerifyClockwiseImage()]

    results += [ExitApplication(app_name)]

    print('##################           ', sum(results), '/', len(results), '        ##################')
    print('############### Test Cases', 'Failed:', -(sum(results)-len(results)), 'Passed:',sum(results),' ###############')
