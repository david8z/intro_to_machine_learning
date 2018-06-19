#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import re
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
count = 0
countSalary = 0
countEmail = 0
countTotalPay = 0
total = 0
poiTotalPay= 0

for key in enron_data:
    total += 1
    if ((enron_data[key]['poi'])== True):
        count += 1
        if(enron_data[key]['total_payments'] == 'NaN'):
            poiTotalPay += 1
    if(enron_data[key]['salary'] != 'NaN'):
        countSalary += 1
    if(enron_data[key]['email_address'] != 'NaN'):
        countEmail += 1
    if(enron_data[key]['total_payments'] == 'NaN'):
        countTotalPay += 1


print "Data points: ", len(enron_data)
print "Features: ", len(enron_data["SKILLING JEFFREY K"])
print "POI's: ", count
print "-------------"

print "People Data:"
print enron_data["PRENTICE JAMES"]["total_stock_value"]
print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print enron_data["SKILLING JEFFREY K"]['exercised_stock_options']
print enron_data["SKILLING JEFFREY K"]['total_payments']
print enron_data["LAY KENNETH L"]['total_payments']
print enron_data["FASTOW ANDREW S"]['total_payments']

print "-------------"
print "Count total payments NAN: ", countTotalPay, " Percentage it represent: " , (float(countTotalPay)/float(total))
print "Count salary: ", countSalary
print "Count email: ", countEmail
print "Count total payments NAN: ", countTotalPay, " Percentage it represent: " , (float(countTotalPay)/float(total))
print "Count total payments of POI's NAN: ",poiTotalPay , " Percentage it represent: " , (float(poiTotalPay)/float(count))
# Key = person name, contains features of that person
#for k, v in enron_data.iteritems():
#    print k 
