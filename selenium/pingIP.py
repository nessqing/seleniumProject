import os
hostnames = []
for i in range (51,256,1) :
    print(i)
    hostnames.append('192.168.119.' + str(i))
print(hostnames)

textfile = open('/Users/haru/Desktop/seleniumProject/selenium/profile.properties', "w")
for host in hostnames :
    textfile.write(host + '\n')
textfile.close()
# textfile.write(hostnames)

# textfile = open('/Users/haru/Desktop/seleniumProject/selenium/profile.properties', "w")
#
# for host in hostnames :
#     textfile.write(host)
#     print(host)
#
# textfile.close()
    # textfile = open('/Users/haru/Desktop/seleniumProject/selenium/profile.properties', "w")
    # textfile.writelines(host)
    # textfile.close()
    # response = os.system('ping -c 1 ' + host)
    # if response == 0:
    #     print(host, 'is up')
    #     textfile = open('/Users/haru/Desktop/seleniumProject/selenium/profile.properties',"w")
    #     # pa = host
    #     pa = "{}\n".format(host.split('.',4))
    #     print(pa)
    #     textfile.write(pa)
    #     textfile.close()
    # else:
    #     print(host,'is down')
