# eSMC2
Contains the R-package to run eSMC2, as well as script examples. A detailed description of the method can be found here: https://doi.org/10.1101/701185 , https://www.biorxiv.org/content/10.1101/2020.07.23.217091v2 , https://doi.org/10.1101/2022.07.29.502030 and https://doi.org/10.1101/2022.09.28.508873  : 


Please always update your version of the package as the new version generally contains bug fix, code optimization or new features.

A detailed tutorial with script example for almost all case scenario can be found in the tutorial folder. All the data has been already simulated, only the path to file location might need to be changed. Here is what the Tutorial folder contains : 

Tutorial 1 : Installation 


Tutorial 2 (Optional) : Simulation (contains all the scripts to simulate data and all simulation results)


Tutorial 3 : How to run and use eSMC2 (can estimate selfing, dormancy and recombination rate along with past variation of population size)


Tutorial 3 A : Best case convergence of eSMC2 under different Bottleneck scenario

Tutorial 3 B : Observed transition matrix of eSMC2 under different Bottleneck scenario

Tutorial 3 C : Best case convergence of eSMC2 using different sequence length

Tutorial 3 D : Running eSMC2 on simulated sequence data (msprime format output)

Tutorial 3 E : Running eSMC2 on real sequence data

Tutorial 3 F : Running eSMC2 on simulated sequence data (VCF format output)


Tutorial 4 : How to run and use teSMC (can estimate selfing and recombination rate through time along with past variation of population size)


Tutorial 4 A : Best case convergence of teSMC in estimating a transition to selfing 

Tutorial 4 B : Running teSMC on simulated sequence data (msprime format output) to estimate a transition to selfing 

Tutorial 4 C : Running teSMC on real sequence data to estimate a transition to selfing 

Tutorial 4 D : Running teSMC on simulated sequence data (VCF format) to estimate a transition to selfing 


Tutorial 5 : How to run and use the Sequentially Markovian Beta Coalescent (SMBC) (can estimate the alpha parameter of the Beta distribution along with the past variation of population size)


Tutorial 5 A : Best case convergence of SMBC in estimating the past demography, alpha and the recombination rate

Tutorial 5 B : Best case convergence of SMBC under neutral in estimating the past demography, alpha along the genome and the recombination rate

Tutorial 5 C : Best case convergence of SMBC in presence of strong positive selection in estimating the past demography, alpha along the genome and the recombination rate

Tutorial 5 D : Running SMBC on simulated sequence data (msprime output) to estimate alpha, the recombination rate and the past demography

Tutorial 5 E : Running SMBC on the output of ARGweaver to estimate alpha, the recombination rate and the past demography

Tutorial 6 : SMCtheo (runs the PSMC' on sequence data of theoretical marker)

Tutorial 7 : SMCm (runs the PSMC' on genome and methylome data)


Otherwise a quick one can be find below :

Input file description:

The input file for eSMC2 is the same as for eSMC, which is a "Segregating Matrix". The matrix must have M+2 lines (M is the number of haplotypes). The first M lines of the Segregating Matrix are the nucleotides of the M haplotypes at all the SNP positions (it can be encoded as nucleotide letters or as numbers). The M+1 line contains the number of site called between two segregatin sites (as in MSMC). The last line of the matrix contains the position on the sequence of the SNPs. The number of columns is thus equal to the number of SNPs. The Segregating Matrix can be built from a multihetsep file (https://github.com/stschiff/msmc/blob/master/guide.md) or from simulated data through functions of the package. 

How to use eSMC2:

Step one: Download or clone the repository eSMC2 (We recommand the use of the latest version). Extract the zip file.

Step two: Open the script install_eSMC2.R in Rstudio or a text editor. Make sure the path of the package (e.g. eSMC2_5.1.0.tar.gz) is correct (line 6), name of package may depend on it's version. If the package is in a different folder, modify the path to the correct folder. Execute the script to install the package on your local machine (by selecting everything and then clicking run in Rstudio).


Application to simulated data or real data :

eSMC2 can be used as eSMC, users can also follow the tutorial of eSMC (https://github.com/TPPSellinger/eSMC) for application to simulated sequence data or real sequence data. As eSMC is simpler than eSMC2, it might be easier to start with eSMC.


Tutorial for theoretical convergence :

We deliver 4 scripts explaining how to get the theoretical convergence. The script, simulate constant demographic scenarios. Feel free to modify them in order to study the demographic scenarios you are interested in. To optain the theoretical convergence of PSMC', you can download and run PSMC_theo.R. To obtain the heat plot, indacting if there is enough data for inference, run PSMC_heat.R. To check the theoretical convergence of MSMC, download and run  MSMC_theo.R. To obtain the heat plot for MSMC, indacting if there is enough data for inference, run MSMC_heat.R.

Regularization Penalty: 
You can specify the L1 and L2 parameter to penalyze variation of population size (However we do not recommend it, bounding the population size is recommended). Here is the formula:

LH=LH-L1(10^(abs(Log10(Xi)))-L2(10^(abs(Log10(Xi²)))

Where Xi is the vector of population size paramter (i.e. Xi_t=Ne_t/Ne_0).


Warnings: 

Computation time can be increased considerably if:
- more than one chromosome in one analysis is used
- more than 10 haplotypes are simultaneously analyzed
- more than 60 hidden states are used

If the following statements are true, poor results are to be expected:
- using less than 30 hidden states
- using sequence lengths smaller than 1 Mb
- using data with less than 1000 SNPs
- depending on the ecological parameters, the recombination rate can be undersetimated if, per base pair, the recombination rate is higher than the mutation rate 

It is important to note:
- Our method cannot distinguish self-fertilization from seed banks. Simultaneously estimating both varaibles without strong prior knowledge is not advised. 


If you encounter any issue or whish to add a feature, feel free to open an issue.
