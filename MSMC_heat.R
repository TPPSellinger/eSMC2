###################
# Source function #
###################
library(eSMC2)
#install.packages("scrm")
library(scrm)
#install.packages("plot.matrix")
library('plot.matrix')
########
#Script#
########

# Set a working directory 
setwd("~/scrm_data")

# Parameters 

M=4 # number of sequences
L=10^7 # Sequence length
nsim=10 # number of iteration
Pop=10^4 # current effective population size
mu=1.25* 10^-8 #mutation rata
r=10^-7  #recombination rate

theta=4*Pop*mu*L
rho=4*Pop*r*L
n=30 # number of hidden state
# Creating scenario

command_simu=paste(M,1,"-t",theta,"-r",rho,L,sep=" ")
# add parameter for demographic scenario here 
# example for bottleneck : command_simu=paste(command_simu," -eN 0.2 0.1 -eN 0.5 1 " ,sep="")   
command_simu=paste(command_simu," -T -p 10" ,sep="")  
#name of the file to read 
name="MSMC_theo.txt"

# Object containing output file

mu_ex=matrix(0,ncol = nsim,nrow=1)
rm_ex=matrix(0,ncol = nsim,nrow=1)
results=list()

for(x in 1:nsim){
  scrm(command_simu,name)
  result=Optimize_MM_N(file=name,theta = theta,gamma=1,L=L,n=n,ER=T,Pop=T,Boxr=c(1,1),pop_vect=NA,NC=1,M_a=M,mut=T,Correct_window=T)
  results[[(1+length(results))]]=result
}



N=numeric(n*n*0.5*M*(M-1)*0.5*M*(M-1))
for(x in 1:nsim){
  N=cbind(N,as.numeric(results[[x]]$N))
}

N=N[,-1]
for(x in nsim){
  N[which(is.na(as.numeric(N[,x]))),x]<-0
}
N_heat=matrix(c(apply(N,1,sd)/apply(N,1,mean)),nrow = n*0.5*M*(M-1),ncol = n*0.5*M*(M-1))
plot(N_heat)

