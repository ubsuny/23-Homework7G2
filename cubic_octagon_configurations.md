# Tetramer NaCl Configurations:
The tetramer form of NaCl consists of four NaCl molecules.
the predicted equilibrium distance as calculated using theory is 2.312 $\mathring{A}$ and the emperical value was 2.36 $\mathring{A}$. [1](https://www.researchgate.net/publication/201976884_Evolving_few-ion_clusters_of_Na_and_Cl) 

I applied the equilibrium distance as 2.36 $\mathring{A}$ or 0.236 nm for both configurations.
## cubic configuration:
**Na positions Array** consists of the x,y and z coordinates of 4 atoms and similarly **Cl positions array** as follows:

```
a = 0.236 #nm
r_na = np.array( [ [a,0,0], [0, a, 0], [0, 0, a],[a, a, a] ] )
r_cl = np.array( [ [0, 0, 0],[a, a, 0],[a, 0, a],[0, a, a] ] )

```

This is for the cubic configuration where the larger sphere represent the Na+ ions and the smaller ones represent the Cl- ions
![image](https://github.com/yasmensarhan27/23-Homework7G2/assets/38404107/67ccd44a-8789-4769-8196-491b0834e70e)


Then applied scipy optimization function using BFGS method ``` res = scipy.optimize.minimize( fun=cluster, x0=vals_init, tol=1e-3, method="BFGS")  ```
Create a 3D graph of the initial and the new positions of Na and Cl ions
The Green and yellow dots are the initial Na and Cl positions respectively and the red dots are for Na+ new positions and the blue for Cl- ion

the potential energy was ``` initial V  : -27.085601041071918 ``` and the final is ```Final potential: -28.235830565026856```

this means the potential energy per ion pair changed from ~ -6.77 eV to ~ -7.05 eV

**comparing the old and new positions:**
they are approximately simialr to each other:
![Unknown-10](https://github.com/yasmensarhan27/23-Homework7G2/assets/38404107/08f1dce8-a122-43d1-ad09-3ee230a07cf3)


## Octagon Configuration

Using the same equilibrium distance, The initial positions are assumed to be:

```
r_na = np.array( [ [0, 0, 0], [0.167,0.403,0], [0.57, 0.236, 0],[0.403, 0.167, 0] ] )
r_cl = np.array( [ [0, 0.236, 0],[0.57, 0, 0],[0.167, -0.167, 0],[0.403, 0.403, 0] ] )


```
![image](https://github.com/yasmensarhan27/23-Homework7G2/assets/38404107/d71e15f5-0638-48ee-811a-03a1fbb532b9)

process similar to the cubic:
the potential energy was ``` initial V  : -22.980062797276656 ``` and the final is ```Final potential: -27.7298422847269```

this means the potential energy per ion pair changed from ~ -0.825 eV to ~ -6.945 eV

**comparing the old and new positions:**
the initial positions are not near the final positions:
This means that considering initial positions with z components = zero wasn't the best estimation.


![Unknown-14](https://github.com/yasmensarhan27/23-Homework7G2/assets/38404107/4c887b93-1223-41f9-aea3-b191bdd43d6d)



References:
[1. Evolving few-ion clusters of Na and Cl](https://www.researchgate.net/publication/201976884_Evolving_few-ion_clusters_of_Na_and_Cl)
[2. 
