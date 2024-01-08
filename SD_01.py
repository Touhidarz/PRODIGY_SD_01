from tkinter import *

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def fahrenheit_to_kelvin(fahrenheit):
    kelvin = (fahrenheit + 459.67) * 5/9
    return kelvin

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def kelvin_to_fahrenheit(kelvin):
    fahrenheit = (kelvin * 9/5) - 459.67
    return fahrenheit


def convert():
    try:
        temperature = float(entry_temp.get())
        unit = dropdown_menu.get()

        if unit == "Celsius":
            fahrenheit = celsius_to_fahrenheit(temperature)
            kelvin = celsius_to_kelvin(temperature)
            label_fahrenheit["text"] = f"{fahrenheit:.1f} Fahrenheit"
            label_kelvin["text"] = f"{kelvin:.1f} Kelvin"
        elif unit == "Fahrenheit":
            celsius = fahrenheit_to_celsius(temperature)
            kelvin = fahrenheit_to_kelvin(temperature)
            label_celsius["text"] = f"{celsius:.1f} Celsius"
            label_kelvin["text"] = f"{kelvin:.1f} Kelvin"
        elif unit == "Kelvin":
            celsius = kelvin_to_celsius(temperature)
            fahrenheit = kelvin_to_fahrenheit(temperature)
            label_celsius["text"] = f"{celsius:.1f} Celsius"
            label_fahrenheit["text"] = f"{fahrenheit:.1f} Fahrenheit"
        else:
            print("Invalid unit. Please select a valid option.")
    except ValueError:
        print("Invalid input. Please enter a numerical value for temperature.")

root = Tk()
root.title("Temperature Converter")


label_temp = Label(root, text="Temperature:", font="Arial 12")
label_temp.grid(row=0, column=0, pady=10)
label_unit = Label(root, text="Unit:", font="Arial 12")
label_unit.grid(row=1, column=0, pady=10)
label_celsius = Label(root, text="", font="Arial 12")
label_celsius.grid(row=2, column=1, pady=10)
label_fahrenheit = Label(root, text="", font="Arial 12")
label_fahrenheit.grid(row=3, column=1, pady=10)
label_kelvin = Label(root, text="", font="Arial 12")
label_kelvin.grid(row=4, column=1, pady=10)


entry_temp = Entry(root, width=10)
entry_temp.grid(row=0, column=1, pady=10)


dropdown_menu = StringVar()
dropdown_menu.set("Celsius")
options = ["Celsius", "Fahrenheit", "Kelvin"]
dropdown = OptionMenu(root, dropdown_menu, *options)
dropdown.grid(row=1, column=1, pady=10)


button_convert = Button(root, text="Convert", command=convert)
button_convert.grid(row=5, column=1, pady=10)

root.mainloop()

