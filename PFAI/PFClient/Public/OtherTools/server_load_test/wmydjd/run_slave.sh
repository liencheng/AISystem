#! /bin/bash
# require: python 3.6+
# requrie: locust 2+

# locust worker param: 
# --slave :	locust run as worker
# --master-host :	report to this locust master
# -u :	user counts
# -r :	add user step (per sec)
# --run-time: running locust worker time, m: minitue
# 

locust --config=myworker.conf