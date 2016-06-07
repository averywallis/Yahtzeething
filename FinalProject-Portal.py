"""
FinalProject-Portal.py
Author: Avery Wallis
Sources: Hayden Hatfield, Mr. Dennison
Marcelo Almaguer for the Chell character model used in his own version of Portal called "Remember the Game"
maxiesnax for the Orange Portal Image: "http://orig05.deviantart.net/58ec/f/2012/361/2/5/portal___orange_portal_by_maxiesnax-d5pcfmj.png"
Blue Portal Image "http://vignette4.wikia.nocookie.net/kirby-bulborb/images/1/12/Blue_Portal.png/revision/latest?cb=20151004085207"
Scott Bouloutian for the Companion Cube image: "https://lh4.ggpht.com/afyb1Nyo1suLIWpbtEACIY65SHW2Fjr5g1-KN8ONkA3aNSPd7cJKSeIefsngjSaVjtA=w300"
All sounds are from the game files themselves. I personally own the game, so I don't think this will infringe on any copyrights seeing as I'm not selling this game
Special thanks to Valve for creating such an awesome game. Hopefully you can count to three.
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, LineAsset
from ggame import ImageAsset, PolygonAsset, Frame, Sound, SoundAsset, TextAsset
import time

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
exitempty=CircleAsset(70, thinline, white)
exitsmall=CircleAsset(20, thinline, platc)
plat=RectangleAsset(250, 50, noline, platc)
platsmall=RectangleAsset(250, 25, noline, platc)
doorline=LineAsset(0, 120, thinline)
goo=RectangleAsset(1000,100,noline,gooy)

# global variables changed with the classes
cpx = 0
cpy = 0
cox = -100
coy = -100
cbx = -100
cby = -100
ccx = 0
ccy = 0
hold = 1
holding = 1
win = 0
play = 0


# sounds
bp = Sound(SoundAsset("sounds/portalgun_shoot_blue1.wav"))
op = Sound(SoundAsset("sounds/portalgun_shoot_red1.wav"))
pe = Sound(SoundAsset("sounds/portal_enter_01.wav"))
e1 = Sound(SoundAsset("sounds/00_part1_entry-1.wav"))
e2 = Sound(SoundAsset("sounds/00_part1_entry-2.wav"))
e3 = Sound(SoundAsset("sounds/00_part1_entry-3.wav"))
e4 = Sound(SoundAsset("sounds/00_part1_entry-4.wav"))
e5 = Sound(SoundAsset("sounds/00_part1_entry-5.wav"))
e6 = Sound(SoundAsset("sounds/00_part1_entry-6.wav"))
e7 = Sound(SoundAsset("sounds/00_part1_entry-7.wav"))
cdeath = Sound(SoundAsset("sounds/material_emancipation_01.wav"))
success1 = Sound(SoundAsset("sounds/00_part2_success-1.wav"))
success2 = Sound(SoundAsset("sounds/01_part2_success-1.wav"))
euth = Sound(SoundAsset("sounds/13_part1_euthanized-1.wav"))
# Secret sounds not able to play because Chrome can only take so much
"""
apcpass = Sound(SoundAsset("sounds/apc_alarm_pass1.wav"))
ic = Sound(SoundAsset("sounds/f_innactionisconspiracy_spkr.wav"))
mfoffwr = Sound(SoundAsset("sounds/fprison_missionfailurereminder.wav"))
mh = Sound(SoundAsset("sounds/manhack_alert_pass1.wav"))
toffwr = Sound(SoundAsset("sounds/f_trainstation_offworldrelocation_spkr.wav"))
gman2 = Sound(SoundAsset("sounds/gman_04.wav"))
"""

class Chell(Sprite):
    asset = ImageAsset("images/ChellSpriteSheet.png", Frame(0,0,205,361), 2, 'horizontal')
    def __init__(self, position):
        super().__init__(Chell.asset, position)
        # assorted variables modified during code
        self.visible = True
        self.x = 50
        self.y = 410
        self.vx = 0
        self.vy = 0
        self.jump = 0
        self.hold = 1
        self.click = 0
        self.mright = 0
        self.mleft = 0
        self.alt = 0
        self.image = 0
        self.scale = .25
        self.op = 0
        self.reset = 0
        self.win = 0
        self.g = 0
        self.t1 = 0
        self.c1 = 0
        self.u1 = 0
        self.i1 = 0
        self.m1 = 0
        # all key inputs
        PortalGame.listenKeyEvent("keydown", "d", self.rightOn)
        PortalGame.listenKeyEvent("keyup", "d", self.rightOff)
        PortalGame.listenKeyEvent("keydown", "a", self.leftOn)
        PortalGame.listenKeyEvent("keyup", "a", self.leftOff)
        PortalGame.listenMouseEvent("click", self.ClickOn)
        PortalGame.listenKeyEvent("keydown", "alt", self.altOn)
        PortalGame.listenKeyEvent("keyup", "alt", self.altOff)
        PortalGame.listenKeyEvent("keydown", "space", self.jumpOn)
        PortalGame.listenKeyEvent("keyup", "space", self.jumpOff)
        PortalGame.listenKeyEvent("keydown", "e" , self.holdOn)
        # secret sounds
        """
        PortalGame.listenKeyEvent("keydown","t", self.tOn)
        PortalGame.listenKeyEvent("keyup", "t", self.tOff)
        PortalGame.listenKeyEvent("keydown","c", self.cOn)
        PortalGame.listenKeyEvent("keyup", "c", self.cOff)
        PortalGame.listenKeyEvent("keydown","u", self.uOn)
        PortalGame.listenKeyEvent("keyup", "u", self.uOff)
        PortalGame.listenKeyEvent("keydown","i", self.iOn)
        PortalGame.listenKeyEvent("keyup", "i", self.iOff)
        PortalGame.listenKeyEvent("keydown","m", self.mOn)
        PortalGame.listenKeyEvent("keyup", "m", self.mOff)
        """
        
    def step(self):
        global play
        if play == 1:
            # move orange portal and play sound
            if self.click == 1 and self.alt != 1:
                op.play()
                global cox
                cox = cpx
                global coy
                coy = cpy
                self.click = 0
            # move blue portal and play sound      
            if self.click == 1 and self.alt == 1:
                bp.play()
                global cbx
                cbx = cpx
                global cby
                cby = cpy
                self.click = 0
            
            # hold cube
            if self.collidingWithSprites(CompanionCube) and self.hold == -1:
                global ccx
                ccx = self.x
                global ccy
                ccy = self.y
            
            # player and orange portal detection
            if self.x<= cox-20 and self.x>=cox-30 and self.y <= coy - 20 and self.y >= coy-40 and cby>=0 and cbx>=0 and self.hold != -1:
                self.x = cbx - 10
                self.y = cby - 40
                pe.play()
            # player and blue portal detection    
            elif self.x<=cbx-20 and self.x>=cbx-30 and self.y <= cby - 10 and self.y >= cby-50 and coy>=0 and cox>=0 and self.hold != -1:
                self.x = cox - 10
                self.y = coy - 40
                pe.play()
            # player, orange portal, and holding companion cube detection:
            if self.x<= cox-20 and self.x>=cox-30 and self.y <= coy-10 and self.y >= coy-40 and cby>=0 and cbx>=0 and self.collidingWithSprites(CompanionCube) and self.hold == -1:
                self.x = cbx - 10
                self.y = cby - 40
                global holding
                holding = -1
                global ccx
                ccx = self.x
                global ccy
                ccy = self.y
                pe.play()
            # player, blue portal, and holding companion cube detection:    
            elif self.x<=cbx-20 and self.x>=cbx-30 and self.y <= cby-10 and self.y >= cby-40 and coy>=0 and cox>=0 and self.collidingWithSprites(CompanionCube) and self.hold == -1:
                self.x = cox - 10
                self.y = coy - 40
                global holding
                holding = -1
                global ccx
                ccx = self.x
                global ccy
                ccy = self.y
                pe.play()
            else:
                global holding
                holding = 0
                
            # win
            global win
            self.wining = win
            if self.collidingWithSprites(ExitDoor) and self.win == 0 and self.wining == 1:
                self.wintxt = YouWin((250,200))
                # self.secretstxt = Secrets((280,290))
                self.win = 1
                success2.play()
            
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
                
            # if collliding with platform, go up to counteract the moving down, effectively staying still    
            if self.collidingWithSprites(Platforms):
                self.vy -= .1
                self.y += self.vy
                self.vy = 0
                # jump
                if self.jump == 1:
                    self.vy = -3
            # constantly moving down for gravity if not colliding with platform
            else:    
                self.vy += .1
                self.y += self.vy
                
            # death by goo    
            if self.y >= 560:
                self.x = 50
                self.y = 410
                self.vy =0
                global cox
                cox = -100
                global coy
                coy = -100
                global cbx
                cbx = -100
                global cby
                cby = -100
            # borders
            if self.x <0:
                self.x = 0
            if self.x > 947:
                self.x = 947
            
            """    
            # play secret sounds
            # citizen notice, failure to cooperate will result in permanent off world relocation
            if self.t1 == 1:
                toffwr.play()
            # apc pass    
            if self.c1 == 1:
                apcpass.play()
            # mission failure will result in permanent off world assignment
            if self.u1 == 1:
                mfoffwr.play()
            # innaction is conspiracy
            if self.i1 == 1:
                ic.play()
            # manhack pass
            if self.m1 == 1:
                mh.play()
            
    # secret key input stuff
    def tOn(self,event):
        self.t1 = 1
    def tOff(self,event):
        self.t1 = 0
    def cOn(self,event):
        self.c1 = 1
    def cOff(self,event):
        self.c1 = 0
    def uOn(self,event):
        self.u1 = 1
    def uOff(self,event):
        self.u1 = 0
    def iOn(self,event):
        self.i1 = 1
    def iOff(self,event):
        self.i1 = 0
    def mOn(self,event):
        self.m1 = 1
    def mOff(self,event):
        self.m1 = 0
    """
            
    # key input changing stuff
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
    def holdOn(self,event):
        self.hold = self.hold * (-1)
        global hold
        hold = hold * (-1)
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
    # blue portal
    asset = ImageAsset("images/Blue_Portal.png", Frame(25,10,350,475), 1, 'vertical')
    def __init__(self, position):
        super().__init__(BluePortal.asset, position)
        self.scale = .25
        self.center = (0,0)
        
    def step(self):
        self.x = cbx - 50
        self.y = cby - 60
        
class OrangePortal(Sprite):
    # orange portal
    asset = ImageAsset("images/portal___orange_portal_by_maxiesnax-d5pcfmj.png", Frame(25,10,350,475), 1, 'vertical')
    def __init__(self, position):
        super().__init__(OrangePortal.asset, position)
        self.scale = .25
        self.center = (0,0)

    def step(self):
        self.x = cox - 50
        self.y = coy - 60
    
class Platforms(Sprite):
    # thin platform to collide with for gravity
    platc=Color(0xB9BDBB,1.0)
    plat=RectangleAsset(250, 1, noline, platc)
    def __init__(self, position):
        super().__init__(Platforms.plat, position)

class ExitDoor(Sprite):
    # exit door, with two different images, closed and open
    door = ImageAsset("images/PortalDoor.png", Frame(0,0,195,210), 2, 'horizontal')
    def __init__(self, position):
        super().__init__(ExitDoor.door, position)
        self.scale = .65
    def step(self):
        global win
        self.win = win
        # if win (cube colliding with button and not held), the set image to open door
        if self.win == 1:
            self.setImage(1)
        # else set image to closed door
        else:
            self.setImage(0)

class YouWin(Sprite):
    # you win text
    youwintxt = TextAsset(text="YOU WIN!!", width=700, align='center',style='100px Arial', fill=Color(0xff2222,1))
    def __init__(self, position):
        super().__init__(YouWin.youwintxt, position)
"""
class Secrets(Sprite):
    # secrets text
    secretstxt = TextAsset(text="There are secrets", width=700, align='center',style='100px Arial', fill=Color(0xff2222,1))
    def __init__(self, position):
        super().__init__(Secrets.secretstxt, position)
