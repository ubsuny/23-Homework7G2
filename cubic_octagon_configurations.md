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




The Green and yellow dots are the initial Na and Cl positions respectively 


![Unknown-10](https://github.com/yasmensarhan27/23-Homework7G2/assets/38404107/08f1dce8-a122-43d1-ad09-3ee230a07cf3)











References:
[1. Evolving few-ion clusters of Na and Cl](https://www.researchgate.net/publication/201976884_Evolving_few-ion_clusters_of_Na_and_Cl)
