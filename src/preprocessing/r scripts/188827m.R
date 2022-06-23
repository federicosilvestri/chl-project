library(GEOquery)
library(data.table)

data <- getGEO("GSE188827", GSEMatrix=TRUE)

sup <- read.csv(file='~/Desktop/Pisa/y2s2/chl/prj/supdatasets/GSE188827_Alg_Expression_raw_counts.csv', sep = ",")
tsup <- transpose(sup)
genes = tsup[1,2:45369]
patientsid = list("6A_Alg",	"6A_2D", "6D_Alg",	"6D_2D",	"6F_Alg",	"E87_2D",	"6F_2D",	"D13_Alg",	
                  "D13_2D",	"D94_Alg",	"D94_2D",	"E75_Alg",	"E75_2D",	"E87_Alg")
patientsexpr <- tsup[3:16,2:45369]
df = data.frame(patientsexpr)
colnames(df) = genes
rownames(df) = patientsid
write.csv(df, "~/Desktop/Pisa/y2s2/chl/prj/mdatasets/eGSE188827m.csv")

pData(data[[1]])

patients <- pData(data[[1]])
p <- endsWith(pData(data[[1]])$title, "Aggrewell")
q <- endsWith(pData(data[[1]])$title, "AlgGroup_2D")
r = !(p+q)
patients <- pData(data[[1]])[r,]

write.csv(patients, "~/Desktop/Pisa/y2s2/chl/prj/mdatasets/pGSE188827m.csv")
