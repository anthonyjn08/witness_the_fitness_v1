# **Witness The Fitness Testing**

[Back to README](README.md)

The site has been tested on various browsers across PC, mobile and tablet and works across all devices.

## **Manual Testing**

I undertook manual testing of functionality of the site to ensure a smooth user experience.

### **Test: Add item to bag**

* **Expected outcome:** When clicking add to bag, the item will be added to the shopping bag.
* **Actual Outcome:** Pass - item successfully added to the shopping bag.

### **Test: Update shopping bag**

* **Expected outcome:** When viewing the shopping bag, users can update or delete items.
* **Actual Outcome:** Pass - users can successfully update or delete items in their shopping bag.

### **Test: Checkout**

* **Expected outcome:** Users are able to successfully complete their purchase using the checkout form.
* **Actual Outcome:** Pass - users can successfully checkout. Any incorrect data in the form displays a message stating what is missing or invalid.

### **Test: Bag item quantities**

* **Expected outcome:** Users are not able to go above or below the min and max quantity limits in the shopping bag.
* **Actual Outcome:** Pass - users can update the quantities of items in the bag but cannot go above or below the min(1) and max(5) values set.

### **Test: Update details during checkout if registered user**

* **Expected outcome:** When checking out, if there billing address is blank, users are able to save their billing details using the checkout form if they have registered to the site.
* **Actual Outcome:** Pass - users can successfully update their billing details with the checkout form if the checkbox is ticked.

### **Test: Order details email**

* **Expected outcome:** When completing an order, users receive an email with the order details.
* **Actual Outcome:** Pass - order confirmation emails sent when an order is completed using google mail.

### **Test: Users can register to the site**

* **Expected outcome:** When clicking on the register link, user can create an account for the site.
* **Actual Outcome:** Pass - users can fill out the register form, this will result in a validation email being sent. When the validation link is clicked the registration is complete.

### **Test: Registered users can create comments on blog posts**

* **Expected outcome:** Registered users are able to complete a comment for and then submit to post comments on blog posts.
* **Actual Outcome:** Pass - users can post comments in the post detail page of blog posts.

### **Test: Registered users can create comments on blog posts**

* **Expected outcome:** Registered users are able to complete a comment for and then submit to post comments on blog posts.
* **Actual Outcome:** Pass - users can post comments in the post detail page of blog posts.

### **Test: Registered users can delete their comments on blog posts**

* **Expected outcome:** Registered users are able to delete their own comments on blog posts.
* **Actual Outcome:** Pass - users can post delete their comments in the post detail page of blog posts.

### **Test: Admins(superusers) can manage classes(products)**

* **Expected outcome:** Admins can use the class management link in the my profile dropdown to add, edit and delete classes using the form.
* **Actual Outcome:** Pass - admins have CRUD fuctionality for the management of classes.

### **Test: Admins(superusers) can manage their own blog posts**

* **Expected outcome:** Admins can use the CRUD functionality in the blog section to create, update and delete their own blog posts.
* **Actual Outcome:** Pass - admins have CRUD fuctionality for the management of their own blog posts.