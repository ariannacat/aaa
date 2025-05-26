import numpy as np
''' The below functions are due to an issue in the specific dataset that I used and should not be intended as general'''

def newindex(index): #Reindexing for easier cleaning
    match = re.search(r'_(\w+_\w\d+)',index)
    return match.group(1)

def update_index(index, cell_name, cell_line): #Updating index for easier cleaning
    if 'Hypo' in index:
        return f'Hypoxia_{cell_name}' 
    elif 'Norm' in index:
        return f'Normoxia_{cell_name}'
    return index

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

def hypoxic_cells(df):

    n = df.shape[0]
    n_hypo = 0

    for i in df["Condition"]:
        if i == 1:
            n_hypo = n_hypo + 1
    
    prop = n_hypo/n
    return prop

def data_cleaning(df_filtered):
    """
    Cleans and prepares dataframe for analysis:
    - Strips quotes from index
    - Transposes and reindexes
    - Extracts condition and inserts metadata
    - Applies dataset-specific preprocessing
    """

    # Clean index
    df_filtered.index = [x.strip('"') for x in df_filtered.index]

    # Transpose and clean again
    df_filtered = df_filtered.transpose()
    df_filtered.index = [x.strip('"') for x in df_filtered.index]

    # Apply new indexing
    df_filtered.index = [newindex(index) for index in df_filtered.index]
    print("Index Changed")

    # Assign condition labels
    df_filtered.insert(0, 'Condition', [condition_smartseq(index) for index in df_filtered.index])
    print("Condition Included")

    # Add placeholder for cell line info
    df_filtered.insert(1, 'Cell Line', 'cell line')

    # Apply hypoxia-specific processing
    hypoxic_cells(df_filtered)

    return df_filtered
