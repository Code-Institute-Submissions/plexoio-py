## [HOME | RETURN](https://github.com/plexoio/py/tree/main#documentation-index-legacy)

## Actual Features Explained

We are extremely pleased with our accomplishments, particularly given initial concerns about time constraints due to personal reasons, as well as external challenges like government decisions and unexpected changes toward the end.

Reflecting on the project, it's clear that each feature offers room for enhancement and future development, thanks to its modular structure. This iteration introduces simplified design elements and includes all CRUD functionalities: creating products, services, and downloads (admin); reading frontend items (admin & user); updating items (admin); deleting accounts (users); and consistently providing appropriate feedback.

## Homepage

<details>
<summary>Homepage</summary>

### Header & CTA Section
The header introduces users to the platform with a clear call-to-action (CTA) that encourages them to either participate or learn more about the software marketplace.

![Header & CTA Section](../../assets/img/header_cta.png)

### Product & Service Cards & See More Button
The section showcases a highlighted row of product and service cards, each with a brief description and metrics to facilitate an informed choice. A "See More" option allows users to view additional entries.

![Product & Service Cards & See More Button Image](../../assets/img/product_service.png)

### Product Cards & See More
Displays only Product cards. The "See More" link directs users to a comprehensive list of all Product entries.

![Product Cards & See More](../../assets/img/product_instances.png)

### Service Cards & See More
Highlights only Service cards. Users can explore more Service entries by clicking on "See More."

![Service Cards & See More](../../assets/img/service_instances.png)

### Footer
Contains essential links, platform information, newsletter signup, and other resources for users to navigate and understand the platform better.

![Footer](../../assets/img/footer.png)

</details>

## Single Product/Service Page

<details>
<summary>Single Product/Service Page</summary>

![Product/Service Page](../../assets/img/product_service_single.png)

### Card Features
This section details the specifics of the instance, including its description, price, category, likes, comments, newsletter signup and more.

### Add to Cart, Like & Comment Feedback
This feature informs users of the outcome of their actions related to the instance they selected.

### Cart & Payment Process
The cart accumulates the user's choices, allowing them to check out once they have finished selecting their products or services. The cart is versatile; users can increase or decrease the number of items, as well as remove them entirely. Currently, only Stripe payments are accepted, and progressive disclosure is implemented throughout the process.

</details>

## Account Management

<details>
<summary>Account Management</summary>

### Login
The login feature provides a secure interface for users to access their accounts, either manually or through Google login.

![Login](../../assets/img/login.png)

### Signup
This feature allows new users to join the platform by creating an account, either manually or through Google login.

![Signup](../../assets/img/signup.png)

</details>

### User Dashboard

<details>
<summary>User Dashboard</summary>

![User Dashboard](../../assets/img/user_dashboard.png)

#### My Settings
Here, users can modify their personal information, preferences, and limited account settings.

![Settings](../../assets/img/settings.png)

#### My Orders
This section displays a list of orders placed by the user, showing their status, the ability to update them, and other important information.

![My Orders](../../assets/img/orders.png)

#### My Likes & My Comments
Provides an overview of the likes & comments of the user, detailing their action taken.

#### Likes
![My Likes](../../assets/img/likes.png)

#### Comments
![My Comments](../../assets/img/comments.png)

#### My Role
Describes the user's permissions, roles, and capabilities within the platform.

![My Role](../../assets/img/user_role.png)

</details>

### Admin Dashboard

<details>
<summary>Admin Dashboard</summary>

![Admin Dashboard](../../assets/img/admin_dashboard.png)

#### My Settings
In this section, admins can adjust their personal information, preferences, and account settings, which are more extensive compared to regular users.

![Settings](../../assets/img/admin_settings.png)

#### User Management (Future Feature)
- NA

#### Order Management
This page displays all created orders. Edit and details capabilities for each entry are available. Additionally, there is a cleaning button for removing old, unfinished orders.

![Created Orders](../../assets/img/admin_orders.png)

#### Asset Management
Here you'll find options to manage products and services. This section shows how many items have been created and also provides the option to create new ones.

##### Product & Service Control
![Product Control](../../assets/img/admin_product_control.png)

##### Product & Service Create
![Product Create](../../assets/img/admin_product_create.png)

#### File Management
In this section, admins can manage or create download instances that can then be linked to their created products and services.

##### File Control
![File Management Control](../../assets/img/admin_file.png)

##### File Upload
![File Management Upload](../../assets/img/admin_file_upload.png)

#### Comment & Like Management
This area allows the admin to view and manage comments as well as theoretically control likes. The like-update function is active, although changes are not reflected elsewhere in this iteration.

##### Comment
![Comment Image](../../assets/img/admin_comments.png)

##### Like
![Like Image](../../assets/img/admin_likes.png)

#### My Role
This section details the administrative permissions and capabilities available to the user.

![My Role](../../assets/img/admin_role.png)

</details>

## Digital Downloads Marketplace Logic

<details>
<summary>Digital Downloads Marketplace Logic</summary>

#### User Purchases a Product or Service
This process allows users to make purchases using Stripe and create orders. After a successful payment, users can comment and like the product or service they purchased, as well as download the associated file from their user dashboard.

#### Order Instances
This feature allows users to visualize their orders, even if the order was not completed.

</details>

## Support

<details>
<summary>Accountability</summary>

### FAQ
A section containing frequently asked questions about the platform. It may also contain videos to assist users in troubleshooting common issues and learning more about the marketplace.

![FAQ](../../assets/img/faq.png)

### Contact
Provides users with the means to get in touch with platform support for technical issues, feedback, or inquiries.

![Contact](../../assets/img/contact.png)

</details>