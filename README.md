# TechFest

A basic registration website built with HTML, CSS, and JavaScript for the frontend. It allows students to register their details for participation in a Techfest. This project was developed to offer students an alternative registration experience to traditional forms like Google Forms.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Setup and Usage](#setup-and-usage)
- [Contributors](#contributors)
- [License](#license)

## Features 

- ✅ **Easy Student Registration** – A seamless and hassle-free registration process for students.  
- ✅ **Choose Your Event** – Students can easily browse and select the event they want to participate in.  
- ✅ **Manual Payment with Organized Summary** – Added a manual payment method with a well-structured summary and detailed information for better clarity.  
- ✅ **Admit Card After Payment** – Upon successful payment, students will receive an admit card confirming their participation.  

# Easy Student Registration
![TechFest Preview](../x-assets/Image1.png)
# Choose Your Event
![TechFest Preview](../x-assets/Image3.png)
# Manual Payment with Organized Summary
![TechFest Preview](../x-assets/Image2.png)

## Technologies Used
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Backend:** Django
- **Database:** SQLite 

## Installation
To set up and run this project locally, follow these steps:

### Prerequisites
Make sure you have the following installed:
- Python (>=3.8)
- Django (latest stable version)


### Clone the Repository
```sh
git clone https://github.com/pandeynikhilone/ProjectThree-TechFestEvent.git
cd ProjectThree-TechFestEvent
```

### Backend Setup
1. Create and activate a virtual environment:
```sh
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
2. Install dependencies:
```sh
pip install -r requirements.txt
```
3. Apply migrations:
```sh
python manage.py migrate
```
4. Create a superuser (optional, for admin access):
```sh
python manage.py createsuperuser
```
5. Run the server:
```sh
python manage.py runserver
```

## Contributors
- **Frontend Developer:** [Nikhil Pandey](https://github.com/pandeynikhilone)
- **Backend Developer:** [Dev Athwani](https://github.com/devathwani1)

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
For any queries or contributions, feel free to reach out via GitHub issues.
