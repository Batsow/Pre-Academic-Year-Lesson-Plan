months = [
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
        date = input("Date: ").strip()  
        
        if "," in date:
            month,day,year = date.replace(",","").split(" ")
            month = month.title()
            month = months.index(month) + 1
            
        else:
            month,day,year = date.split("/")
            
        month,day,year = int(month), int(day), int(year)
        
        if 1 <= month <= 12 and 1 <= day <= 31:
            print(f"{year}-{month:02}-{day:02}")
            break
    
    except ValueError:
        pass
    
    
    
        
        
        
        
   