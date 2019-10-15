#free fall model
#joshlucpoll.com

'''
using the equation:

a = (W - D) / m

Ref:
https://www.grc.nasa.gov/www/k-12/airplane/falling.html

'''

import inputs
from texttable import Texttable
import webbrowser
import matplotlib.pyplot as plt
import numpy as np

def calculate(timeInterval, acceleration, initialVelocity, dragCoefficient, mass, area):

    #initialises all necessary variables for calculations
    initialAcceleration = acceleration
    previousVelocity = initialVelocity
    previousDistance = 0.0
    currentTime = 0.0

    weight = mass * initialAcceleration
    densityOfAir = 1.2754       #At IUPAC standard temperature and pressure

    #creates lists for all the data to be stored in
    timeList = [0]
    accelerationList = [acceleration]
    velocityList = [initialVelocity]
    distanceList = [0]

    while True:
        
        #calculates the drag
        drag = dragCoefficient * 0.5 * densityOfAir * previousVelocity * previousVelocity * area

        #calculate acceleration
        acceleration = round(((weight - drag) / mass), 3)
        accelerationList.append(acceleration)

        #calculate velocity
        currentVelocity = round(((acceleration * timeInterval) + previousVelocity), 3)
        velocityList.append(currentVelocity)

        #calculate distance
        currentDistance = round(((currentVelocity * timeInterval) + previousDistance), 3)
        distanceList.append(currentDistance)

        #increments time
        currentTime += timeInterval
        timeList.append(round(currentTime, 2))

        #checks to see if terminal velocity has been reached
        if currentVelocity == previousVelocity or currentVelocity <= 0:
            
            #adds on terminal string to last velocity
            terminal = velocityList.pop()
            velocityList.append("Terminal - " + str(terminal))
            break
        
        
        previousVelocity = currentVelocity
        previousDistance = currentDistance
            

    return(timeList, accelerationList, velocityList, distanceList)


def renderTable(timeList, accelerationList, velocityList, distanceList):
    #using the data from the lists, renders the table and prints it

    #initialises table and headers
    table = Texttable(max_width=0)
    table.add_row(["Time(s)", "Acceleration(m/s^2)", "Velocity(m/s)", "Distance(m)"])
    
    #adds all the rows for the data
    for i in range(len(timeList)):
        table.add_row([timeList[i], accelerationList[i], velocityList[i], distanceList[i]])

    #create a txt file and outputs the table
    f = open("output.txt", "w+")
    f.write(table.draw())
    f.close()
    
    #open file in default txt editor
    webbrowser.open("output.txt")

    #removes the terminal velocity value as it's repeated
    velocityList.pop()
    timeList.pop()

    #generates a velocity time graph
    plt.title('Velocity-Time Graph for Free Fall')
    plt.ylabel('Velocity (m/s)')
    plt.xlabel('Time (seconds)')
    plt.axis([0, timeList[-1], 0, (velocityList[-1] + 10)])
    plt.plot(timeList, velocityList)
    
    #places arrow on graph to show terminal velocity and the time
    arrowString = 'Terminal:\n' + str(velocityList[-1]) + ' m/s\n' + str(timeList[-1]) + ' seconds'
    plt.annotate((arrowString), xy=(timeList[-1], velocityList[-1]), xytext=(timeList[-1] - 10, velocityList[-1]- 20), arrowprops=dict(facecolor='black', shrink=0.05))
    
    #displays the graph
    plt.show()



if __name__ == "__main__":

    #gathers all necessary variables to calculate model
    timeInterval, acceleration, initialVelocity, dragCoefficient, mass, area = inputs.get()
    
    #passes those variables onto calculate()
    timeList, accelerationList, velocityList, distanceList = calculate(timeInterval, acceleration, initialVelocity, dragCoefficient, mass, area)
    
    #gets lists and passes them to be rendered
    renderTable(timeList, accelerationList, velocityList, distanceList)


