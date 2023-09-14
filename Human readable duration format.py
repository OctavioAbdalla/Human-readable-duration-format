
def format_duration(seconds):

    result = ''
    
    if seconds == 0: return "now"
    
    def format(seconds):
        formats = [31536000, 86400, 3600, 60, 1]
    
        for d in range(len(formats)):
            if seconds > formats[d] and seconds % formats[d] != 0: return ", "
            elif seconds % formats[d] == 0: return " and "
        
    year = seconds//31536000
    if year > 0: 
        seconds = seconds % 31536000
        if year > 1: result += str(year) +" years"
        elif year == 1: result += "1 year"
        if seconds == 0: pass 
        else: result += format(seconds)
    
    day = seconds//86400
    if day > 0: 
        seconds = seconds % 86400
        if day > 1: result += str(day)+" days"
        elif day == 1: result += "1 day"
        if seconds == 0: pass 
        else: result += format(seconds)

    hour = seconds//3600
    if hour > 0: 
        seconds = seconds % 3600
        if hour > 1: result += str(hour)+" hours"
        elif hour == 1: result += "1 hour"
        if seconds == 0: pass 
        else: result += format(seconds)
    
    minute = seconds//60
    if minute > 0: 
        seconds = seconds % 60
        if minute > 1: result += str(minute)+" minutes" 
        elif minute == 1: result += "1 minute"
        if seconds == 0: pass 
        else: result += format(seconds)
         
    if seconds > 1: result += str(seconds) + " seconds"    
    elif seconds == 1: result += "1 second"
    
    return result
    

format_duration(0)