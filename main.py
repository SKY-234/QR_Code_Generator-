import qrcode


#we have to take  UPI id as input
upi_id=input("Enter the UPI ID")

#upi://pay?pa=UPI_ID&pn=NAME&am=AMOUNT&cu=CURRENCEY&tn=MESSAGE

#First we should define payment URL based on the UPI ID and PAyment APP
#we can modify the PAyment APP

PHONE_PAY_URL=f'upi://pay?pa={upi_id}&pn=recipient%20NAme&mc=1234'

PATYM_URL=f'upi://pay?pa={upi_id}&pn=recipient%20NAme&mc=1234'

GOOGLE_PAY_URL=f'upi://pay?pa={upi_id}&pn=recipient%20NAme&mc=1234'

#create qr codes 
PHONE_PAY_qr=qrcode.make(PHONE_PAY_URL)
PATYM_qr=qrcode.make(PATYM_URL)
GOOGLE_PAY_qr=qrcode.make(GOOGLE_PAY_URL)

#SAVING IMAGE OF QRCODE 

PHONE_PAY_qr.save('PHONE_PAY_qr.png')
PATYM_qr.save('PATYM_qr.png')
GOOGLE_PAY_qr.save('GOOGLE_PAY_qr.png')

# now we want to dispaly our qr code 
#we should install pillow lib

PHONE_PAY_qr.show()
#PATYM_qr.show()
#GOOGLE_PAY_qr.Show()
 