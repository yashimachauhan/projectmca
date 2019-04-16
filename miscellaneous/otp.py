import random
import datetime as dt
def otpgenerate():
    otp=random.randint(10000,100000)
    time=dt.datetime.now().time()

    return otp,time

