library(GEOquery)
library(data.table)

data <- getGEO("GSE174475", GSEMatrix=TRUE)

sup <- read.table(file='~/Desktop/Pisa/y2s2/chl/prj/supdatasets/GSE174475_expr.txt')
genes <- rownames(sup)
patients <- colnames(sup)
tsup <- transpose(sup)
colnames(tsup) = genes
rownames(tsup) = patients
write.table(tsup, "~/Desktop/Pisa/y2s2/chl/prj/mdatasets/eGSE174475m.csv", col.names=NA)


pData(data[[1]])

mdata <- pData(data[[1]])

write.csv(mdata, "~/Desktop/Pisa/y2s2/chl/prj/mdatasets/pGSE174475m.csv")


###


data <-read.csv(file='~/Desktop/Pisa/y2s2/chl/prj/chl-prj/dataset/eGSE174475m.csv',sep="",header=TRUE)
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

write.table(data, "~/Desktop/Pisa/y2s2/chl/prj/chl-prj/dataset/eGSE174475m.csv", sep=",", col.names=NA)

