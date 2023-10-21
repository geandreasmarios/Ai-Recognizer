import tkinter as tk
from PIL import Image, ImageTk, ImageGrab
from model import CNN, load_model

pencil_radius = 10
POSOSTA_FONT =  ("Arial", 16)

def on_drag(event):
    canvas.create_oval(
        event.x - pencil_radius, event.y - pencil_radius,
        event.x + pencil_radius, event.y + pencil_radius,
        fill = "white", outline = "white"
    )

def clear_canvas():
    canvas.delete("all")


ai_model = load_model()

def recognize():
    canvas.update()
    pad = 4
    x = window.winfo_rootx()+canvas.winfo_x() + pad
    y = window.winfo_rooty()+canvas.winfo_y() + pad
    x1 = x + canvas.winfo_width() - 2*pad
    y1 = y + canvas.winfo_height() - 2*pad
    # lhspsh eikonas apo canva
    im = ImageGrab.grab().crop((x,y,x1,y1))
    #ΞΞ΅ΟΞ±ΟΟΞΏΟΞ· ΟΞ΅ Ξ±ΟΟΟΞΏΞΌΞ±ΟΟΞΏ
    im = im.convert("L")
    #allagh mege8ous se 28x28 pixel
    im = im.resize((28,28))
    result, pososta = ai_model.predict_img(im)
    output_label.config(text = f'pistevw zwgrafizeis to {result}')

    pososta1 = ""
    for i, pososto in enumerate(pososta):
        pososta1 += f'{i} {pososto*100:5.2f}%\n'
    print(pososta1)

    pososta_label.config(text = pososta1, )
    

window = tk.Tk()
window.geometry("400x400")
window.title("Mnist Recognizer")
window.resizable(False, False)

pososta_label = tk.Label(window,text = "pososta", bg="#DFD9E2", fg="purple", font=POSOSTA_FONT)
pososta_label.pack(side=tk.LEFT)

canvas = tk.Canvas(window, bg = "black")
canvas.bind("<B1-Motion>", on_drag)
canvas.pack(fill=tk.BOTH, expand = True)


clear_button = tk.Button(window, text="clear", bg="purple", command=clear_canvas)
clear_button.pack()

recognize_button = tk.Button(window,text = "recognize", bg="purple", command=recognize)
recognize_button.pack()

output_label = tk.Label(window, text = "nomizw zwgrafises to 7")
output_label.pack()


recognize()
window.mainloop()


