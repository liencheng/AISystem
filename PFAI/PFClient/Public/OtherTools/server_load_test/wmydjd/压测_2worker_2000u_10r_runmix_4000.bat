 : master-port 默认是5557，此处本项目使用5565
: -workers 指定需要连接的worker数量
: -u 总体数量，会平均分给slave
: -c 100表示每个Worker的并发用户数为100 暂不支持
: -r 20表示每秒启动的用户数为20
start locust -f load_tests\l_login_and_mix_all.py --master --master-host=127.0.0.1 --headless --expect-workers 2 -u 2000 -r 10 --logfile=load_test_4000.log --loglevel=INFO
start locust -f load_tests\l_login_and_mix_all.py --worker --master-host=127.0.0.1 --account_prefix z15_ --account_start_at 3000
start locust -f load_tests\l_login_and_mix_all.py --worker --master-host=127.0.0.1 --account_prefix z15_ --account_start_at 4000
pause