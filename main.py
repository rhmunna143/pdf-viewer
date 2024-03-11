import os
from tkinter import Tk, Button, filedialog
from tkPDFViewer import tkPDFViewer as pdf

def browseFiles():
    filename = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Select PDF file",
        filetype=(("PDF files", "*.pdf"), ("All files", "*.*"))
    )
    
    if filename:
        pdf_viewer = pdf.ShowPdf()
        pdf_window = pdf_viewer.pdf_view(
            app,
            pdf_location=filename,
            width=77,
            height=100
        )
        pdf_window.pack(pady=(0, 10), padx=10, expand=True, fill="both")

# initialize Tkinter
app = Tk()
app.geometry("800x600+300+50")
app.title("Bulgy PDF Viewer")
app.config(bg="white")

# Create a button and place it in the window
open_button = Button(
    app,
    text="Open PDF",
    command=browseFiles,
    width=40,
    font="arial 14",
    bd=4
)
open_button.pack(pady=20)

app.mainloop()