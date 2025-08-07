# Semantic-Code-Searcher
Semantic Code Search with Mistral AI

This command-line tool leverages the codestral-embed model from Mistral AI to perform semantic searches across a set of local files. Instead of relying on keyword matching, it finds the most contextually relevant file based on a natural language problem description, making it an efficient way to navigate and understand a codebase.

You can provide it with a list of files and a query, and it will rank the files based on how semantically similar their content is to your query.

Features

    Dynamic Querying: Interactively prompts for a search query every time it's run.

    Semantic Understanding: Uses Mistral AI's powerful codestral-embed model to understand the context of both the code and the query.

    Ranked Results: Calculates a similarity score for each file and presents a ranked list, highlighting the top match.

    Secure API Key Entry: Uses getpass to ensure your Mistral API key is not displayed on the screen as you type it.

How It Works

The script follows a straightforward process:

    Input: It securely prompts for your Mistral API Key. It then asks for a list of file paths and a natural language query (a "problem statement").

    Embedding: The content of each file and the query are converted into numerical vector representations (embeddings) using the codestral-embed model.

    Similarity Calculation: It computes the cosine similarity between the query's embedding and each file's embedding. A higher score (closer to 1.0) signifies a stronger contextual match.

    Ranking: The files are ranked according to their similarity scores, and the results are printed to the console.

Prerequisites

    Python 3.7+

    A Mistral AI account and API Key.
