import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-2,8*np.pi,70)
sin=np.sin(x)
cos=np.cos(x)
plt.plot(x,sin,'bo:',linewidth=3)
plt.plot(x,cos,'gs-',linewidth=2)
plt.show()