"""
            
class CompanionCube(Sprite):
    cc = ImageAsset("images/companioncube.png", Frame(20,20,260,260), 1, 'horizontal')
    def __init__(self, position):
        super().__init__(CompanionCube.cc, position)
        self.scale = 1/7
        self.x = 10
        self.y = 63
        self.visible = True
        self.vx = 0
        self.vy = 0
        self.held = 1
        self.d = 0
    def step(self):
        # moving up if colliding with platforms to counteract gravity
        if self.collidingWithSprites(Platforms):
            self.vy -= .1
            self.y += self.vy
            self.vy = 0
        else:    
            self.vy += .1
            self.y += self.vy
        # if colliding with Chell and being held, then change to be "held"
        global hold
        self.held = hold
        if self.collidingWithSprites(Chell) and self.held == -1:
            self.vy = 0
            self.x = ccx + 10
            self.y = ccy + 25
        # if Chell goes through portal while holding, go to Chell
        global holding
        self.holding = holding
        if self.holding == -1:
            self.x = ccx + 10
            self.y = ccy + 25
            
        global cox
        global coy
        global cbx
        global cby
        # orange portal and not being held detection
        if self.x<= cox-10 and self.x>=cox-30 and self.y <= coy-5 and self.y >= coy-50 and cby>=0 and cbx>=0 and self.held != -1:
            self.x = cbx
            self.y = cby - 10
        # blue portal and not being held detection
        elif self.x<=cbx-10 and self.x>=cbx-30 and self.y <= cby-10 and self.y >= cby-50 and coy>=0 and cox>=0 and self.held != -1:
            self.x = cox
            self.y = coy - 10
        

        # death by goo
        if  self.y >= 620:
            if self.d == 0:
                cdeath.volume = 25
                cdeath.play()
                euth.play()
                self.x = 10
                self.y = 63
                self.vy =0
                self.d = 1
            else:
                cdeath.volume = 50
                cdeath.play()
                self.x = 10
                self.y = 63
                self.vy =0
            
class CubeButton(Sprite):
    button = RectangleAsset(100,10,noline,red)
    def __init__(self, position):
        super().__init__(CubeButton.button, position)
        self.x = 700
        self.y = 490
        self.w = 0
    def step(self):
        global hold
        self.hold = hold
        # if cube is colliding with the button and isn't being held, have win be possible
        if self.collidingWithSprites(CompanionCube) and self.hold != -1:
            global win
            win = 1
            # play exposure to button sound once
            if self.w == 0:
                success1.play()
                self.w = 1
        # else don't have win be possible
        else:
            global win
            win = -1
        
class Glados(Sprite):
    cc = CircleAsset(5,thinline,black)
    def __init__(self, position):
        super().__init__(Glados.cc, position)
        self.p = 0
    def step(self):
        # intro sound 1
        if self.p == 0:
            e1.play()
            self.p = 1
            self.t = time.time()
        # intro sound 2
        if time.time() > self.t + 6.75 and time.time() < self.t + 7.25 and self.p == 1:
            e2.play()
            self.p = 2
            self.t = time.time()
        # intro sound 3
        if time.time() > self.t + 4.5 and time.time() < self.t + 5 and self.p == 2:
            e3.play()
            self.p = 3
            self.t = time.time()
        # intro sound 4
        if time.time() > self.t + 5 and time.time() < self.t + 6 and self.p == 3:
            e4.play()
            self.p = 4
            self.t = time.time()
        # intro sound 5
        if time.time() > self.t + 10.5 and time.time() < self.t + 11.25 and self.p == 4:
            e4.stop()
            self.p = 5
            e5.play()
            self.t = time.time()
        # intro sound 6
        if time.time() > self.t + 5 and time.time() < self.t + 6 and self.p == 5:
            e5.stop()
            e6.play()
            self.p = 6
            self.t = time.time()
        # intro sound 7
        if time.time() > self.t + 5 and time.time() < self.t + 6 and self.p == 6:
            e7.play()
            self.p = 7
            self.t = time.time()
        if time.time() > self.t + 6 and time.time() < self.t + 6.5 and self.p == 7:
            global cox
            global coy
            cox = 120
            coy = 440
            op.play()
            self.p = 8
            global play
            play = 1
        
class PortalGame(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        # defining of text on screen
        imagetxt = TextAsset(text="Certain Sprites Take a While to Load, so be patient. You aren't able to move for a while anyways.", width=(400-100), align='center',style='10px Arial', fill=Color(0xff2222,1))
        movetxt = TextAsset(text="A to Move Left, D to Move Right", width=200, align='center',style='10px Arial', fill=Color(0xff2222,1))
        jumptxt = TextAsset(text="Space to Jump, E to Interact", width=200, align='center',style='10px Arua==ial',fill=Color(0xff2222,1))
        optxt = TextAsset(text="Left Click to Place Orange Portal", width=200, align='center',style='10px Arial', fill=Color(0xff2222,1))
        bptxt = TextAsset(text="Alt + Left Click to Place Blue Portal", width=200, align='center',style='10px Arial', fill=Color(0xff2222,1))
        errortxt = TextAsset(text="If not teleporting through portal, press E once", width=200, align='left',style='9px Arial', fill=Color(0xff2222,1))
        #background
        Sprite(wall, (0,0))
        Sprite(exitbig, (75,450))
        Sprite(exitsmall, (75,450))
        Sprite(doorline, (75,380))
        #goo
        Sprite(goo, (0,650))
        # creation of text
        Sprite(imagetxt,(0,680))
        Sprite(movetxt,(0,700))
        Sprite(jumptxt,(0,710))
        Sprite(optxt, (0,720))
        Sprite(bptxt, (0,730))
        Sprite(errortxt, (0,740))
        # exit sprite
        ExitDoor((700,50))
        # assorted platforms
        Sprite(plat,(0,500))
        Platforms((0,500))
        Sprite(platsmall,(10,100))
        Platforms((10,100))
        Sprite(plat,(650,150))
        Platforms((650,150))
        Sprite(plat,(600,500))
        Platforms((600,500))
        # button
        CubeButton((0,0))
        # portals, companion cube, and Chell
        BluePortal((0,0))
        OrangePortal((0,0))
        Chell((0,0))
        CompanionCube((0,0))
        # Glados for voices
        Glados((-100,-100))
        
    def step(self):
        for chell in self.getSpritesbyClass(Chell):
            chell.step()
        for blueportal in self.getSpritesbyClass(BluePortal):
            blueportal.step()
        for orangeportal in self.getSpritesbyClass(OrangePortal):
            orangeportal.step()
        for cc in self.getSpritesbyClass(CompanionCube):
            cc.step()
        for cubebutton in self.getSpritesbyClass(CubeButton):
            cubebutton.step()
        for door in self.getSpritesbyClass(ExitDoor):
            door.step()
        for glados in self.getSpritesbyClass(Glados):
            glados.step()
            
myapp = PortalGame(1000,750)
myapp.run()