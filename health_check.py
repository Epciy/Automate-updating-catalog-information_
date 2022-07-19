#!/usr/bin/env python3
import psutil
import socket
import emails

# set system thresholds:
max_cpu_usage= 80
max_disk_available = 20
max_memory_available = 500
check_local_host_ip = "127.0.0.1"


def check_CPU():
    """check if CPU usage % exceeds max threshold"""
    cpu_usage = psutil.cpu_percent(interval=3)
    
    return cpu_usage> max_cpu_usage


def check_Disk():
    """check if Disk usage exceeds max threshold"""
    max_disk_usage_perc = 100 - max_disk_available
    dsk_usage_perc = psutil.disk_usage("/").percent
    
    return dsk_usage_perc > max_disk_usage_perc


def check_Memory():
    """check if Memory usage % exceeds max threshold"""
    one_mb = 2 ** 20
    max_mem_available = one_mb * max_memory_available
    mem_available = psutil.virtual_memory().available
    
    return mem_available < max_mem_available

def check_Net():
    """check if local host name resolves to local IP"""
    local_host_ip = socket.gethostbyname("localhost")
    return local_host_ip != check_local_host_ip


def sendAlert(alert):
    """output alert error and send email"""
    content = {
        "sender": "automation@example.com",
        "receiver": "student@example.com",
        "subject": alert,
        "body": "Please check your system and resolve the issue as soon as possible.",
        "attachment": None,
    }
    try:
        message = emails.generate_email(**content)
        emails.send_email(message)
    except:
        print("unable to send alert email notification!")
    finally:
        print(alert)
        exit(1)


def main():
    # check system resources:
    print("checking system resources")
    alert = None
    if check_CPU():
        alert = f"Error - CPU usage is over {max_cpu_usage}%"
    elif check_Disk():
        alert = f"Error - Available disk space is less than {max_disk_available}%"
    elif check_Memory():
        alert = f"Error - Available memory is less than {max_memory_available}MB"
    elif check_Net():
        alert = f"Error - localhost cannot be resolved to {check_local_host_ip}"

    # alert if error raised:
    if alert:
        sendAlert(alert)
    else:
        print("system ok")


if __name__ == "__main__":
    main()



