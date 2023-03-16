# **RISING WOMEN**

![amiresponsive mockups of project](ADD-LINK-HERE)

**[Link to the deployed/ live site](https://rising-women.herokuapp.com/)**

![GitHub last commit](https://img.shields.io/github/last-commit/rachel-o-donnell/rising-women?color=fuschia&style=for-the-badge)
![GitHub contributors](https://img.shields.io/github/contributors/rachel-o-donnell/rising-women?color=purple&style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/rachel-o-donnell/rising-women?color=blue&style=for-the-badge)
![GitHub top language](https://img.shields.io/github/languages/top/rachel-o-donnell/rising-women?color=yellow&style=for-the-badge)

# Project Overview
Rising Women is a platform developed by women for women in technology to help mitigate the lack of representation in technical roles, particularly in leadership positions by:
* promoting awareness of leading women in technology by curating a list of successful, inspiring role models
* enabling women in technology leaders to mentor and support other women through insights-, skills- and strategies-sharing
* providing opportunities for women technologists to learn from, be inspired by and network with other women and women role models in field

This platform was built using Django, Python, JavaScript and Bootstrap 4. The site was deployed on Heroku and uses Cloudinary for cloud storage.

Rising Women is Team 6: Code Sisters' project submission for Code Institute's Women in Technology Hackathon, March 2023.

---
**TABLE OF CONTENTS**
* [USER EXPERIENCE](#user-experience)
    * [Strategy Plane](#strategy-plane)
        * [Project Goals](#project-goals)
            * [Problems We Are Trying to Solve](#problems-we-are-trying-to-solve)
            * [Platform Goals](#platform-goals)
    * [Scope Plane](#scope-plane)
        * [Feature Planning](#feature-planning)
    * [Structure Plane](#structure-plane)
        * [Interaction Design](#interaction-design)
            * [User Flow Diagram](#user-flow-diagram)
        * [Information Architecture](#information-architecture)
            * [Site Map](#site-map)
        * [Database Design](#database-design)
            * [Database ERD](#database-erd)
            * [Data Modelling](#data-modelling)
                * [User Model](#user-model)
                * [UserProfile](#userprofile-model)
                * [Category Model](#category-model)
                * [Subcategory Model](#subcategory-model)
                * [Mentor Model](#product-model)
                * [Bookmark Model](#order-model)
        * [User Stories](#user-stories)
    * [Skeleton Plane](#skeleton-plane)
        * [Wireframes](#wireframes)
    * [Surface Plane](#surface-plane)
        * [Typography](#typography)
        * [Colour Palette](#colour-palette)
        * [Imagery](#imagery)
* [Agile Methodology](#agile-methodology)
    * [GitHub Projects](#github-projects)
* [Features](#features)
    * [Mentor Expetise Categorization](#mentor-expertise-categorization)
    * [Defensive Programming](#defensive-programming)
    * [Accessibility](#accessibility)
    * [Extra Meta Tags for Specific Pages](#extra-meta-tags-for-specific-pages)
    * [Mentor Management - Authorized Personnel Only](#product-management---authorized-personnel-only)
    * [Bookmark](#bookmark)
    * [Site Features Common to All Pages](#site-features-common-to-all-pages)
    * [Site Pages](#site-pages)
* [Future Development, Iteration and Implementation](#future-development-iteration-and-implementation)
* [Technologies Used](#technologies-used)
    * [Languages Used](#languages-used)
    * [Frameworks Used](#frameworks-used)
    * [Databases Used](#databases-used)
    * [Libraries and Packages Used](#libraries-and-packages-used)
    * [Programmes and Applications Used](#programmes-and-applications-used)
    * [Cloud Application Platforms Used](#cloud-platforms-used)
    * [Cloud Storage Services Used](#cloud-storage-services-used)
* [Testing](#testing)
* [Bugs, Issues and Solutions](#bugs-issues-and-solutions)
* [Deployment and Local Development](#deployment-and-local-development)
    * [Deployment](#deployment)
    * [Local Development](#local-development)
        * [How to Fork](#how-to-fork)
        * [How to Clone](#how-to-clone)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)
---

# USER EXPERIENCE
## Strategy Plane
Numerous case studies, research reports and white papers point to and acknowledge that Women in technology/ technical roles are still woefully underrepresented, particularly in leadership positions.

A [PwC UK research report, Women in Tech - Time to close the gender gap, 2017](https://www.pwc.co.uk/women-in-technology/women-in-tech-report.pdf) pointed out that: *Despite decades of progress towards workplace equality, women remain woefully underrepresented in the UK’s technology workforce.* According to the report,
* just **23%** of the people working in STEM (Science, Technology Engineering and Mathematics) roles across the UK are female
* only **5%** of leadership positions in the technology industry are held by women

According to [Anita Borg Institute's Advancing Women Technologists into Positions of Leadership report, 2020](https://anitab.org/wp-content/uploads/2020/08/advancing-women-technologists-leaders.pdf), *The lack of advancement of women technologists is staggering. At current advancement rates, it will take **100 years** for women in technical and non-technical roles combined to reach parity with men at the C-level.*

### Project Goals
This section aims to answer the key question: *What problems are we trying to solve?*

The Rising Women project is focused on tackling the challenges around the Hackathon Topic 2: **Lack of representation: Women are often underrepresented in technical roles, particularly in leadership positions. This can create a culture where women feel isolated and excluded, and may not have role models or mentors to support their career development.**

#### Problems We Are Trying to Solve
* Problem 1: Women technologists may not have access to mentors to support their career

To help women reach their full potential in the industry, we believe that it is imperative that access to mentorship initiatives
aimed at supporting women to achieve their short-term and mid-term careers goals as well as advance to more senior positions.

* Problem 2: Women technologists may not have women role models to be inspired by

One of the call to action from PwC's report stated that: *You can’t be what you can’t see: The importance of visible role models at all levels.*

We aim build a list of women in the industry role models at all levels and *shout louder about the role models already working in tech...so that they become more visible* to everyone of us in the field.

* Problem 3: Women technologists may feel isolated and excluded in a male-dominated industry

We aim to help combat the feeling of being isolated and excluded by creating opportunities for networking, being mentored and potentially also mentoring other women who are a level or two below them in terms of experience and seniority.

* Platform Goals
1. Grow list of volunteer women in tech mentors
2. Publicly recognize/ promote inspiring women in tech from all levels
3. Provide a safe, easy to use platform for networking with other women in the field

## Scope Plane
* Feature Planning
When planning the Rising Women's features and scope, we drew up a the Desirability, Importance and Viability analysis of all the features to be included in the project, and ranked each of these by order of importance from low (1) to high (5). The features that ranked the highest will be prioritised and delivered as part of the MVP. The target users for each ranked feature were also included.

| # | Feature | Target User | Desirability | Importance | Viability  | Delivered |
| --- | --- | --- | --- | --- | --- | --- |
| User Accounts |  |  |  |  |  |  |
| 1 | User Role Permissions | All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 2 | Account Registration | All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 3 | User Email Confirmation | All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 4 | Password Reset | All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 5 | Social Media Registration &amp; Login | All Visitors | 5 | 2 | 2 | ❌ |
| 6 | User Profile Page | Registered Users | 5 | 5 | 5 | ✅ |
| Navigation |  |  |  |  |  |  |
| 7 | Top Navigation to include: logo, search bar, my account (register, login) | All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 8 | Top Navigation to include: my account (my profile, logout), bookmark | Logged In Users | 5 | 5 | 5 | ✅ |
| 9 | Top Navigation Search Bar: to be enabled for mentor name, description and category search | All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 10 | Top Navigation to include: my account (my profile, logout) and bookmark | Logged In Superadmins | 5 | 5 | 5 | ✅ |
| 11 | Main Navigation to include links to: mentors, inspirational women in tech, about us | All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| Mentors |  |  |  |  |  |  |
| 12 | Featured Mentors | All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 13 | Mentor Categories (Expertise) | All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 14 | Mentor Detail page to include: [add-fields-here] | All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| Bookmark |  |  |  |  |  |  |
| 15 | Individual User's Bookmark - Create, Read, Update and Delete Bookmark | Logged In Users | 5 | 5 | 5 | ✅ |
| Digital Marketing |  |  |  |  |  |  |
| 16 | Social Media Presence | Superadmins | 5 | 5 | 5 | ✅ |
| Email Marketing |  |  |  |  |  |  |
| 17 | Email Subscription, Powered by MailChimp | Registered Subscribers | 3 | 3 | 3 | ❌ |
| Contact Us |  |  |  |  |  |  |
| 18 | Contact Form | All Users <sup>1</sup> | 3 | 3 | 3 | ❌ |


1. All Users: Site Visitors, Logged In Users, Shop Owners, Superadmins


## Structure Plane
### Interaction Design
* User Flow Diagram
### Information Architecture
* Site Map
### Database Design
* Database ERD
* Data Modelling
    * User Model
    * UserProfile
    * Category Model
    * Subcategory Model
    * Mentor Model
    * Bookmark Model
### User Stories

## Skeleton Plane
* Wireframes
## Surface Plane
* Typography
* Colour Palette
* Imagery
# Agile Methodology
* GitHub Projects
# Features
* Mentor Expetise Categorization
* Defensive Programming
* Accessibility
* Extra Meta Tags for Specific Pages
* Mentor Management - Authorized Personnel Only
* Bookmark
* Site Features Common to All Pages
* Site Pages
# Future Development, Iteration and Implementation
# Technologies Used
## Languages Used
## Frameworks Used
## Databases Used
## Libraries and Packages Used
## Programmes and Applications Used
## Cloud Application Platforms Used
## Cloud Storage Services Used
# Testing
## Bugs, Issues and Solutions
# Deployment and Local Development
## Deployment
## Local Development
* How to Fork
* How to Clone
# Credits
# Acknowledgements

