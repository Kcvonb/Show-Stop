

Hi, my name is Kc Blumgold, and welcome to my web app Show Stop. This is a full stack web application built with Python, Jinja, HTML, CSS, SQL and JavaScript on a Flask framework. 

When users arrive at the homepage, I’ve given them 3 options; the option to login if they’ve already created an account, the option to create an account if they do not have one, or the option to begin searching without an account. I placed a relative URL on the homepage to lead users to the search page.

From the search page, I give users the ability to find a show by specifying a genre, and a date range using datetime. Once users complete these parameters and click on search, I have a flask route in the server that handles a POST request for searching show information using the Ticketmaster API. I also have a dictionary containing parameters to be sent with the API request. In my view function I make a GET request to the Ticketmaster API. I use the python requests library to format the request payload with the Ticketmaster API key and the search parameters. Finally, I use my jinja template to render the results to HTML. The results page now displays all the shows within the search parameters.

Registered users are then able to save their favorite shows. To do this, I use AJAX to post the show data to my server. From here I use SQL alchemy to relate the show to the logged in user and save that relationship to my postgresSQL database. Finally, I create a JSON response to the user, indicating that the show has been successfully saved.

At the bottom of the results page, users are prompted to continue their search, or go to their user page if they are registered. On the user page, users can see their saved shows displayed. Once they click on the link to their desired show, it will take them directly to ticketmaster to learn more about the show, and purchase tickets.

Going forward, the sky's the limit! I have dozens of ideas of features I’d like to implement using an array of languages and data structures. I would definitely like this application to be able to be used globally, as well as use additional API’s from different ticketing platforms. 

That’s Show Stop, thanks for stopping by.
