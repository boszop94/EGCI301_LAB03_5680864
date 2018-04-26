import cv2
import numpy as np
x = 150
y = 200

def circle(x,y):
    cv2.circle(img,(x,y),15,(0,0,0),-1)

status = 'false'
inRange = 'fasle'


k = 0

while k!=27:
    img = cv2.imread('close.jpg',1)
    circle(x,y)    
    cv2.imshow('image',img)
    print("x : " , x , " y : " , y)
    print("status : ",status)
    print("inRange: ",inRange)
    if( x>670 and x<775 and y>250 and y<380):
        inRange = 'true'
    else:
        inRange = 'false'

    if(x>366 and x<=730 and y>222 and y<407):
        status = 'true'
    else:
        status = 'false'

    if(inRange == 'false'):
        img = cv2.imread('close.jpg',1)
        circle(x,y)
        cv2.imshow('image',img)
    elif(inRange == 'true'):
        img = cv2.imread('open.jpg',1);
        circle(x,y)
        cv2.imshow('image',img)

    k = cv2.waitKey(0)

    if(status == 'false'):
        if (k==ord('w')):
            if((x>310 and y<455 and y>165 and x<760) or (x>0 and x<1130 and y<=0) or (x>703 and x<760 and y>165 and y<300)):
                y=y
            else:
                y-=20
                if((x>310 and x<760 and y>165 and y<455) or (x>0 and x<1130 and y<=0) or (x>703 and x<760 and y>165 and y<300)):
                    y+=20
        if (k==ord('s')):
            if((x>310 and y>165 and y<455 and x<760) or (x>0 and x<1130 and y>620) or (x>703 and x<760 and y>350 and y<455)):
                y=y
            else:
                y+=20
                if((x>310 and x<760 and y>165 and y<455) or (x>0 and x<1130 and y>620) or (x>703 and x<760 and y>350 and y<455)):
                    y-=20
        if (k==ord('d')):
            if((y>165 and y<455 and x>310 and x<=730) or (x>1120 and y>0 and y<620)):
                x=x
            else:
                x+=20 
                if((x>310 and x<760 and y>165 and y<455) or (y>0 and y<645 and x>1120)):
                    x-=20
        if (k==ord('a')):
            if((y<455 and y>360 and x<760 and x>703) or (y>160 and y<277 and x<760 and x>703) or (y>0 and x<30 and y<645)):
                x=x
            else:
                x-=20
                if((y>0 and y<645 and x<30) or (y>360 and y<455 and x<760 and x>730) or (y>160 and y<277 and x<760 and x>703)):
                    x+=20

    if(status == 'true'):
        if (k==ord('w')):
                    # inside reg                          boarder
            if((x>495 and y<355 and y>284 and x<585) or ( y<222 and x>366 and x<703) or (x>703 and x<760 and y>165 and y<300)):
                y=y
            else:
                y-=20
                if((x>366 and x<703 and y<222) or ( x>495 and y<355 and x<585 and y>284) or (x>703 and x<760 and y>165 and y<300)):
                    y+=20
        if (k==ord('s')):
            if((x>495 and y>284 and y<355 and x<585) or ( y>407 and x>366 and x<703) or (x>703 and x<760 and y>350 and y<455)):
                y=y
            else:
                y+=20
                    #   boarder                           reg
                if((x<703 and x>366 and y>407) or ( x>495 and y>284 and x<585 and y<355 ) or (x>703 and x<760 and y>350 and y<455)):
                    y-=20

        if (k==ord('a')):
            if((x>495 and y>284 and y<355 and x<585) or ( y>222 and x<366 and y<407)):
                x=x
            else:
                x-=20
                    #  boarder                           reg
                if((x<366 and y>222 and y<407) or ( y>284 and y<355 and x<585 and x > 495)):
                    x+=20
        if(k==ord('d')):
            if((x>495 and y>284 and y<355 and x<585) or (y<277 and y>222 and x>703) or (x>703 and y>360 and y<407)):
                x=x
            else:
                x+=20
                if((x>703 and y>222 and y<277) or ( y>284 and y<355 and x>495 and x<585) or (x>703 and y>360 and y<407)):
                    x-=20

    
