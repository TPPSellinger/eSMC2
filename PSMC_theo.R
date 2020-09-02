###################
# Source function #
###################
library(eSMC2)
#install.packages("scrm")
library(scrm)
########
#Script#
########

# Set a working directory 
setwd("~/scrm_data")

# Parameters 

M=2 # number of sequences
L=10^8 # Sequence length
nsim=1 # number of iteration
Pop=10^4 # current effective population size
mu=1.25* 10^-8 #mutation rata
r=10^-8  #recombination rate

theta=4*Pop*mu*L
rho=4*Pop*r*L

# Creating scenario

command_simu=paste(M,1,"-t",theta,"-r",rho,L,sep=" ")
# add parameter for demographic scenario here 
# example for bottleneck : command_simu=paste(command_simu," -eN 0.2 0.1 -eN 0.5 1 " ,sep="")   
command_simu=paste(command_simu," -T -p 10" ,sep="")  
#name of the file to read 
name="PSMC_theo.txt"

# Object containing output file

mu_ex=matrix(0,ncol = nsim,nrow=1)
rm_ex=matrix(0,ncol = nsim,nrow=1)
results=list()

for(x in 1:nsim){
  scrm(command_simu,name)
  result=Optimize_N(file=name,theta = theta,Rho = rho,L=L,n=40,ER=T,Pop=T,Boxr=c(1,1),pop_vect=NA,mut=T,Correct_window=T)
  results[[(1+length(results))]]=result
  rm_ex[1,x]=(result$rho/(result$mu)) 
  mu_ex[1,x]=result$mu
}


plot(c(10,10^6),c(1,1), log=c("x"), ylim =c(3,5) ,
     type="n", xlab= paste("Generations ago",sep=" "), ylab="population size (log10)",main = "")
for(x in 1:nsim){
  Pop_=mu_ex[1,x]/(mu)
  lines((results[[x]]$Tc*Pop_), log10((results[[x]]$Xi)*0.5*Pop_), type="s", col="red")
  
}
abline(h=log10(Pop), col="black")
title(" Theoretical convergence of PSMC' ")

