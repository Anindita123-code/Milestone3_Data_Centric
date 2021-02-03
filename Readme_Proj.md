![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Views and Reviews

## Project Overview

The Views and Reviews project caters to individuals of interest by Sharing their Reviews about one or more than one book. The reviewers of the books are registered users of the website. And this website helps capturing various perspectives on a book which a reader can reference before they decide on having a personal copy to themselves. 

This website will provide as a reference for any book buyer, to search for reviews and provide a rating for the reviews that has been posted. However, only registered users can post a review. This project has been build using Pyhon and Flask Framework as Backend and MongoDB as the database. Details of this is provided in the detailed sections below.
 
## UX

### Strategy Plane

The "Views and Reviews" project has been concieved having in mind for the book readers community. Readers often require to read a short review of a book to understand whether it would be the one of their next reading lists. This website will help the users get a deeper insight into a book, and post a review on any kind of books ranging from story books, Cookery books, Art books, Biographies, Comics and more. Any user can search the website for reviews that might be posted already. They can also rate a review.

### Scope Plane

The scope of "Views and Reviews" is capped at the following:
    1. Users will be able to register and thereby login into the website to post a review on any book of their choice
    2. All users will be able to search and read a review on any books. They can also rate a review.
    3. Tha Admin user can publish any of the existing reviews as the review of the week. And will have superuser access to remove any reviews from the website.

* Here, the focus is on reviews posted by user, and hence user management in detail is considered outside the scope of this system. 
* Any kind of analysis with the ratings of reviews is outside the scope of this project.

### Structure Plane 

The website is structured so that the user can navigate easily and fulfill their goal of either reading reviews or posting a review for any book. A sitemap of the project is enclosed below

![Project Sitemap](/Design/Sitemap.png)

The Data is stored in the Backend. The database being used to store this is MongoDB. The Data is structured in the form of JSON files. 

{{ ER diagrams here }}

### Skeleton Plane

The representation of the information of this system is treated differently in different devices. The system uses the rule of three to organize data in accordance with the devices that run the application. The flow of data is depicted as follows:

![Data Flow Diagram](/Design/dfd.png)

### User stories

The project aims to address the following user stories
1. As an Admin user, I should be able to create Category / Genre of Books, Edit and Delete this from the database. So that I can have some control on how the books and reviews are organized.
2. As an Admin user, I should be able to mark a review as a featured review which will be displayed on the home page of the website and will be visible to any first time visitor of the site without having to perform a search
3. As an Admin user, I should be able to Edit and Delete information about any Registered User. So that, I can clear up the database for users who has never logged in.
4. As an Admin user, I should be able to Edit and Delete Reviews that has been added by a Registered user of the website. So that I can remove any obnoxious comment written by any reviewer on a book.
5. As a registered user, I should be able to add a review for existing books in the website. So that I do not have to upload duplicate books in for sharing my review.
6. As a registered user, I should be able to add new books to the website and then write a review for it. So that I have the freedom to add new books even if they are not there in the website. 
7. As a registered user, I should be able to view what reviews I have added in my profile page.
8. As a registered user, I should be able to delete or modify the books and reviews that has been added by me.
9. As a guest user, I should be able to read any existing reviews in the website.
10. As a guest user, I should be able to search for reviews on a particular book, book genre, author and content of review. So that I can read any reviews posted in the site
11. As a guest user, I should be able to rate a review after I have read this. So that this is visible to the next reader of the review
12. As user of the website, I should be able to navigate easily through the website, and get appropriate alert messages, when I perform any important action. So that i have a great user experience


In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:
- As a user type, I want to perform an action, so that I can achieve a goal.

This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.


## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits
For creating the sitemap I have used [Gloomaps](https://www.gloomaps.com/EJjeybEnhs)
For Creating the Data Flow Diagram I have used [Miro] (https://miro.com/app/board/o9J_lWeK1kc=/)

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X
