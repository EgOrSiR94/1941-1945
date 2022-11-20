x = 10
y = 10
def setup():
    size(600,400)
    strokeWeight(1)
def draw():
    global x,y
    strokeWeight(x)
    line(200,300,250,100)
    line(300,300,250,100)
    line(200,300,300,200)
    line(300,300,200,200)
    line(200,200,300,200)
    x +=1
    
