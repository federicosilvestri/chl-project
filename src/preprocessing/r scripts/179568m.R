library(GEOquery)
library(data.table)

data <- getGEO("GSE179568", GSEMatrix=TRUE)

#write.csv(sup, "~/Desktop/Pisa/y2s2/chl/prj/mdatasets/temp.csv")

p<-startsWith(pData(data[[1]])$title, "PDR")

patients <- pData(data[[1]])[p,]

sup <- read.csv(file='~/Desktop/Pisa/y2s2/chl/prj/supdatasets/GSE179568_data.csv', sep = ";")
tsup <- transpose(sup)
genes <- t(sup[,1])
#columnnames = c("Patients", genes)
patientsid = list("PDR S1", "PDR S2", "PDR S3", "PDR S4", "PDR S5", "PDR S6", "PDR S7")
patientsexpr <- tsup[6:12,]
df = data.frame(patientsexpr)
colnames(df) = genes
rownames(df) = patientsid
#genes_new=cbind(c("Patient name"), genes)
write.csv(df, "~/Desktop/Pisa/y2s2/chl/prj/mdatasets/eGSE179568m.csv")

write.csv(mdata, "~/Desktop/Pisa/y2s2/chl/prj/mdatasets/pGSE179568m.csv")

###
library(dplyr)

data <-read.csv2(file='~/Desktop/Pisa/y2s2/chl/prj/chl-prj/dataset/eGSE179568m.csv',sep=",",header=TRUE)
rownames(data) <- data$X
data <- data[,2:ncol(data)]
colnames(data) <- sub("^X", "", colnames(data))
# Remove NA
data <- data[, colSums(is.na(data)) == 0]
# Remove columns with all 0s
data <- data[, colSums(data) > 0]
# Remove columns without gene symbol
data <- data[,nzchar(colnames(data))]
# Remove double names genes (GENE1 /// GENE2)
colnames(data) <- gsub(" ///.*", "", colnames(data))
# Make all columns uppercase
colnames(data) <- toupper(colnames(data))
# Remove columns which start by "NA" because they didn't refer to any gene
null_columns <- grep("NA.", colnames(data))
data <- data[,-null_columns]

write.table(data, "~/Desktop/Pisa/y2s2/chl/prj/chl-prj/dataset/eGSE179568m.csv", sep=",", col.names=NA)
