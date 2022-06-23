library(GEOquery)
library(data.table)

data <- getGEO("GSE117146", GSEMatrix=TRUE)

pData(data[[1]])

p<-startsWith(pData(data[[1]])$characteristics_ch1.2, "treatment: none")
q<-startsWith(pData(data[[1]])$characteristics_ch1.2, "treatment: Untreated")
r<-p+q
r = r==1
patientsid <- pData(data[[1]])[r,]

sup <- read.table(file='~/Desktop/Pisa/y2s2/chl/prj/supdatasets/GSE117146_data-voom.txt', header = TRUE)
genes <- sup[,2]
#patients <- colnames(sup)
tsup <- transpose(sup)
tsup<-tsup[3:80,]
#expr <- subset(expr, rownames(expr) %in% rownames(patients))
patients <- subset(tsup, patients %in% patientsid$title)
rownames(patients) = patientsid$title
colnames(patients) = genes
#write.table(patients, "~/Desktop/Pisa/y2s2/chl/prj/mdatasets/eGSE117146m.csv", col.names=NA)


###

data<-read.csv(file='~/Desktop/Pisa/y2s2/chl/prj/chl-prj/dataset/eGSE117146m.csv',sep="",header=TRUE)


rownames(data) <- data$X
data <- data[,2:ncol(data)]

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

write.table(data, "~/Desktop/Pisa/y2s2/chl/prj/chl-prj/dataset/eGSE117146m.csv", sep=",", col.names=NA)
