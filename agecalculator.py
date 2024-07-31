from tkinter import *
from datetime import date

# Create the main window
root = Tk()
root.geometry("1200x1200")
root.resizable(True, True)
root.title("Age Calculator")

# Load and display the image
try:
    photo = PhotoImage(file="ageconverter.png")
    myimage = Label(root, image=photo)
    myimage.pack(padx=15, pady=15)
except Exception as e:
    print("Error loading image:", e)

# Define the function to calculate age
def calculateAge():
    try:
        today = date.today()
        birthDate = date(int(yearEntry.get()), int(monthEntry.get()), int(dayEntry.get()))
        age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
        Label(text=f"{nameValue.get()} your age is {age}", font=30).place(x=500, y=500)
    except ValueError as e:
        print("Invalid date:", e)

# Labels for user input
Label(text="Name", font=23).place(x=400, y=700)
Label(text="Year", font=23).place(x=400, y=750)
Label(text="Month", font=23).place(x=400, y=800)
Label(text="Day", font=23).place(x=400, y=850)

# Variables for storing user input
nameValue = StringVar()
yearValue = StringVar()
monthValue = StringVar()
dayValue = StringVar()

# Entry fields for user input
nameEntry = Entry(root, textvariable=nameValue, width=30, bd=3, font=20)
nameEntry.place(x=500, y=700)

yearEntry = Entry(root, textvariable=yearValue, width=30, bd=3, font=20)
yearEntry.place(x=500, y=750)

monthEntry = Entry(root, textvariable=monthValue, width=30, bd=3, font=20)
monthEntry.place(x=500, y=800)

dayEntry = Entry(root, textvariable=dayValue, width=30, bd=3, font=20)
dayEntry.place(x=500, y=850)

# Button to trigger age calculation
Button(root, text="Calculate Age", font=20, bg="black", fg="white", width=20, height=5, command=calculateAge).place(x=500, y=900)

# Run the main loop
root.mainloop()
