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

## **Bugs and Fixes**

* **Bug:** Checkout App - bad.request in /checkout/cache_checkout_data, webhook payment.intent gave 301err.
* **Solution:** Typos ins checkout views.py file. Once resolved issue went.

* **Bug:** Search - if class not found, there was no error message stating this.
* **Solution:** Had to add an if sport, else statement to the sports.html template to resolve this.

* **Bug:** Delete comment - when viewing delete_comment.html, if the user wishes to cancel this the back button returns an object error.
* **Solution:** Had to use javascript for the href in the back to post button.

* **Bug:** Post Like - liking a post results in SimpleLazyObject error.
* **Solution:** This was because the model here was using UserProfile as a foreign key not User. In PostLike in views.py wherever the request was request.user, this had to become request.user.userprofile.

### Unsolved Bugs

Unfortunately I didn't have time to resolve all the bugs I encountered. The unsovlved bugs are below. Despite these, the site is fully functional.

* **Bug:** Checkout App - full name is not saved into profile when the checkbox is ticked.
* **Solution:** This bug is currently unsolved, so users have to manually enter their full name in the checkout billing details form.

* **Bug:** Footer - on mobile the site links become untidy when trying to fit
* **Solution:** This bug is currently unfixed. Unforuntately I couldn't solve this using css in the time given.

## **Validator Testing**

**HTML**
I have tested the HTML code using the [W3C HTML Validator](https://validator.w3.org/). The errors found were caused by the django curly braces {} and also using {% extends "base.html" %} in place of <"head"> tags.

**CSS**
I have tested the CSS code using the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) and found no errors.