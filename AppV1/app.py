from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk
import os

# Get the current directory
current_directory = os.path.dirname(os.path.realpath(__file__))

# Set the current directory as the root path
os.chdir(current_directory)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Multi-page App")

        # Create a notebook with three pages
        self.notebook = ttk.Notebook(self)
        self.page1 = ttk.Frame(self.notebook)
        self.page2 = ttk.Frame(self.notebook)
        self.page3 = ttk.Frame(self.notebook)
        self.notebook.add(self.page1, text="Acrobat")
        self.notebook.add(self.page3, text="Photoshop")  # Changed the label of the page
        self.notebook.add(self.page2, text="Illustrator")  # Changed the order of the pages
        self.notebook.pack(expand=True, fill=tk.BOTH)

        # Page 1 GUI elements
        label1 = ttk.Label(self.page1, text="Acrobat")
        text1 = tk.Text(self.page1, height = 5, width = 52 ,wrap=tk.WORD)
        label1.pack(pady=10)
        fact1 = "Adobe Inc. originally called Adobe Systems Incorporated, is an American multinational computer software company incorporated in Delaware and headquartered in San Jose, California."
        text1.insert(tk.END, fact1)
        text1.config(state=tk.DISABLED)
        img1 = Image.open('images/adobe_acrobat.png')
        photo1 =  ImageTk.PhotoImage(img1)
        label_image1 = ttk.Label(self.page1, image=photo1)
        label_image1.image = photo1
        label_image1.pack(pady=10)
        button1 = ttk.Button(self.page1, text="Go to Page Adobe Photoshop", command=self.show_page2)
        button1.pack(pady=10)
        button4 = ttk.Button(self.page1, text="Go to Page Adobe Illustrator", command=self.show_page3)
        button4.pack(pady=10)

        # Page 2 GUI elements
        label2 = ttk.Label(self.page3, text="Photoshop")  # Changed the label of the page
        label2.pack(pady=10)
        img2 = Image.open('images/adobe_phtoshop.png')
        photo2 =  ImageTk.PhotoImage(img2)
        label_image2 = ttk.Label(self.page3, image=photo2)
        label_image2.image = photo2
        label_image2.pack(pady=10)
        
        rb1 = tk.IntVar()
        rb2 = tk.IntVar()
        rb1.set(0)
        rb1.set(0)
        tk.Radiobutton(self.page3, 
               text="PNG format",
               padx = 20, 
               variable=rb1, 
               value=1,
               ).pack(anchor=tk.W)
        tk.Radiobutton(self.page3, 
               text="JPG format",
               padx = 20,
               variable=rb2, 
               value=1,
               ).pack(anchor=tk.W)
        
        def clear_page3():
            rb1.set(0)
            rb2.set(0)
            sample_text.config(state='normal')
            sample_text.delete("1.0","end")
            sample_text.config(state=tk.DISABLED)

        clearBttn = tk.Button(self.page3, text="Clear", width=15, height=2, relief="ridge", anchor=tk.CENTER, command=clear_page3)
        clearBttn.pack(padx=70)

        sample_text = tk.Text(self.page3, height = 5, width = 52,wrap=tk.WORD)
        sample_text.pack()
        sample_text.config(state=tk.DISABLED)

        def set_text_by_button():
            sample_text.config(state='normal')
            sample_text.delete("1.0","end")

            if rb1.get() and rb2.get():
                sample_text.insert(tk.END, "Images will be downloaded in both JPG and PNG format")
            elif rb1.get():
                sample_text.insert(tk.END, "Images will be downloaded PNG format")
            elif rb2.get():
                sample_text.insert(tk.END, "Images will be downloaded JPG format")
            else:
                sample_text.insert(tk.END, "Config not yet set")
            sample_text.config(state=tk.DISABLED)

        set_up_button = tk.Button(self.page3, height=1, width=5, text="Set",
                    command=set_text_by_button)
        set_up_button.pack(padx=70)
        sample_text.config(state=tk.DISABLED)
        

        scrollbar2 = ttk.Scrollbar(self.page3, orient=tk.VERTICAL)  # Added a vertical scrollbar
        scrollbar2.pack(side=tk.RIGHT, fill=tk.Y, pady=10)
        button2 = ttk.Button(self.page3, text="Go to Main Page", command=self.show_page1)
        button2.pack(pady=10)

        # Page 3 GUI elements
        label3 = ttk.Label(self.page2, text="Illustrator")  # Changed the label of the page
        label3.pack(pady=10)
        img3 = Image.open('images/adobe_illustrator.png')
        photo3 =  ImageTk.PhotoImage(img3)
        label_image3 = ttk.Label(self.page2, image=photo3)
        label_image3.image = photo3
        label_image3.pack(pady=10)
        check_var1 = tk.IntVar()
        check_var1.set(0)
        checkbox1 = ttk.Checkbutton(self.page2, text="Rotate thumbnail clockwise", variable=check_var1)  # Added a checkbox
        checkbox1.pack(pady=10)
        text1.pack()

        image = Image.open("images/square.png")
        width, height = image.size
        image.thumbnail((width/5, height/5))
        photoimage = ImageTk.PhotoImage(image)
        image_label = tk.Label(self.page2, image=photoimage, bg="white", relief=tk.SUNKEN)
        image_label.pack(pady=5)

        def rotate_image(degrees):
            new_image = image.rotate(-int(degrees)) if check_var1.get() else image.rotate(int(degrees))
            photoimage = ImageTk.PhotoImage(new_image)
            image_label.image = photoimage #Prevent garbage collection
            image_label.config(image = photoimage)
        
        rotate_image(0)
        w2 = tk.Scale(self.page2, from_=0, to=360, tickinterval= 30, orient=tk.HORIZONTAL, length=300, command = rotate_image)
        w2.pack(anchor = tk.CENTER)
        button3 = ttk.Button(self.page2, text="Go to Main Page", command=self.show_page1)
        button3.pack(pady=10)

    def show_page1(self):
        self.notebook.select(self.page1)

    def show_page2(self):
        self.notebook.select(self.page3)

    def show_page3(self):
        self.notebook.select(self.page2)

if __name__ == "__main__":
    app = App()
    app.mainloop()