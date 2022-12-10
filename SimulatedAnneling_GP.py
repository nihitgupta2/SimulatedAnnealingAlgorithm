# Nihit Gupta 
# Id 20759430
import random
import math

def SimulatedAnnealing(initialTemperature,iterations,stepSize,initialXValues,alpha):
    currentTemperature = initialTemperature
    currentSolution = Fx(initialXValues[0],initialXValues[1])
    currentXValues = []
    currentXValues = initialXValues
    while(currentTemperature>0.001):
        for i in range(iterations):
            r1 = random.uniform(-stepSize,stepSize)
            r2 = random.uniform(-stepSize,stepSize)
            x1buffer = None
            x2buffer = None
            costbuffer = None
            P = None
            if currentXValues[0]+r1<-100 or currentXValues[0]+r1>100:
                continue
            else:
                x1buffer = currentXValues[0]+r1

            if currentXValues[1]+r2>100 or currentXValues[1]+r2<-100:
                continue
            else:
                x2buffer = currentXValues[1]+r2
            
            costbuffer = Fx(x1buffer,x2buffer)
            deltaCost = costbuffer - currentSolution
            if deltaCost < 0:
                P = 1
                currentXValues = [x1buffer,x2buffer]
                currentSolution = costbuffer
            else:
                P = math.exp(-deltaCost/currentTemperature)
                a = random.uniform(0, 1)
                if a<P:
                    currentXValues = [x1buffer,x2buffer]
                    currentSolution = costbuffer
                else:
                    continue

            i+=1
        currentTemperature=currentTemperature*alpha
    return currentXValues,currentSolution,currentTemperature

def Fx (x1,x2):
    result = -math.cos(x1)*math.cos(x2)*math.exp(-((x1-math.pi)**2)-((x2-math.pi)**2))
    return result 

def main ():
    stepSize = 4
    initialTemperature = 500
    x1Initial = -100
    x2Initial = 100
    initialSolution = [x1Initial,x2Initial]
    iterations = 250
    alpha = 0.98 # for linear annealing
    xSolutionValues,cost,temp = SimulatedAnnealing(initialTemperature,iterations,stepSize,initialSolution,alpha)
    print("completed")
    print(xSolutionValues)
    print(cost)
    print(temp)

    
if __name__ == '__main__':
    main()      #invoking the main function

