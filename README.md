# Balkan Cottage

note for me: here comes the screenshot for "am I responsive"

__Developed by Stefan Stanisavljevic__


note: live website

## Table of Contents
- [About](#about)
- [User Goals](#user-goals)
- [Site Owner Goals](#site-owner-goals)
- [User Experience](#user-experience)
- [User Stories](#user-stories)
- [Design](#design)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Validation](#validation)
- [Testing](#testing)
- [Bugs](#bugs)
    - [Fixed Bugs](#fixed-bugs)
- [Heroku Deployment](#heroku-deployment)
- [Credits](#credits)



### About
### User Goals
### Site owner Goals
### User Experience
### User Stories
### Design
### Technologies Used
### Features
### Validation
### Testing
### Bugs

#### Fixed Bugs
* When deploying the error " at=error code=H10 desc="App crashed" method=GET path="/" " occured which caused the homepage to crash. The problem was in the config vars
  CLOUDINARY_URL which by mistake contained invalid values. This bug was resolved by correcting the CLOUDINARY_URL .
* Beside the content, code was also displayed on menu.html page. The bug was fixed by adding {{ variable_name | safe }}
* @method_decorator(login_required) in django https://stackoverflow.com/questions/42306257/what-is-the-difference-between-login-required-and-method-decoratorlogin-requi
* Get and post functions
* update crispy form version
* https://stackoverflow.com/questions/2035288/getting-a-list-of-errors-in-a-django-form

### Heroku Deployment

The project was deployed using Heroku.

* Steps for deployment
    1. Create a new Heroku app
    2. Create database in Heroku using postgresSQL
    3. Connect the Heroku App to the Github Repository
    4. Add the necessary variables in Config Vars
    5. Click the Deploy button


### Credits

#### Images
Backgound image <a href="https://www.freepik.com/free-photo/grill-background-barbecue-fire-grill-close-up-isolated-black-background_13012809.htm#query=bbq&position=5&from_view=search&track=sph">Image by jcomp</a> on Freepik

Pljeskavica dish Image by <a href="https://www.freepik.com/free-photo/high-angle-burger-meat-grill_12656694.htm#query=grilled%20burger&position=0&from_view=search&track=robertav1_2_sidr">Freepik</a>