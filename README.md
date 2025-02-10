# Blogs by Jessica W - A capstone Django Project

![Responsive site preview](Mediafiles/responsive.png)

## Overview
Blogs by Jesscica W is a simplistic, MVP standard web app designed as a blog site to act as a social/community extension of the Cakesbyjessicaw independent baking business created by my partner as a way to turn a hobby into a self sustaining passion project. This inspired me to theme my blog around this with the idea being to bring individuals both to the business, and to form a community around that in which other people can gain inspiration and insights around baking of all kinds, all in a digestible and friendly format.

## UX Design Process
- **Link to User Stories in GitHub Projects:**
  - [GitHub Projects Kanban Board](https://github.com/users/jackgroves2024/projects/3)
- **Wireframes:**
  - [Wireframe Images Here](https://github.com/jackgroves2024/capstone-cakeblog/tree/main/WIREFRAMES%20FOR%20CAPSTONE)
  -  The navigation is simplistic and visually streamlined to keep the pages readable and simple to understand. The overall aim was to avoid clutter whilst providing prominent enough content and interactivity that enhances user experience. Each wireframe was built with consistency in mind as the app's different pages are supposed to appear as extensions of the 'hub' that is the home page.

  **ERD**

  - [Entity Relationship Diagram](Mediafiles/erd.png)
  
- **Design Rationale:**
  - The colour theme was not determined on the wireframes but has been chosen based on the Cakesbyjessicaw business logo and existing designs used in promotional material, branding, and social media icons. The import font family used provides a soft readable set of characters that still feel fitting for the 'comfortable theme' of the overall app without compromising the experience's accessibility. The app's core features and general structure is dependent on the organisation and responsivity that Bootstrap5 provides, from the paginated card layout to the appearance of the various forms present. It has kept things dynamic and accessible across devices by enabling a mobile first development approach.

  - The website's colour palette has been ran through contrast checkers for text readability. Whilst not flawless in lighthouse testing, I believe the standard is kept consciously high whilst maintaining the visual intergrity of the connections to the CakesbyjessicaW aesthetic.

- **Reasoning For Any Final Changes:**
  - The design originally intended to be backed by a page containing a gallery of image posts relating to the various orders/products, and whilst this would have been a simple implementation in the grand scheme of the project, taking on the learning of new apps, django features and external skills to create a mail system for the first time ended up being more time consuming than would be ideal. However, I am satisfied with this decision as it was one I made to help expand my horizons with brand new development knowledge, which I believe is a greater asset to me in the long term.

  - Another change in more simpler areas revolved around the tweaking of hexcodes for the colours that define the business related look for the project. Some of the exact colours in the brand materials that existed prior to my work were not at a level I was satisfied with when reviewing contrast for readability and overall visual appearance.
  
  - Alterations were kept subtle but I believe have had a major impact on my quality of work when considering those in various circumstances, all of which should feel welcome and capable of engaging with a community building page that is considerate of all users equally.
  

## Key Features
- **User Account System:** A secure registration system for users to create accounts to enable interactions with blog posts they can view. Users can login/logout on demand, with access to CRUD features of their personal content protected behind login. Users can opt to add their email to their account when creating it, and user passwords have minimum requirements to ensure strong security implementation for each account's details.

- **Paginated Blog Posts:** 
  The blog posts on the site are paginated to enhance user experience by breaking down content into manageable sections. This feature ensures that users can easily navigate through the blog posts without being overwhelmed by a long, continuous scroll. Pagination improves load times and provides a more organized and accessible way to browse through the content, making it easier for users to find and read the posts they are interested in.

- **Email Subscription System:** 
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
    - Reflection: Having access to copilot's extension with VSCode proved to be a major asset in enhancing the quality and pacing of my produced work, thanks to it's assistance in quickly producing simple starter code, such as HTML boilerplate, auto completion of lines based on the context of my work, and allowing me to quickly make comments within my code to enhance the readability and identification of my work's function throughout various files. For heavier use in production, accessing the chat to receive step by step guidance enabled me to identify a starting point in what I wished to create or achieve, with each step breaking down the code to allow me to ensure my own understanding of it before choosing to implement it into my workspace.

    - Key Example - Mail System: Step by step production using the chat feature assisted me in constructing my Email Update system, as I was unfamiliar with the processes required in the backend to enable functionality of a feature that acts mainly on an external environment, being the emails sent out themselves. I had no prior knowledge of where to begin, but was then able to learn about the existence and implementation of STMP servers and handling them securely to prevent leaking of sensitive information.
  - **Debugging:** 
    - Reflection: Key interventions included resolving logic errors and enhancing maintainability, with a focus on simplifying complex logic to make it accessible.
  - **Performance and UX Optimization:** 
    - Reflection: Minimal manual adjustments were needed to apply AI-driven improvements, which enhanced application speed and user experience for all users.

- **Overall Impact:**
  - AI tools streamlined repetitive tasks, enabling focus on high-level development.
  - Efficiency gains included faster debugging, comprehensive testing, and improved code quality.
  - Challenges included contextual adjustments to AI-generated outputs, which were resolved effectively, enhancing inclusivity.

## Testing Summary
- **Manual Testing:**
  - **Devices and Browsers Tested:** Windows 11, Android 14, Google Chrome, Opera GX, Samsung Browser, Microsoft Edge
  - **Features Tested:** All main site features were manually tested, including navigation, CRUD operations, and User/Admin Authentication
  - **Results:** [Summarise testing results, e.g., "All critical features worked as expected, including accessibility checks."]


## Future Enhancements
- [List potential improvements or additional features for future development.]
- Consider enhancements to improve accessibility further, such as voice input capabilities or additional language support.
