# /bin/env/python3

def ipaddress(data):
    octet=data.split(".")
    first_byte=int(octet[0])
    second_byte=int(octet[1])
    third_byte=int(octet[2])
    fourth_byte=int(octet[3])
    if (first_byte==0 or first_byte<=127 )and (second_byte==0 or second_byte<=255) and (third_byte==0 or third_byte<=255 )and (fourth_byte==0 or fourth_byte<=255):
        print("Class A IP")
    elif (first_byte==128 or first_byte<=191) and (second_byte==0 or second_byte<=255) and( third_byte==0 or third_byte<=255 )and (fourth_byte==0 or fourth_byte<=255):
        print("Class B IP")
    elif (first_byte==192 or first_byte<=223 )and (second_byte==0 or second_byte<=255 )and (third_byte==0 or third_byte<=255 )and (fourth_byte==0 or fourth_byte<=255):
        print("Class C IP")
    elif  (first_byte==224 or first_byte<=239 )and (second_byte==0 or second_byte<=255) and (third_byte==0 or third_byte<=255 )and (fourth_byte==0 or fourth_byte<=255):
        print("Class D IP")
    elif (first_byte==240 or first_byte<=255 )and (second_byte==0 or second_byte<=255 )and (third_byte==0 or third_byte<=255 )and (fourth_byte==0 or fourth_byte<=255):
        print("Class E IP")
    else:
        print("Invalid IP")
    


data = input("Enter the ip address to check its class")
ipaddress(data)
