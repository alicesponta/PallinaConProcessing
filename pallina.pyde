x=10
y=20
VersY=0
VersX=0
x1=25
x2=0


def setup ():
     size(600,400)
     
x=10
y=20
VerX=1
VerY=1
raggio=50


def setup ():
     size(600,400)
     
     
def draw():
    global x,y,VerX,VerY,raggio,x1
    background(0, 0, 0)
    ellipse (x,y,20,20)
    x=x+(4*VerX)
    y=y+(4*VerY)
    raggio=raggio+(1*VerX)
    ' primo rett'
    if  y<0:
        VerY*=-1
    if y+25>height-25 and x>x1 and x<=x1+80:
        VerY*=-1
    if x>width or x<0:
        VerX*=-1   
    rect(x1,height-25,80,25)
    rect(x2,0,80,25)
   
    
    

    
def keyPressed():
    global x1,x2
    if keyCode == LEFT:
        x1=x1-25
    if x1<=0-25:
        x1=0    
    if keyCode == RIGHT:
        x1=x1+25
    if x1>=width-80:
        x1=800-80
    if keyCode == 65:
        x2=x2-25
    if x2<=0-25:
        x2=0   
    if keyCode == 83:
        x2=x2+25
    if x2>=width-80:
        x2=800-80 
        
