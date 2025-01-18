from datetime import datetime

name = str(input('Enter your name: '))

print(f"Hi, {name}! are the { datetime.now().hour}:{datetime.now().minute}:{ datetime.now().second} o'clock")