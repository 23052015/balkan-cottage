Return to [README.md](/README.md)  

# Testing  

## Methodology  
Testing was an integral part of the project development process. It was carried out using a combination of Django debug pages, print statements, and various testing methodologies. In-depth testing was conducted, including manual tests to validate user stories and acceptance criteria. Additionally, the code underwent validation through online tools, as outlined below. 

&nbsp;

### Test Cases  
&nbsp;
### User Stories

#### Menu page
| Testing  | Steps | Expected Outcome | Results |  
| - | - | - | - |
| Client can view menu page | PASS |

#### Registration 
| Testing  | Steps | Expected Outcome | Results |  
| - | - | - | - |
| Customer signup page | Test link is working | Customer is directed to the signup page | PASS |
| Customer signup - Form validation | Submit empty form | Form validation prompts the user | PASS |
| Customer signup - Form validation | Submit invalid email address | Form validation prompts the user | PASS |
| Customer signup - Form validation | Submit invalid password | Form validation prompts the user | PASS |
| Customer signup - Form validation | Submit non matching passwords | Form validation prompts the user | PASS |
| Customer signup - Form validation | Submit already taken username | Form validation prompts the user | PASS |
| Customer login page | Test link is working | Customer is directed to the login page | PASS |
| Customer login - Form validation | Submit incorrect password | Form validation prompts the user | PASS |
| Customer Logout page | Test link is working | User is logged out | PASS |

#### Reservations
| Testing  | Steps | Expected Outcome | Results |  
| - | - | - | - |
| Form validation reservation page | Check that each required field is working correctly in the form | Form validation prompts the user | PASS |
| Submit button reservation page | Click the submit button to check that the reservation is saved | PASS |
| Reservations are shown on myReservation spage | Check that each reservation for a user are shown on the my Reservation spage | PASS |
| Reservations can be edited | Check that the edit button works and that the updated reservation is submitted to the my reservation page when edited | reservation is updated with the corresponding reservation details | PASS |
| Reservationscan can be deleted | Check that the delete button works and that the deleted reservation is removed from the my reservation page when deleted | My reservation list is updated | PASS |

#### Navbar
| Testing  | Steps | Expected Outcome | Results |  
| - | - | - | - |
| Navbar | Check that each link is working correctly | Customer is able to open each link to browse the webpage | PASS |

#### Admin
| Testing  | Steps | Expected Outcome | Results |  
| - | - | - | - |
| Admin login - Form validation | Submit incorrect password | Form validation prompts the user | PASS |
| Admin login - Form validation | Submit incorrect name | Form validation prompts the user | PASS |
| Admin login - Form validation | Submit incorrect name | Form validation prompts the user | PASS |
| Admin panel | Owner is able to delete reservations | Reservation is deleted from current booking list | PASS |


## Further Testing
-   The website was thoroughly tested on different browsers including Google Chrome, Internet Explorer, Safar and Microsoft Edge. Extensive testing was performed to make sure all the links and navigation work properly. Testing on different devices to make sure it scales properly.  


  

-   [W3C Markup Validator](https://validator.w3.org/nu/) 
    - Parse Errors are shown. No impact on the project

-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) 
    - Warning concerning uploading files in django admin panel. 

-   [Python Validator](https://extendsclass.com/python-tester.html#:~:text=To%20check%20your%20code%2C%20you,use%20this%20python%20checker%20tool.) 
    - No errors or warnings was shown 

### Lighthouse performance
- ![Home](/ReadMeDocumentation/images/home_lighthouse..png)
- ![Reservation](/ReadMeDocumentation/images/reservation_lighthouse.png)
- ![My reservation](/ReadMeDocumentation/images/my_reservations_lighthouse.png)