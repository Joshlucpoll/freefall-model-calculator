def get():    
  #gets variables from user

  #get time interval
  while True:
      try:
          timeInterval = input("\nEnter time interval between calculations. (Seconds)\nDefault is 0.1\n")
          print(timeInterval)
          if timeInterval == "":
            timeInterval = 0.1
            break
          timeInterval = float(timeInterval)
          if timeInterval <= 0:
              print("\n\tPlease enter a positive value")
          else:
              break
      except ValueError:
          print("\n\tPlease enter an integer or decimal value")

  #get acceleration
  while True:
      try:
          acceleration = input("\nPlease enter a downwards acceleration in metres per second squared\nDefault is 9.81\n")
          if acceleration == "":
            acceleration = 9.81
            break
          acceleration = float(acceleration)
          if acceleration < 0:
              print("\n\tPlease enter a positive value")
          else:
              break
      except ValueError:
          print("\n\tPlease enter an integer or decimal value")

  #gets initial velocity
  while True:
      try:
          initialVelocity = input("\nPlease enter a downwards initial velocity in metres per second\nDefault is 0\n")
          if initialVelocity == "":
            initialVelocity = 0.0
            break
          initialVelocity = float(initialVelocity)
          if initialVelocity < 0:
              print("\n\tPlease enter a positive value")
          else:
              break
      except ValueError:
          print("\n\tPlease enter an integer or decimal value")

  #gets the drag coefficient
  while True:
      try:
          dragCoefficient = input("\nPlease enter the drag coefficient of the object\n")
          dragCoefficient = float(dragCoefficient)
          if dragCoefficient <= 0:
              print("\n\tPlease enter a positive value")
          else:
              break
      except ValueError:
          print("\n\tPlease enter an integer or decimal value")

  #gets mass of object
  while True:
      try:
          mass = input("\nPlease enter the mass of the object(Kg)\n")
          mass = float(mass)
          if mass <= 0:
              print("\n\tPlease enter a positive value")
          else:
              break
      except ValueError:
          print("\n\tPlease enter an integer or decimal value")

  #gets area of object
  while True:
      try:
          area = input("\nPlease enter the area of the object(m^2)\n")
          area = float(area)
          if area <= 0:
              print("\n\tPlease enter a positive value")
          else:
              break
      except ValueError:
          print("\n\tPlease enter an integer or decimal value")

  return timeInterval, acceleration, initialVelocity, dragCoefficient, mass, area
