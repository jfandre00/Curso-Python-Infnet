import pandas as pd
import numpy as np
#import matplotlib as plt
import matplotlib.pyplot as plt

print(pd.__version__)
print(np.__version__)
#print(plt.__version__)
print("Hello, world!")

#Exemplo de uso do pandas

data = {
    'apples': [3, 2, 0, 1],
    'oranges': [0, 3, 7, 2]
}

purchases = pd.DataFrame(data)

print(purchases)

#Exemplo de uso do numpy

a = np.array([1, 2, 3])
print(a)

#Exemplo de uso do matplotlib

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()
