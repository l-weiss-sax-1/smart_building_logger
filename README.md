# Smart Building Energy Logger
Purpose: Simulates room temperature and CO2 sensor readings, logs them to a file
Relevance: ESG / SDG 11 & 13 (smart, sustainable buildings). More on SDG goals [see](https://sdgs.un.org/goals) 


### Development notes 
- Git clone the application to a location suitable for you
- `Poetry install` the project. The project requires python 3.12+
- When running the `main.py` there won't be any output to the terminal but the program will write logs to `output.log`. These logs can be fed to a logstash instance. Use Kibana for visualization.
- The output.log provided in the repo is just to be used as an example! Please run the program for about 5 - 10 - 30 minutes to populate the output.log files yourself. You won't have to delete the old logs. They might still be useful ;)


### Lousy implementation
The main.py is currently using the logger.py. All the other files are just stubs not currently in use. However, in the future after we have added logging we would like to start using them. For now.. implement the logging in those files as described in the object on LMS. You don't have to couple the files together!