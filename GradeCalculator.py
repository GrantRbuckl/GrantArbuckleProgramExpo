print("This program gives you a letter grade based on the percent you give.")

ui = int(input("Please enter the percentage you got on the test: "))
letter = ""
if ui<59:
    letter = "an F"
elif ui>59 and ui<70:
    letter = "a D"
elif ui>69 and ui<80:
    letter = "a C"
elif ui>79 and ui<90:
    letter = "a B"
elif ui>89 and ui<101:
    letter = "an A"
ui = str(ui)
if (ui == "18") or (ui=="8") or (ui[0] == "8"):
    ui="An "+ui
else:
    ui="A "+ui
print(f"{ui} earned you {letter}.")
