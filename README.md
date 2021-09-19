# video-scrubber
multimedia metadata scrubbing microservice


## Data model

![image](https://user-images.githubusercontent.com/37352122/133807312-1481d302-e48f-4a20-8030-ccc73b4fcd89.png)


## API structure

![image](https://user-images.githubusercontent.com/37352122/133819186-913c1167-c535-46b2-ad75-4d8fe31eeabc.png)

A [Postman collection](postman/VideoScrapper.postman_collection.json) is included with all the sample input and output request formats, In order to properly test the API.

## Deployment

This application has been deployed in a digitalOcean droplet and made accessible under the following route:
-http://159.89.103.171/api/v1

For the database system, a MYSQL instance was used to store the application resources and relations.

I used gunicorn as web server along with ngnix to proxi traffic to the app instance.

## Usage
- Create a user making a POST request on http://159.89.103.171/api/v1/users/ according to the postman collection format.
- Upload files making post requests to http://159.89.103.171/api/v1/users/<user_id>/files/ endpoint as follows:
![image](https://user-images.githubusercontent.com/37352122/133867844-c745b432-f6d0-453f-8fbb-70ad61f358fd.png)

- Check and update File metadata as follows:
![image](https://user-images.githubusercontent.com/37352122/133867895-5b160744-a651-43c2-aa6f-f42d946c300c.png)


The API JSON responses will guide you to different URLs for viewing or updating the resources.
