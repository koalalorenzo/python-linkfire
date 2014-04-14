python-linkfire
===============

Python linkfire.com API. To install it use `pip` command:

    pip install -U python-linkfire

## Basic Usage
In order to use the API, you must have a valid account on [linkfire.com](https://linkfire.com). Every API Object in this library will use the method `authenticate()` that will catch the API keys you need to perform every call to the linkfire server.

Every link must have these information:

 * The old URL
 * A title
 * A description
 
Once you have all these informations you can create a Link Object in this way:

    from linkfire import Link
    
    my_link = Link(
        url="http://who.is.lorenzo.setale.me/?",
        title="my website", 
        description="Description of a super cool website."
    )
    
And then you have to autenticate the API object in this way:

    my_link.authenticate(username, password)

Once you get authenticated, you can perform the main API call to make the link shorter:

    my_link.make_it_shorter()
    
Once it will be ready you can use the Link object as normal string or use its property to get the shorter URL:

    my_link.shortlink
    print str(my_link)

