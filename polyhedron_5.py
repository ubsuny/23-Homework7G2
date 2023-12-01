import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import itertools
import scipy.optimize

ke2 = 197 / 137 # eV-nm   Coulomb force charge
alpha = 1.09e3  # eV      parameter of model
rho = 0.0321    # nm      parameter of model
b = 1.0         # eV      regular
c = 0.01        # nm

r_na = np.array( [[0.236, 0, 0], [0.103, 0.458, 0], [0, 0.236, 0], [0, 0, 0.245]] )
r_cl = np.array( [[0,0,0], [0, 0.472, 0], [0.103, 0.222, 0], [0,-0.204, 0]] )

cluster = Cluster(r_na, r_cl)
vals_init = cluster.get_vals()
print('initial Na positions:\n', r_na)
print('initial Cl positions:\n', r_cl)
print('initial positions flattened shape:\n', vals_init )
print('initial V  :', cluster.V() )

res = scipy.optimize.minimize( fun=cluster, x0=vals_init, tol=1e-3, method="BFGS")
cluster.set_vals(res.x)  # For some reason, "minimize" is not updating the class at the last iteration
print ("Final optimized cluster positions")
print(cluster.positions)
print("Final potential:", res.fun)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

charges = cluster.charges
x,y,z = cluster.positions[:, 0], cluster.positions[:, 1], cluster.positions[:, 2]
#The yellow dots are for Cl, the green dots are for Na.
old_na_x= r_na[:,0]
old_na_y= r_na[:,1]
old_na_z=r_na[:,2]
old_cl_x=r_cl[:,0]
old_cl_y=r_cl[:,1]
old_cl_z=r_cl[:,2]
ax.scatter(old_na_x,old_na_y,old_na_z, c='green', label='old Na positions')
ax.scatter(old_cl_x,old_cl_y,old_cl_z, c='yellow', label='old Cl positions')
# The blue dots are Cl, the red dots are Na.

ax.scatter( x,y,z, c=charges, cmap='coolwarm', label='Na')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.legend()
plt.show()
