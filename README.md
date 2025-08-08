# Semantic Code Search with Mistral AI

This command-line tool leverages the `codestral-embed` model from Mistral AI to perform semantic searches across a set of local files. Instead of relying on keyword matching, it finds the most contextually relevant file based on a natural language problem description, making it an efficient way to navigate and understand a codebase.

You can provide it with a list of files and a query, and it will rank the files based on how semantically similar their content is to your query.

## Features

- **Dynamic Querying:** Interactively prompts for a search query every time it's run.
- **Semantic Understanding:** Uses Mistral AI's powerful `codestral-embed` model to understand the context of both the code and the query.
- **Ranked Results:** Calculates a similarity score for each file and presents a ranked list, highlighting the top match.
- **Secure API Key Entry:** Uses `getpass` to ensure your Mistral API key is not displayed on the screen as you type it.

## How It Works

The script follows a straightforward process:

1. **Input:** Securely prompts for your Mistral API Key. Then asks for a list of file paths and a natural language query (a "problem statement").
2. **Embedding:** The content of each file and the query are converted into numerical vector representations (embeddings) using the `codestral-embed` model.
3. **Similarity Calculation:** Computes the cosine similarity between the query's embedding and each file's embedding. A higher score (closer to 1.0) signifies a stronger contextual match.
4. **Ranking:** Files are ranked according to their similarity scores, and the results are printed to the console.

## Prerequisites

- Python 3.7+
- A Mistral AI account and API Key.

## Installation

### Clone the Repository
```bash
git clone <your-repository-url>
cd <your-repository-name>
```

### Create a requirements.txt file
Create a file named `requirements.txt` and paste the following dependencies into it:

```
mistralai
sentence-transformers
numpy
tqdm
datasets
langchain
faiss-cpu
huggingface_hub
mistral-common
```

### Install Dependencies
Install all the required libraries using pip:
```bash
pip install -r requirements.txt
```

## Usage

Run the script from your terminal:
```bash
python embed_demo.py
```
You will be prompted to enter your credentials and search parameters in sequence:

- First, enter your Mistral API Key.
- Next, provide the comma-separated names of the files you wish to search.
- Finally, type the problem description you want to search for.

### Example Session
```bash
$ python embed_demo.py
Enter your MISTRAL_API_KEY: ················
Enter all file names (comma-separated): database_manager.py, api_routes.py, utils.py
Enter the problem statement: a function that formats user data before saving it to the database

All file similarity scores:
utils.py: 0.8152
database_manager.py: 0.5634
api_routes.py: 0.3411

Top match:
utils.py (Score: 0.8152)
```
## Demo Video
