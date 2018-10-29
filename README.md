# flask
In this code I create an web API to read and process a csv file using flask and pandas.

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
 
- All parameters are mandatory and should follow the format ‘YYYY-MM-DD HH:MM’ for dates and lowercase for strings.
- To run, it is necessary to run python in terminal window, music_report.py file and parameters for start, end and channel, like in the following example:
python music_report.py '2018-01-01 10:00' '2018-02-25 13:45' 'rte'


