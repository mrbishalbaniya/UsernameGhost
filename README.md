# UsernameGhost: Powerful Social Media Username Search Tool

![Social Media Username Search]  

## Overview

**UsernameGhost** is a cutting-edge tool designed for quick and accurate **social media username search** across multiple platforms. Whether you're a **cybersecurity researcher**, **digital marketer**, or just someone interested in **tracking usernames** online, UsernameGhost provides an efficient solution for finding where a specific username is used on popular social media networks.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
   - [Requirements](#requirements)
   - [Clone the Repository](#clone-the-repository)
3. [Usage](#usage)
4. [Contributing](#contributing)
5. [License](#license)

## Features

- **Fast Username Search**: Quickly checks multiple social media platforms for the given username.
- **Real-time Progress Bar**: Monitor the search status with an interactive progress bar.
- **Results in JSON**: Saves the found usernames and URLs in a clean, easy-to-read JSON file.
- **Focused Output**: Displays only the **available usernames** and their corresponding URLs, filtering out the unavailable ones.

## Installation

### Requirements

Before you start using **UsernameGhost**, ensure you have the following prerequisites installed:

- **Python 3.x**: The latest version of Python is recommended.
- **Python Libraries**: Install the required libraries using `pip`:


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
