import psutil
cpu_threshold = 2
while True:
    
    try:
        cpu_status = psutil.cpu_percent(interval=1)
        if cpu_status > cpu_threshold:
            print("Alert! CPU usage exceeds threshold: " + str(cpu_status)+ "%")
    except Exception as e:
        print("An exception occured during cpu_percent: ",e)