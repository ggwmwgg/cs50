## Finance (from CS50 course Problem Set 9)

### Description
A website via which users can register, login , view, “buy” and “sell” stocks

#### Technologies used:
- *Python/Flask*
- *HTML*
- *CSS*
- *SQL*

#### Configuring:
- API:
	- Visit iexcloud.io/cloud-login#/register/.
	- Select the “Individual” account type, then enter your name, email address, and a password, and click “Create account”.
	- Once registered, scroll down to “Get started for free” and click “Select Start plan” to choose the free plan.
	- Once you’ve confirmed your account via a confirmation email, visit https://iexcloud.io/console/tokens.
	- Copy the key that appears under the Token column (it should begin with pk_).
	- In your terminal window, execute:
	```
	$ export API_KEY=value
	```
	where ```value``` is that (pasted) value, without any space immediately before or after the ```=```. You also may wish to paste that value in a text document somewhere, in case you need it again later.
- Running
	- Start Flask’s built-in web server (within finance/):
	```
	$ flask run
	```
	- Visit the URL outputted by flask to see the code in action. 

#### Contributing
Pull requests are welcome. For major changes please open an issue first to discuss what you would like to change.