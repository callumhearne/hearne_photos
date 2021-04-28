Testing

The testing process I went through is listed below:
- Testing user stories.
- Validating the code.
- Checking if the website is repsonsive.
- Manually testing the websites features.

Testing user stories

New users :

- New users are able to see only photos from the north east by either selecting the north east page or the usering the search bar. 
- New users are able to see only photos from the other place by either selecting the others page or the usering the search bar.

Returing users:

- Store owners will be able to edit any photos on the site.
- Store owners are able to add and edit any photos on the site. 

User:

- The website is fully repsonsive on tablets and phones so this user will be able to use the website fine.

Validating my code

HMTL

To validate my code I used: https://validator.w3.org/

bag.html:
- When putting this page through the validator it knocks back all of the jinja as errors however they are working as intended. 

checkout.html:
- When putting this page through the validator it knocks back all of the jinja as errors however they are working as intended. 

base.html:
- When putting this page through the validator it knocks back all of the jinja as errors however they are working as intended. 

home.html:
- When putting this page through the validator it knocks back all of the jinja as errors however they are working as intended. 

faq.html:
- When putting this page through the validator it knocks back all of the jinja as errors however they are working as intended. 

policy.html:
- When putting this page through the validator it knocks back all of the jinja as errors however they are working as intended.

add_photo.html:
- When putting this page through the validator it knocks back all of the jinja as errors however they are working as intended.

edit_photo.html:
- When putting this page through the validator it knocks back all of the jinja as errors however they are working as intended.

photo_detail.html:
- When putting this page through the validator it knocks back all of the jinja as errors however they are working as intended.

photo_ne.html:
- When putting this page through the validator it knocks back all of the jinja as errors however they are working as intended.

photo_other.html:
- When putting this page through the validator it knocks back all of the jinja as errors however they are working as intended.

photos.html:
- When putting this page through the validator it knocks back all of the jinja as errors however they are working as intended.

profile.html:
- When putting this page through the validator it knocks back all of the jinja as errors however they are working as intended.

main-nav.html:
- When putting this page through the validator it knocks back all of the jinja as errors however they are working as intended.

mobile-top-header.html:
- When putting this page through the validator it knocks back all of the jinja as errors however they are working as intended.

templates/base.html:
- When putting this page through the validator it knocks back all of the jinja as errors however they are working as intended.

base.html:
- When putting this page through the validator it knocks back all of the jinja as errors however they are working as intended.

alllauth templates:
- When putting this page through the validator it knocks back all of the jinja as errors however they are working as intended.

CSS
-
To validate my code I used: https://jigsaw.w3.org/css-validator/

base.css errors:
- No errors found.
profile.css errors:
- No errors found.

JavaScript

To validate my code I used: https://jshint.com/

- No errors found.

Python

- I used the python3 -m flake8 command to see all of the python errors, I have went through the individual errors to correct them apart from errors coming from the setting.py and migrations because they weren't created by me and shouldnt be changed.

Manual Testing

- I went through each of the buttons in the nav bar from each page to make sure they worked and in repsonsive mode so that I have tested the mobile and proper nav bar.
- I added an photo, using the photo management page to test it worked.
- I tested trying to get onto the photo management page using a url without admin to see that I could not access it.
- I used an account with and without admin to see that the buttons for edit and delete appear correctly.
- I created a new photo edited it and then deleted it to test that all the admin functions worked.
- I created a new profile to test that the email confirmation worked correctly.
- I added some photos to the bag to see if the success toast works and to see if the photos added corretly.
- I checked that the photos were displaying the correct information.
- I added under 50 and over worth of items to see if the delievery deal works correctly or not.
- I've did some fake checkouts to test that the confirmation email comes through correctly.
- I have checked that the search bar searches for the photo location as well as the description.
- I've test the filters so that if I select high to low or low to high it will filter the photos prices correctly.
- I've test the main nav bar so that it will filter the correct photos when selected. Such as only north east photos appearing when selecting the north east page and sorting correctly by high to low etc.
- I've tested that all the buttons on the my profile page work correctly in the normal nav bar and on the mobile bar.
- I've test all the buttons for back to browsing to make sure that they are going to the all photos page.
- I didn't add anything to the basket and went to the checkout page to test that the 'nothing in the basket' message appears.
- I have tested logging in and logging out to make sure it works correctly.

 

