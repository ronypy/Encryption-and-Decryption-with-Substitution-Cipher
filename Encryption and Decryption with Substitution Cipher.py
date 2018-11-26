import re
import math
import numpy as np

################### Encryption function #################################

def encryption():    
    name = input("Please enter plaintext:")  # Here, user will input plaintext to encrypt.
    #print (name)
    ss7 = re.sub('[^a-zA-Z]+', '', name)   # remove any character other than a-z/A-Z from user input
    #print (ss7)
    ee1=len (ss7)   # length of trimmed plaintext
    #print (ee1)
    ppp= [ord(ppp) for ppp in ss7]  # ppp is a list with charracter's ASCII value
    #print ("%s" % ppp)
    n = int(input("Please enter a number n between 3 to 5: ")) # Here, user will input any number n in between 3 to 5
    a= [(a+n)%26 for a in ppp] # Here ascii values got substituted by (p+n) mod 26 
    #print(a)
    b = len(a)  # length of resulting ciphertext after substituted by (p+n) mod 26
    c= math.ceil(b/16)  # number of rows
    p=np.zeros( (c,16) )
    p1=np.zeros( (c,16) )
    d= c*16 - b # number of required padding 
    i=0
    j=0
    l=0
    m=16-d # d is number of padding. so, m is the number of column, upto which, in last row input will be from ciphertext. after m column, rest column will be padded with "x" in last row.
    k=0
    k=len(a)
    s =c-1
    ss=ord("x") # ASCII conversion of padding "x"
    # This part will work to create ciphertext matrix if the user input is less than or equal 16 character
    while b<=16:
        while i<m:
            p[0,i]=a[(b-k)] # p is getting filled by list element befor m column. 
            k-=1
            i+=1
            while (i>=m and i<=15):
                p[0,i]=ss # rest of p is getting filled by padding"x"
                i+=1
        break
    if b<=16:
        p1= [(p1+1)%26 for p1 in p] # adding row number then performing mod by 26
    #print(p1)
# This part will work to create ciphertext matrix if the user input is greater than 16 character
    while b>16:
        while j<m:  # for columns, less than m
            i=0
            while i<s: # for rows, less than s
                p[i,j]=a[(b-k)] # 2-dimensional p matrix will get filled by data of a
                k-=1
                i+=1
                while i == s: # for last row
                    p[i,j]=a[(b-k)] # last row data will get filled by data of a
                    k-=1
                    i+=1
                    j+=1
                    while j>=(m): # for columns greater than or equal m 
                        while k>0:
                            while l<(b-1): 
                                p[l,j]=a[(b-k)]  # except last row, other rows where column is greater than m will be filled by data from a
                                l+=1
                                k-=1
                                while l==(c-1): # in last row, after m column, it will get filled by padding "x"
                                    p[l,j]=ss
                                    j+=1    
                                    l=l-(c-1)
                                break
                        break    
        break
    t=0
    q=0
    #print(p)
    if b>16: 
        while t<=(c-1):
            t+=1
            #print(t)
            q=0
            while q<=15:
                p1[(t-1),q]=(p[(t-1),q]+t)%26  # adding respective row number then performing mod by 26
                q+=1
                
    #print(p1)
    p2=np.reshape(p1,(1, -1))  #.reshape(1, -1) basically means "reshape to 1 row and as many columns as necessary (-1)". it is needed to do concatenation.
    #print(p2)
    a2=sum(p2) # need to convert 2 dimensional matrix to 1 dimentional
    #print(a2)
    a3=[int(i) for i in a2]
    #print(a3)
    a4=[(a4+65) for a4 in a3] 
    # After performing step 2 of assignment, all numbers are less than 26 for modulas.
    # If I convert it back to ASCII value it does not give any english character. 
    # since all english capital letters ASCII value are within 65-90. And modulus value is within 0 to 25. 
    # So, to show ciphertext as english letter, I added 65 with every element of a3.
    # It will get subtracted in Decryption part at first.
    q2=[chr(q2) for q2 in a4]
    q3=str(q2)
    ss3 = re.sub('[^a-zA-Z]+', '', q3)
    print("Ciphertext is:", end="")
    print ("%s" % ss3) # printing Ciphertext
    
    #### End of Encryption part#####




############# Decryption function ######################################################################
def decryption():
    name = input("Please enter cipher text:") # Here user will input ciphertext
    #print (name)
    ss7 = re.sub('[^a-zA-Z]+', '', name)
    #print (ss7)
    ppp= [ord(ppp) for ppp in ss7] # convert it to ASCII value
    #print ("%s" % ppp)
    a4=[(a4-65) for a4 in ppp] # subtracting 65 which was added in last stage of encryption to show ciphertext as english letter
    #print(a4)
    w = int(input("Enter padding count: "))# input of padding
    b=len(a4)
    i=0
    j=0
    #started from here for length >16
    h=0
    m=0
    c= math.ceil(b/16) # number of rows
    a12=np.zeros( (c,16) )
    a13=np.zeros( (1,(b-w)) )
    a5=[]
    a6=[]
    a7=[]
    a8=[]
    a9=[]
    a10=[]
    a11=[]
    a14=[]
    #This part will work when ciphertext is 16 character
    while b<=16:
        for i in range(0,(b-w)):
            a5.append(a4[i]) # except padding, every element of list will be appended on a5
        a5=[(a5-1)%26 for a5 in a5] # subtracting row number, then performing modulas
        break
    #print(a5)
    i=0
    j=0

    #This part will work when ciphertext length is more than 16
    while b>16 and h<c:
        for m in range(0,b): # for ciphertext length
            for h in range(0,c): # for rows less than c
                for i in range(0,16): # for columns less than c
                    a12[h,i]=a4[m]  # data of a4 will be distributed in rows and column of a12. breaking of concatenation from encryption part 
                    m+=1
            break    
        break
    
    i=0
    j=0
    h=0
    m=0
    n=0
    #print(a12)
    for h in range(0,c):
        a12[h,]=(a12[h,]-(h+1))%26 # subtracting row number and performing mod
    #print(a12)
    while b>16: 
        for j in range(0,(16-w)): # column before padding
            for i in range(0,c): # all rows
                a13[0,m]=a12[i,j] # doing matrix element re-shuffle to undo matrix performance during encryption 
                m+=1
        break
    while b>16:    # padding elements are discarded here.
        for j in range((16-w),16): # column after padding
            for i in range(0,(c-1)): # all row except last row
                a13[0,m]=a12[i,j] # doing matrix element re-shuffle to undo matrix performance during encryption 
                m+=1 
        break
    i=0
    j=0

    #print(a13)
    while b>16:
        a14=sum(a13) # converting 2 dimentional matrix into 1 dimensional matrix
        #print(a14)
        a5=[int(i) for i in a14]
        break
    #print(a5)
