from netmiko import ConnectHandler
from functools import wraps

def user_check(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        username = kwargs.get('username') or (args[2] if len(args) > 2 else None)
        if username != "root":
            print("Access denied. Only 'root' user is allowed to connect.")
            return None
        return func(*args, **kwargs)
    return wrapper

@user_check
def device_connect(device_type, hostname, username, password):
    try:
        with ConnectHandler(
            device_type=device_type,
            host=hostname,
            username=username,
            password=password
        ) as net_connect:
            print(net_connect.find_prompt())
    except Exception as e:
        print("Connection failed:", e)


cisco = device_connect(
    device_type="cisco_ios",
    hostname="cisco_9110",
    username="root",  
    password="password"
)

