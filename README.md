# Casioplot-Flappybird
A very simple flappybird clone made using the casioplot library, only compatible with the CG100.

Made using the Casioplot library, only compatible with the CG100 (not the CG50), as it is the only calculator, that supports the get_key() function.
As far as i know, this is the first program to use casioplot in this way, as a fully gui interface.

To install simply connect your calculator in usb flash mode and transfer the .py file over, then run it in the python app.
It runs very slowly ~ 1 fps, due to the limitations of python, the hardware, and my coding ability - im sure someone with more experience could optimise it.

The main file, flappybird.py is 100% human, but runs very slowly ~ 1fps
The faster and probably preferable file geminiOptmised.py, this is what gemini responded with when i asked it to optimise flappybird.py, this runs around 3fps

Controls:

  * OK or EXE: moves bird up - I reccomend holding it down as it may not register with short presses

  * Home: Stops game

  * Tools: Pauses game

  * AC: KeyboardInterupt - use this to clear the screen and go back to the main interface or to exit if it crashes
