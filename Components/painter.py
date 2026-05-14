import turtle
import tkinter as tk
from Components.Utils import datastore, theme, colorPicker
import random


def init():
    datastore.init()
    store = datastore.get_store("ProgramData")
    
    root = tk.Tk()
    root.title("Turtle Studio")
    root.configure(bg="#1a1a1a")

    main_frame = tk.Frame(root, bg="#c1c1c1")

    main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    canvas_w, canvas_h = 900, 700
    canvas_frame = tk.Frame(main_frame, bg="black", highlightbackground="#3498db", highlightthickness=2)
    canvas_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    cv = tk.Canvas(canvas_frame, width=canvas_w, height=canvas_h, bg="white", highlightthickness=0)
    cv.pack()



    def showColorUi():
        colorPicker.showUI()



    screen = turtle.TurtleScreen(cv)
    screen.bgcolor(store.get("bg_color", "white"))
    screen.tracer(0)
    
    t = turtle.RawTurtle(screen)
    t.pencolor(store.get("color", "#000000"))
    t.pensize(store.get("size", 3))
    t.speed(0)
    t.ht()

    side_panel = tk.Frame(main_frame, bg="#2c3e50", width=250)
    side_panel.pack(side=tk.RIGHT, fill=tk.Y, padx=(10, 0))

    def update_config(key, value):
        store.set(key, value)

    def change_color(c):
        t.pencolor(c)
        update_config("color", c)
        screen.update()

    def set_bg(c):
        screen.bgcolor(c)
        update_config("bg_color", c)
        screen.update()

    tk.Label(side_panel, text="PALETA", bg="#2c3e50", fg="#3498db", font=("Segoe UI", 12, "bold")).pack(pady=10)






    btn_frame = tk.Frame(side_panel, bg="#2c3e50")
    btn_frame.pack(pady=5)
    
    colors = ["#f1c40f", "#e67e22", "#e74c3c", "#9b59b6", "#2ecc71", "#3498db", "#ffffff", "#000000"]
    for i, c in enumerate(colors):
        btn = tk.Button(btn_frame, bg=c, width=4, height=1, relief=tk.FLAT, command=lambda col=c: change_color(col))
        btn.grid(row=i//2, column=i%2, padx=3, pady=3)

    

    tk.Button(side_panel, text="Podrobnější výběr barvy", command=lambda: showColorUi()).pack(pady=(15,10))


    tk.Label(side_panel, text="Tloušťka", bg="#2c3e50", fg="white").pack(pady=(15, 0))
    scale = tk.Scale(side_panel, from_=1, to=30, orient=tk.HORIZONTAL, bg="#2c3e50", fg="white", 
                     highlightthickness=0, command=lambda v: [t.pensize(int(v)), update_config("size", int(v))])
    scale.set(store.get("size", 3))
    scale.pack(fill=tk.X, padx=15)

    tk.Label(side_panel, text="Pozadí", bg="#2c3e50", fg="white").pack(pady=(15, 0))
    bg_frame = tk.Frame(side_panel, bg="#2c3e50")
    bg_frame.pack()
    for bc in ["#ffffff", "#ecf0f1", "#2c3e50", "#1a1a1a"]:
        b_btn = tk.Button(bg_frame, bg=bc, width=3, command=lambda c=bc: set_bg(c))
        b_btn.pack(side=tk.LEFT, padx=2)

    control_frame = tk.Frame(side_panel, bg="#2c3e50")
    control_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=20)

    def clear_screen():
        t.clear()
        screen.update()

    clear_btn = tk.Button(control_frame, text="VYMAZAT", command=clear_screen)
    

    theme.apply_style(clear_btn, "danger")
    clear_btn.pack(fill=tk.X, padx=15, pady=5)

    def random_color():#
        color_code = f"#{random.randint(0, 0xFFFFFF):06x}"
        #print(color_code)
        change_color(color_code)

        

    
    #random výběr barvy
    randomButton = tk.Button(control_frame, text="Vygenerovat random barvu", command=random_color)
    theme.apply_style(randomButton, "danger")
    randomButton.pack(fill=tk.X, padx=20,pady=5)


    def on_click(event):
        x = event.x - canvas_w / 2
        y = canvas_h / 2 - event.y
        t.penup()
        t.goto(x, y)
        t.pendown()
        screen.update()

    def on_drag(event):

        x = event.x - canvas_w / 2
        y = canvas_h / 2 - event.y
        t.goto(x, y)
        screen.update()

    cv.bind("<Button-1>", on_click)
    cv.bind("<B1-Motion>", on_drag)

    screen.update()
    root.mainloop()