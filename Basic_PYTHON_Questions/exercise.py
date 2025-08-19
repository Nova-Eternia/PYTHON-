# write the code which greets you with good morning , good morning and good evening according to the time .
import time

timestamp=int(time.strftime("%H"))
print (timestamp)

if( timestamp<12):
    print("good morning")
elif(timestamp<18):
    print("good afternoon")
else:print("good eaving")