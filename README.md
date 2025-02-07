# Blogs by Jessica W

## Overview
[Briefly describe the purpose of the project, the problem it solves, and its value to users.]

## UX Design Process
- **Link to User Stories in GitHub Projects:**
  - [GitHub Projects Kanban Board](https://github.com/users/jackgroves2024/projects/3)
- **Wireframes:**
  - [Wireframe Images Here](https://github.com/jackgroves2024/capstone-cakeblog/tree/main/WIREFRAMES%20FOR%20CAPSTONE)
  -  The navigation is simplistic and visually streamlined to keep the pages readable and simple to understand. The overall aim was to avoid clutter whilst providing prominent enough content and interactivity that enhances user experience. Each wireframe was built with consistency in mind as the app's different pages are supposed to appear as extensions of the 'hub' that is the home page.
- **Design Rationale:**
  - The colour theme was not determined on the wireframes but has been chosen based on the Cakesbyjessicaw business logo and existing designs used in promotional material, branding, and social media icons. The import font family used provides a soft readable set of characters that still feel fitting for the 'comfortable theme' of the overall app without compromising the experience's accessibility. The app's core features and general structure is dependent on the organisation and responsivity that Bootstrap5 provides, from the paginated card layout to the appearance of the various forms present. It has kept things dynamic and accessible across devices by enabling a mobile first development approach.
  - [Highlight any considerations made for users with disabilities, such as screen reader support.]
- **Reasoning For Any Final Changes:**
  - [Summarise significant changes made to the design during development and the reasons behind them.]
  - [Reflect on how these changes enhance inclusivity and accessibility.]

## Key Features
- **User Account System:** A secure registration system for users to create accounts to enable interactions with blog posts they can view. Users can login/logout on demand, with access to CRUD features of their personal content protected behind login. Users can opt to add their email to their account when creating it, and user passwords have minimum requirements to ensure strong security implementation for each account's details.
- **Feature 2:** [Briefly describe the implemented feature.]
- **Inclusivity Notes:** 
  - [Mention how the features address the needs of diverse users, including those with SEND.]

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
(Highlight how prompts, such as reverse, question-and-answer or multi-step, were used to support learners with SEND or ALN where relevant.)

  - **Code Creation:** 
    - Reflection: Strategic use of AI allowed for rapid prototyping, with minor adjustments for alignment with project goals. 
    - Examples: Reverse prompts for alternative code solutions and question-answer prompts for resolving specific challenges.
  - **Debugging:** 
    - Reflection: Key interventions included resolving logic errors and enhancing maintainability, with a focus on simplifying complex logic to make it accessible.
  - **Performance and UX Optimization:** 
    - Reflection: Minimal manual adjustments were needed to apply AI-driven improvements, which enhanced application speed and user experience for all users.
  - **Automated Unit Testing: (If undertaken)**
    - Reflection: Adjustments were made to improve test coverage and ensure alignment with functionality. Prompts were used to generate inclusive test cases that considered edge cases for accessibility.

- **Overall Impact:**
  - AI tools streamlined repetitive tasks, enabling focus on high-level development.
  - Efficiency gains included faster debugging, comprehensive testing, and improved code quality.
  - Challenges included contextual adjustments to AI-generated outputs, which were resolved effectively, enhancing inclusivity.

## Testing Summary
- **Manual Testing:**
  - **Devices and Browsers Tested:** [List devices and browsers, ensuring testing was conducted with assistive technologies such as screen readers or keyboard-only navigation.]
  - **Features Tested:** [Summarise features tested manually, e.g., CRUD operations, navigation.]
  - **Results:** [Summarise testing results, e.g., "All critical features worked as expected, including accessibility checks."]
- **Automated Testing: (If undertaken)**
  - Tools Used: [Mention any testing frameworks or tools, e.g., Django TestCase.]
  - Features Covered: [Briefly list features covered by automated tests.]
  - Adjustments Made: [Describe any manual corrections to AI-generated test cases, particularly for accessibility.]

## Future Enhancements
- [List potential improvements or additional features for future development.]
- Consider enhancements to improve accessibility further, such as voice input capabilities or additional language support.