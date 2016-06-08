import subprocess
user=input('Enter SSID : ')
key=input('Enter Key : ')
stri='netsh wlan set hostednetwork ode=allow ssid=%s key=%s'%(user,key)
net=subprocess.Popen(stri,shell=False,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
output,errors=net.communicate()
if errors:
    print('WARNING : ',errors)
elif output:
    print('SUCCESS :',output)
    sta=subprocess.Popen('netsh wlan start hostednetwork',shell=False,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
    out,err=sta.communicate()
    if err:
        print('ERR START : ',err)
    elif out:
        print('STARTED : ',out)





#Shell set to false because of security concerns.
#If set to True, the cmd wont appear briefly while its running the lines
