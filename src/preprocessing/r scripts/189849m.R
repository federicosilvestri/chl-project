library(GEOquery)

data <- getGEO("GSE189849", GSEMatrix=TRUE)

pData(data[[1]])

mdata <- pData(data[[1]])

sup <- read.table(file='~/Desktop/Pisa/y2s2/chl/stuff/supdatasets/GSE189849_raw_counts.txt', header = TRUE)

genes = sup[,1]
tsup = transpose(sup[,2:10])
rownames(tsup) = colnames(sup[,2:10])
colnames(tsup) = genes
write.table(tsup, "~/Desktop/Pisa/y2s2/chl/stuff/mdatasets/eGSE189849m.csv", col.names = NA)

###


data <-read.csv(file='~/Desktop/Pisa/y2s2/chl/prj/chl-prj/dataset/eGSE189849m.csv',sep="",header=TRUE)
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

write.table(data, "~/Desktop/Pisa/y2s2/chl/prj/chl-prj/dataset/eGSE189849m.csv", sep=",", col.names=NA)

