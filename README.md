# feedtheworm
Feed the Worm: Extreme Edition (based off snake)

Welcome to my Feed The Worm repository. This game is a remake of the original snake game created by me in python using the pygame libraries. 

How to play the game:
	
	1. Run the program using a Python IDE such as IDLE or Spyder 
	2. You will then be greeted with the Start Menu. On the Start Menu choose the 'Play' button to start the game. 
	3. The game should now start, you will be shown a grid with the worm (orange) and food (red) on it.
	4. To control the worm you can use either; WASD controls or Arrow Key controls (UP, DOWN, LEFT, RIGHT)
	5. Interact with the worm using either one of these controlling methods to move around the playing surface to eat the food pieces.
	6. Each time you eat a food piece, you gain one point (added to your score)
	7. You're good to go! Enjoy Feed the Worm and get as many points as possible!
	
Future Improvements:

From this experience I would say that a few improvements could definitely be made. Mainly being that the game is a bit too boring, especially if you play it for a while, I believe the game could’ve been more enjoyable if I was to implement more objects into the game with special rounds that give you extra points. 

Libraries

	For this game I have used four different libraries; Pygame, Pygame Menu, Sys, and Random.

	1. Pygame https://www.pygame.org/news. I have used the pygame library as it was the main requirement for this project, I have used a series of shapes including cubes and rectangles to emulate the snake playing surface. 

	2. Pygame Menu https://pygame-menu.readthedocs.io/en/latest/. I have also used the pygame menu library (which is a separate library to Pygame itself) to include a start menu to my game. Pygame menu allows you to easily import a start menu with working buttons to easily lead to your game, this helps the user interact with the game easily. 

	3. Sys. The third library I have used is Sys. Sys is actually built into Python which requires no installation externally, I have used sys to import the scoreboard's font and sizing. The font I have chosen from the Sys library is "Helvetica Bold" in Size 32. 

	4. Random. And lastly, Random. Random is also built into python which requires no external installation. I have used Random as a number randomiser in my game. As the Feed the Worm game is built off of a Worm eating food across the surface, the Random library allows the game to randomly bring a number which will correlate to the placement of the food every time the Worm eats a piece. 



Other References:

I have used a tutorial from the YouTube channel Kite to help me create the framework for this game, I took this tutorial to help create some of my code and extended it to make something better! From this tutorial I was able to fully understand how pygame works as a library and in a real life circumstance like this one. 

https://www.youtube.com/watch?v=9bBgyOkoBQ0&t
