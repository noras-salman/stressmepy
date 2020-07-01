from stressmepy import StressTest 

# Number of concurent requests to be performed
requests=500

# Construct the request to be performed
s=StressTest("http://www.example.com",requests,options={
    "method":"GET",
    "headers":{"Cookie":"hello_im_a_cookie_header"}
})

# Run the test
s.run()

# Get the results
results=s.results()

# Print the results
print(results)