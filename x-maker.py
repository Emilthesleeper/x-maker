word="emilio eine nervensäge"

length=100
pos=0

while length/2>=pos:
    str_=""
    str_2=""
    for j in range(pos):str_=str_+" "
    for j in range(int(length-pos*2)):str_2=str_2+" "
    print(str_+word+str_2+word)
    pos+=1

while length>=pos :
    str_=""
    str_2=""
    for j in range(length-pos):str_=str_+" "
    num=length-int(length-pos*2)-length
    for j in range(num):str_2=str_2+" "
    #print(str(num)+str_+word+str_2+word)
    print(str_+word+str_2+word)
    pos+=1