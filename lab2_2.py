#Programmer: Andy Li
#Assignment Lab 2 pt 2
#IFT333
#Spring 2019 B

#open two input sources
fast_inp = open("fast.csv", "r")
furious_inp = open("furious.csv", "r")

#open two output csv files
vehicle_out = open("vehicle_out.csv", "w")
service_out = open("service_out.csv", "w")

#create a dictionary to hold car id
cars = {}

#scan the furious file line by line(furious first since it has more information)
for line in furious_inp:
    (vin, model, make, color, issue, date)= line.rstrip().split(",")
    #avoid storing car information multiple times:
    if vin not in cars:
        cars[vin] = 1;
        vehicle_out.write(vin + "," + model + "," + make + "," + color+"\n")
    service_out.write(vin + "," + issue + "," + date + "\n")

#scan the fast file line by line
for line in fast_inp:
    (vin, issue_date, issue, result, result_date)= line.rstrip().split(",")
    #avoid storing car information multiple times:
    if vin not in cars:
        cars[vin] =1;
        vehicle_out.write(vin + "\n")
    service_out.write(vin + "," + issue + "," + issue_date + "," + result + "," + result_date + "\n")

#close files
fast_inp.close()
furious_inp.close()
vehicle_out.close()
service_out.close()    