#usr/env/python3
import sys
import math

def cont():
  print("Do you want to continue ")
  print("Press Y/N to continue and exit respectively")
  inputchar=input()
  if(inputchar=="Y" or inputchar=="y"):
       switch()
  elif(inputchar=="N" or inputchar=="n"):
       sys.exit()
       

def switch():
    print("-"*40)
    print("1) Check Class of IPV4 Address")
    print("2) Exit")
    print("-"*40)
    option = int(input("your option : "))
    if  option == 1:
        data = input("Enter the ip address to check its class:")
        octet=data.split(".")
        (first_byte,second_byte,third_byte,fourth_byte)=(int(octet[0]),int(octet[1]),int(octet[2]),int(octet[3]))
        if len(str(first_byte))>3 :
            print("Incorrect lenght of  IP in first octet")
            cont()
        elif  len(str(second_byte))>3 :
            print("Incorrect lenght of  IP in second octet")
            cont()
        elif  len(str(third_byte))>3 :
            print("Incorrect lenght of  IP in third octet")
        elif len(str(fourth_byte))>3 :
            print("Incorrect lenght of  IP in fourth octet")
            cont()
        elif octet[4:]:
            print("Extra bits encountered so  Give IP in Format as A.B.C.D ")
            cont()

        if (first_byte==0 or first_byte<=127):
            if (second_byte==0 or second_byte<=255):
                if( third_byte==0 or third_byte<=255 ):
                    if (fourth_byte==0 or fourth_byte<=255):
                        print("Class A IP")
                        subnet(octet,'A')
                        cont()
                    else:
                        print("Invalid 4th octet of Class A IP")
                        cont()
                else:
                    print("Invalid 3rd octet of Class A IP")
                    cont()
            else:
                print("Invalid 2nd octet of Class A IP")
                cont()                         
               
        elif (first_byte==128 or first_byte<=191):
            if (second_byte==0 or second_byte<=255):
                if( third_byte==0 or third_byte<=255 ):
                    if (fourth_byte==0 or fourth_byte<=255):
                        print("Class B IP")
                        subnet(octet,'B')
                        cont()
                    else:
                        print("Invalid 4th octet of Class B IP")
                        cont()
                else:
                    print("Invalid 3rd octet of Class B IP")
                    cont()
            else:
                print("Invalid 2nd octet of Class B IP")
                cont()   
        elif (first_byte==192 or first_byte<=223):
            if (second_byte==0 or second_byte<=255):
                if( third_byte==0 or third_byte<=255 ):
                    if (fourth_byte==0 or fourth_byte<=255):
                        print("Class C IP")
                        subnet(octet,'C')
                        cont()
                    else:
                        print("Invalid 4th octet of Class C IP")
                        cont()
                else:
                    print("Invalid 3rd octet of Class C IP")
                    cont()
            else:
                print("Invalid 2nd octet of Class C IP")
                cont()                         
        elif (first_byte==224 or first_byte<=239):
            if (second_byte==0 or second_byte<=255):
                if( third_byte==0 or third_byte<=255 ):
                    if (fourth_byte==0 or fourth_byte<=255):
                        print("Class D IP")
                        subnet(octet,'D')
                        cont()
                    else:
                        print("Invalid 4th octet of Class D IP")
                        cont()
                else:
                    print("Invalid 3rd octet of Class D IP")
                    cont()
            else:
                print("Invalid 2nd octet of Class D IP")
                cont()                         
        elif (first_byte==240 or first_byte<=255):
            if (second_byte==0 or second_byte<=255):
                if( third_byte==0 or third_byte<=255 ):
                    if (fourth_byte==0 or fourth_byte<=255):
                        print("Class E IP")
                        subnet(octet,'E')
                        cont()
                    else:
                        print("Invalid 4th octet of Class E IP")
                        cont()
                else:
                    print("Invalid 3rd octet of Class E IP")
                    cont()
            else:
                print("Invalid 2nd octet of Class E IP")
                cont()                         

        else:
                print("Invalid IP")
                cont()
        
    elif option == 2:
                print("Exit")
     

def subnet(octet,clas):
  print("Do you want to Subnet",".".join(octet), " IP  \n" ,"\bPress Y/N to continue subnetting and exit respectively")
  inputchar=input()
  if(inputchar=="Y" or inputchar=="y"):
      print("Enter cidr value")
      cidr=input()
      if(clas=="A"):
          classA(octet,cidr)
      elif(clas=="B"):  
          classB(octet,cidr)
      elif(clas=="C"):
          classC(octet,cidr)
      elif(clas=="D"):
          classD(octet,cidr)
      elif(clas=="E"):
          classE(octet,cidr)
      else:
          print("Under Construction")
  elif(inputchar=="N" or inputchar=="n"):
       sys.exit()

