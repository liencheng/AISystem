
rem require: python 3.6+
rem requrie: locust 2+

rem locust worker param: 
rem --slave :	locust run as worker
rem --master-host :	report to this locust master
rem -u :	user counts
rem -r :	add user step (per sec)
rem --run-time: running locust worker time, m: minitue


locust -f load_tests\l_login.py --worker --master-host=10.5.11.8 --headless -u 10 -r 1 --run-time 5m