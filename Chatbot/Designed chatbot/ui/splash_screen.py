import tkinter as tk
from .main_app import open_app

def open_splash():
    splash = tk.Tk()
    splash.overrideredirect(True)
    
    splash_width = 400
    splash_height = 200
    
    #TODO: set splash screen size and position 

    screen_width = splash.winfo_screenwidth()
    screen_height = splash.winfo_screenheight()
    display_x = (screen_width // 2) - (splash_width // 2)
    display_y = (screen_height // 2) - (splash_height // 2)
    splash.geometry(f"{splash_width}x{splash_height}+{display_x}+{display_y}")
    splash.title("Code Sinaia 2025 - Chatbot App")
    
    
    splash.configure(bg="#333333")
    label = tk.Label(splash, text="Welcome to Chatbot!", font=("Helvetica", 24), fg="white", bg="#333333")
    label.pack(expand=True)

    def close_splash():
        splash.destroy()
        open_app()
        
    splash.after(3000, close_splash)
    splash.mainloop()