# FOR N=3 VALUE CONSIDERED & OUTPUT IS CAPITAL LETTER.
#Ascii code range for capital letter is 65-90. when value of a5[j] is less than 15. a6=26*3+{0 to 15 anyone}-3{value of n}=90(max)/75(min);it falls within capital letter group  
    while j<(b-w):
        if a5[j]<=15:
            a6.append(26*3+a5[j]-3)
            j+=1
#For value greater than 15, 26 need to multiply with 2 otherwise the product will be in the range of small letter. But, I considered plaintext will not be a mix of capital and small letter. 
        else:
            a6.append(26*2+a5[j]-3)
            j+=1
    #print(a6)
    j=0
#for n=3 value considered & output small letter
##Ascii code range for small letter is 97-122. when value of a5[j] is less than 21. a6=26*4+{0 to 21 anyone}-3{value of n}=101(min)/122(max);it falls within small letter group
    while j<(b-w):
        if a5[j]<=21:
            a7.append(26*4+a5[j]-3)
            j+=1
#For value greater than 21, 26 need to multiply with 3 otherwise the product will be in the range of capital letter. But, I considered plaintext will not be a mix of capital and small letter.
        else:
            a7.append(26*3+a5[j]-3)
            j+=1
    #print(a7)
    j=0
# FOR N=4 VALUE CONSIDERED & OUTPUT IS CAPITAL LETTER.
    while j<(b-w):
        if a5[j]<=16:
            a8.append(26*3+a5[j]-4)
            j+=1
        else:
            a8.append(26*2+a5[j]-4)
            j+=1
    #print(a8)
    j=0
#for n=4 value considered & output small letter
    while j<(b-w):
        if a5[j]<=22:
            a9.append(26*4+a5[j]-4)
            j+=1
        else:
            a9.append(26*3+a5[j]-4)
            j+=1
    #print(a9)
    j=0
# FOR N=5 VALUE CONSIDERED & OUTPUT IS CAPITAL LETTER.
    while j<(b-w):
        if a5[j]<=17:
            a10.append(26*3+a5[j]-5)
            j+=1
        else:
            a10.append(26*2+a5[j]-5)
            j+=1
    #print(a10)
    j=0
#for n=5 value considered & output small letter
    while j<(b-w):
        if a5[j]<=23:
            a11.append(26*4+a5[j]-5)
            j+=1
        else:
            a11.append(26*3+a5[j]-5)
            j+=1
    #print(a11)
    j=0

#converting list elements as char type
    c2=[chr(c2) for c2 in a6]
    c3=[chr(c3) for c3 in a7]
    c4=[chr(c4) for c4 in a8]
    c5=[chr(c5) for c5 in a9]
    c6=[chr(c6) for c6 in a10]
    c7=[chr(c7) for c7 in a11]

    q2=str(c2)
    q3=str(c3)
    q4=str(c4)
    q5=str(c5)
    q6=str(c6)
    q7=str(c7)

    #print ("%s" % q2)
    #print ("%s" % q3)
    #print ("%s" % q4)
    #print ("%s" % q5)
    #print ("%s" % q6)
    #print ("%s" % q7)
# trimming
    ss2 = re.sub('[^a-zA-Z]+', '', q2)
    ss3 = re.sub('[^a-zA-Z]+', '', q3)
    ss4 = re.sub('[^a-zA-Z]+', '', q4)
    ss5 = re.sub('[^a-zA-Z]+', '', q5)
    ss6 = re.sub('[^a-zA-Z]+', '', q6)
    ss7 = re.sub('[^a-zA-Z]+', '', q7)
    print("PLAINTEXT OUTPUT FOR n=3 & CAPITAL LETTER:", end=" ")  
    print(ss2)   #PLAINTEXT OUTPUT FOR n=3 & CAPITAL LETTER
    print("plaintext output for n=3 & small letter:", end=" ")  
    print(ss3)   #plaintext output for n=3 & small letter
    print("PLAINTEXT OUTPUT FOR n=4 & CAPITAL LETTER:", end=" ")  
    print(ss4)  #PLAINTEXT OUTPUT FOR n=4 & CAPITAL LETTER
    print("plaintext output for n=4 & small letter:", end=" ")  
    print(ss5)   #plaintext output for n=4 & small letter
    print("PLAINTEXT OUTPUT FOR n=5 & CAPITAL LETTER:", end=" ")  
    print(ss6)   #PLAINTEXT OUTPUT FOR n=5 & CAPITAL LETTER
    print("plaintext output for n=5 & small letter:", end=" ")  
    print(ss7)  #plaintext output for n=5 & small letter


## calling encryption and decryption function##
encryption()
decryption()
