- Description
    Welcome to the challenge! In this challenge, you will explore a web application and find an endpoint that exposes a file containing a hidden flag.
    The application is a simple blog website where you can read articles about various topics, including an article about API Documentation. Your goal is to explore the application and find the endpoint that generates files holding the server’s memory, where a secret flag is hidden.
    The website is running [picoCTF News](http://verbal-sleep.picoctf.net:57391/).

- Hints

    `1. Explore backend development with us`
    `2. The head was dumped.`

    ![alt text](image.png)

- Web GUI 

    ![alt text](image-1.png)

- After some searching, I discovered an endpoint that hosts the website's APIs at [#API Documentation](http://verbal-sleep.picoctf.net:57391/api-docs/)

    ![alt text](image-2.png)

    - Noticed a suspicious API at `/heapdump`

    ![alt text](image-3.png)

    - I tried searching for flags with cURL and the flag 
