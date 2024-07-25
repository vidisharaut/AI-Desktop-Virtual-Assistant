from datetime import datetime

def Action(query):
    query = query.lower()
    if 'how are you' in query:
        return 'I am fine. Thank you!' 
    elif 'the time' in query:
        now = datetime.now()
        curr_time = now.strftime("%H Hour:%M min")
        return curr_time
    
