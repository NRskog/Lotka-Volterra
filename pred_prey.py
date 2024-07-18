import numpy as np
from scipy.integrate  import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def parameters():
    #Parametetrar använder siberiska tigrar och älgar i sibirien :D
    """
    alpha = 1.3  # bytespopulations tillväxthastighet (nya föds)
    beta =  0.005    # bytes chans att bli uppätna   (dödade)
    gamma =  0.1   # Rovdjurs naturlgiga dödhet (svälta)
    delta =  0.01   # rovdjurs tillväxt baserat på antal byte (mat)
    """
    alpha = 1.1  
    beta =  0.01    
    gamma =  0.1   
    delta =  0.001   
    tmin = 0
    tmax = 150
    t_steps = 10000



    t = np.linspace(tmin, tmax , t_steps )   # En array med tidpunkter

    return alpha, beta, gamma, delta, t


def boundary_conditions():
    x0 = 100   #Bytesdjursantal vid start
    y0 =  35  #Rovdjursantal vid start 
    z0 = [x0, y0] #scipy gillar vektorer
    return z0

def lotka_volterra(z, t, alpha, beta, gamma, delta):

    #ekvationerna
    x,y = z
    dx_dt = alpha*x - beta*x*y
    dy_dt = delta*x*y - gamma*y
    return [dx_dt, dy_dt]



def module_rk4( alpha, beta, gamma, delta, t):

    z0 = boundary_conditions()
    #function = lotka_volterra()
    sol = odeint(lotka_volterra, z0, t, args = (alpha, beta, gamma, delta) )
    x = sol[:, 0]
    y = sol[:, 1]
    return x, y 


def plot(x, y, t):

    plt.plot(t, x, label='Bytesdjur (x)')
    plt.plot(t, y, label='Rovdjur (y)')
    plt.xlabel('Tid')
    plt.ylabel('Population')
    plt.legend()
    plt.title('Lotka-Volterra Modell med odeint')
    plt.show()


def main():
    alpha, beta, gamma, delta, t = parameters()
    x,y = module_rk4(alpha, beta, gamma, delta, t)
    plot(x,y, t)

if __name__ == "__main__":
    main()


"""
def own_rk4():
    pass
"""


