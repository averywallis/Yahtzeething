"""
FinalProject.py
Author: Avery Wallis
Sources: Hayden Hatfield, Mr. Donnelly, 
Marcelo Almaguer for the Chell character model used in his own version of Portal called "Remember the Game"
maxiesnax for the Orange Portal Image:0 "http://orig05.deviantart.net/58ec/f/2012/361/2/5/portal___orange_portal_by_maxiesnax-d5pcfmj.png"
Blue Portal Image "http://vignette4.wikia.nocookie.net/kirby-bulborb/images/1/12/Blue_Portal.png/revision/latest?cb=20151004085207"
Special thanks to Valve for creating such an awesome game. Hopefully you can count to three.
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, LineAsset
from ggame import ImageAsset, PolygonAsset, Frame, Sound, SoundAsset, TextAsset

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
orange = Color(0xffa500, 1.0)
skin =Color(0xFCD15B, 1.0)
wall=Color(0xE8E8E8, 1.0)
orange=Color(0xFFa500,1.0)
plat=Color(0xB9BDBB,1.0)
gooy=Color(0xCDF238,1.0)
white=Color(0xFFFFFF,1.0)
darkblue=Color(0x052099,1.0)

thinline= LineStyle(1, black)
thickline= LineStyle(5, black)
thickishline= LineStyle(2.5, black)
noline= LineStyle(0, black)
portalline= LineStyle(1, blue)
portalline2= LineStyle(1, orange)

wall=RectangleAsset(1000,750, noline, wall)
exitbig=CircleAsset(70, thinline, plat)
exitsmall=CircleAsset(20, thinline, plat)
plat=RectangleAsset(250, 50, noline, plat)
doorline=LineAsset(0, 120, thinline)
goo=RectangleAsset(1000,100,noline,gooy)

cpx = 0
cpy = 0
cox = -100
coy = -100
cbx = -100
cby = -100

class Chell(Sprite):
    asset = ImageAsset("images/ChellSpriteSheet.png", Frame(0,0,205,361), 2, 'horizontal')
    def __init__(self, position):
        super().__init__(Chell.asset, position)
        self.visible = True
        self.x = 0
        self.y = 410
        self.vx = 0
        self.vy = 0
        self.jump1 = 0
        self.thing = 0
        self.click = 0
        self.mright = 0
        self.mleft = 0
        self.alt = 0
        self.image = 0
        self.scale = .25
        self.op = 0
        self.reset = 0
        PortalGame.listenKeyEvent("keydown", "d", self.rightOn)
        PortalGame.listenKeyEvent("keyup", "d", self.rightOff)
        PortalGame.listenKeyEvent("keydown", "a", self.leftOn)
        PortalGame.listenKeyEvent("keyup", "a", self.leftOff)
        PortalGame.listenMouseEvent("click", self.ClickOn)
        PortalGame.listenKeyEvent("keydown", "alt", self.altOn)
        PortalGame.listenKeyEvent("keyup", "alt", self.altOff)
        PortalGame.listenKeyEvent("keydown","r", self.resetOn)
        PortalGame.listenKeyEvent("keyup", "r", self.resetOff)
        PortalGame.listenKeyEvent("keydown", "space", self.jumpOn)
        PortalGame.listenKeyEvent("keyup", "space", self.jumpOff)

        
    def step(self):
        if self.click == 1 and self.alt != 1:
            global cox
            cox = cpx
            global coy
            coy = cpy
            self.click = 0
                
        if self.click == 1 and self.alt == 1:
            global cbx
            cbx = cpx
            global cby
            cby = cpy
            self.click = 0
        
        # player and orange portal detection
        if self.x<= cox-20 and self.x>=cox-30 and self.y <= coy-10 and self.y >= coy-40 and cby>=0 and cbx>=0:
            self.x = cbx - 10
            self.y = cby - 40
        
        # player and blue portal detection    
        if self.x<=cbx-20 and self.x>=cbx-30 and self.y <= cby-10 and self.y >= cby-40 and coy>=0 and cox>=0:
            self.x = cox - 10
            self.y = coy - 40
        
        # move right and left
        if self.mright == 1:
            self.setImage(0)
            self.x += 1
            self.y = self.y
        if self.mright == 0:
            self.x =self.x
            self.y=self.y
        if self.mleft == 1:
            self.setImage(1)
            self.x += -1
            self.y = self.y
        if self.mleft == 0:
            self.x = self.x
            self.y = self.y
            
        # basic jump
        self.vy += .001
        self.y += self.vy
        if self.jump1 == 1:
            if self.thing == 1 and self.jump1 == 1:
                self.vy += .001
                self.y += self.vy
                if self.y >= self.thing2:
                    self.vy = 0
                    self.y = self.y
            else:
                self.thing2 = self.y
                self.thing = 1
                self.vy = -10
            
            
        # borders    
        if self.y >= 560:
            self.x = 100
            self.y = 410
        if self.x <0:
            self.x = 0
        if self.x > 947:
            self.x = 947
        
        # reset
        if self.reset == 1:
            self.x = 0
            self.y = 410
            global cox
            cox = -100
            global coy
            coy = -100
            global cbx
            cbx = -100
            global cby
            cby = -100
            self.reset = 0

    def ClickOn(self,event):
        self.click = 1
        global cpx 
        cpx = event.x
        global cpy
        cpy = event.y
    def jumpOn(self,event):
        self.jump1 = 1
    def jumpOff(self,event):
        self.jump1 = 0
    def resetOn(self,event):
        self.reset = 1
    def resetOff(self,event):
        self.reset = 0
    def rightOn(self,event):
        self.mright = 1
    def rightOff(self,event):
        self.mright = 0
    def leftOn(self,event):
        self.mleft = 1
    def leftOff(self,event):
        self.mleft = 0
    def altOn(self,event):
        self.alt = 1
    def altOff(self,event):
        self.alt = 0

class BluePortal(Sprite):
    asset = ImageAsset("images/Blue_Portal.png", Frame(25,10,350,475), 1, 'vertical')
    def __init__(self, position):
        super().__init__(BluePortal.asset, position)
        self.scale = .25
        self.center = (0,0)

        
    def step(self):
        self.x = cbx - 50
        self.y = cby - 60
        
class OrangePortal(Sprite):
    asset = ImageAsset("images/portal___orange_portal_by_maxiesnax-d5pcfmj.png", Frame(25,10,350,475), 1, 'vertical')
    def __init__(self, position):
        super().__init__(OrangePortal.asset, position)
        self.scale = .25
        self.center = (0,0)

        
    def step(self):
        self.x = cox - 50
        self.y = coy - 60
        
class PortalGame(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        txt_asset= TextAsset(text="A to Move Left, D to Move Right", width=200, align='center',style='10px Arial', fill=Color(0xff2222,1))
        txt_asset1= TextAsset(text="Left Click to Place Orange Portal", width=200, align='center',style='10px Arial', fill=Color(0xff2222,1))
        txt_asset2= TextAsset(text="Alt + Left Click to Place Blue Portal", width=200, align='center',style='10px Arial', fill=Color(0xff2222,1))
        resettxt= TextAsset(text="Press R to reset", width=200, align='center',style='10px Arial', fill=Color(0xff2222,1))
        Sprite(wall, (0,0))
        Sprite(goo, (0,650))
        Sprite(exitbig, (800,100))
        Sprite(exitsmall, (800, 100))
        Sprite(doorline, (800, 30))
        Sprite(plat, (0,500))
        Sprite(plat, (650, 150))
        Sprite(goo, (0,650))
        Sprite(txt_asset,(0,0))
        Sprite(txt_asset1, (0,10))
        Sprite(txt_asset2, (0,20))
        Sprite(resettxt,(0,30))
        BluePortal((0,0))
        OrangePortal((0,0))
        Chell((0,0))
        
    def step(self):
        for chell in self.getSpritesbyClass(Chell):
            chell.step()
        for blueportal in self.getSpritesbyClass(BluePortal):
            blueportal.step()
        for orangeportal in self.getSpritesbyClass(OrangePortal):
            orangeportal.step()
    
            
myapp = PortalGame(1000,750)
myapp.run()