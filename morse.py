import RPi.GPIO as GPIO
import time

# Copyright Gregory Schultz 2016

# About this Program:
# Given the proper LED and Pin setup, this program will take a phrase and translate
# it into morse code on the Raspberry Pi
# Supported characters: A-Z 0-9
# Spaces between words have a rest time of 5 seconds
# Spaces between characters have a rest time of 1 seconds

GPIO.setmode(GPIO.BOARD)
# SET THIS TO THE PIN YOU ARE USING
gpio_pin="7"
GPIO.setup(int(gpio_pin),GPIO.OUT)

s="GPIO.output ("+gpio_pin+", GPIO.HIGH); time.sleep(1);GPIO.output (" +(gpio_pin)+", GPIO.LOW); time.sleep(1);"
l="GPIO.output ("+gpio_pin+", GPIO.HIGH); time.sleep(2);GPIO.output (" +(gpio_pin)+", GPIO.LOW); time.sleep(1);"
breaker="time.sleep(5)"

alphabet={" ": breaker, "a": s+l, "b": l+s+s+s, "c": l+s+l+s, "d": l+s+s, "e": s, "f": s+s+l+s, "g":l+l+s, "h":s+s+s+s, "i": s+s, "j": s+l+l+l, "k": l+s+l, "l": s+l+s+s, "m": l+l, "n": l+s, "o": l+l+l, "p": s+l+l+s, "q": l+l+s+l, "r": s+l+s, "s": s+s+s, "t": l, "u":s+s+l, "v": s+s+s+l, "w": s+l+l, "x": l+s+s+l, "y": l+s+l+l, "z": l+l+s+s, "0":l+l+l+l+l, "1": s+l+l+l+l, "2": s+s+l+l+l, "3": s+s+s+l+l, "4": s+s+s+s+l, "5": s+s+s+s+s, "6": l+s+s+s+s, "7": l+l+s+s+s, "8": l+l+l+s+s, "9": l+l+l+l+s}

phrase=raw_input ("What is your phrase to translate? ")
phrase=list(phrase)
          
executable=[]
for char in phrase:
        try:
            char=char.lower()
        except:
            pass
        if char in alphabet:
          executable.append(alphabet[char])
for item in range(len(executable)):
          print "Character %s" %phrase[item]
          exec(executable[item])
        

GPIO.cleanup()
