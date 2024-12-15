# Virtual Pet Simulator

Welcome to the **Virtual Pet Simulator**! This Python program allows you to interact with a virtual pet by feeding, playing, and checking its stats. Your pet's hunger, health, and happiness levels will change based on your actions. Keep your pet healthy and happy!

## Features
- **Feed**: Feed your pet to reduce its hunger level.
- **Play**: Play with your pet to increase its happiness.
- **Check Stats**: Check your pet's hunger, health, and happiness.
- **Exit**: Exit the game when you're done.

## How It Works
1. When you start the game, you will be prompted to name your pet.
2. The game will present you with a menu of actions:
    - **Feed**: Reduces hunger.
    - **Play**: Increases happiness.
    - **Check Stats**: Displays current hunger, health, and happiness levels.
    - **Exit**: Ends the game.
3. The game will automatically check the stats after each action (feeding or playing), and inform you if your pet is in a critical condition (e.g., starving).
4. The game ends when the pet's health reaches 0 or when you choose to exit.

## Example Usage

```
Welcome to the Virtual Pet Simulator!
What would you like to name your pet? oggy

oggy is ready to play with you!

What would you like to do?
1. Feed
2. Play
3. Check Stats
4. Exit
Enter your choice: 1
oggy enjoyed the food!

Pet's Name: oggy
Hunger: 2
Health: 11
Happiness: 6

What would you like to do?
1. Feed
2. Play
3. Check Stats
4. Exit
Enter your choice: 2
oggy had a lot of fun!

Pet's Name: oggy
Hunger: 4
Health: 10
Happiness: 8
```
