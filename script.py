import os
from dotenv import load_dotenv
from github import Github, Auth
from tabulate import tabulate

# # # # # # # # # # # # # # # # # # # # # # # # #

# Load environment variables from .env file
load_dotenv()

# Using an access token
auth = Auth.Token(os.getenv('GITHUB_ACCESS_TOKEN'))

# Public Web Github
g = Github(auth=auth)

# # # # # # # # # # # # # # # # # # # # # # # # #

def fetch_and_calculate_languages_for_repos(user):
     """
     Fetches the language information for each repository owned by the user and calculates the total count
     for each repository. This function is used to process and analyze the programming languages used
     in the user's repositories.

     Args:
          user (github.NamedUser.NamedUser): The GitHub user for which to analyze repositories.
     """

     print(f'user: {user.name}')

     # Dictionary to store language counts and their percentages
     languages = {}

     for repo in user.get_repos(type='owner'):
          # Get the language information for each repo
          repo_languages = repo.get_languages()

          # Calculate the total count for this repo
          total_count = sum(repo_languages.values())
     
          # Update the language percentages
          for language, count in repo_languages.items():
               percentage = (count / total_count) * 100
               if language in languages:
                    # Update the existing language's percentage
                    languages[language] = (languages[language] + percentage) / 2
               else:
                    # Add a new language to the dictionary
                    languages[language] = percentage

          # Update the languages percentages that not exist in current repo
          for language in set(languages.keys()) - set(repo_languages.keys()):
               languages[language] = (languages[language] + 0) / 2

     # Sort the languages by percentage in descending order
     sorted_languages = {k: v for k, v in sorted(languages.items(), key=lambda item: item[1], reverse=True)}

     # Initialize a variable to accumulate the total percentage of languages used in repositories
     total_percentage = 0

     # Create a list to store the data for the table
     table_data = []

     # Format the result for the table
     for language, percentage in sorted_languages.items():
          total_percentage += percentage
          table_data.append([language, f'{percentage:.2f}%'])

     # Ensure the total_percentage is exactly 100% by rounding
     total_percentage = round(total_percentage, 2)

     # Define the headers for the table
     table_headers = ['Language', 'Percentage']

     # Print the table
     print(tabulate(table_data, headers=table_headers, tablefmt="grid"))

     # Print the accumulated total percentage of languages used across all repositories
     print(f'TOTAL: {total_percentage:.0f}% \n\n')

# # # # # # # # # # # # # # # # # # # # # # # # #

# Get the user
user = g.get_user()
fetch_and_calculate_languages_for_repos(user=user)

# Get the user's following
user_following = user.get_following()
for following in user_following:
     fetch_and_calculate_languages_for_repos(user=following)

# # # # # # # # # # # # # # # # # # # # # # # # #

# Close the connection
g.close()
