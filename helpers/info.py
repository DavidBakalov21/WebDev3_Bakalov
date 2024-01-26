endpoints_info = {
  "endpoints": [
    {
      "path": "/",
      "method": "GET",
      "description": "Get endpoints information",
    },
    {
      "path": "/images/",
      "method": "GET",
      "description": "It will show you an image which name you provided in the endpoint (example:http://localhost:8000/images/frog.png)",
    },
    {
      "path": "/docs/",
      "method": "GET",
      "description": "It will show you a doc which name you provided in the endpoint (example:http://localhost:8000/docs/Lorem.txt)",
    },
    {
      "path": "/",
      "method": "POST",
      "description": "Posts the data you put",
    },
    {
      "path": "/checkURL",
      "method": "POST",
      "description": "It will provide info about url (input example:http://localhost:8000/checkURL, body: {'url':'https://youtu.be/mypath/deeper?param1=xxx&param2=qqq'} (!!! replace '' to double quotation marks !!!!) )",
    },
    {
      "path": "/fileExeminer",
      "method": "POST",
      "description": "it will provide an info about the text file (input example: {'path':'./assets/docs/Lorem.txt', 'word':'Lorem'} , http://localhost:8000/fileExeminer) (!!! replace '' to double quotation marks !!!!)",
    },
  ]
}