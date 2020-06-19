# eSMC2
Contains the R-package to run eSMC2, as well as script examples. A detailed description of the method can be found here: https://doi.org/10.1101/701185 and : 

Input file:

The input file for eSMC2 is the same as for eSMC, which is a "Segregating Matrix". The matrix must have M+1 lines (M is the number of haplotypes). The first M lines of the Segregating Matrix are the nucleotides of the M haplotypes at all the SNP positions (it can be encoded as nucleotide letters or as numbers). The last line of the matrix contains the position on the sequence of the SNPs. The number of columns is thus equal to the number of SNPs. The Segregating Matrix can be built from a multihetsep file (https://github.com/stschiff/msmc/blob/master/guide.md) or from simulated data through functions of the package. 

How to use eSMC2:

Step one: Download or clone the repository eSMC2 (We recommand the use of the latest version). Extract the zip file.

Step two: Open the script install_eSMC2.R in Rstudio or a text editor. Make sure the path of the package (eSMC_2.0.0.tar.gz) is correct (line 6), name of package may depend on it's version. If the package is in a different folder, modify the path to the correct folder. Execute the script to install the package on your local machine (by selecting everything and then clicking run in Rstudio).


Application to simulated data or to data :

eSMC2 can be used a eSMC, hence we invite users to follow the tutorial of eSMC (https://github.com/TPPSellinger/eSMC) for application to simulated sequence data or real sequence data.


Theoretical convergence :

We deliver 4 scripts explaining how to get the theoretical convergence. The script, simulate constant demographic scenarios. Feel free to modify them in order to study the demographic scenarios you are interested in. To optain the theoretical convergence of PSMC', you can download and run PSMC_theo.R. To obtain the heat plot, indacting if there is enough data for inference, run PSMC_heat.R. To check the theoretical convergence of MSMC, download and run  MSMC_theo.R. To obtain the heat plot for MSMC, indacting if there is enough data for inference, run MSMC_heat.R.

Warnings: 

Computation time can be increased considerably if:
- more than one chromosome in one analysis is used
- more than 10 haplotypes are simultaneously analyzed
- more than 80 hidden states are used

If the following statements are true, poor results are to be expected:
- using less than 30 hidden states
- using sequence lengths smaller than 1 Mb
- using data with less than 1000 SNPs
- depending on the ecological parameters, the recombination rate can be undersetimated if, per base pair, the recombination rate is higher than the mutation rate 

It is important to note:
- Our method cannot distinguish self-fertilization from seed banks. Simultaneously estimating both varaibles without strong prior knowledge is not advised. 


If you encounter any issue or whish to add a feature, feel free to contact me at : thibaut.sellinger@tum.de

