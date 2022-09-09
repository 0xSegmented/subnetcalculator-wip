ip = input("Enter IP\n")
# format ip: 000.000.000.000
ip_list = ip.split('.')     # print(ip_list[0])
int_ip_list = [int(x) for x in ip_list]
print(int_ip_list)
if int_ip_list[0] >= 10 and int_ip_list[0] <= 126:
    print("Class A")
    subnetA = int(input("Choose subnet: 8, 9, 10, 11, 12, 13, 14, 15\n"))
    if subnetA == 8:      
        print("255.0.0.0")
    elif subnetA == 9:
        print("255.128.0.0")
    elif subnetA == 10:
        print("255.192.0.0")
    elif subnetA == 11:
        print("255.224.0.0")
    elif subnetA == 12:
        print("255.240.0.0")
    elif subnetA == 13:
        print("255.248.0.0")
    elif subnetA == 14:
        print("255.252.0.0")
    elif subnetA == 15:
        print("255.254.0.0")
    else:
        print("Choose between 8 and 15")
else:
    print("fail")
