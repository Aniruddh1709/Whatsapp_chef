<h1 align="center">WhatsApp Chef</h1>
<h5 align="center">Cuz you're always in the mood for food</h5>

<br>
<div>
  <p>This project aims to create a “virtual chef”, which returns the recipes of food item to the user, accessible to everyone in the form of a WhatsApp chatbot. The process of using the chatbot begins when the user sends an image of a food item. The chatbot then takes the image, sends it to the backend, which runs a machine learning script to detect the type of food item. The model is trained with 2000 images falling into 20 categories. Once detected, the backend then runs a web crawler to search through the internet and return links of recipes for creating the said item. These links are then sent to the user. </p>
</div>

<h2>Technologies used:</h2>

<div>
  <div align="center">
    <img src="https://www.brandeps.com/logo-download/F/Flask-logo-vector-01.svg" width="100">
    <img src="https://twilio-cms-prod.s3.amazonaws.com/images/twilio-mark-red.width-808.png" width="100">
    <img src="https://jeancochrane.com/static/images/blog/pytorch-functional-api/pytorch-logo.png" width="100">
    <img src="https://jsonhilder.github.io/imgs/ngrok-logo.png" width="100">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRR7fvQ745woNd9Q6cSPY230dbzzOD8TGirhg&usqp=CAU" width="100">
  </div>

  <div>
    <h4><b>Flask : </b>Micro webservice backend framework for creating and deploying web apps</h4>
    <h4><b>Twilio : </b>Perform communication functions using its web service APIs</h4>
    <h4><b>Pytorch : </b>To train the image classifier on Food20 dataset</h4>
    <h4><b>ngrok : </b>To expose a web server running on your local machine to the internet.</h4>
    <h4><b>BeautifulSoup : </b>Gets the recipe links from Google</h4>
  </div>
</div>

## Video demo link:

* https://www.youtube.com/watch?v=Y4cgALd04Z4

## Screenshots:

<div align="center">
  <img src="images/screenshot.png" width="800px">
</div>


## Instructions:

* Clone the repository
* Download the trained model from the link below
https://drive.google.com/drive/folders/1ruaB-xkFLX3o7VzZnGbb_H-M37Uzydai?usp=sharing
* Paste it into app/prediction folder
* Go to the official site of twilio an create a free account to get the required account_sid and auth_token and set the environment variables with these values. You will get a twilio whatsapp number.
* Send the joining text from your number to the temporary whatsapp number provided by twilio.
* Go to app/crud_view/resources/controllers.py and edit the account_sid , auth_token as well as replace YOUR_NUMBER and YOUR_TWILIO_NUMBER.
* Navigate to the app folder
* Install Pytorch from the official website according to your PC specifications
* Create a virtual environment
* Run
```py
> pip install -r "requirements.txt"
> python run.py
```
* Download <a href="https://ngrok.com/download">ngrok</a>. Open another console in the ngrok folder and run
``` py
> ngrok http PORT_WHERE_run.py_IS_RUNNING
```
* Copy the url on which ngrok is forwarding and paste it in Twilio->'Programmable Messaging'->'Settings'->'Whatsapp Sandbox Settings'->'When a message comes in'
* You are done! Send a food name or a food image to the number and wait for the recipe.
