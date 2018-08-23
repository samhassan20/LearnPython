import datetime

now = datetime.datetime.now()   #you can just write datetime.now()  if from datetime import datetime

#using str method
print "Current date and time using str method of datetime object:"
print str(now)

print "Current year: %d" % now.year
print "Current month: %d" % now.month
print "Current day: %d" % now.day
print "Current hour: %d" % now.hour
print "Current minute: %d" % now.minute
print "Current second: %d" % now.second
print "Current microsecond: %d" % now.microsecond

#using strftime

print "Current date and time using strftime:"
print now.strftime("%Y-%m-%d %H:%M")


#using timedelta

print "1 week ago : ", now - datetime.timedelta(weeks=1)
print "100 days from now : ", now + datetime.timedelta(days=100)


bday = datetime.datetime(2018,9,20)

print "Birthday is in ... ", bday - now