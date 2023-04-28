def weekday_name(day_of_week):
    """Return name of weekday."""
    
    days= {1 : "Sunday",
    2 : "Monday",
    3 : "Tuesday", 4 :"Wednesday", 5 : "Thursday", 6 :"Friday" , 7 : 'Saturday'}
    if day_of_week > 7 | day_of_week == 0:
        return None
    else: 
        return days[day_of_week]
        
weekday_name(1)

        
weekday_name(7)

    
weekday_name(9)
weekday_name(0)
    