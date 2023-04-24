import pytest
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk
import os

# Get the current directory
current_directory = os.getcwd()

# Set the current directory as the root path
os.chdir(current_directory)
from main_v1 import App

app = App()

def test_create_app():
    global app
    assert isinstance(app, App)

def test_pages():
    global app
    pages = [app.page1, app.page2, app.page3]
    assert len(pages) == 3
    for page in pages:
        assert isinstance(page, ttk.Frame)

def test_notebook():
    global app
    assert app.notebook.tab(app.page1, "text") == "Acrobat"
    assert app.notebook.tab(app.page2, "text") == "Illustrator"
    assert app.notebook.tab(app.page3, "text") == "Photoshop"

def test_page1_gui():
    global app
    assert app.page1.winfo_children()[0]["text"] == "Acrobat"
    assert app.page1.winfo_children()[3]["text"] == "Go to Page Adobe Photoshop"
    assert app.page1.winfo_children()[4]["text"] == "Go to Page Adobe Illustrator"
    assert isinstance(app.page1.winfo_children()[3], ttk.Button)
    assert isinstance(app.page1.winfo_children()[4], ttk.Button)
    assert isinstance(app.page1.winfo_children()[0], ttk.Label)

def test_page3_gui():
    global app
    assert app.page3.winfo_children()[0]["text"] == "Photoshop"
    assert isinstance(app.page3.winfo_children()[1], ttk.Label)
    assert isinstance(app.page3.winfo_children()[2], tk.Radiobutton)
    assert isinstance(app.page3.winfo_children()[3], tk.Radiobutton)
    assert isinstance(app.page3.winfo_children()[4], tk.Button)
    assert isinstance(app.page3.winfo_children()[5], tk.Scrollbar)
    assert isinstance(app.page3.winfo_children()[6], ttk.Button)

def test_page2_gui():
    global app
    assert app.page2.winfo_children()[0]["text"] == "Illustrator"
    assert isinstance(app.page2.winfo_children()[1], ttk.Label)
    assert isinstance(app.page2.winfo_children()[3], tk.Label)
    assert isinstance(app.page2.winfo_children()[2], ttk.Checkbutton)
    assert isinstance(app.page2.winfo_children()[4], tk.Scale)
    assert isinstance(app.page2.winfo_children()[5], ttk.Button)

def test_images():
    img1 = Image.open("images/adobe_acrobat.png")
    img1 = ImageTk.PhotoImage(img1)
    img2 = Image.open("images/adobe_phtoshop.png")
    img2 = ImageTk.PhotoImage(img2)
    img3 = Image.open("images/adobe_illustrator.png")
    img3 = ImageTk.PhotoImage(img3)
    global app
    assert app.page1.winfo_children()[2].image == img1
    assert app.page3.winfo_children()[1].image == img2
    assert app.page2.winfo_children()[3].image == img3
