from tkinter import *
import speedtest


def speedCheck():

    sp = speedtest.Speedtest()
    sp.get_servers()

    download = str(round(sp.download() / (1024 ** 2), 3)) + " Mbps"
    upload = str(round(sp.download() / (1024 ** 2), 3)) + " Mbps"

    lab_downloading.config(text=download)
    lab_uploading.config(text=upload)

    print("Choosing best server...")
    best = sp.get_best_server()
    print(f"Found : {best['host']} located in {best['country']}")

    print("Performing download test...")
    download_result = sp.download()

    print("Performing upload test...")
    upload_result = sp.upload()

    ping_result = sp.results.ping

    print(f"Download speed : {download_result / 1024 / 1024:.2f} Megabits per second")
    print(f"Upload speed : {upload_result / 1024 / 1024:.2f} Megabits per second")
    print(f"Ping : {ping_result} ms")


sp = Tk()

sp.title("Internet Speed Test")
sp.geometry("500x650")
sp.config(bg="#383838")

lab = Label(sp, text="Internet Speed Test", font=("Time New Roman", 25, "bold"), bg="#383838", fg="White")
lab.place(x=60, y=40, height=50, width=380)

lab = Label(sp, text="Download Speed", font=("Time New Roman", 25, "bold"), bg="#fbff05", fg="Black")
lab.place(x=60, y=130, height=50, width=380)

lab_downloading = Label(sp, text="00", font=("Time New Roman", 25, "bold"), bg="#383838", fg="White")
lab_downloading.place(x=60, y=200, height=50, width=380)

lab = Label(sp, text="Upload Speed", font=("Time New Roman", 25, "bold"), bg="#fbff05", fg="Black")
lab.place(x=60, y=290, height=50, width=380)

lab_uploading = Label(sp, text="00", font=("Time New Roman", 25, "bold"), bg="#383838", fg="White")
lab_uploading.place(x=60, y=360, height=50, width=380)

button = Button(sp, text="RUN SPEED TEST", font=("Time New Roman", 25, "bold"), relief=RAISED, bg="#05b4ff", command=speedCheck)
button.place(x=60, y=460, height=50, width=380)

sp.mainloop()
