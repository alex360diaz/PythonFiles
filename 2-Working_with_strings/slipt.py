# split(separator) --> Breaks a string into smaller parts

# Example: How to separate date from time
stamp = "2026-03-31 20:00"
new_stamp =stamp.split(" ")
print(new_stamp)
#Example: How to saparate year, month, day
date = "2026-03-31"
new_date =date.split("-")
print(new_date)
#Example: 
csv_file = "1234,Alex,Mexico,1999,M"
new_csv = csv_file.split(",")
print(new_csv)