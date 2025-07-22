distance =  int(input ("ระยะทาง : "))
price = 0
if (distance > 500 ) :
    price = 45  
elif (distance > 301) :
    price = 35 
elif (distance > 101) :
    price = 25  
elif (distance > 51) :
    price = 15 
elif (distance > 5) :
    price = 10 
else :
    price = 0
vat = price * 7/100
print( "ระยะทาง : " , distance , "km" , "ราคา : " , price , "บาท" , "ภาษี" , vat , "บาท" , "ราคารวมvat" , (price + vat ) , "บาท" )
   


