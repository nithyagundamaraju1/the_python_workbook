secs=int(input("Total duration in seconds:"))
days=secs//86400
secs =secs%(24*3600)
hrs=secs//3600
secs = secs%3600
mins=secs//60
secs = secs%60
print(f"Equivalent Time: {days:02d}:{hrs:02d}:{mins:02d}:{secs:02d}")