from locust import events
from locust.runners import MasterRunner, WorkerRunner
import TestParam


# 自定义命令行参数
@events.init_command_line_parser.add_listener
def _(parser):
    #env_var="LOCUST_ACCOUNT_PREFIX", env_var="LOCUST_ACCOUNT_START_AT",
    parser.add_argument("--account_prefix", type=str, include_in_web_ui=False, default="a_", help="set account prefix, default is a_")
    parser.add_argument("--account_start_at", type=int, include_in_web_ui=False, default=10000, help="set account start, default is 10000")


@events.init.add_listener
def _(environment, **kw):
    if not isinstance(environment.runner, MasterRunner):
        TestParam.account_prefix = environment.parsed_options.account_prefix
        TestParam.account_startwith = environment.parsed_options.account_start_at
        print(f"in init Custom argument supplied: {environment.parsed_options.account_prefix}")
        print(f"in init Custom argument supplied: {environment.parsed_options.account_start_at}")


# @events.test_start.add_listener
# def _(environment, **kw):
#     args = environment.parsed_options
#     if args.account_prefix != "a_":
#         print("account_prefix is set to", args.account_prefix)
#     else:
#         print("account_prefix is not set")
#
#     if args.account_start_at != 10000:
#         print("account_start_at is set to", args.account_start_at)
#     else:
#         print("account_start_at is not set")

# # Fired when the worker receives a message of type 'test_users'
# def setup_test_users(environment, msg, **kwargs):
#     for user in msg.data:
#         print(f"User {user['name']} received")
#         # send message to target
#     environment.runner.send_message('acknowledge_users', f"Thanks for the {len(msg.data)} users!")
#
# # Fired when the master receives a message of type 'acknowledge_users'
# def on_acknowledge(msg, **kwargs):
#     print(msg.data)
#
# @events.init.add_listener
# def on_locust_init(environment, **_kwargs):
#     if not isinstance(environment.runner, MasterRunner):
#         # message handler on workers
#         environment.runner.register_message('test_users', setup_test_users)
#     if not isinstance(environment.runner, WorkerRunner):
#         # message handler on master, receive acknowledge
#         environment.runner.register_message('acknowledge_users', on_acknowledge)
#
# @events.test_start.add_listener
# def on_test_start(environment, **_kwargs):
#     # master send
#     if not isinstance(environment.runner, WorkerRunner):
#         users = [
#             {"name": "User1"},
#             {"name": "User2"},
#             {"name": "User3"},
#         ]
#         environment.runner.send_message('test_users', users)