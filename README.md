# Full stack Frameworks Project - Spectrum Ltd

- An e-commerce Project written using Django

The project utilises skills learnt in the full stack frameworks course from Code Institute.
The project will demonstrate what I have learnt in the course from frontend, backend and full stack web development.
It is a Django project with multiple apps

Spectrum Ltd is a fictitious e-commerce shop providing wall prints, to furnish rooms, homes, living spaces and offices, with a hope to add a 'Drop of Colour' to your rooms, to your life and world. 
They include prints supporting new artists and are keen to support up and coming artists with their work. 
The target audience is adults and young adults who enjoy art prints or wish to have some new furnishings for their wall.
This can be for their office walls, their homes, flats for sale/rent or even restauranteurs and cafe-owners.

The goal was to create a website for existing and potential customers to buy products online easily and also for shop managers and assistants
to manage the shop online easily.

The project is available on Heroku via [https://spectrum-ltd.herokuapp.com/](https://spectrum-ltd.herokuapp.com/)

## Index

[UX](#ux)
- User Stories
- Wireframes

[Features](#features)
- [Existing Features](#existing-features)
- [Enhancement Features](#enhancement-features)

[Technologies Used](#technologies-used)
- Essential Technologies
- Authentication
- Deployment
- SQL Database
- Storage
- Styling
- Testing

[Testing](#testing)
- Testing Stripe Payments
- Testing sending of emails
- General Testing

[Automated Testing](#automated-testing)
- [Travis CI](#travis-ci)
- [Coverage](#coverage)

[Manual Testing](#manual-testing)
- [Browser Testing](#browser-testing)
- [Device Testing](#device_testing)

[Known Issues](#known-issues)

[Deployment](#deployment)
- [Development Version vs Production/Deployed Version](#development-version-vs-production/deployed-version)
    - [Development Version](#development-version) 
    - [Production/Deployed Version](#production/deployed-version) 

[Setting up Heroku](#setting-up-heroku)

[Credits](#credits)

[Content](#content)

[Acknowledgements](#acknowledgements)

[Getting this code up and running](#getting-this-code-up-and-running)


## UX
This website is for any user interested in buying photographic prints for their office, cafe, restaurant, house, flat, living space or walls.
The ecommerce shop is for both the online shopping browser, the working person on the go, who may only access the site via mobile, or tablet,
and individual photographers and artists who are looking for an online stockist.

Spectrum Ltd's online shop has been designed to be easy to use with filtering options to find a specific image that a shopper would want, 
this can be based on the image description, the colour, the size or the price. 
The shop also allows online reviews of products made by other purchasers.
The purchasing system is easy to use and allows for quick checkout.

[User Stories](https://github.com/Andreaytm/spectrum/blob/master/misc/user-stories.pdf) have been created and are available via the link. Two main users were created the shop manager/assistant (The Superusers), 
general browsing users who are potential customers who have browsed on to the site and are looking around, 
and authenticated users who are customer of the site. 
As this is a range of individuals who could be of varying ages I have referred to them as just users.

However this could be:
- Jane, mum with 2 daughters looking to decorate her house and daughter's room with some prints.
- Ryan, restaurant owner, browsing for some prints for his new Caribbean styled restaurant.
- Leanne, landlady of 3 properties searching for prints for her new flat.
- Richard, up and coming artist specialising in abstract impressionistic paintings looking for a stockist for his new collection.
- Rhiannon, office manager browsing online for some prints to brighten up her office.
- Lee and Josie, a young couple looking for prints to brighten up their first flat together.

The planning of the style, look and feel of the website was captured in the
[Wireframes](https://github.com/Andreaytm/spectrum/blob/master/misc/project3-wireframes.pdf) which are available via the link.


## Features

### Existing Features
- **Navigation of website**
    - All basic users can navigate website but with some limited functionalities
        - can look at products - shop
        - can look at reviews - reviews
        - can use carousel - mainpage 
        - can navigate to social media channels
        - can find information about Spectrum Ltd: About, Delivery, Contact Us page.
        - can search for products via search bar
        - can add products to cart, but cannot checkout
        - can register for account or login
        
- **User Authentication**
    - login/logout/registration and password request features via completion of relevant forms.
    - specific logged in user access 
        - create/update/delete review
        - purchase products
        - see profile page 
            - edit delivery address
            - see orders placed
            
- **e-commerce functionality**
    - easy to use checkout system (user must log in)
    - search bar to search for products
    - add and remove products from cart
    - single payment
    - sort products alphabetically or reverse alphabetical order
    - sort products by cost Low-High or High-Low
    
- **Review products (provided logged in)**
    - user can rate products
    - add own product images
    - edit/update and delete their own reviews (provided user is owner of review, unless superuser)
    - search for reviews on specific product by product name
    
- **Contact us form**
    - with SMTP backend use
    - user receives copy of email
    
- **Search bars** 
    - filtering of products by name/description keywords
    - filtering of reviews by product name
    
- **Responsive UI** 
    - cross browser compatible (use of Bootstrap, and media queries where necessary) 
        - Edge
        - IE
        - Firefox
        - Opera
        - Chrome
    - cross device compatible
        - Laptop/Computer
        - Android Mobile
        - iPhone 
        - Tablet
        - iPad

### Enhancement Features

These features will require more development time. 
- Creation of functionality allowing user to input saved address to billing address.
- Creation of bar charts as average review rating of specific products.
- Advanced product pages to select sizes of products and review be added to selected bought products only.
- Delivery select options that influence overall total (eg airmail, european delivery etc).
- Free delivery for spending over £50.
- Email receipt of order.
- Pagination of pages for products.
- Add custom error pages.


## Technologies Used

Essential Technologies:
- [Cloud 9](https://aws.amazon.com/cloud9/?origin=c9io) online code editor for development of the project
- CSS for website styling
- [Django](https://www.djangoproject.com/)
- [Github](https://github.com/) for version control.
- HTML5 for basic markup language and provide semantic elements to webpage design.
- [jQuery](https://jquery.com/) to manage events and effects for enhanced user experience.
- JavaScript-for UI enhancements

Authentication:
- Use of Cross-Site Request Forgery (CSRF) tokens to mitigate CSRF attacks was used on all forms on the project.
- [STRIPE](https://stripe.com/gb) for authentication of payment for e-commerce functionality. 
- [Django Secret Key Generator](https://www.miniwebtool.com/django-secret-key-generator/) for generation of new SECRET_KEY.

Deployment:
- [Gunicorn](https://gunicorn.org/)-A Python package, used for running HTTP servers on UNIX based operating systems and to connect to Heroku.
- [Heroku](https://www.heroku.com/) for deployment and hosting of project.

SQL Database:
- [dj-database-url](https://pypi.org/project/dj-database-url/) - package allows connection to a database URL (eg Heroku Postgres)
- [Heroku Postgres](https://www.heroku.com/postgres)- cloud-based Postgres managed SQL database to use in deployment instead of sqlite3 for production.
- [Psycopg2](https://pypi.org/project/psycopg2/) - package to connect to Postgres databases
- [SQLite3 DB](https://docs.python.org/2/library/sqlite3.html) - the standard database on django using Django's ORM in development for local testing.

Storage:
- [Pillow](https://pypi.org/project/Pillow/) allows uploading of images through admin page.
- [Amazon Web Services (AWS)](https://aws.amazon.com/)
    - [S3 Storage](https://aws.amazon.com/s3/?nc2=type_a) used to store mediafiles (images) and staticfiles (JS, CSS, Font Awesome) on cloud-based storage.
    - [Identity and Access Management (IAM) Console](https://aws.amazon.com/iam/) to manage who can access the Amazon AWS services.
    - [Django-storages and Boto3](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html) to connect to AWS S3 bucket

Styling:
- [Django-Forms-Bootstrap](https://pypi.org/project/django-forms-bootstrap/) to allow usage of bootstrap in templates.
- [Bootstrap](https://getbootstrap.com/) for responsive simplistic layouts.
- [Font Awesome](https://fontawesome.bootstrapcheatsheets.com/) for styling and improved UI.
- [Favicon Generator](https://www.favicon-generator.org/) to create my own favicon for the website.
- [Pencil](https://pencil.evolus.vn/) for creation of wireframes.

Testing:
- [FreeFormatter.com](https://www.freeformatter.com/) for formatting and indentation.
- [Coverage](https://coverage.readthedocs.io/en/v4.5.x/) for displaying test reports from Django unit tests.
- [Travis CI](http://travis-ci.org) allows for Continuous Integration, which runs tests on code every time it is pushed to GitHub.
- [CSS](https://jigsaw.w3.org/css-validator/) for CSS validation
- [HTML Validators](https://validator.w3.org/) for HTML validation.
- [JSHint](https://jshint.com/) for JavaScript validation.
- [PEP8](http://pep8online.com/) for Python validation.

## Testing:
Testing STRIPE payments: 
- [Test Cards](https://stripe.com/docs/testing#cards)
- Tested that all fields requires completion prior to submission of form with exception of CVV as test cards do not require CVV entry)
- Viewed testing on Stripe Dashboard to ensure that information passed through.


Testing sending of emails via contact form: 
- ```EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'```
- Tested initially on console to display email message.
- Tested again via smtp to ensure that message goes through to emails.

General Testing:
- Iterative testing has been included throughout the process of the project through observation of complex changes on localhost.
- Checked syntax for errors against existing Code Institute learnt code.
- Validation of syntax through [CSS](https://jigsaw.w3.org/css-validator/) and [HTML Validators](https://validator.w3.org/), and 
- Validation of JavaScript code on [JSHint](https://jshint.com/) and Python on [PEP8](http://pep8online.com/).
- Used [FreeFormatter](https://www.freeformatter.com/) to reindent tabs to ensure code is structured cleanly.
- Checked console for errors in JavaScript.


### Automated Testing

#### Travis CI
- Automated testing was done using Travis-CI. 
[![Build Status](https://travis-ci.org/Andreaytm/spectrum.svg?branch=master)](https://travis-ci.org/Andreaytm/spectrum)

#### Coverage 

- Installation: 
```sudo pip3 install coverage``` 
- To run reports in terminal:
```coverage run manage.py test <app name>``` 
or 
```coverage run --source=<app name> manage.py test```
- Then to display report on app in terminal:
```coverage report```
- To display content in a html webpage:
```coverage html```
then go to **htmlcov** folder find index.html open and run the file in a new tab.

A % of testing was carried out via coverage and additional testing completed via BDD(Behavioural Driven Development) and additional manual testing.
- accounts = 73% = Tested template views as Django handles testing of authentication
- review = 90% = Tested CRUD (Create, Read, Update, Delete) functionality via BDD(Behavioural Driven Development) 
- contacts = 88% = Specific testing of send_mail was done via BDD (including display of HttpResponse error messages)
by sending test emails and checking in gmail account. However can test that this is also working via unittest 
as redirects to thanks instead of returning HttpResponse('Invalid header found') or blank contact form.

- cart = 58% = Test was mostly done via TDD and manual testing.
- search = approx 52% = Testing of search bars, filtering and sorting done via BDD and manual testing.
- products = 93% = Did not test apps as the code is generated automatically by Django.
- home = 92% = Did not test apps as not required, as the code is generated automatically by Django.
- checkout = 80% = Testing of stripe payment done via use of test cards.

In addition I did not test the urls as this was tested via manual testing.


### Manual Testing:

#### Behavioural Driven Development Testing (BDD)
See [Behavioural Driven Development Testing (BDD)](https://github.com/Andreaytm/spectrum/blob/master/misc/behaviour-driven-development.pdf) for further details of scenarios.
- CRUD (Create, Read, Update, Delete) Functionality - Reviews page (documented in pdf)
- Stripe Payment - Tested with test card '4242' on all devices and browsers
- Emails - Contacts and Registration (manually tested using Gmail)
- Search and sorting (documented in pdf)
- URLs- navigation (documented in pdf) 

#### Browser Testing
- Google Chrome (v71.0.3...)
- IE (v11.4...)
- Edge (42.1...)
- Firefox (Mozilla v63.0.3...)
- Opera (Stable v56.0.3..)

#### Device Testing
- Acer Laptop (Aspire 5750) (col-lg)
- iPad Mini 2 (col-sm (portrait) & col-md (landscape) & apple)
- Android- Samsung Galaxy S8 (col-xs & android)
- iPhone 2 (col-xs)

- Installed various browsers: Opera, IE, Edge, Firefox, Chrome for testing for cross-compatibility 
- and borrowed various devices for testing as above: Android, Apple ipad and iphone. 

The dropdown menu within the review page is stylistic different across browsers and devices.
This was initially an issue due to the colour of the caret however I have rectified by having
some help text included to prompt the user to select a dropdown option. 
The hover in both Opera and Edge displays grey on the caret.

The alerts on forms also display differently across browsers, with Chrome displaying a popup
speech bubble alert, IE and Edge display red boxes around each required fields and mobile/tablet 
devices display with popup alerts to complete fields.

The images sizes within reviews, products and carousels alter across devices. On smaller devices 
the nav menu displays as a collapsed menu icon.


## Known Issues
**Stripe Payments - Solved**:
Initially I thought I had issues with Stripe Payments and payment being accepted even if CVV field was empty. 
I attempted solving with a required=True however this affected '4242' card being accepted.
I later found out that test card '4242' does not need a CVV field to be filled in for the form to work.

**iPhone/iPad - Solved**:
Issues with dropdown menus in nav. I found out that nav dropdown menus require a href of "#" so to ensure it works in iPhone or iPad.
This does not affect the overall functionality of the website. But is something that needs to be included for iPhone and iPad compatibility.

**Issue with flex-box in iPad  - Solved**: this affected reviews and products displayed. Altered col-sm and col-md (for portrait and landscape views) 
and added container-fluid to various templates. This also solved an issue I was experiencing with Firefox where the carousel on the main
index page was 'jumping'.

**Browser - Solved**:
Dropdown styling (reviews search) was differing across browsers, some of which were affecting icons being seen (dropdown arrow)
I added some help-text to ensure that users will select from dropdown to search for a review and added a message in body should no results be returned.

**Browser - IE - Solved** :
Navbar was returning blue in IE whereas all other browsers returned the rainbow spectrum I had stylised. I later found out there was a typo
in the css code which affected the rendering of the colours in IE but no other browser!

**Migration Issues - Solved** :
I had some migration issues during the development and deployment of the project. I used the following to update database where there were issues that could not be resolved.
[Stack Overflow](https://stackoverflow.com/questions/42150499/how-do-i-delete-db-sqlite3-in-django-1-9-to-start-from-scratch)

```
1. Delete the sqlite database file (often db.sqlite3) in your django project folder (or wherever you placed it)
2. Delete everything except __init__.py file from migration folder in all django apps
3. Make changes in your models (models.py).
4. Run the command python manage.py makemigrations or python3 manage.py makemigrations
5. Then run the command python manage.py migrate
```

**Email Issues - Solved** : I ensured the following was entered in the settings.py for both my contact form and my reset-password forms.
There was an issue with the contacts form upon deployment after the PEP8 validation. 
I have altered the contacts/views.py once more to ensure emails are working.
The issue was with the PEP8 stating that lines were more than 75 characters long. 
I had altered the code to ensure that lines were not more than 75 however this affected the functionality of the contact form.

```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get("EMAIL_ADDRESS")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASSWORD")
EMAIL_PORT = 587
```

## Deployment

### Development Version vs Production/Deployed Version
I have noted below the differences of each of the project versions. 

#### Development Version
- uses SQLite3 database which was standard of Django

```
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```

- Storage of config var keys on env.py

```
import os 

os.environ.setdefault("SECRET_KEY", "")
os.environ.setdefault("STRIPE_SECRET", "")
os.environ.setdefault("STRIPE_PUBLISHABLE", "")
os.environ.setdefault("EMAIL_ADDRESS", "")
os.environ.setdefault("EMAIL_PASSWORD", "")
os.environ.setdefault("DATABASE_URL", "")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "")
os.environ.setdefault("AWS_ACCESS_KEY_ID", "")

```
- Uses Pillow and uploading of media files via admin dashboard
- Static files were kept in the project file structure

```
import env
...
DEBUG = True
....
ALLOWED_HOSTS = [os.environ.get('C9_HOSTNAME')]
```

- Media and static files are currently stored via: 

```
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR, 'static')]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```


#### Production/Deployed Version
- Uses Heroku Postgres database with dependencies of Psycopg2 and dj-database-url.
- Comment out import env, import dj_database_url, add Database and set DEBUG to False.


```
# import env
import dj_database_url
...
DEBUG = False


DATABASES = { 'default' :dj_database_url.parse(os.environ.get('DATABASE_URL')) }
```

- Config vars keys were stored within Heroku:
    - SECRET_KEY
    - STRIPE_SECRET
    - STRIPE_PUBLISHABLE
    - DATABASE_URL
    - EMAIL_ADDRESS
    - EMAIL_PASSWORD
    - AWS_ACCESS_KEY_ID
    - AWS_SECRET_ACCESS_KEY
    - and additional key of **DISABLE_COLLECTSTATIC with key of 1**.
    
- Uses AWS cloud-based storage of media and static files with dependencies of django-storages and Boto3.

```
ALLOWED_HOSTS = [....., 'spectrum-ltd.herokuapp.com')]
...

INSTALLED_APPS = [.... 'storages', ]
```

- Media and static files are stored differently in Production/deployed version with 'storage' listed in 
settings.py of 'INSTALLED_APPS'.

```
# AWS Storage Bucket
AWS_STORAGE_BUCKET_NAME = 'spectrum-ltd'
AWS_S3_REGION_NAME = 'eu-west-2'
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# Static Files
STATICFILES_LOCATION ='static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'

STATIC_URL = '/static/'
STATICFILES_DIRS =(
    os.path.join(BASE_DIR, "static"),
    )

# Media Files
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
MEDIAFILES_LOCATION = 'media'

MEDIA_URL= "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

- The final version has some settings.py with code allowing both development and deployment to be used as follows:
```
if os.environ.get('DEVELOPMENT'):
    development = True
else:
    development = False
...
    
if "DATABASE_URL" in os.environ:
    DATABASES = { 'default': dj_database_url.parse(os.environ.get('DATABASE_URL')) }
else:
    print("Database URL not found. Using SQLite instead")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```

- The deployed version is available here on Heroku via [https://spectrum-ltd.herokuapp.com/](https://spectrum-ltd.herokuapp.com/)

### Setting up Heroku
I used Code Institute lessons for the deployment of the project.

Heroku
- I went to [Heroku](https://www.heroku.com/) to set up an app 'spectrum'
- To add Posgres database go to Resources> add database **Postgres** choose **'HobbyDev Free'**

For use of Heroku Postgres:
- On Cloud 9 console install dj-database-url: 
```sudo pip3 install dj-database-url```. This package allows connection to a database URL. 
- Then install psycopg2 ```sudo pip3 install psycopg2``` which allows connection to the postgres database.
- Create a requirements.txt file with all dependencies listed ```pip3 freeze > requirements.txt``` .
- **import dj_database_url** at top of settings.py file and change default sqlite3 database to be default dj_database_url
```DATABASES = { 'default' :dj_database_url.parse(os.environ.get('DATABASE_URL')) }```
- Add DATABASE_URL config vars code to env.py 
- Make migrations to migrate all files to new database.

```
python3 manage.py makemigrations
python3 manage.py migrate
```

- Create new superuser via ```python3 manage.py createsuperuser``` and add username, email and password.
**This will be production database for deploying on Heroku**
- Update settings.py file spectrum app folder to include URL on Heroku in ALLOWED_HOSTS '<project-name>.herokuapp.com'
and DATABASE_URL from Postgres Database

Heroku
- Ensure Heroku has all Config Vars code required = SECRET_KEY, STRIPE_SECRET, STRIPE_PUBLISHABLE, EMAIL_ADDRESS, EMAIL_PASSWORD, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
add DISABLE_COLLECTSTATIC set to 1. The latter will disable staticfiles from being added to Heroku so the project uses the AWS bucket.
- To allow deployment via github automatic/manual select Deploy> GitHub> connect to repo = 'spectrum' in Heroku menu. For automatic deployment select button 'enable automatic deploys'.
- Otherwise use manual deployment to 'deploy branch'

Cloud9
- Install gunicorn ```sudo pip3 install gunicorn```.
- Ensure all dependencies are added to requirements.txt with command ```pip3 freeze > requirements.txt```
- Create and add a file called **Procfile** which contains text 'web: gunicorn spectrum.wsgi:application'
- Git add, git commit then git push the code to GitHub

Heroku
- Select Deploy >deploy branch if using manual deployment
- To ensure working smoothly select top right menu option in Heroku >'more' >'restart all dynos' to ensure that the project is updated.

Important
- Ensure the Allowed Host Heroku name is projectname.herokuapp.com and does not contain 'Https://'
- Ensure any irrelevant dependencies are removed from the project eg

## Credits
- [Django Contact Form Tutorial: William S Vincent](https://wsvincent.com/django-contact-form/) the contact form which was adapted for this project.
- Andreas Grapentin and David on [Stack Overflow](https://stackoverflow.com/questions/5805059/how-do-i-make-a-placeholder-for-a-select-box) support on select box placeholder options.
- Stars in review taken from post on [Stack Overflow](https://stackoverflow.com/questions/1987524/turn-a-number-into-star-rating-display-using-jquery-and-css/1987545).

## Content
[GoogleFonts](https://fonts.google.com/)
The photos used in this site are my own.


## Acknowledgements
- **Code Institute Tutors**:
    - Haley Schafer
    - Neil McEwen
    - Nakita McCool
    
- Tiffany Snell for words of encouragement and general check-ups

- **Mentor**:
    - Jim Richmond
    
- **Students on Code Institute on Slack**: 
    - Simen Daehlin:@eventyret 
    - Anthony Bonello: @bonello
    - Sarah Barron


## Getting this code up and running

To contribute to this project please following the steps below on Cloud 9 and GitHub 
1. Cloning this repository
Run git clone <https://github.com/Andreaytm/spectrum> command.
2. Create new project in cloud9 on a blank workspace.
3. install everything in the requirements.txt
```$ sudo pip3 -r install requirements.txt```
4. Ensure the db.sqlite3 and media and staticfiles are also installed
5. You will need to generate your own keys for the following: SECRET_KEY, 
STRIPE_SECRET, STRIPE_PUBLISHABLE, EMAIL_ADDRESS, EMAIL_PASSWORD, 
and create a env.py file in the root of the project with this data.
(Note you will only need the AWS keys if you wish to host static and media files on S3 AWS 
(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY))
6. If working locally you will need to update the settings.py and comment back in env.py.
7. You will also need to remove 'storages' from INSTALLED_APPS in setttings.py 
and change the location of static and media files to

```
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR, 'static')]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

8. To run the project on localhost, run the following in the Cloud9 terminal:
```python3 ~/workspace/manage.py runserver $IP:$C9_PORT"``` alternatively 
you can add a shortcut by adding the following:  
 ```alias run="python3 ~/workspace/manage.py runserver $IP:$C9_PORT"```
to .bash_aliases file which is hidden in cloud9 settings menu under 'Show Home in Favourites' menu
If you add the shortcut remember to close the terminal and open a new one before running 'run'