from datasets import load_dataset

def load_combined_dataset():
    bc5cdr_dataset = load_dataset("tner/bc5cdr")
    ncbi_dataset = load_dataset("ncbi_disease")
    combined_train_dataset = concatenate_datasets([bc5cdr_dataset["train"], ncbi_dataset["train"]])
    combined_validation_dataset = concatenate_datasets([bc5cdr_dataset["validation"], ncbi_dataset["validation"]])
    combined_test_dataset = concatenate_datasets([bc5cdr_dataset["test"], ncbi_dataset["test"]])
    return combined_train_dataset, combined_validation_dataset, combined_test_dataset
