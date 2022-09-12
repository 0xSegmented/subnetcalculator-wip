ip = input("Enter IP\n")
# format ip: 000.000.000.000
ip_list = ip.split('.')     # print(ip_list[0])
int_ip_list = [int(x) for x in ip_list]
print(int_ip_list)
if int_ip_list[0] >= 0 and int_ip_list[0] <= 126: # Half-Duplex CLASS A
    print("Class A")   # Subnet kiezen \/
    subnetA = int(input("Choose subnet: 8, 9, 10, 11, 12, 13, 14, 15\n"))
    # 128 64 32 16 8 4 2 1
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
elif int_ip_list[0] >= 128 and int_ip_list[0] <= 191:
    print("Class B")
    subnetB = int(input("Choose subnet: 16, 17, 18, 19, 20, 21, 22, 23\n"))
    if subnetB == 16:
        print("255.255.0.0")
    elif subnetB == 17:
        print("255.255.128.0")
    elif subnetB == 18:
        print("255.255.192.0")
    elif subnetB == 19:
        print("255.255.224.0")
    elif subnetB == 20:
        print("255.255.240.0")
    elif subnetB == 21:
        print("255.255.248.0")
    elif subnetB == 22:
        print("255.255.252.0")
    elif subnetB == 23:
        print("255.255.254.0")
    else:
        print("Choose between 16 and 23")

# IP in stukken bijv: 192 168 1 0
# Subnet los: 255 255 255 0
elif int_ip_list[0] >= 192 and int_ip_list[0] <= 223:
    print("Class C")
    subnetC = int(input("Choose subnet: 24, 25, 26, 27 28\n"))
    if subnetC == 24:
        st = "255.255.255.0"
        sp = st.split('.')
        xs = [int(x) for x in sp]
        timeszero = 8
        hosts = (2**timeszero)-2
        network = (2**(32-subnetC))-2
        print("Subnet: 255.255.255.0")
        print(f"available hosts:{hosts}")
        print(f"available network:{network}")
        # showing the hosts and networks
        # int_ip_list
        count = -1 
        while count <= network:
            count +=1
            print(f"{int_ip_list[0]}.{int_ip_list[1]}.{count}.1-254")
    elif subnetC == 25:
        st = "255.255.255.128"
        sp = st.split('.')
        xs = [int(x) for x in sp]
        print(xs)
    elif subnetC == 26:
        st = "255.255.255.192"
        sp = st.split('.')
        xs = [int(x) for x in sp]
        print(xs)
    elif subnetC == 27:
        st = "255.255.255.224"
        sp = st.split('.')
        xs = [int(x) for x in sp]
        print(xs)
    elif subnetC == 28:
        st = "255.255.255.240"
        sp = st.split('.')
        xs = [int(x) for x in sp]
        print(xs)
    else:
        print("Choose between 24 and 28")


else:
    print("fail")
