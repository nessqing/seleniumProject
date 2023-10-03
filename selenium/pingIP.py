import os
hostnames=['192.168.0.169','192.168.0.168']

for host in hostnames :
    response = os.system('ping -c 1 ' + host)
    if response == 0:
        print(host, 'is up')
        textfile = open('/Users/haru/Desktop/seleniumProject/selenium/profile.properties',"w")
        pa = "{}\n".format(host.split('.',4))
        print(pa)
        textfile.write(pa)
        textfile.close()
    else:
        print(host,'is down')
