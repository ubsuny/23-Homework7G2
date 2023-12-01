"""
This code defines a class for a cluster of Na and Cl atoms and uses 
scipy.optimize.minimize to find the minimum potential energy configuration of the cluster.

The code imports numpy, matplotlib, mpl_toolkits, itertools, and scipy libraries.

The code defines a function cp(l) that takes a list l and returns a numpy array of 
all possible pairs of elements from l.

The code defines a class Cluster that takes two numpy arrays of shape (N, 3) 
for the positions of N Na and N Cl atoms, and initializes the following attributes:
- positions: a numpy array of shape (2N, 3) for the positions of all atoms in the cluster
- charges: a numpy array of shape (2N,) for the charges of all atoms in the cluster
(+1 for Na and -1 for Cl)
- combs: a numpy array of shape (2N*(2N-1)/2, 2) for all possible pairs of indices of
atoms in the cluster
- chargeprods: a numpy array of shape (2N*(2N-1)/2,) for the product of the charges 
of each pair of atoms in the cluster
- rij: a numpy array of shape (2N*(2N-1)/2,) for the distance between each pair of 
atoms in the cluster

The class Cluster also defines the following methods:
- Vij(): calculates and returns a numpy vector of the potential energy of each pair 
of atoms in the cluster, using the Coulomb and Lennard-Jones potentials
- V(): calculates and returns the total potential energy of the cluster, which is the 
sum of the Vij vector
- get_vals(): returns the positions of all atoms as a flattened array of shape (6N,)
- set_vals(vals): takes a flattened array of shape (6N,) and sets the positions of 
all atoms accordingly, and updates the rij array
- __call__(vals): takes a flattened array of shape (6N,) and returns the total potential 
energy of the cluster with the given positions
The code then creates an instance of the Cluster class with some initial positions of Na and 
Cl atoms, and prints the initial positions and the initial potential energy.
The code then uses scipy.optimize.minimize to find the minimum potential energy configuration 
of the cluster, using the BFGS method and a tolerance of 1e-3. The code prints the final 
optimized positions and the final potential energy.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import itertools
import scipy.optimize

#Helpful solution to convert itertools combinations to numpy arrays here:
## https://stackoverflow.com/questions/33282369/convert-itertools-array-into-numpy-array
def cp(l):
    return np.fromiter(itertools.chain(*itertools.combinations(l,2)),dtype=int).reshape(-1,2)

class Cluster:
    def __init__(self, r_na, r_cl):
        '''
        Inputs the list of Na and Cl positions. Na has charge +1, Cl has -1.
        The array of ions itself does not change throughout the calculation, and
        neither do the charges. As such, we can just compute the combinations one time
        and refer to it throughout the calculation.
        '''
        self.positions = np.concatenate( (r_na,r_cl))
        self.charges = np.concatenate( [np.ones(r_na.shape[0]), np.full(r_cl.shape[0], -1)] )
        self.combs = cp(np.arange(self.charges.size))
        self.chargeprods = self.charges[self.combs][:,0] * self.charges[self.combs][:,1]
        self.rij = np.linalg.norm(self.positions[self.combs][:,0] - self.positions[self.combs][:,1], axis=1)

    def Vij(self):
        '''Calculate a numpy vector of all of the potentials of the combinations'''
        self.Vij_ = np.zeros_like(self.rij)
        pos = self.chargeprods>0
        neg = ~pos
        self.Vij_[pos] = ke2 / self.rij[pos] + b*(c/self.rij[pos])**12
        self.Vij_[neg] =-ke2 / self.rij[neg] + alpha*np.exp(-self.rij[neg]/rho) + b*(c/self.rij[neg])**12
        return self.Vij_

    def V(self):
        '''Total potential, which is a sum of the Vij vector'''
        return np.sum(self.Vij())

    def get_vals(self):
        '''Positions interpreted as a flat shape'''
        return np.reshape(self.positions, -1)

    def set_vals(self, vals ):
        '''Inputs flat shape of positions, used by __call__'''
        self.positions = vals.reshape(self.positions.shape)
        self.rij = np.linalg.norm(self.positions[self.combs][:,0] - self.positions[self.combs][:,1], axis=1)


    def __call__(self, vals):
        '''Function that  scipy.optimize.minimize will call'''
        self.set_vals(vals)
        return self.V()
