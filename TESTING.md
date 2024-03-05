# APHROS Skincare Online Store

![Am I Responsive](docs/readme/amiresponsive.PNG)

(Developer: Martyna Nowak)

[Live Webpage](https://aphros-4bc91bf82566.herokuapp.com/)

## Table of Contents

1. [Validation](#validation)
    1. [HTML Validation](#html-validation)
    2. [CSS Validation](#css-validation)
    3. [Python Linting](#python-linting)
    4. [Accessibility Testing](#accessibility-testing)
    5. [Performance Testing](#performance-testing)
2. [Manual Testing](#manual-testing)
    1. [Device Testing](#device-testing)
    2. [Browser compatibility](#browser-compatibility)
    3. [Testing User Stories](#testing-user-stories)
    4. [Feature Testing](#feature-testing)
3. [Bugs](#bugs)
    1. [Resolved](#resolved)
    2. [Unresolved](#unresolved)

## Validation

### HTML Validation

The W3C Markup Validation Service was used to validate the HTML of the website. All errors found were corrected, currently there are no errors.

See results:

* ![Index Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Faphros-4bc91bf82566.herokuapp.com%2F)
* ![Products Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Faphros-4bc91bf82566.herokuapp.com%2Fproducts%2F)
* ![Product Detail Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Faphros-4bc91bf82566.herokuapp.com%2Fproducts%2F2)
* ![Add Product Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Faphros-4bc91bf82566.herokuapp.com%2Fproducts%2Fadd%2F)
* ![Edit Product Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Faphros-4bc91bf82566.herokuapp.com%2Fproducts%2Fedit%2F2%2F)
* ![Profile Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Faphros-4bc91bf82566.herokuapp.com%2Fprofile%2F)
* ![Cart Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Faphros-4bc91bf82566.herokuapp.com%2Fcart%2F)
* ![Checkout Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Faphros-4bc91bf82566.herokuapp.com%2Fcheckout%2F)
* ![Reviews Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Faphros-4bc91bf82566.herokuapp.com%2Freviews%2Freviews%2F2%2F)
* ![Add Review Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Faphros-4bc91bf82566.herokuapp.com%2Freviews%2Fadd_review%2F2%2F)
* ![Edit Review Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Faphros-4bc91bf82566.herokuapp.com%2Freviews%2Fedit_review%2F12%2F)
* ![Favourites Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Faphros-4bc91bf82566.herokuapp.com%2Ffavourites%2Fview_favourites%2F)
* ![Register Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Faphros-4bc91bf82566.herokuapp.com%2Faccounts%2Fsignup%2F)
* ![Log in Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Faphros-4bc91bf82566.herokuapp.com%2Faccounts%2Flogin%2F)

## Manual Testing

### Feature Testing

**All Pages**

| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** | **Pass/Fail** |
| --- | --- | --- | --- | --- |
| Navigation bar | Responsive | Test on various devices | Collapses on smaller screens | Pass |
| Logo | Leads to Index page when clicked on | Click on the logo | Leads to index page | Pass |
| Logo | Changes on hover | Hover the logo | Changes colour | Pass |
| Navbar links | Lead to relevant pages | Click on the links | Correct pages open | Pass |
| Search bar | Displays search queries | Input query into the form | Shows results for a given query | Pass |
| Order total | Correct order total displays | Add products to cart | Correct order total displays | Pass |
| Product dropdown | Shows product categories | Click on the dropdown | Displays product categories | Pass |
| Product dropdown | Displays products for a relevant category | Click on the dropdown links | Displays products for a relevant category | Pass |
| Free delivery banner | Shows a correct free delivery threshold | Open all pages | Free Delivery Threshold displayed | Pass |
| Footer | Displayed on all pages | Open all pages | Footer appears | Pass |
| Toasts | Appear after an action is performed | Perform | Correct order total displays | Pass |

**Index Page**

| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** | **Pass/Fail** |
| --- | --- | --- | --- | --- |
| Image | Displays on load | Go to the index page | Image appears | Pass |
| Button | Opens the Product Page | Click on the button | Product page opens | Pass |

**Products Page**

| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** | **Pass/Fail** |
| --- | --- | --- | --- | --- |
| Product cards | Display product image | Open the Products Page | Images appear | Pass |
| Product cards | Display product name and price | Open the Products Page | Names and prices appear | Pass |
| Rating div | Display average rating score if the product has any | Find a product with rating | Rating score appears | Pass |
| Product image | Clicking on the image opens a relevant product detail page | Click on the image | Correct Product Detail page opens | Pass |
| Product name | Clicking on the name opens a relevant product detail page | Click on the name | Correct Product Detail page opens | Pass |
| Admin buttons | Appear to the superuser | Log in as superuser | Buttons appear | Pass |
| Product image | Clicking on the image opens a relevant product detail page | Click on the image | Correct Product Detail page opens | Pass |
| Edit button | Opens a product edit page | Click on the button | Edit Product page opens for the correct product | Pass |
| Delete button | Opens a modal | Click on the button | Modal opens | Pass |
| Delete Modal button | Deletes a product | Click on the button | Product deleted | Pass |
| Toasts | Appear when a product is edited or deleted | Edit or delete a product | Toasts appear | Pass |
| Dropdown | Sort products | Select different sorting options | Products sorted correctly | Pass |
| Category page | Appears when clicked on a category name | Click a category name on a product card | Correct products appear | Pass |
| Category name | Appears on a category page | Click a category name on a product card | Correct name appears | Pass |
| Product count | Shows the amount of product within the categoy | Click a category name on a product card | Correct number appears | Pass |
| Product query | Shows relevant products | Type a query into the search bar | Correct products appear | Pass |
| Back to the top button | Takes user back to the top of the page | Click on the button | Works as expected | Pass |

**Product Details Page**

| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** | **Pass/Fail** |
| --- | --- | --- | --- | --- |
| Product Detail page | Displays correct product information | Go to the Product Detail page for any product | Correct information displayed | Pass |
| Product rating | Displays average product rating if exists | Add a few reviews | Correct average rating displayed | Pass |
| Add to Cart button | Adds product to cart | Click on the button | Product added | Pass |
| Quantity selector | Select quantity | Add to cart | Correct quantity added | Pass |
| Add to Cart button | Min value is 1, max value is 99 | Try to add less than 1 or more than 99 products | Impossible to add | Pass |
| Added to Cart toast | Appears when a product is added to the cart | Add to cart | Toast appears | Pass |
| Added to Cart toast | Shows items in cart | Add to cart | Items displayed | Pass |
| Added to Cart toast | Shows total price | Add to cart | Total price correct | Pass |
| Added to Cart toast | Shows how much the user must spent to get free delivery | Add to cart | Works as expected | Pass |
| Added to Cart toast | Go to Secure Checkout button opens cart | Click on the button | Correct page opens | Pass |
| Add to Favourites icon | Adds or removes from favourites | Click on the icon | Works as expected | Pass |
| See Product Reviews Button | Leads to a relevant Reviews page | Click on the button | Correct page opens | Pass |
| Add Review Button | Leads to a relevant Add Review page | Click on the button | Correct page opens | Pass |
| Edit button | Opens a product edit page | Click on the button | Edit Product page opens for the correct product | Pass |
| Delete button | Opens a modal | Click on the button | Modal opens | Pass |
| Delete Modal button | Deletes a product | Click on the button | Product deleted | Pass |

**Add Product Page**

| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** | **Pass/Fail** |
| --- | --- | --- | --- | --- |
| Product form | Loads all the fields | Go to the Add Product Page | Works as expected | Pass |
| Image field | Image name appears | Add image | Works as expected | Pass |
| Product form | Adds a new product | Fill out the form and click submit | New product added | Pass |

**Edit Product Page**

| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** | **Pass/Fail** |
| --- | --- | --- | --- | --- |
| Product form | Fields prepopulated with existing information | Go to the Edit Product Page | Works as expected | Pass |
| Image field | Current image displayed | Go to the Edit Product Page | Works as expected | Pass |
| Product form | Updates the product | Fill out the form and click submit | Product updated | Pass |

**Cart Page**

| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** | **Pass/Fail** |
| --- | --- | --- | --- | --- |
| Table | Display product image, name, price, quantity and subtotal | Add products to cart | Works as expected | Pass |
| Quantity selector | Updates product quantity | Change quantity and click Update | Works as expected | Pass |
| Quantity selector | Min value is 1, max value is 99 | Try to add less than 1 or more than 99 products | Impossible to add | Pass |
| Toast | Appears when quantity updated | Update quantity | Works as expected | Pass |
| Remove link | Removes product from cart | Click on | Works as expected | Pass |
| Toast | Appears when product removed | Remove product | Works as expected | Pass |
| Prices | Subtotal, Cart Total, Delivery and Grand Total show the correct amount | Add products to cart | Works as expected | Pass |
| Secure Checkout button | Opens the checkout page | Click on the button | Works as expected | Pass |

**Checkout Page**

| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** | **Pass/Fail** |
| --- | --- | --- | --- | --- |
| Order Summary | Displays correct details | Add products to cart and go to checkout | Works as expected | Pass |
| Delivery info | Loads correct fields | Go to checkout | Works as expected | Pass |
| Save delivery info | Saves delivery info | Check the tickbox and go to the profile | Works as expected | Pass |
| Stripe payment | Make a payment | Input dummy card details | Works as expected | Pass |
| Spanner | Appears when payment is being processed | Click Complete Order | Works as expected | Pass |
| Toast | Appears when an order is successfully processed | Click Complete Order | Works as expected | Pass |

**Checkout Success Page**

| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** | **Pass/Fail** |
| --- | --- | --- | --- | --- |
| Checkout Success Page | Appears when an order is successfully placed | Place an order | Works as expected | Pass |
| Email | Displays the right user email | Place an order | Works as expected | Pass |
| Order number | Displays an order number | Place an order | Works as expected | Pass |

**Profile Page**

| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** | **Pass/Fail** |
| --- | --- | --- | --- | --- |
| Default Delivery Information form | Displays correct fields | Go to the profile page | Works as expected | Pass |
| Default Delivery Information form | Shows saved delivery info | Save delivery info and go to the profile page | Works as expected | Pass |
| Default Delivery Information form | Updates default delivery info | Click Update Information | Works as expected | Pass |
| Order History | Shows past orders' details | Place orders and go to the profule page | Works as expected | Pass |
| Order number | Displays past order confirmation when clicked on | Click on the order number | Works as expected | Pass |

**Favourites Page**

| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** | **Pass/Fail** |
| --- | --- | --- | --- | --- |
| Favourites Page | Displays products added to favourites by the user | Add products to favourites | Works as expected | Pass |
| Remove from favourites button | Opens a modal | Click the button | Works as expected | Pass |
| Remove from favourites modal | Removes product from favourites | Click the button | Works as expected | Pass |
| Removed from favourites toast | Shows when product succesfully removed | Remove product | Works as expected | Pass |

**Reviews Page**

| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** | **Pass/Fail** |
| --- | --- | --- | --- | --- |
| Reviews page | Displays existing reviews for a product | Go to the Reviews page | Works as expected | Pass |
| Edit review button | Opens the Edit Review page for a relevant review | Click on the button | Works as expected | Pass |
| Delete review button | Opens a modal | Click on the button | Works as expected | Pass |
| Delete review modal | Deletes the correct review | Click on the button | Works as expected | Pass |
| Toast | Appears when a review deleted | Delete a review | Works as expected | Pass |

**Add a Review Page**

| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** | **Pass/Fail** |
| --- | --- | --- | --- | --- |
| Product name and image | Displays correctly | Open the Add a Review page | Works as expected | Pass |
| Review Form | Displays correct fields | Open the Add a Review page | Works as expected | Pass |
| Review Form | Submits a review | Fill out the form and click submit | Works as expected | Pass |
| Go back button | Redirect to the Product Detail page | Click on the button | Works as expected | Pass |
| Toast | Appears when a review is added successfully | Add a review | Works as expected | Pass |

**Edit a Review Page**

| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** | **Pass/Fail** |
| --- | --- | --- | --- | --- |
| Product name and image | Displays correctly | Open the Add a Review page | Works as expected | Pass |
| Review Form | Displays correct fields | Open the Edit a Review page | Works as expected | Pass |
| Review Form | Fields pre-populated with existing information | Open the Edit a Review page | Works as expected | Pass |
| Review Form | Updates the review | Fill out the form and click Update | Works as expected | Pass |
| Toast | Appears when a review is updated successfully | Edit a review | Works as expected | Pass |

**Register Page**

| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** | **Pass/Fail** |
| --- | --- | --- | --- | --- |
| Register form | Displays correct fields | Go to the Register Page | Works as expected | Pass |
| Back to Login button | Redirects to the Log in page | Click on the button | Works as expected | Pass |
| Sign in link | Redirects to the Log in page | Click on the link | Works as expected | Pass |
| Toasts | Appear when a confirmation email is sent and when the email address is confirmed | Create a new account | Works as expected | Pass |
| Confirmation email | Received when a new account is created | Create a new account | Works as expected | Pass |

**Log in Page**

| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** | **Pass/Fail** |
| --- | --- | --- | --- | --- |
| Log in form | Displays correct fields | Go to the Log in Page | Works as expected | Pass |
| Sign up link | Redirects to the Register page | Click on the link | Works as expected | Pass |
| Home button | Redirects to the Index page | Click on the button | Works as expected | Pass |
| Forgot Password link | Redirects to the Forgot Password page | Click on the link | Works as expected | Pass |
| Sign in button | Logs the user in | Click on the button | Works as expected | Pass |
| Toast | Appears when the user logs in successfully | Log in | Works as expected | Pass |

**Log out Page**

| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** | **Pass/Fail** |
| --- | --- | --- | --- | --- |
| Cancel button | Redirects to the Index page | Click on the button | Works as expected | Pass |
| Sign out button | Logs the user out | Click on the button | Works as expected | Pass |
| Toast | Appears when the user logs out successfully | Log out | Works as expected | Pass |

**Forgot Password Page**

| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** | **Pass/Fail** |
| --- | --- | --- | --- | --- |
| Forgot password form | Displays the email field | Go to the Forgot Password | Works as expected | Pass |
| Back to Login button | Redirects to the Log in page | Click on the button | Works as expected | Pass |
| Reset Password button | Send a Reset Password Email | Click on the button | Works as expected | Pass |

**Error Pages**

| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** | **Pass/Fail** |
| --- | --- | --- | --- | --- |
| Custom Error Pages | Displays a correct error number | Manually trigger error | Works as expected | Pass |
| Go Home button | Redirects to the Index page | Click on the button | Works as expected | Pass |




