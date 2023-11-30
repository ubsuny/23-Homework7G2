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

This is for the cubic configuration 

![image](https://github.com/yasmensarhan27/23-Homework7G2/assets/38404107/67ccd44a-8789-4769-8196-491b0834e70e)

















References:
[1. Evolving few-ion clusters of Na and Cl](https://www.researchgate.net/publication/201976884_Evolving_few-ion_clusters_of_Na_and_Cl)
