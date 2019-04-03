add_library('pdf')

def setup():
    global i
    global o
    global k
    global nazwa
    global nazwa1
    global nazwa2
    global ext
    nazwa = "paszportowe"
    nazwa1 = "okularyps.png"
    nazwa2 = "kokardka.png"
    ext = ".jpg"
    i = loadImage(nazwa+ext)
    o = loadImage(nazwa1)
    k = loadImage(nazwa2)
    beginRecord(PDF, "mojPDFinny.pdf")
    size(413, 531)
    print(type(i))
    imageMode(CENTER)
    
def draw():
    global i
    global o
    global k
    global nazwa
    global nazwa1
    global nazwa2
    global ext
    image(i, width/2, height/2, width, height)
    if keyPressed:
        if key == "O" or key == "o":
            image(o, (width/2)-5, height/2, (width/2)+40, (height/2)-140)
    if keyPressed:
        if key == "R" or key == "r":
            image(o, (width/2)-5, height/2, (width/2)+40, (height/2)-140)
            image(k, (width/2)+80, (height/2)-100, width/2, height/2)
    if keyPressed:
        if key == "K" or key == "k":
            image(k, (width/2)+80, (height/2)-100, width/2, height/2)
    endRecord()
    
