library(GEOquery)
library(data.table)

data <- getGEO("GSE176230", GSEMatrix=TRUE)

sup <- read.csv(file='~/Desktop/Pisa/y2s2/chl/prj/supdatasets/GSE176230_all.fpkm_anno.csv', sep="\t")
tsup <- transpose(sup)
genes = tsup[75,]
patientsid = c("X2.0T_FPKM", "X4.0T_FPKM","X6.0T_FPKM" ,"X9.0T_FPKM" ,"X10.0T_FPKM" ,
               "X11.0T_FPKM","X14.0T_FPKM","X15.0P_FPKM","X16.0T_FPKM","X17.0T_FPKM",  
               "X18.0P_FPKM","X19.0T_FPKM","X20.0T_FPKM","X21.0P_FPKM","X22.0P_FPKM",
               "X24.0P_FPKM","X25.0P_FPKM")
patientsexpr = transpose(sup[patientsid])
df = data.frame(patientsexpr)
colnames(df) = genes
rownames(df) = patientsid
write.table(df, "~/Desktop/Pisa/y2s2/chl/prj/mdatasets/eGSE176230m.csv",col.names=NA)


pData(data[[1]])

t<-endsWith(pData(data[[1]])$treatment, ")")

mdata <- pData(data[[1]])[t,]

write.csv(mdata, "~/Desktop/Pisa/y2s2/chl/prj/mdatasets/pGSE176230m.csv")

###


data <-read.csv(file='~/Desktop/Pisa/y2s2/chl/prj/chl-prj/dataset/eGSE176230m.csv',sep="",header=TRUE)
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

write.table(data, "~/Desktop/Pisa/y2s2/chl/prj/chl-prj/dataset/eGSE176230m.csv", sep=",", col.names=NA)
