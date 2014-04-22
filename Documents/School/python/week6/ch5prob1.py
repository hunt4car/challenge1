def main():
    # get the day month and year
    dateStr = input("Please a date (mm/dd/yyyy): ")

    day, month, year = dateStr.split("/")

    months = ["January", "February", "March", "April",
              "May", "June", "July", "August",
              "September", "October", "November", "December"]
    date= int(day),months[month],int(year)
    return date

    print ("The date is", date)

main()
#not sure to to get this fully running...