def classA(octet,cidr):
    if(int(cidr)<8 or int(cidr)>=33):
        print("Invalid CIDR for class A IP, Class a CIDR value must be 8<cidr<=32")
    else:       
        (first_byte,second_byte,third_byte,fourth_byte)=(int(octet[0]),0,0,0)
        extracidr=int(cidr)-8
        Networknumber=math.pow(2,extracidr)
        Validipnumber=math.pow(2,24-int(cidr))-2
        print("No. of Networks",Networknumber)
        print("No of valid host per Network",Validipnumber)
        fsm=255 #fistsubnetmask aka fsm
        ssm=0
        tsm=0
        lsm=0
        blocksize=0
        if(fsm==255 and int(cidr)>8):
            n=7 #defining no. bits to obtain the subnet mask e.g if 1 bit is on that means 255.10000000.0.0 we can 2power7 and if 2 bit is on  we can do 2power7+2power6 and soon
        
            if not (ssm==255):
                for bits in range(0,extracidr):
                    if True:
                        ssm=ssm+int(math.pow(2,n-bits))

                if(ssm==255 and int(cidr)>16):
                    for bits in range(0,extracidr-8):
                        if True:
                            tsm=tsm+int(math.pow(2,n-bits))
                if(tsm==255 and int(cidr)>24):
                    for bits in range(0,extracidr-16):
                        if True:
                            lsm=lsm+int(math.pow(2,n-bits))
           

        print("New Subnet mask is ",fsm,"\b.",ssm,"\b.",tsm,"\b.",lsm)
        #if int(cidr) in range(9,17): logic of finding blocksize
        #    if(ssm>=0 and ssm<=255 and tsm==0):
        #        blocksize=256-ssm
        #elif int(cidr) in range(17,25):
        #    if(tsm>0 and tsm<=255 and lsm==0):
        #        blocksize=256-tsm
        #elif int(cidr) in range(25,33):
        #    if(lsm>0 and lsm<=255):
        #        blocksize=256-tsm
     
    #print("Blocksize of the Network is ",blocksize)
    print("-"*50)
    print("Network Id \t Valid IPs \t Broadcast Id")
    print("-"*50)
    if int(cidr) in range(9,17):
        if(ssm>=0 and ssm<=255 and tsm==0):
            blocksize=256-ssm
            print("Blocksize of the Network is ",blocksize)
            while not (second_byte==256):
                    print(first_byte,".",second_byte,".",third_byte,".",fourth_byte, end="")
                    print("\t",first_byte,".",second_byte,".",third_byte,".",fourth_byte+1, end="  ------")
                    second_byte+=int(blocksize)
                    print("\t",first_byte,".",second_byte-1,".",third_byte+255,".",fourth_byte+255-1, end="")
                    print("\t",first_byte,".",second_byte-1,".",third_byte+255,".",fourth_byte+255)

    elif int(cidr) in range(17,25):
        if(tsm>0 and tsm<=255 and lsm==0):
            blocksize=256-tsm
            print("Blocksize of the Network is ",blocksize)
            while not (third_byte==256):
                    print(first_byte,".",second_byte,".",third_byte,".",fourth_byte, end="")
                    print("\t",first_byte,".",second_byte,".",third_byte,".",fourth_byte+1, end="  ------")
                    third_byte=third_byte+int(blocksize)
                    print("\t",first_byte,".",second_byte,".",third_byte-1,".",fourth_byte+255-1, end="")
                    print("\t",first_byte,".",second_byte,".",third_byte-1,".",fourth_byte+255)
                    
                    
    elif int(cidr) in range(25,33):
        if(lsm>0 and lsm<=255):
            blocksize=256-tsm
            print("Blocksize of the Network is ",blocksize)
            while not (second_byte==256):
                    print(first_byte,".",second_byte,".",third_byte,".",fourth_byte, end="")
                    print("\t",first_byte,".",second_byte,".",third_byte,".",fourth_byte+1, end="  ------")
                    fourth_byte+=int(blocksize)
                    print("\t",first_byte,".",second_byte,".",third_byte-1,".",fourth_byte-2, end="")
                    print("\t",first_byte,".",second_byte,".",third_byte,".",fourth_byte-1)
                

        
        
switch()