"""
This code imports from the maon module Nacl_main.py
The main source is: https://github.com/ubsuny/CompPhys/blob/main/MinMax/nacl.ipynb
This with calculate the potential energy and apply optimization function to get a lower
potential then the ions will be re arranged.
"""
"""
    Optimize the ionic configuration to minimize potential energy.

    Parameters:
    - initial_na_positions (np.ndarray): Initial positions of Na+ ions.
    - initial_cl_positions (np.ndarray): Initial positions of Cl- ions.
    - tolerance (float): Tolerance for optimization convergence. Default is 1e-3.
    - method (str): Optimization method. Default is "BFGS".

    Returns:
    - optimized_positions (np.ndarray): Optimized positions of Na+ and Cl- ions.
    - final_potential (float): Final potential energy after optimization.
    """
from nacl_main import *
# the initial coordinates of Na+ and Cl- ions.
r_na = np.array( [ [0, 0, 0], [0.167,0.403,0], [0.57, 0.236, 0],[0.403, 0.167, 0] ] )
r_cl = np.array( [ [0, 0.236, 0],[0.57, 0, 0],[0.167, -0.167, 0],[0.403, 0.403, 0] ] )
# cluster them in one array then flatten this array and print the aarays
cluster = Cluster(r_na, r_cl)
vals_init = cluster.get_vals()
print('initial Na positions:\n', r_na)
print('initial Cl positions:\n', r_cl)
print('initial positions flattened shape:\n', vals_init )
print('initial V  :', cluster.V() )
#use scipy optimization function to minimize the potential energy
# the scipy optimization method used it BFGS
res = scipy.optimize.minimize( fun=cluster, x0=vals_init, tol=1e-3, method="BFGS")
cluster.set_vals(res.x)  # For some reason,"minimize" is not updating class at the last iteration
#print the rearranged positions
print ("Final optimized cluster positions")
print(cluster.positions)
print("Final potential:", res.fun)
#plot a 3D figure to show the configuration
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#plot the old or initial positions in green and yellow colors.
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
#The blue dots are Cl, the red dots are Na.
#the color is chosen based on the charge if - will reflect red color
#if + will reflect a blue color according to the heat map from -1 to +1
ax.scatter( x,y,z, c=charges, cmap='coolwarm', label='Na')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.legend()
plt.show()
