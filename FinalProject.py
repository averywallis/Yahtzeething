"""
FinalProject.py
Author: Avery Wallis
Sources: Hayden Hatfield,
Marcelo Almaguer for the Chell character model used in his own version of Portal called "Remember the Game"
maxiesnax for the Orange Portal Image:0 "http://orig05.deviantart.net/58ec/f/2012/361/2/5/portal___orange_portal_by_maxiesnax-d5pcfmj.png"
Blue Portal Image "http://vignette4.wikia.nocookie.net/kirby-bulborb/images/1/12/Blue_Portal.png/revision/latest?cb=20151004085207"
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, LineAsset
from ggame import ImageAsset, PolygonAsset, Frame

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
noline=LineStyle(0, black)
portalline=LineStyle(1, blue)
portalline2=LineStyle(1, orange)

wall=RectangleAsset(500,500, noline, wall)
blueportal=EllipseAsset(27, 60, noline, blue)
orangeportal=EllipseAsset(27, 60, noline, orange)
innerportal=EllipseAsset(24, 57, noline, white)
exit=CircleAsset(70, thinline, plat)
exit2=CircleAsset(20, thinline, plat)
plat=RectangleAsset(250, 50, noline, plat)
doorline=LineAsset(0, 120, thinline)
goo=PolygonAsset([(0,500),(800,500),(800,600,),(0,600)],noline,gooy)

class Chell(Sprite):
    asset = ImageAsset("images/Chell1.png")
    assetflip = ImageAsset("images/Chell2.png")
    def __init__(self, position):
        super().__init__(Chell.asset, position)
        self.visible = True
        self.x = 250
        self.y = 250
        self.click = 0
        self.mright = 0
        self.mleft = 0
        self.alt = 0
        self.image = 0
        self.scale = .25
        self.op = 0
        PortalGame.listenKeyEvent("keydown", "d", self.rightOn)
        PortalGame.listenKeyEvent("keyup", "d", self.rightOff)
        PortalGame.listenKeyEvent("keydown", "a", self.leftOn)
        PortalGame.listenKeyEvent("keyup", "a", self.leftOff)
        PortalGame.listenMouseEvent("click", self.ClickOn)
        PortalGame.listenKeyEvent("keydown", "alt", self.altOn)
        PortalGame.listenKeyEvent("keyup", "alt", self.altOff)
        self.oportal = None
        self.bportal = None
        
    def step(self):
        if self.click == 1 and self.alt != 1:
            if self.oportal:
                self.oportal.destroy()
                self.oportal = OrangePortal((self.cox-60,self.coy-70))
                self.click = 0
            else:
                self.oportal = OrangePortal((self.cox-60,self.coy-70))
                self.oportal
                self.click = 0
                
        if self.click == 1 and self.alt == 1:
            if self.bportal:
                self.bportal.destroy()
                self.bportal = BluePortal((self.cox-60,self.coy-70))
                self.click = 0
            else:
                self.bportal = BluePortal((self.cox-60,self.coy-70))
                self.bportal
                self.click = 0
    
        if self.mright == 1:
            self.setImage(Chell.asset)
            self.x += .75
            self.y = self.y
        if self.mright == 0:
            self.x =self.x
            self.y=self.y
        if self.mleft == 1:
            self.image = Chell.assetflip
            self.x += -.75
            self.y = self.y
        if self.mleft == 0:
            self.x = self.x
            self.y = self.y
            
    def ClickOn(self,event):
        self.click = 1
        self.cox = event.x
        self.coy = event.y
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
    asset = ImageAsset("images/Blue_Portal.png")
    def __init__(self, position):
        super().__init__(BluePortal.asset, position)
        self.scale = .25
        self.center = (0,0)
        
    def step(self):
        self.x = self.x
        self.y = self.y
        
class OrangePortal(Sprite):
    asset = ImageAsset("images/portal___orange_portal_by_maxiesnax-d5pcfmj.png")
    def __init__(self, position):
        super().__init__(OrangePortal.asset, position)
        self.scale = .25
        self.center = (0,0)
        
    def step(self):
        self.x = self.x
        self.y = self.y
        
class PortalGame(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        Sprite(wall, (400,20))
        Sprite(wall, (100,20))
        Sprite(exit, (800,100))
        Sprite(exit2, (800, 100))
        Sprite(doorline, (800, 30))
        Sprite(plat, (100,400))
        Sprite(plat, (650, 150))
        Sprite(goo, (100,0))
        Chell((0,0))
        
    def step(self):
        for chell in self.getSpritesbyClass(Chell):
            chell.step()
            
myapp = PortalGame(1000,750)
myapp.run()