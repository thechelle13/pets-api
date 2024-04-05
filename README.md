# Python + Django

## Community Pets - Project README

## Introduction

This project is a practice API created for a previous front-end capstone project. It serves as a backend for managing pets and related data.

## Project Origin

As a professional pet sitter, I often have clients ask for sits when I am unavailable. I thought it would be cool if I could connect my clients in one spot so that when I am not available for sits, they could trade sits with each other.

## Planning

An Entity-Relationship Diagram (ERD) of base information was designed to include the users, who can create a profile, add their pets, or edit either entity within the UI while keeping their information only visible to the user who is logged in at the time. The structure of the post includes relevant information but does not share the user's information, allowing responses on the site in a comment, response, and like ability.

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository_url>

   cd community-pets
   pip install -r requirements.txt
   python manage.py migrate

   python manage.py runserver

## ERD:  
https://dbdiagram.io/d/My-page-API-64ff5c7302bd1c4a5e5d5bb6


## Testing with Postman

1. **Install Postman from [https://www.postman.com/downloads/](https://www.postman.com/downloads/).**

2. **Open Postman and import the collection file `community_pets.postman_collection.json` provided in the project.**

3. **Use the imported collection to test the API endpoints. Make sure the Django development server is running.**


Feel free to adjust the formatting or add more details as needed. Let me know if you need further assistance!







