"""
Calendar Matching
Imagine that you want to schedule a meeting of a certain duration with a coworker. 
You have access to your calendar and your coworker's calendar (both of which contain your respective meetings for the day, in the form of [startTime, endTime]), 
as well as both of your daily bounds (i.e., the earliest and latest times at which you're available for meetings every day, in the form of [earliestTime, latestTime]). 
Write a function that takes in your calendar, your daily bounds, your coworker's calendar, your coworker's daily bounds, and the duration of the meeting that you want to schedule, 
and that returns a list of all the time blocks (in the form of [startTime, endTime]) during which you could schedule the meeting. 
Note that times will be given and should be returned in military time (example times: '8:30', '9:01', '23:56').

Sample input:
['9:00', '10:30] , ['12:00', '13:00] , ['16:00', '18:00'],
['9:00', '20:00'],
['10:00', '11:30], ['12:30', '14:30], ['14:30', '15:00'], ['16:00', '17:00'],
['10:00', '18:30],
30

Sample output: ['11:30', '12:001 , '15:00', '16:00', '18:00', '18:30']
"""

# Solution 1 --->  
# Time - O(c1 + c2)  | Space - O(c1 + c2)
---------------------------------

def CalendarMatching(c1,db1,c2,db2,dur):
    updated_c1 = updateCalendar(c1,db1)
    updated_c2 = updateCalendar(c2,db2)
    mergedcalendar = merge(updated_c1,updated_c2)
    flattenedcalendar = flatten(mergedcalendar)
    return getavailabilities(flattenedcalendar,dur)
    
    
def updateCalendar(c,db):
    updated_c = [['00:00' , db[0] ]] + c[:]  + [ [db[1], '23:59'] ]
    return list(map(lambda m: [timetomin(m[0]),timetomin(m[1])],updated_c))

def merge(c1,c2):
    merged = []
    i,j = 0,0
    while i < len(c1) amd j < len(c2):
        if c1[i][0] < c2[j][0]:
            merged.append(c1[i])
            i += 1
        else:
            merged.append(c2[j])
            j += 1
            
    while i < len(c1):
        merged.append(c1[i])
        i += 1
    while j < len(c2):
        merged.append(c2[j])
        j += 1
    
    return merged

def flatten(c):
    flat = [c[0][:]]
    for i in range(1,len(c)):
        curstart,curend = c[i]
        prevstart,prevend = flat[-1]
        
        if curstart <= prevend:
            newtime = [prevstart, max(curend,prevend)]
            flat[-1] = newtime
        else:
            flat.append(c[i][:])
    return flat
  
def getavailabilities(c,dur):
    avail = []
    for i in range(1,len(c)):
        prevend = c[i-1][1]
        curstart = c[i][0]
        duration = curstart - prevend
        if duration >= dur:
            avail.append([prevend,curstart])
    
    return list(map(lambda m : [mintohour(m[0]),mintohour(m[1])],avail))

def mintohour(time):
    hours = str(time//60)
    mins = '0' + str(time%60) if time % 60 < 10 else str(time%60)
    return hours + ':' + mins
 
def timetomin(time):
    hours,mins = time.split(':')
    return int(hours) * 60 + int(mins)

