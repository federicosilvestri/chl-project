library(GEOquery)
library(data.table)

data <- getGEO("GSE171276", GSEMatrix=TRUE)

pData(data[[1]])

sup <- read.table(file='~/Desktop/Pisa/y2s2/chl/prj/supdatasets/MO_Experiment_FCDI.txt', header = TRUE)
genes = sup[,2]
tsup = transpose(sup[,3:10])
rownames(tsup) = colnames(sup[,3:10])
colnames(tsup) = genes
write.table(tsup, "~/Desktop/Pisa/y2s2/chl/prj/mdatasets/eGSE171276m.csv", col.names=NA)
