# Dumb as dirt API query for Tesla's used inventory

Everything I had found was using a querystring with URL which wasn't working for me. 
This uses the API instead, but in a workaround kind of way. Queries sent through the request library were all failing, so fell back on Selenium. 
Change the hard coded path to your version of the Chrome Driver. 

You will need to install Selenium and BeautifulSoup 4. 

This queries the API and displays the results by showing some properties. You can easily create your own automation with it, send 
