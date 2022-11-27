import subprocess
import tkinter
import customtkinter


class ExampleApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("300x100")
        #self.geometry("500x400")

        self.button = customtkinter.CTkButton(self, text="scan networks", command=self.create_toplevel)
        self.button.pack(side="top", padx=40, pady=40)

    def create_toplevel(self):
        window = customtkinter.CTkToplevel(self)
        window.geometry("500x400")

        #the network scanner stuff
        # using the check_output() for having the network term retrieval
        devices = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])

        # decode it to strings
        devices = devices.decode('ascii')
        devices = devices.replace("\r", "")

        # create label on CTkToplevel window
        label = customtkinter.CTkLabel(window, text=devices)
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)


app = ExampleApp()
app.mainloop()