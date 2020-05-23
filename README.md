# flask
In this code I create a web API to read and process a csv file using flask and pandas.

Considerations and how to use
● All code was tested on Python2.7 running on a Mac with MacOS 10.14.
● Libraries used are: standard with the addition of pandas and flask. Those are Open
Source.
● No data validation is performed.
● This code assumes all dates are within the same time zone.
● Paths inside the code are hardcoded and should be run at the same level as
“tvav_test-files”.

** URL API MODE

To run, you must type: 
python flask_example.py in the terminal window. 

Then from a web browser, visit the address: http://127.0.0.1:5000/query? followed by parameters for dates, country and title the URL API style. Like in the following example,
http://127.0.0.1:5000/query?start=20180101&end=20180903&country=IRL&t itle=Papillon

Note that dates are specified in the format ‘YYYYMMDD’.

** FORM MODE

To run, you must type:
python flask_example.py in the terminal window. 

Then from a web browser, visit the address: 
http://127.0.0.1:5000/form. 

This will show a window asking for the parameters for this report. Dates should be written using the format ‘YYYYMMDD’.

