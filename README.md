# Blogs by Jessica W - A capstone Django Project

## Overview
Blogs by Jesscica W is a simplistic, MVP standard web app designed as a blog site to act as a social/community extension of the Cakesbyjessicaw independent baking business created by my partner as a way to turn a hobby into a self sustaining passion project. This inspired me to theme my blog around this with the idea being to bring individuals both to the business, and to form a community around that in which other people can gain inspiration and insights around baking of all kinds, all in a digestible and friendly format.

![Responsive site preview](Mediafiles/responsive.png)

## UX Design Process
- **Link to User Stories in GitHub Projects:**
  - [GitHub Projects Kanban Board](https://github.com/users/jackgroves2024/projects/3)
- **Wireframes:**
  - [Wireframe Images Here](https://github.com/jackgroves2024/capstone-cakeblog/tree/main/WIREFRAMES%20FOR%20CAPSTONE)
  -  The navigation is simplistic and visually streamlined to keep the pages readable and simple to understand. The overall aim was to avoid clutter whilst providing prominent enough content and interactivity that enhances user experience. Each wireframe was built with consistency in mind as the app's different pages are supposed to appear as extensions of the 'hub' that is the home page.

-  **ERD**
   - [Entity Relationship Diagram](Mediafiles/erd.png)
  
- **Design Rationale:**
  - The colour theme was not determined on the wireframes but has been chosen based on the Cakesbyjessicaw business logo and existing designs used in promotional material, branding, and social media icons. The import font family used provides a soft readable set of characters that still feel fitting for the 'comfortable theme' of the overall app without compromising the experience's accessibility. The app's core features and general structure is dependent on the organisation and responsivity that Bootstrap5 provides, from the paginated card layout to the appearance of the various forms present. It has kept things dynamic and accessible across devices by enabling a mobile first development approach.

  - The website's colour palette has been ran through contrast checkers for text readability. Whilst not flawless in lighthouse testing, I believe the standard is kept consciously high whilst maintaining the visual intergrity of the connections to the CakesbyjessicaW aesthetic.

- **Reasoning For Any Final Changes:**
  - The design originally intended to be backed by a page containing a gallery of image posts relating to the various orders/products, and whilst this would have been a simple implementation in the grand scheme of the project, taking on the learning of new apps, django features and external skills to create a mail system for the first time ended up being more time consuming than would be ideal. However, I am satisfied with this decision as it was one I made to help expand my horizons with brand new development knowledge, which I believe is a greater asset to me in the long term.

  - Another change in more simpler areas revolved around the tweaking of hexcodes for the colours that define the business related look for the project. Some of the exact colours in the brand materials that existed prior to my work were not at a level I was satisfied with when reviewing contrast for readability and overall visual appearance.
  
  - Alterations were kept subtle but I believe have had a major impact on my quality of work when considering those in various circumstances, all of which should feel welcome and capable of engaging with a community building page that is considerate of all users equally.
  

## Key Features
- ### User Account System: [Login system feature](Mediafiles/feature_login.png) & [Signup system feature](Mediafiles/feature_signup.png)
   A secure registration system for users to create accounts to enable interactions with blog posts they can view. Users can login/logout on demand, with access to CRUD features of their personal content protected behind login. Users can opt to add their email to their account when creating it, and user passwords have minimum requirements to ensure strong security implementation for each account's details.

- ### Paginated Blog Posts: [View here](Mediafiles/feature_paginated.png)
  The blog posts on the site are paginated to enhance user experience by breaking down content into manageable sections. This feature ensures that users can easily navigate through the blog posts without being overwhelmed by a long, continuous scroll. Pagination improves load times and provides a more organized and accessible way to browse through the content, making it easier for users to find and read the posts they are interested in.

- ### Email Subscription System: [View here](Mediafiles/feature_mail.png)
  The email subscription system allows users to subscribe to receive updates and notifications about new blog posts. This feature helps keep users engaged and informed about the latest updates on the site. Users can easily subscribe by providing their email address, and unsubscribe at any time. The system ensures that all email communications are handled securely and efficiently, enhancing the overall user experience and fostering a sense of community among subscribers.

 ### Inclusivity Notes: 
  Each feature of this site ties into a simple overarching structure with the design being made to avoid any longwinded scrolling, or other lengthy operations required to use anything on the site, from it's posts down to its accounts system. By keeping such things simple but effective, along with the coding considerations for accessibility tools, I believe the features displayed are functionally effective for user experience whilst remaining ultimately simplistic in practice.

## Deployment
- **Platform:** Heroku
- **High-Level Deployment Steps:** 
  1. Clone the repository: `git clone https://github.com/jackgroves2024/capstone-cakeblog.git`
  2. Set up the Heroku environment with a PostgreSQL database.
  3. Configure environment variables for sensitive data (e.g., secret keys, STMP server keys).
  4. Deploy using Heroku Git or GitHub integration.
- **Verification and Validation:**
  - I have deployed and compared the heroku app to my local test environment to verify the consistency in function and design (e.g. ensuring static files are served correctly.)
  - I have also compared the visual readability matches on the deployment and local server across different device screen sizes to ensure responsive user experience is appropriate for users with accessibility needs, such as limited sight, colour blindness, etc.
- **Security Measures:**
  - Use of environment variables for sensitive data being kept out of the raw code, added to the config vars section of the Heroku App Dashboard.
  - `DEBUG MODE` set to `False` for deployed versions of the app for security benefit.
  - `env.py` file used to store sensitive information in local repository, added to .gitignore to remain hidden from public view.

## AI Implementation and Orchestration

### Use Cases and Reflections:

  - **Code Creation:** 
    - Having access to copilot's extension with VSCode proved to be a major asset in enhancing the quality and pacing of my produced work, thanks to it's assistance in quickly producing simple starter code, such as HTML boilerplate, auto completion of lines based on the context of my work, and allowing me to quickly make comments within my code to enhance the readability and identification of my work's function throughout various files. For heavier use in production, accessing the chat to receive step by step guidance enabled me to identify a starting point in what I wished to create or achieve, with each step breaking down the code to allow me to ensure my own understanding of it before choosing to implement it into my workspace.

    - Key Example - Mail System: Step by step production using the chat feature assisted me in constructing my Email Update system, as I was unfamiliar with the processes required in the backend to enable functionality of a feature that acts mainly on an external environment, being the emails sent out themselves. I had no prior knowledge of where to begin, but was then able to learn about the existence and implementation of STMP servers and handling them securely to prevent leaking of sensitive information.

  - **Debugging:** 
    - Microsoft Copilot, as well as OpenAI's ChatGPT model were collectively capable of providing me with feedback on code segments, or even entire documents when facing major errors or failing functionality in my features. A major example of this was in establishing some efficient styling rules within my media queries to fix the responsiveness of my navigation bar and my footer,as both of these started to break and misplace content as I developed more to place within them, such as the about page, and the email newsletter box in the footer. In each of these cases, upon addition, other features on the page started to overflow out of their respective areas and fill the main content segment of the website, impacting every page that I had as they were implemented into the base template used to build the consistent visuals of the app.

  - **Performance and UX Optimization:** 
    - Taking the right approach with my AI prompts helped to eliminate the need for major alterations or intervention where things had been provided incorrectly. This allowed me to make additions to my code in well-paced increments whilst also knowing enough about what was being provided to me to be able to understand and manipulate my own work. The limited recollections I have regarding false information being provided as a result of AI assistance were primarily due to human error on my behalf as I was enquiring about certain features or ideas that I was not confident in my initial comprehension of, causing my prompts to be too lengthy, and inefficient.

- **Overall Impact:**
  - AI tools streamlined repetitive tasks, allowing additional time on feature development and refinement.
  - Efficiency gains included faster debugging, new skill development, and improved code quality by maintaining correct practice.
  - Challenges included ensuring effective prompts were given to produce correct outputs, an issue that reduced over time with use, enhancing performance and helping to highlight accessibility inclusion.

## Testing Summary
- **Manual Testing: (See [here](https://github.com/jackgroves2024/capstone-cakeblog/blob/main/Manual%20Testing.md) for full documentation)**

  - **Devices and Browsers Tested:** Windows 11, Android 14, Google Chrome, Opera GX, Samsung Browser, Microsoft Edge, iOS, MacOS, Safari

  - **Features Tested:** All main site features were manually tested, including navigation, mail services, CRUD operations, and User/Admin Authentication

  - **Results:** All test cases were reviewed as successful in their methods of verifying the functionality of the site's main features, along with the validation of correct coding practices, and the inclusion of appropriate accessibility features throughout each appropriate file. All files have been checked via appropriate validators to clear all major HTML, CSS, JS & Python usage in this project.


## Future Enhancements
- **Feature additions/alterations:**
  Following this project, I hope to return to working on this site in order to include some greater user accessibility to reach the unsubscribe option for the email update system from the website itself rather than just being directed from the email unsubscribe link, as this is currently far too limited for users to feel comfortably in control of their consent to contact.

  As a new feature, the next app addition to the site will be some form of image collection based on the photography taken of customer orders from the baking business, to provide a gallery of appealing visuals as well as serving promotional purposes for the products available to individuals should they wish to look into that side of this community environment. This may be styled either in the form of pulling from the social media feed of the business accounts existing online, or in the form of a showcase image set related to the e-commerce site that is planned for this business in the future as a method of expanding outreach.

- **Accessibility additions/enhancements:** 

  Advancements in the tools and systems available will have left room for improvements to be made across the project site as it changes and grows. I hope to develop personally in  my skills base with implementing such features. For example, the business that this social community would be tied to is likely to be based in and around the city of Birmingham, as the business is a local independent individual acting within their postcode area. 
  
  Birmingham is known as a major cultural melting pot, with communities of various backgrounds and nationalities. As a result, some form of language localisation/translation options for the site could prove greatly beneficial in including some of these locals who, regardless of their level of understanding of the English language (if any), could see this as a considerate and inclusive addition that encourages to engage and involve themselves. This in turn can ultimately lead to a growing customer base, a key goal for any smaller business.

  ## Credits, Acknowledgements & Sources (See [Requirements](requirements.txt) file for extended usage list)

  ### Credits/Sources
  - 'I Think Therefore I Blog' Walkthrough - Code Institute (Code assistance, Initial Setup Guidance)
  - Build a Blog From Scratch With Django - [Real Python](https://realpython.com/build-a-blog-from-scratch-django/#set-up-the-development-environment) (Code assistance, concept understanding)
  - MS Copilot, Copilot Chat Extension - [Microsoft](https://copilot.microsoft.com) (Code implementation, concept understanding, bugfixing, accessibility)
  - ChatGPT Model 4.0 - [OpenAI](https://chatgpt.com) (Bugfixing, concept understanding)
  - Nu HTML Checker - [W3C.org HTML Validator](https://validator.w3.org) (HTML5 Standard code validation)
  - Jigsaw CSS Validation Service - [W3C.org CSS Validation Service](https://jigsaw.w3.org/css-validator/) (CSS3 Standard code/format validation)
  - JSHint, a JavaScript Code Quality Tool - [JSHint](https://jshint.com) (JavaScript Standard code/format validation for web browser use)
  - CI Python Linter - [Code Institute Python Validator](https://pep8ci.herokuapp.com/#) (Python pep8 standard code validator, format checker)
  - Bootstrap v5.3.x Toolkit - [Bootstrap](https://getbootstrap.com)
  - Heroku Application Hosting - [Heroku Cloud Platform](https://www.heroku.com)
  - Django v4.2.18 - [Django Web Framework](https://www.djangoproject.com)
  - Graphviz - [The Graphviz Authors](https://graphviz.gitlab.io) (Graph visualisation, ERD generation)
  - Favicon.io PNG to ICO - [Favicon.io](https://favicon.io) (Brand favicon conversion)
  - CakesByJessicaW - [Jessica White](https://www.instagram.com/cakesbyjessicaw/) (Branding, site theme, icon imagery)

  ### Acknowledgements
  - Many thanks to my partner, self-ran business owner, and inspiration for this project's theme, **Jessica White**, for the emotional support, testing assistance, and consent to use the business to motivate the work I have produced with a personal connection. Without this support, this capstone project, and my growth within this course would not have been as profound as they are at this stage. Her own educational and career background in Computing & Data Science has been a source of education and inspiration. I hope our continued support of the `@Cakesbyjessicaw` name can keep bringing homemade and affordable joy to many across our city.

  - Many thanks to my friends and family for the emotional support provided from everybody around me during the intensive work period of producing this piece of work, and all work I have engaged in prior to this. This environment enables me to pursue challenges like this with a healthy maintenance of work-life balance, promoting stable mental health.

  - Many thanks to the supportive staff within my Code Institute staff for their consistent and reliable streams of contact, individual check-ins, readily accessible support, and provision of up-to-date resources for all of us to take full advantage of in our work and our personal growth in the development field. **Emma, Spencer, and Roo**, none of us would be where we are today without the knowledge and sincerity you have offered to our group.

  - I acknowledge personally that I am the *only* contributor to this repository for the duration of this project. Any future alterations or collaborations will occur outside the period of assessment.