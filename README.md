# GitHub Repository Language Analyzer

## Overview

This Python script allows you to analyze the programming languages used in a GitHub user's repositories and those of the users they are following. It calculates the percentage of each programming language across these repositories, providing insights into coding preferences and expertise not only for the user but also for their network.

## Features

- Retrieve and analyze the language statistics of a GitHub user's repositories and those they are following.
- Calculate the percentage of each programming language used across these repositories.
- Handle cases where languages are not present in some repositories.
- Ensure that the total percentage sums to 100% with optional rounding.
- Present the results in a clear and visually appealing table.

## Usage

1. Obtain a GitHub access token.
2. Rename the file named `.env.example` to `.env`.
3. Set the value of `GITHUB_ACCESS_TOKEN` in the `.env` file.
4. Run the script to analyze the user's repositories.
5. Additionally, analyze repositories of users the user is following.

Example usage:

```python
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 script.py
```
