from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from redis import Redis
import config

# Database Connection
host = config.REDIS_CFG["host"]
port = config.REDIS_CFG["port"]
pwd = config.REDIS_CFG["password"]
redis = Redis(host=host, port=port, password=pwd, charset="utf-8", decode_responses=True)

# Flask Application
app = Flask(__name__)

# Helpers
def isempty(input):
	
	result = False

	# An argument is considered to be empty if any of the following condition matches
	if str(input) == "None":
		result = True
	
	if str(input) == "":
		result = True
	
	return result

# Routes
@app.route("/home")
def index():
	
	# View constants
	TITLE="Geolocation-aware applications with Redis"
	DESC="This application allows you to search for breweries that are close to specific cities."
	
	city=request.args.get("city")
	dist=request.args.get("dist")

	if (not isempty(city)) and (not isempty(dist)):

		#All necessary args passed
		print("DEBUG: city = {}".format(city))
		print("DEBUG: dist = {}".format(dist))

		# Task 1 - Scan for a city with a specific name prefix
		## Hint: The cursor-based iteration is already implemented by the client library
		rs = redis.hscan_iter("idx:city_by_name", city + "*", 100)
		
		try:
			# Take the first city
			## BTW: This might cause some unexpected results (e.g., London in the USA doesn't have breweries in the database)
			r = next(rs)
			name = r[0]
			id = r[1]

			# Task 2 - Retrieve the country of the city
			country = redis.hget("ct:{}".format(id), "country")
			
			print("DEBUG: id = {}, city = {}, country = {}".format(id, name, country))

			# Task 3 - Retrieve the coordinates of the city
			pos = redis.geopos("idx:cities", id)
			

			#Task 4 - Find max. 10 close-by breweries
			## Don't fetch the distance, but the id of the brewery and the coordinates only!
			lng = pos[0][0]
			lat = pos[0][1]
			
			brewcoords = redis.georadius("idx:breweries", lng, lat, int(dist), "mi", False, True, False, 10)
			print("DEBUG: coordinates = {}".format(brewcoords))

			#Task 5 - Retrieve brewery details
			breweries = []
			
			for c in brewcoords:
				bid = c[0]
				bcoord = c[1]
				blng = bcoord[0]
				blat = bcoord[1]
				b = redis.hgetall("brw:{}".format(bid))

				breweries.append({ "name" : b["name"], "city" : b["city"], "lng" : blng, "lat" : blat})

				print("DEBUG: breweries = {}".format(breweries))

			# Render
			return render_template('home.html', title=TITLE, desc=DESC, result=breweries,status="{} breweries found in a radius of {} miles that are close to '{}*' in the country {}".format(len(breweries),dist,city, country))
		
		except:
			# No sophisticated error handling here
			err = "Ooops! Did you search for a valid city?"
			return render_template('home.html', title=TITLE, desc=DESC, error=err)
	else:
		# Arguments missing
		return render_template('home.html', title=TITLE, desc=DESC, warn="Please provide the full name or the prefix of a name of a city!")
		
	return render_template('home.html', title=TITLE, desc=DESC)

	

@app.route("/db/test")
def dbtest():
	# View constants
	TITLE="Test Connectivity"
	DESC="Testing database connectivity ..."
	
	try:
		redis.set("_app:db:test", "Database connectivity works as expected!");
		status = redis.get("_app:db:test")
		return render_template('dbtest.html', title=TITLE, desc=DESC, status=status)
	except RedisError as err:
		return render_template('dbtest.html', title=TITLE, desc=DESC, error=err)

@app.route("/")
def root():
	return redirect("/home")
 
# Main    
if __name__ == "__main__":
	app.debug = False
	app.run(host="0.0.0.0", port=5000)
