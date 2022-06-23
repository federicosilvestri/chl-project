library(GEOquery)

data <- getGEO("GSE25462", GSEMatrix=TRUE)

pData(data[[1]])

t<-endsWith(pData(data[[1]])$characteristics_ch1.3, "DM")

mdata <- pData(data[[1]])[t,]

expr <- t(exprs(data[[1]]))
expr <- subset(expr, rownames(expr) %in% rownames(mdata))

#write.csv(mdata, "~/Desktop/Pisa/y2s2/chl/prj/mdatasets/pGSE25462m.csv")
write.table(expr, "~/Desktop/Pisa/y2s2/chl/prj/mdatasets/eGSE25462m.csv", col.names=NA)


###


data <- read.csv(file='~/Desktop/Pisa/y2s2/chl/prj/chl-prj/dataset/eGSE25462m.csv',sep="",header=TRUE)

rownames(data) <- data$X
data <- data[,2:ncol(data)]
colnames(data) <- sub("^X", "", colnames(data))

library(hgu133plus2.db)
# Get gene symbol
x <- hgu133plus2SYMBOL
# Get the probe identifiers that are mapped to a gene name
mapped_probes <- mappedkeys(x)
# Convert to a list
xx <- as.list(x[mapped_probes])
# Transform matrix in a table
ref_gene <- do.call(rbind, xx)
ref_gene <- as.data.frame(ref_gene)
# Add column to get a reference between old and new gene
ref_gene$old_gene <- rownames(ref_gene)
colnames(ref_gene) <- c("new_gene", "old_gene")
# Make smaller table to speedup the translation
ref_gene_data <- data.frame(colnames(data))
colnames(ref_gene_data) <- c("old_gene")
ref_gene <- merge(x=ref_gene, y=ref_gene_data, by="old_gene")
# Get Gene Symbol from platform columns
new_col <- c()
for (i in colnames(data)) {
  new_col <- append(new_col, ref_gene[ref_gene$old_gene == i, 'new_gene'])
}

colnames(data) <- new_col

data[1:5,1:5]

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

write.table(data, "~/Desktop/Pisa/y2s2/chl/prj/chl-prj/dataset/eGSE25462m.csv", sep=",", col.names=NA)
