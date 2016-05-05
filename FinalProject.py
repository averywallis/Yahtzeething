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
# colors
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
orange = Color(0xffa500, 1.0)
skin =Color(0xFCD15B, 1.0)
wall=Color(0xE8E8E8, 1.0)
orange=Color(0xFFa500,1.0)
platc=Color(0xB9BDBB,1.0)
gooy=Color(0xCDF238,1.0)
white=Color(0xFFFFFF,1.0)
darkblue=Color(0x052099,1.0)

# lines
thinline= LineStyle(1, black)
thickline= LineStyle(5, black)
thickishline= LineStyle(2.5, black)
noline= LineStyle(0, black)
portalline= LineStyle(1, blue)
portalline2= LineStyle(1, orange)

# assorted environmental sprites
wall=RectangleAsset(1000,750, noline, wall)
exitbig=CircleAsset(70, thinline, platc)
exitsmall=CircleAsset(20, thinline, platc)
plat=RectangleAsset(250, 50, noline, platc)
doorline=LineAsset(0, 120, thinline)
goo=RectangleAsset(1000,100,noline,gooy)

# global variables changed with the classes
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
        self.x = 50
        self.y = 410
        self.vx = 0
        self.vy = 0
        self.jump = 0
        self.click = 0
        self.mright = 0
        self.mleft = 0
        self.alt = 0
        self.image = 0
        self.scale = .25
        self.op = 0
        self.reset = 0
        # all key inputs
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
        # move orange portal
        if self.click == 1 and self.alt != 1:
            global cox
            cox = cpx
            global coy
            coy = cpy
            self.click = 0
        # move blue portal        
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
            
        # win
        if self.collidingWithSprites(WinDoor):
            self.win = YouWinTxt(100,100)
        
        # move right and left
        if self.mright == 1:
            self.setImage(0)
            self.x += 2
            self.y = self.y
        if self.mright == 0:
            self.x =self.x
            self.y=self.y
        if self.mleft == 1:
            self.setImage(1)
            self.x += -2
            self.y = self.y
        if self.mleft == 0:
            self.x = self.x
            self.y = self.y
            
        # constantly moving down for gravity
        self.vy += 6
        self.y += self.vy
        self.vy = 0
        # if collliding with platform, go up to counteract the moving down, effectively staying still
        if self.collidingWithSprites(Platforms):
            self.y -= 6
            self.vy = 0
            # jump
            if self.jump == 1:

                self.vy = -100
                self.jump = 0
        
        # death by goo    
        if self.y >= 560:
            self.x = 50
            self.y = 410
        # borders
        if self.x <0:
            self.x = 0
        if self.x > 947:
            self.x = 947
        
        # reset
        if self.reset == 1:
            self.x = 50
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
            self.setImage(0)

    def ClickOn(self,event):
        self.click = 1
        global cpx 
        cpx = event.x
        global cpy
        cpy = event.y
    def jumpOn(self,event):
        self.jump = 1
    def jumpOff(self,event):
        self.jump = 0
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
    
class Platforms(Sprite):
    platc=Color(0xB9BDBB,1.0)
    plat=RectangleAsset(250, 1, noline, platc)
    def __init__(self, position):
        super().__init__(Platforms.plat, position)

class WinDoor(Sprite):
    exitsmall=CircleAsset(20, thinline, platc)
    def __init__(self, position):
        super().__init__(WinDoor.exitsmall, position)
        self.x = 800
        self.y = 100
        
class YouWin(Sprite):
    youwintxt = TextAsset(text="YOU WIN!!", width=200, align='center',style='10px Arial', fill=Color(0xff2222,1))
    def __init__(self, position):
        super().__init__(YouWin.youwintxt, position)

class PortalGame(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        # defining of text on screen
        movetxt = TextAsset(text="A to Move Left, D to Move Right", width=200, align='center',style='10px Arial', fill=Color(0xff2222,1))
        jumptxt = TextAsset(text="Space to Jump", width=200, align='center',style='10px Arua==ial',fill=Color(0xff2222,1))
        optxt = TextAsset(text="Left Click to Place Orange Portal", width=200, align='center',style='10px Arial', fill=Color(0xff2222,1))
        bptxt = TextAsset(text="Alt + Left Click to Place Blue Portal", width=200, align='center',style='10px Arial', fill=Color(0xff2222,1))
        resettxt = TextAsset(text="Press R to reset", width=200, align='center',style='10px Arial', fill=Color(0xff2222,1))
        #background
        Sprite(wall, (0,0))
        #entrance sprites
        Sprite(exitbig, (75,450))
        Sprite(exitsmall, (75,450))
        Sprite(doorline, (75,380))
        #goo
        Sprite(goo, (0,650))
        # creation of text
        Sprite(movetxt,(0,0))
        Sprite(jumptxt,(0,10))
        Sprite(optxt, (0,20))
        Sprite(bptxt, (0,30))
        Sprite(resettxt,(0,40))
        # exit sprites
        Sprite(exitbig, (800,100))
        # win door
        WinDoor((0,0))
        Sprite(doorline, (800, 30))
        # assorted platforms
        Sprite(plat,(0,500))
        Sprite(plat,(650,150))
        Platforms((0,500))
        Platforms((650,150))
        # portals and Chell
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