list=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        date=input("Date: ")
        if '/' in date:
            date=date.split('/')
            month, day, year = map(int, date)
            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year}-{month:02d}-{day:02d}")
                break
        elif ',' in date:
            date=date.replace(',', '').split()
            day, year = int(date[1]), int(date[2])
            month=list.index(date[0])+1
            if 1 <= month <= 12 and 1 <= int(day) <= 31:
                print(f"{year}-{month:02d}-{day:02d}")
                break
        else:
            pass

    except:
        pass