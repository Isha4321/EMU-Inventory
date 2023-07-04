from tkinter import *
import subprocess

def speedcheck():
    process = subprocess.Popen(['speedtest-cli', '--simple'], stdout=subprocess.PIPE)
    output, error = process.communicate()
    result = output.decode()

    lines = result.split("\n")
    download_speed = lines[1].split(":")[1].strip()
    upload_speed = lines[2].split(":")[1].strip()

    lab_down.config(text=download_speed)
    lab_up.config(text=upload_speed)


sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x650")
sp.config(bg="Blue")

lab = Label(sp, text="Internet Speed Test", font=("Times New Roman", 30, "bold"), bg="Blue", fg="White")
lab.place(x=60, y=40, height=50, width=380)

lab = Label(sp, text="Download Speed", font=("Times New Roman", 30, "bold"))
lab.place(x=60, y=130, height=50, width=380)

lab_down = Label(sp, text="00", font=("Times New Roman", 30, "bold"))
lab_down.place(x=60, y=200, height=50, width=380)

lab = Label(sp, text="Upload Speed", font=("Times New Roman", 30, "bold"))
lab.place(x=60, y=290, height=50, width=380)

lab_up = Label(sp, text="00", font=("Times New Roman", 30, "bold"))
lab_up.place(x=60, y=360, height=50, width=380)

button = Button(sp, text="CHECK SPEED", font=("Times New Roman", 30, "bold"), relief=RAISED, bg="Red", command=speedcheck)
button.place(x=60, y=460, height=50, width=380)

sp.mainloop()
