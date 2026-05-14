import importlib
import os
import tkinter as tk
import time
from Components.Utils import config_manager

#Pomocne values 
MODULES_DIR = "Components"
loaded_Modules ={} 


def show_loading_screen():
    root = tk.Tk()
    root.overrideredirect(True) 
    

    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()
    w, h = 400, 300
    root.geometry(f"{w}x{h}+{(screen_w-w)//2}+{(screen_h-h)//2}")
    root.configure(bg="#1a1a1a")

    #config_manager.init_config()
    #img_path = config_manager.get_loading_image()

    #try:
        #img

    #except:
    tk.Label(root, text="Inicializace modůlu...", fg="white", bg="#1a1a1a", font=("Arial", 20)).pack(expand=True)

    progress_bar = tk.Frame(root, bg="#3498db", height=5)
    progress_bar.place(x=0, y=h-5, width=0)


    def animate_and_start(step=0):
        if step <= 100:
            progress_bar.place(width=(w * step / 100))
            root.after(20, lambda: animate_and_start(step + 2))
        else:
            root.destroy()
            start_app()

    root.after(100, animate_and_start)
    root.mainloop()
 



def start_app():
    modules = {}
    for filename in os.listdir(MODULES_DIR):

 

        if filename.endswith(".py") and filename != "__init__.py":
            print(f"Starting {filename}")
            print(f"Started {filename}")
            name = filename[:-3]
            module = importlib.import_module(f"{MODULES_DIR}.{name}")
            
            if hasattr(module, "init"):
                module.init()
            modules[name] = module
           

        #return filename
        
    return modules
    

if __name__ == "__main__":
    show_loading_screen()