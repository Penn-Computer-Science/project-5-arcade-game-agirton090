[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/7WcCjJC0)
<h1 align="center">TKinter Arcade Game</h1>


<h2 align="center">Project Overview</h2>

You will design and build your own **80s-style arcade game** using Python and Tkinter.

Your game should feel inspired by classic arcade games (shooters, dodging games, paddle games, etc.), but it must be **your own design**.

You may work:

- Individually  
- In a pair
  -  Pair Programming: Both students MUST:
    -  Contribute code
    -  Understand how the game loop wroks
    -  Understand how collision detection works

<h2 align="center">Learning Goals</h2>

By completing this project, you will demonstrate that you can:

- create and move game objects
- animate using the Tkinter game-loop pattern
- detect collisions
- manage game state (score, game over, reset)
- build simple sprites using pixel patterns

<h2 align="center">Concepts You MUST Use</h2>

Your game must use **all** of the following concepts.

Tkinter Canvas

Use at least one of:

- `create_rectangle`
- `create_oval`
- `create_image`

A game loop

Using:

```python
root.after(...)
```
Keyboard Input

Using:

```python
root.bind(...)
```
Lists of Objects

Examples:

```python
enemies = []
lasers = []
```
Collision Detection

Using Bounding Boxes:

```python
canvas.bbox(...)
```
At least one custom sprite

Using:

```python
tk.PhotoImage(...)
```
Sprite Generator: https://docs.google.com/spreadsheets/d/1hCECE6pL8cBCcmxJ0UXMRfsEYbBepv6a8k0mKkpYJaA/copy

<h2 align="center">Requirements</h2>

Your game *must* include:
- A player object
- At least one type of enemy or obstacle
- At least one interactice object
- A scoring system
- A game over state
- A restart function

<h2 align="center">Recommended Code Structure</h2>
Organize your program into functions similar to:

  -  create_player()
  -  spawn_enemy()
  -  fire_laser()
  -  game_loop()
  -  reset_game()
   
<h2 align="center">Game Loop Rules</h2>

  -   Do NOT use
```python
time.sleep()
```
  - Use
```python
root.after(...)
```

<h2 align="center">Inspiration</h2>

  -  Space Shooters
  -  Dodge and Survive
  -  Top down arena game
  -  Defender style game
  -  Lane runner
  -  **MAKE THIS YOURS!

<h2 align="center">Minimum Playability Checklist</h2>

  -  Make sure that:
      -  The player moves correctly
      -  Enemies or obstacles spawn
      -  Collisions are working
      -  Score updates
      -  End game state
      -  Reset function
      -  No crashes during NORMAL play
   
<h2 align="center">README Requirement</h2>

  -  Create a README.md in your repo that includes:
      -  Name of your game
      -  Controls
      -  Short description of how the game works
   
<h2 align="center">Stretch Goals</h2>

  -  For some Extra Credit, try to add one (or more) of the following:
      -  Multiple enemy types
      -  Player lives
      -  Increasing/scaling difficulty
      -  Sound effets
      -  Animated sprites
      -  Title Screen
   
<h2 align="center">Rubric</h2>

| Area                     | Points |
|:-------------------------|:------:|
| Game loop & animation    | 20     |
| Player control           | 15     |
| Enemies / obstacles      | 15     |
| Collision system         | 15     |
| Scoring + game over      | 15     |
| Sprite creation          | 10     |
| Code organization        | 10     |
| **Total**                | **100**|
