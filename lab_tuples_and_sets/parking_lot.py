'''Write a program that:
•	Records a car number for every car that enters the parking lot
•	Removes a car number when the car leaves the parking lot
On the first line, you will receive the number of commands - N. On the following N lines, you will receive the\
direction and car's number in the format: "{direction}, {car_number}". The direction could only be "IN" or "OUT".\
Print the car numbers which are still in the parking lot. Keep in mind that all car numbers must be unique. If the\
parking lot is empty, print "Parking Lot is Empty".
Note: The order in which we print the result does not matter.
Example:
10
IN, CA2844AA
IN, CA1234TA
OUT, CA2844AA
IN, CA9999TT
IN, CA2866HI
OUT, CA1234TA
IN, CA2844AA
OUT, CA2866HI
IN, CA9876HH
IN, CA2822UU
'''

car_numbers = [input() for plate_numbers in range(int(input()))]
parking_lot = set()

for record_plate in car_numbers:
    command, plate_number = record_plate.split(", ")

    if command == "IN":
        parking_lot.add(plate_number)
    elif command == "OUT":
        parking_lot.discard(plate_number)

if parking_lot:
    for plates in parking_lot:
        print(plates)
else:
    print("Parking Lot is Empty")
