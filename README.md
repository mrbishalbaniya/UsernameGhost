## UsernameGhost
UsernameGhost is a Python tool that searches for a given username across multiple social media platforms. It checks various sites to see if the username exists and organizes the results into "Available," "Not Available," and "Errors" categories. The results are also saved to a JSON file for further analysis.

## Features
Username Search Across Multiple Platforms: Quickly check if a username is available across various social media platforms.
Progress Bar: A progress bar is displayed to show the search status for each platform.
Organized Output: The results are categorized into Available, Not Available, and Errors.
JSON Output: Saves the results in a well-structured JSON file.

## Prerequisites
Python 3.x
requests library
tqdm library (for the progress bar)

## Installation
On Linux/Termux
Install Dependencies: Ensure you have Python 3, and the required libraries installed. If not, install them using:

bash
```bash
sudo apt update
sudo apt install python3 python3-pip
pip3 install requests tqdm
```
## Clone the Repository:

```bash
git clone https://github.com/mrbishalbaniya/usernameghost.git
cd usernameghost
```

## On Windows
Install Dependencies: Ensure you have Python 3 and the required libraries installed. If not, install them using:

```python
python -m pip install requests tqdm
```
Clone the Repository:

```bash
git clone https://github.com/your-repository/usernameghost.git
cd usernameghost
```
## Usage
Command Line
To search for a username, run:

```python 
python UsernameGhost.py <username>
```
Replace <username> with the username you want to search.

## Example
```python

python UsernameGhost.py mrbishalbaniya
```
The script will check for the username across various social media platforms and display the found URLs, categorized into "Available," "Not Available," and "Errors." The results will be saved in a file named mrbishalbaniya.json.

## Configuration
Sites Configuration
The list of social media sites and their URL templates are stored in the sites.json file. You can add or remove sites by modifying this file. The URL templates should use {username} as a placeholder for the username.

Example sites.json Format:

```json 
{
    "Twitter": "https://twitter.com/{username}",
    "Instagram": "https://www.instagram.com/{username}/",
    "Facebook": "https://www.facebook.com/{username}"
    // Add more sites...
}
```
## Progress Bar
The script uses tqdm to display a progress bar while searching.

## Troubleshooting
"Not Available" URLs: This indicates that the username was not found on the given platform.
"Errors" Messages: Issues with network requests or site availability. Check your internet connection or the site’s status.
