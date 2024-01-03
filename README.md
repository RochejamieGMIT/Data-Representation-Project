# Data-Representation-Project

This project is a project for the users to find out information on a specific country of their choosing. 



## Link to web app first page:
https://rochejamie.pythonanywhere.com/find.html

The first page of this app allows users to search for a country by name,
The page then displays mulitple pieces of inforamtion retrieved from the mySQL database table country that stores the countries information. 

The second section returns the weather of the country from the weather API below based in the latitude and longitude that the mysql database returns in the first seciton.
The weather API uses lat and long to retrieve the tempature and weather code. 
The weather code is then processed and converted to a string to describe the weather code.
Weather code examples:
0	Clear sky
1, 2, 3	Mainly clear, partly cloudy, and overcast
further information on weather codes can be found at:
https://open-meteo.com/en/docs

The weater code also matches the name of the ping of the weather picture.
ie weathercode.png, 0.png returns the clear sky picture, 51.png returns a rain picture etc. 

The next section then does the currnecy conversion, taking the currency code from the information returned from the country table, and uses the Currecny Convert API below to convert the 1 euro to the currancy of the country in question. 

finally the map is displayed, the map takes the lat and long from the country table and applies that to the map api below, also the zoom on the map API is set based on the land_area value from the country table. This allows the map to zoom in when displaying smaller countries and zoom out when viewing larger countries.


## Link to web app second  page:
https://rochejamie.pythonanywhere.com/random.html

The second page is a random page, this creates a random variable, and returns the same information as the find page, but the result country displayed in random. 

## Link to web app third  page:
https://rochejamie.pythonanywhere.com/region.html

The third page takes 2 tables from the mysql database, country and regionInfo.

Region info stores the region the country is in, the litercy and the number of phones per 1000 resisdents. 
A table is then populated based on the selected region. 
when selecting a new region, the table rows are deleted and new table rows are added for the new region. 

The query returns the country and capital from the country table, and the region, literacy and phones. 
This page inner joins the tables on the country names. 

This page is mainly just to introduce a second table and showcase the inner join function. 


## Link to web app fourth and final  page:
https://rochejamie.pythonanywhere.com/admin.html

This page is the admin page for the data base, if information of a country needs to be changed, if a country needs to be deleted or added, this can be done from the admin page. 

There is functioning update, delete and create buttons. 

### Links and resources:

world Data added to mysql db table country from:
https://www.kaggle.com/datasets/nelgiriyewithana/countries-of-the-world-2023

More data in second db table regionInfo:
https://www.kaggle.com/datasets/fernandol/countries-of-the-world

Map Api:
https://developer.tomtom.com/

Currecny Convert API:
https://currency-conversion-and-exchange-rates.p.rapidapi.com/latest?from=EUR+&to='+Currency


Weather API:
https://api.open-meteo.com/v1/forecast?latitude='+lat+'&longitude='+lon+'&current=temperature_2m,weather_code&forecast_days=1
