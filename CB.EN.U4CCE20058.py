import numpy as np #library functions
import matplotlib.pyplot as plt

def impusle_calc(h,u1,u2): #fn to store impulse
    for i in range(20):#getting 20 values to store in u[n]
        #u[n] value we are keeping it as high
        if i>=0:
        #we are appending the values to u[1] list
            u1.append(1)
        else:
            #else condition for appending low values
            u1.append(0)     

    for i in range(20):
        #to store u[n-10] we are giving another for loop
        if i>=10:
            #so as below 10 the result would become low so we are appending values greater than 10
            u2.append(1)
        else:
            #else condition for appending low values
            u2.append(0)
#we are just subtracting and storing the values of the impulse equation given in the question
    for i in range(0,10):
        h.append(u1[i]-u2[i]) #This statement stores the impulse response
        
def pulse_input(x,u3,u4):
    #getting 20 values to store in u[n-2]
    for i in range(20):
        #we are appending the values to u3 list
        if i>=2:#since n-2 is given in question we are appending high(1) for values greater than 2
            u3.append(1)
        else:#else we are appending low for other values
            u3.append(0)     
#assigning 20 values to store in u[n-7]
    for i in range(20):
        if i>=7:#since n-7 is given in question we are appending high(1) for values greater than 7
            u4.append(1)
        else:#we are appending low
            u4.append(0)
#we are just subtracting and storing the values of the system input
    for i in range(0,10):
        x.append(u3[i]-u4[i])    
        
        
h = []
u1 = []
u2 = []

x=[]
u3=[]
u4=[]
impusle_calc(h,u1,u2)
pulse_input(x, u3, u4)
plt.title('impulse response')
plt.xlabel('n')
plt.ylabel("h[n]")
plt.stem(np.arange(0,10 ),h)#plotting x-axis with respect toimpulse response on y-axis
plt.xticks(np.arange(10))#defining the values of x-axis here from 0 to 9
plt.yticks(np.arange(0,3,1))#defining the values of y-axis here from 0 to 2
plt.show()#to display the graph

plt.title('system input')
plt.xlabel('n')
plt.ylabel("x[n]")
plt.stem(np.arange(0,10 ),x)#plotting x-axis with respect to the system input which is plotted on y-axis
plt.xticks(np.arange(10))#defining the values of x-axis here from 0 to 9
plt.yticks(np.arange(0,3,1))#defining the values of y-axis here from 0 to 2
plt.show()#to display the graph
#convolution
y=[]
size=len(x)+len(h)-1#we are just adding the no. of values of impulse and input 
#we are just initializing the values to 0 in the array
for i in range(size):
    y.append(0)
#implementing Matrix multiplication
for i in range(len(h)):
    for j in range(len(h)):
        for k in range(len(y)):
            if k==i+j:
                y[k]+=x[i]*h[j]#y[k]=y[k]+x[i]*h[j]
   
print(y)
#Plot for y[n]
plt.title("Plot of y[n]-This is the graph of the Output Signal")
plt.xlabel("n")
plt.ylabel("y[n]")
plt.xticks(np.arange(0,19))#defining the values of x axis from 0 to 18
plt.yticks(np.arange(0,6,1))#defining the values of y-axis here from 0 to 5
plt.stem(np.arange(0,19),y)#plotting x-axis with respect to y-axis
plt.tight_layout()#automatically adjusts subplot and padding and display the output