from tkinter import *
import all_constants as c

class Converter():
    """
    Temperature conversion tool (°C to °F or °F to °C))
    """

    def __init__(self):
        """
        Temperature Converter GUI
        """

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame,
                                  text="Temperature Converter",
                                  font=("Arial", "16", "bold")
                                  )
        self.temp_heading.grid(row=0)

        instructions = ("Please enter a temperature below and then press " 
        "one of the buttons to convert it from centrigade "
        "to Fahrenheit. ")
        self.temp_instructions = Label(self.temp_frame,
                                       text=instructions,
                                       wraplength=250, width=40,
                                       justify="left")
        self.temp_instructions.grid(row=1)

        self.temp_entry = Entry(self.temp_frame,
                                font=("Arial", "14")
                                )
        self.temp_entry.grid(row=2, padx=10, pady=10)


        error = "Please enter a number"
        self.answer_error = Label(self.temp_frame, text=error,
                                fg="#004C99", font=("Arial", "14", "bold"))
        self.answer_error.grid(row=3)

        # Conversion, help and history / export buttons
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        # button list (button text | bg colour | command | row | column)
        button_details_list = [
           ["To Celcius", "#990099", 0, 0, lambda:self.check_temp(c.ABS_ZERO_FAHRENHEIT)],
           ["To Fahrenheit", "#009900", 0, 1, lambda:self.check_temp(c.ABS_ZERO_CELCIUS)],
           ["Help / Info", "#CC6600", 1, 0, ""], 
           ["History / Export", "#004C99", 1, 1, ""]                                
        ]

        # List to hold buttons once they have been made
        self.buttons_ref_list = []

        for item in button_details_list:
            self.make_button = Button(self.button_frame,
                                    text=item[0],
                                    bg=item[1],
                                    fg="#FFFFFF",
                                    font=("Arial", "12", "bold"))
            self.make_button.grid(row=item[2], column=item[3], padx=5, pady=5)
            if item[4]:  # If there's a command
                self.make_button.config(command=item[4])

            self.buttons_ref_list.append(self.make_button)

        # Configure history button after all buttons are created
        self.to_history_button = self.buttons_ref_list[3]
        self.to_history_button.config(state=DISABLED)

    def check_temp(self,min_temp):
        """
        Checks temperature is valid and either invokes calculation function or shows a custom error
        """
        # print("Min Temp: ", min_temp)

        # Retrieve temperature to be converted
        temp_to_convert = self.temp_entry.get()
        # print("to convert", temp_to_convert)

        # Reset label and entry box (if we had an error)
        self.answer_error.config(fg="#004C99", font=("Arial", "13", "bold"))
        self.temp_entry.config(bg="#FFFFFF")

        error = f"Enter a number more than / equal to {min_temp}"
        has_errors = "no"
        
        # checks that amount to be converted is a number above absolute zero
        try:
            to_convert = float(temp_to_convert)
            if to_convert >= min_temp:
               error = ""
               self.convert(min_temp)
            else:
                error = "Too Low"

        except ValueError:
            error = "Please enter a number"

           # display the error if necessary
        if error != "":
            self.answer_error.config(text=error, fg="#9C0000")
            self.temp_entry.config(bg="#F4CCCC")
            self.temp_entry.delete(0, END)

    def convert(self, min_temp, to_convert):
        """
        Converts temperatures and updates answer label. Also stores calculations for Export / History feature
        """

        if min_temp == c.ABS_ZERO_CELCIUS:
            self.answer_error.config(text=f"Converting {to_convert}°C to °F")
        else:
            self.answer_error.config(text=f"Converting {to_convert} °F to °C")
                
# main routine
if __name__ == "__main__": 
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
