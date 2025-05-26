import numpy as np
import scanpy as sc

def remove_noncoding(df): #Removes non-coding genes based on literature
    
    noncoding = []
    
    for column in df.columns:
        if column.startswith("MIR"):
            noncoding.append(column)
        elif column.startswith("LINC"):
            noncoding.append(column)
        elif column.startswith("RNU"):
            noncoding.append(column)

    df.drop(columns = noncoding, inplace = True)
    return df

def remove_duplicates(df):

    df = np.transpose(df)

    duplicate_genes = df[df.duplicated(keep = False)]
    print("The number of duplicate genes is", duplicate_genes.shape[0])

    if duplicate_genes.shape[0] != 0:

        print("The duplicated genes are", duplicate_genes.index)

        df = df.drop_duplicates(keep = 'first')

        removed_genes = []
        for gene in duplicate_genes.index:
            if gene not in df.index:
                removed_genes.append(gene)

        print("The removed genes are", removed_genes)

        df = np.transpose(df)
        return df

def sparsity_threshold(df): # Calculates the sparisity threshold and removes columns where sparsity is too high

    for n in [i/10 for i in range(1, 11)]:
        high_sparsity = []
        for column in df.iloc[:,2:]:
            sparsity = (df[column] == 0).mean()
            if sparsity > n:
                high_sparsity.append(column)
        if "CA9" not in high_sparsity:
            break
    
    print("The sparsity threshold chosen is", n*100,'%')

    if n != 1:

        df.drop(columns = high_sparsity, inplace = True)
        return df
    
    else: 
        return df

def remove_mito(adata): #finds and removes columns with high mitochondrial count

    adata_copy = adata.copy()
 
    adata_copy.var["mt"] = adata_copy.var_names.str.startswith('MT')

    sc.pp.calculate_qc_metrics(
        adata_copy, qc_vars=["mt"], inplace=True, log1p=False)
    
    sc.pl.violin(
        adata_copy,
        ["n_genes_by_counts", "total_counts", "pct_counts_mt"],
        jitter=0.4,
        multi_panel=True,)

    mito_mask = adata_copy.obs['pct_counts_mt'] < 5
    adata_filtered = an.AnnData(
        X=adata_copy[mito_mask].X.copy(),
        obs=adata_copy.obs[mito_mask].copy(),
        var=adata_copy.var.copy()
    )
    
    return adata_filtered

def newindex(index): #Reindexing for easier cleaning
    match = re.search(r'_(\w+_\w\d+)',index)
    return match.group(1)

def update_index(index, cell_name, cell_line): #Updating index for easier cleaning
    if 'Hypo' in index:
        return f'Hypoxia_{cell_name}' 
    elif 'Norm' in index:
        return f'Normoxia_{cell_name}'
    return index

''' The below functions are due to an issue in the specific dataset that I used and should not be intended as general'''
def condition_smartseq(index): #
    match = re.search(r'(\w+)_',index)
    
    if match.group(1) == "Hypoxia":
        return 1
    elif match.group(1) == "Normoxia":
        return 0

def condition_dropseq(index):
    match = re.search(r'_(\w+)',index)
    
    if match.group(1) == "Hypoxia":
        return 1
    elif match.group(1) == "Normoxia":
        return 0

