# PyautoGUI-Testing
GUI testing using PyautoGUI


For this project, **PyAutoGUI** was used to record test cases and report the results.
PyAutoGUI is a Python library for automating tasks on your computer. It can be used to
automate mouse clicks, keyboard strokes, and other GUI interactions. PyAutoGUI has several
functions that can be used to control the mouse and keyboard, such as moveTo(), click(), write(),
and press().

These functions can be used to simulate user actions, such as clicking a button, typing text into
a field, or pressing a key. One of the key features of PyAutoGUI is its ability to take screenshots
and recognize images within those screenshots. This makes it possible to automate tasks that
involve looking for specific images or patterns on the screen.

PyAutoGUI can also be used to control other applications running on your computer, such as
web browsers, video players, and games. PyAutoGUI is a cross-platform library and works on
Windows, macOS, and Linux. It is easy to install using pip, and comes with detailed
documentation and examples to help you get started. However, it's important to note that
PyAutoGUI is a powerful tool that can be used for both good and bad purposes, so use it
responsibly and ethically.

Installation and Execution

To install PyAutoGUI, on command prompt pip install the library: ~ pip install PyAutoGUI

PyAutoGUI library is dependent on Opencv library and thus ensure user has opencv library
installed in the system:

~ pip install pillow

~ pip install opencv-python

We also installed pyperclip library to execute clipboard copy/paste actions in file: ~ pip install pyperclip

Go into the TestApp directory and run the python file test\_cases\_gui.py with the path of the
application that is to be tested sent as an argument. For example:

~ python test\_cases\_gui.py <complete absolute path of the
application>

Test Cases:




<a name="br3"></a>A total of 12 test cases were developed to automate GUI testing:

1\. Check if the application is executable: This test case checks whether the application can

be executed or not.

2\. Check if the Main Page (First Page) of Application Opens: This test case verifies
 whether the main page of the application is opening or not.

3\. Check if the Second page is visited from the First Page: This test case checks whether
 the user is able to navigate from the main page to the second page of the application
 through the button.

4\. Check if the Main page is visited from Second Page: This test case checks whether the
 user is able to navigate back to the main page from the second page of the application
 through the button.

5\. Check if the Third page is visited from the Main Page: This test case checks whether the
 user is able to navigate from the main page to the third page of the application through
 the button.

6\. Check if the Main page is visited from Third Page: This test case checks whether the
 user is able to navigate back to the main page from the third page of the application
 through the button.

7\. Verify Text Present on Main Page: This test case checks whether the main page of the
 application contains the expected text or not.

8\. Verify RadioButtons to download images: This test case verifies whether the radio
 buttons for downloading images are working or not.

9\. Verify Clear Button to reset configuration: This test case verifies whether the clear button
 is resetting the configuration of the application or not.

10\. Verify Slider that rotates image anti-clockwise: This test case verifies whether the slider
 for rotating the image anti-clockwise is working or not.

11\. Verify Checkbox to rotate image clockwise: This test case verifies whether the checkbox
 for rotating the image clockwise is working or not.

12\. Close the Application: This test case checks whether the application can be closed or
 not.

Uncompress Applications.zip file to extract all the directories present in the file which include:

● AppV1: It is the directory of the original application file. Go into the "AppV1" directory and

double-click on the "AppV1.exe" file to open the application. This application has a main
page that provides basic information about Adobe Acrobat and two buttons to navigate
to different pages of the application: Adobe Photoshop (Second Page) and Adobe
Illustrator (Third Page).

The Second Page, or the Adobe Photoshop page, has two radio buttons to select image
formats (PNG or JPG), a "Set" button to apply the selected configuration, and a "Clear"
button to reset the selection. There is also a button to navigate back to the main page.
The Third Page, or the Adobe Illustrator page, has a slider that rotates an arrow image
above it. There is also a button to navigate back to the main page.

In summary, the "AppV1" directory contains a simple application that allows users to
navigate between three pages and perform various actions, such as selecting image
formats and rotating an image.

● AppV2: It is a version of AppV1 with some minor changes in its features. Go into the

"AppV1" directory and double-click on the "AppV1.exe" file to open the application.
Some ways AppV2 is different from AppV1 are:

○ Unlike AppV1 you cannot navigate to page 3 from the main page and can only

navigate to page 2.

○ Unlike AppV1 you cannot navigate to the main page from page 2 and can only
 navigate to page 3.

○ Unlike AppV1 the slider in page 3is not horizontal and is vertical.
○ The AppV1 window is smaller than the AppV2 window.

Some ways AppV2 and AppV1 are similar:

○ Like AppV1 both have the same messages in the text boxes present in page 1

and page 2.

○ Like AppV1 you have 2 options or radio buttons to select file download format.
○ Like AppV1 all share the same images present across applications.

` `Both the applications are created and developed using the Tkinter web framework library
in python and then converted into executable files.

Uncompress TestApp.zip file to extract testcases python file:

● TestApp: "TestApp" directory contains two python files named test\_cases\_gui.py and

test\_cases\_non\_gui.py and a directory of test\_images that contains images for
validation. For this assignment we are only GUI testing and thus will not care about
test\_cases\_non\_gui.py file.




<a name="br2"></a>Go into the TestApp directory and run the python file test\_cases\_gui.py with the path of
the application that is to be tested sent as an argument. For example:

~ python test\_cases\_gui.py <complete absolute path of the application>
Review Report:




<a name="br6"></a>As expected all the test cases were approved for the first GUI application (AppV1), but for the
second GUI application (AppV2) only 7 of 12 test cases were approved and the rest 5 failed as
seen in above screenshots. Reasons to fail the test cases are as follows:

● Test Case 4: Check if the Main page is visited from Second - FAILED: This test case
 failed because there were no buttons present in the main page to navigate to other
 respected pages.

● Test Case 5: Check if Third page is visited from Main - FAILED: This test case also failed
 because there were no buttons present in the main page to navigate to other respected
 pages.

● Test Case 6: Check if Main page is visited from Third - FAILED: This test case failed
 because there were no buttons present in the main page to navigate to other respected
 pages.

● Test Case 10: Verify Slider rotates image anti-clockwise - FAILED This test case failed
 because the slider was horizontal for this app and vertical for the original previous app.
● Test Case 11: Verify Checkbox to rotate image clockwise - FAILED This test case also

failed because the slider was horizontal for this app and vertical for the original previous
app.
