library(GEOquery)

data <- getGEO("GSE185190", GSEMatrix=TRUE)

pData(data[[1]])

p<-endsWith(pData(data[[1]])$characteristics_ch1.3, ")")
q<-endsWith(pData(data[[1]])$characteristics_ch1.5, "Yes")
r=(p+q)==2

mdata <- pData(data[[1]])[r,]

sup1 <- read.table(file='~/Desktop/Pisa/y2s2/chl/stuff/supdatasets/Subject03_Time2_B.txt', header = TRUE)
sup2 <- read.table(file='~/Desktop/Pisa/y2s2/chl/stuff/supdatasets/Subject03_Time2_CD4T.txt', header = TRUE)
sup3 <- read.table(file='~/Desktop/Pisa/y2s2/chl/stuff/supdatasets/Subject03_Time2_CD8T.txt', header = TRUE)
sup4 <- read.table(file='~/Desktop/Pisa/y2s2/chl/stuff/supdatasets/Subject03_Time2_NK.txt', header = TRUE)

sup5 <- read.table(file='~/Desktop/Pisa/y2s2/chl/stuff/supdatasets/Subject03_Time2_B.txt', header = TRUE)
sup6 <- read.table(file='~/Desktop/Pisa/y2s2/chl/stuff/supdatasets/Subject03_Time2_CD4T.txt', header = TRUE)
sup7 <- read.table(file='~/Desktop/Pisa/y2s2/chl/stuff/supdatasets/Subject03_Time2_CD8T.txt', header = TRUE)
sup8 <- read.table(file='~/Desktop/Pisa/y2s2/chl/stuff/supdatasets/Subject03_Time2_NK.txt', header = TRUE)

sup9  <- read.table(file='~/Desktop/Pisa/y2s2/chl/stuff/supdatasets/Subject04_Time2_B.txt', header = TRUE)
sup10 <- read.table(file='~/Desktop/Pisa/y2s2/chl/stuff/supdatasets/Subject04_Time2_CD4T.txt', header = TRUE)
sup11 <- read.table(file='~/Desktop/Pisa/y2s2/chl/stuff/supdatasets/Subject04_Time2_CD8T.txt', header = TRUE)
sup12 <- read.table(file='~/Desktop/Pisa/y2s2/chl/stuff/supdatasets/Subject04_Time2_NK.txt', header = TRUE)

sup13 <- read.table(file='~/Desktop/Pisa/y2s2/chl/stuff/supdatasets/Subject06_Time2_B.txt', header = TRUE)
sup14 <- read.table(file='~/Desktop/Pisa/y2s2/chl/stuff/supdatasets/Subject06_Time2_CD4T.txt', header = TRUE)
sup15 <- read.table(file='~/Desktop/Pisa/y2s2/chl/stuff/supdatasets/Subject06_Time2_CD8T.txt', header = TRUE)
sup16 <- read.table(file='~/Desktop/Pisa/y2s2/chl/stuff/supdatasets/Subject06_Time2_NK.txt', header = TRUE)

sup17 <- read.table(file='~/Desktop/Pisa/y2s2/chl/stuff/supdatasets/Subject11_Time2_B.txt', header = TRUE)
sup18 <- read.table(file='~/Desktop/Pisa/y2s2/chl/stuff/supdatasets/Subject11_Time2_CD4T.txt', header = TRUE)
sup19 <- read.table(file='~/Desktop/Pisa/y2s2/chl/stuff/supdatasets/Subject11_Time2_CD8T.txt', header = TRUE)
sup20  <- read.table(file='~/Desktop/Pisa/y2s2/chl/stuff/supdatasets/Subject11_Time2_NK.txt', header = TRUE)

genes = sup1[,1]
datasets=rbind(sup1[,3],sup2[,3],sup3[,3],sup4[,3],sup5[,3],sup6[,3],sup7[,3],sup8[,3],sup9[,3],sup10[,3],
           sup11[,3],sup12[,3],sup13[,3],sup14[,3],sup15[,3],sup16[,3],sup17[,3],sup18[,3],sup19[,3],sup20[,3])
rownames(datasets) = rownames(mdata)
colnames(datasets) = genes
  
write.table(datasets, "~/Desktop/Pisa/y2s2/chl/stuff/mdatasets/eGSE185190m.csv", col.names = NA)
#write.csv(mdata, "~/Desktop/Pisa/y2s2/chl/stuff/mdatasets/pGSE185190m.csv")
