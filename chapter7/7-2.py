import time
from datetime import datetime

def elapsed(origin_func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = origin_func(*args, **kwargs)
        end = time.time()
        print(f"함수 수행시간 : {round(end-start,3)}초(시작:{datetime.fromtimestamp(start).strftime("%H:%M:%S")},종료:{datetime.fromtimestamp(end).strftime("%H:%M:%S")})")
        return result
    return wrapper

@elapsed
def myFunction(msg):
    print(f"My함수({msg}) 실행...")
    time.sleep(1)

myFunction("Export to Excel")
    
# decorated_myFun = elapsed(myFunction)
# decorated_myFun()
