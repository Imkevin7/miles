# Converting miles to feet and yards
# TODO calculate yards and feets
# facts

def main():
    miles_ran = float(input("Miles ran: "))
    convert_feet(miles_ran)


def convert_feet(m):
    feet = m * 5280
    yards = m * 1760
    fields = yards / 100
    print("You've ran: ")
    print(f"{feet:,.2f} feet.")
    print(f"{yards} yards.")
    print(f"That's {fields} football fields.")
    tracking(m, feet, yards, fields)


def tracking(m, ft, yd, fi):
    import datetime
    x = open("trak.txt", "a")
    date = datetime.datetime.now()
    dated = date.strftime("%x")
    timed = date.strftime("%I:%M %p")
    y = f"{m} mile(s) on {dated} at {timed}:\n {ft} feet\n {yd} yards\n {fi} football fields"
    x.write(y + "\n")
    x.close()


main()
