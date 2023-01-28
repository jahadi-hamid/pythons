#! /usr/bin/python3

import csv
import socket


path = input("enter filepath: ")
with open('ips2.csv', 'w') as csv_file:
   writer = csv.writer(csv_file)
   with open(path) as csv_file:
      csv_reader = csv.reader(csv_file, delimiter='$$$')
      line_count = 0
      for row in csv_reader:
          ip = row[1]
          if line_count == 0:
             line_count += 1
          else:
               if row[2] == "": 
                   try:
                       socket.inet_aton(ip)
                   except Exception as invalid_ip:
                        print ("Invalid IP address = ", (ip))
                        continue
                   try:
                       hostname = socket.gethostbyaddr(ip)[0]
                       row[2] = (hostname)
                       line_count += 1
                   except socket.error:
                       # Probably a similar problem as above; skip this test
                       pass
               else:
                 line_count += 1
          writer.writerow(row)
      print(f'Processed {line_count} lines.')
