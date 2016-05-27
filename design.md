Portal

## Design Specification

The design specificaiton is a counterpart to the Functional Speciffication. Where a functional specification concerns itself
with inputs and outputs from the program, or the *experience* of a user running the program, the design specification is concerned with decisions that the engineer and programmer must make during its creation.

The design specification should include information like:

* What tools or frameworks will you use to build the project (e.g. http://runpython.com or ggame)?
* What language will you use for coding (usually Python 3)?
* For every element of the Functional Specification, what code will need to be written to support it?
* What data will be stored or manipulated by the program? How will it be encoded and organized?
* Describe the logic and/or code behind every interaction with the user, and behind everything displayed.
* If your program uses an unusual or notable *algorithm*, what is the algorithm and how does it work?

I used Python 3, run on http://runpython.com to write and execute my code. I imported ggame for graphics, classes, Sprites and other visual assets.
There are a few global variables that are used to control the cordinates of the blue and orange portals and the companion cube. I had been having issues with layering of the portals because each new instance of a portal would destroy its old one and then create a new one on a layer above Chell, the character you play as, which caused Chell to go behind the portals, making it difficult to see where she was at time. I fixed that by constantly setting the x and y coordinates of the two portals to four different global variables that would be changed when the player clicks to place a new portal, instantly moving the corresponding portal to the place where the mouse was clicked. There were also values changed when the "a", "d", and space keys were pressed and released, causing Chell to move left and right only when the corresponding key was pressed down and to jump only when the spacebar was pressed. I simulated gravity by constantly adding a small number to the y of the character which slowly gets bigger, but only when the character isn't colliding with a platform. This way, the character will fall when not colliding with a platform. When the spacebar is pressed, it changes the value that is added to the y coordinates to a negative number, which then instantly causes the character to move up, because the negative number added to the y coordinates make it move up. As when the character isn't colliding with the platform, a number which is negative but slowly apporaching zero is added to the y coordinates, causing the character to go up fast and first but then slow down and eventually fall. 
In terms of interaction with the user, the only interaction involves the "a", "d", spacebar, alt and left mouse keys, and assorted key inputs for some secrets from valve universes. Pressing the "a" key causes the character on the screen to move left. Pressing the "b" key causes the portal to move right. When the spacebar is pressed, if the character is currently colliding with a platform, it will jump and come back down, assuming it doesn't jump into a portal or onto another platform. When the left mouse buttons is clicked, an orange portal will be created where the mouse was clicked. If the alt key is held down and the left mouse button is clicked, a blue portal is created where the mouse was clicked.
