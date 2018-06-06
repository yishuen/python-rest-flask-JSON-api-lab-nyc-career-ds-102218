
# RESTful Flask App with JSON Lab

## Introduction
In this lab, we will practice creating a RESTful flask app. In programming we talk a lot about convention and the importance to adhering to a convention. Usually, we talk about naming variables and functions in an appropriately descriptive manner so that we, and other developers, can easily understand and maintain it. In this lab we will be focusing on the REST convention. We will adhere to the REST principles and create an application that can take requests from and return information to the client. We will see how REST makes it easier to find resources across different applications as well as scale our own application. 

## Objectives
* Understand what is REST
* Build RESTful routes that return JSON data
* Build RESTful routes that return HTML

## What is REST?
What does RESTful mean? REST stands for **Re**presentational **S**tate **T**ransfer. REST provides standards or conventions between computer systems which make it easier to communicate across systems. RESTful systems also are characterized by a separation of concerns for client and server. In other words, we design what the client consumes separate from what the server does. So, we can make changes to our client's view without affecting how the server operates. Another key element of a RESTful system is that they are stateless. Meaning the server does not need to know anything about the client or what *state* the client is in to complete a request. This way, both client and server can understand any messages without knowledge of previous messages.

If all of this sounds a little confusing don't worry. It will make more sense as we learn more about web applications. But the most important take away from REST is that it provides a convention for creating URLs that represent access to an application's specific **resources**. This makes it easier to scale an application and facilitate more predictable communication between different applications. 

## Building RESTful Routes

### Returning JSON

Now that we have a better idea of what REST means, let's try putting it to practice. We already have an app started for us in our app.py file, and we have a couple templates set up for us as well. We're importing some data from a pictures_data.py file, which contains a list of dictionaries with information about various pictures. We will be returning elements of this data depending upon which information the client provides to the URL.

First, we will build out our own API that returns JSON data for all of our pictures. Run `python app.py` in the terminal to start the server.

`Pictures` from pictures_data.py will be our main **resource**. We will follow the pattern of prepending `/api/` to any route that renders JSON data. This format not only differentiates the routes that return data from the routes that return our HTML, it also visually indicates that we are requesting data instead of a regular HTML web page.

#### A Note on JSON Conversion

The three routes we will create for our API are described below.  Take a quick look at the Pictures resource we are using.  It is a list of dictionaries.  We will need to convert this resource into JSON using the Flask's `jsonify` function.  On top of `Flask` and `render_template`, we will need to add `jsonify` to our imports from flask.  Let's walk through the first example together.

```python
@app.route('/api/pictures')
def pictures():
    return jsonify(Pictures)

# returns a list of all pictures
```

We can convert our Pictures resource into JSON by passing it as an argument into the `jsonify` function.  Now, we can see our JSON when we run the app.py file and go to this route in the browser! Yay!!

Now, let's create a route for each individual picture's data.

```python
"/api/pictures/<int:id>" 
# returns a single dictionary for the picture whose ID matches the ID from the URL
```
> **Note:** By putting `int:` before our variable `id` inside the route, we are telling the route to expect an integer. This serves two purposes; it differentiates the route from other routes that may expect a string as a param in our URL, and it ensures that when we pass the `id` variable to our function, it comes through as an integer instead of a string. Our function defined underneath the route will still take the variable `id`.

What if we wanted our API to also return pictures by country? It seems like someone using our app might want to see all pictures by country instead of just getting all of the pictures or a single picture by its ID. Let's define the following route and have it return a list of dictionaries where the country matches the country provided by the client in the URL.

```python
"/api/pictures/<country>" 
# returns a list of dictionaries whose country matches the country from the URL
# Hint: compare these strings without case sensitivity
```

### Returning HTML

Alright, our API is up and running. Nicely done! Now, let's create some more aesthetic views for our client with HTML templates.

You'll notice that our app already has some templates set up for us. Let's define some RESTful routes that render the appropriate HTML templates for both a single Picture object as well as a list of picture objects.

In future lessons, we will query a relational database containing data on related objects to pull the information we want to render in the HTML view.  For now, we will keep it simple by focusing only on our Pictures resource. To retrieve the data we want to pass to the templates, we must import Pictures from our pictures_data.py file.

Once we pass the correct information to the render_template function, our data should display when we visit the provided routes!

> **Note:** Look carefully at how the templates are expecting the data to be formatted. 

We will want three RESTful routes that return HTML for us:
* `'/pictures'` returns page showing all pictures

* `'/pictures/<int:id>'` returns a page showing the picture having the provided `id`

* `'/pictures/<country>'` returns a page showing pictures of places from the provided `country` 

> **Note:** These will follow a similar pattern to our API routes, however these routes will not be prepended with '/api/' since they will be returning HTML instead of JSON data.

Once we have all of our routes defined, visit them in the browser to see them working! 

# Summary

Great work! In this lab we practiced building a RESTful web application. We designed our URLs to act as resources so that if we wanted all pictures our URL would start with `/api/pictures` and if we wanted something more specific like the the pictures from the USA, our URL would become `/api/pictures/usa`. We then created routes for pages rendering HTML views via HTML templates. We used the information provided in the URL to find the correct data to pass along to our templates for rendering the HTML. Now, we understand that having a convention for defining routes makes it not only easier to scale our application but also easier to communicate between the front-end and back-end of our application. 
