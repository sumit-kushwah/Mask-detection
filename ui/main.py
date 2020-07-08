import tkinter as tk
from PIL import Image, ImageTk
from functions import counter_label
import sys
sys.path.insert(0, '../face_mask_detector')
import detect_mask_video
import detect_mask_image
import webbrowser

def runImage():
    path = entry1.get()
    detect_mask_image.runImage(path)

def callback():
    webbrowser.open_new("https://github.com/sumit-kushwah/Mask-detection")

def clear_entry(event, entry):
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Face Mask Detection")
root.geometry("400x600")

image = Image.open('mask.jpeg')
logo = ImageTk.PhotoImage(image)

header = tk.Frame(root, height=50)
content = tk.Frame(root)
footer = tk.Frame(root, height=30)

header.pack(fill='both')
content.pack(fill='both', expand=True)
footer.pack(fill='both')

image = tk.Label(header, image=logo).pack(side=tk.TOP)
my_label = tk.Label(header, text='Mask detection system', font=('times', 36, 'italic')).pack(side=tk.BOTTOM)

# line = tk.Canvas(header)
# line.create_line(15, 25, 200, 25)
# line.pack()

detail = tk.Label(content, text='Detect mask using any image and real time camera.').pack()

entry1 = tk.Entry (content) 
entry1.insert(0, 'enter image path here ...')
entry1.bind("<Button-1>", lambda event: clear_entry(event, entry1))
entry1.pack()

imageButton = tk.Button(content,
                   text="Open Image",
                   command=runImage)
imageButton.place(relx=0.5, rely=1.0, anchor=tk.CENTER)

videoButton = tk.Button(content,
                   text="Open Camera",
                   command=detect_mask_video.runvideo)
videoButton.place(relx=0.5, rely=1.0, anchor=tk.CENTER)


quitbutton = tk.Button(content, 
                   text="QUIT", 
                   fg="red",
                   command=root.destroy)

quitbutton.place(relx=0.5, rely=1.0, anchor=tk.CENTER)

imageButton.config(width=25)
videoButton.config(width=25)
quitbutton.config(width=25)

imageButton.pack(side=tk.TOP, expand=True)
videoButton.pack(side=tk.TOP, expand=True)
quitbutton.pack(side=tk.TOP, expand=True)

madeby = tk.Label(footer, text="Made by Sumit, Mukesh and Gaurav",font=('times', 18, 'italic'), fg="blue", cursor="hand2")
madeby.pack(side=tk.BOTTOM)
madeby.bind("<Button-1>", lambda e : callback())

header.pack()
content.pack();
footer.pack();


root.mainloop()
