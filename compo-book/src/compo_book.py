#!/usr/bin/python3
import os
import customtkinter as ctk
import platform
import cpuinfo
import psutil
import igpu
import GPUtil
import subprocess
# création de la fenetere


app = ctk.CTk()
app.geometry("500x500")
ctk.set_appearance_mode("dark")
app.title("Compo Book")
frame = ctk.CTkFrame(master=app)

# infos
label = ctk.CTkLabel(app, text="Compo Book")
label.pack()
label = ctk.CTkLabel(app, text="Outil de reconditionnement par Valentin Drouillet")
label.pack()
print("")
label = ctk.CTkLabel(app, text="v0.0.1")
label.pack()
# permet d'avoir les infos du processeur
command = "sudo grep -m 1 'model name' /proc/cpuinfo"
label = ctk.CTkLabel(frame, text="INFO PROCESSEUR")
label.pack()
print("")
label = ctk.CTkLabel(frame, text=cpuinfo.get_cpu_info()['brand_raw'])
label.pack()
print("")

# permet d'avoir les infos de la RAM
ram_usage = psutil.virtual_memory().percent
ram_usage_label = ctk.CTkLabel(frame, text="Utilisation de la RAM")
def update_ram_info():
	ram_usage_label.configure(text=f"Utilisation RAM : {ram_usage}%")
	app.after(1000, update_ram_info)
label = ctk.CTkLabel(frame, text="INFOS RAM")
label.pack()
label = ctk.CTkLabel(frame, text="RAM installée : " + os.popen("sudo dmidecode -t memory | grep -i size").read())
label.pack()

ram_usage_label.pack()
update_ram_info()
# infos sur la carte graphique

label = ctk.CTkLabel(frame, text="INFOS CG")
label.pack()
label = ctk.CTkLabel(frame, text="Nom : " + os.popen("lshw -C display | sed '1d;2d;4d;5d;6d;7d;8d;9d;10d;11d;12d;'").read())
label.pack()
label = ctk.CTkLabel(frame, text="WIP")
label.pack()
# infos sur l'alim


label = ctk.CTkLabel(app, text="")
# infos sur le numero de serie
frame.pack(pady = 20, padx = 60, fill="both", expand=True)
app.mainloop()