# fhirsqldemo

This is a set of instructions to run and modify the FHIRSQLBuilder demo, including an outline of how it works.

- We generate synthetic patient populations via Synthea
- Send them via HTTP to a FHIR Server hosted on AWS
- Use the FHIRSQLBuilder to map the properties of FHIR resources into columns in custom table definitions
- The FHIRSQLBuilder then loads the data into these tables automatically
- We can build custom cubes based on these tables and create dashboards on top of the cubes to visualise the data

All of these steps have been done, but I'll run through them in a bit more detail so they can be modified for other uses.



Find the Synthea Patient Population Generator at https://github.com/synthetichealth/synthea. Follow the READ-ME to install and test.

If you want to generate GB (or NI or Ireland) specific data, go to the Synthea International repository at https://github.com/synthetichealth/synthea-international.
Follow the READ-ME to copy the contents into your Sythea folder and test. 

If you want to restrict your population to patients with certain charateristics, you can do this using Synthea Modules. 
There are some examples in synthea/src/main/resources/modules, or create your own custom Modules. For example, we used the keepcoloncancer.json module to (you guessed it) keep patients who had colon cancer.
You should add any custom modules you create into the synthea directory, and then you can use the module from the command line using the -k option.

For example, we generated patients with the command:

run_synthea -p 5 -k keepcoloncancer.json Somerset Bristol

which gives us up to 5 patients from Bristol with colon cancer, as well as a hospitalinformation FHIR Bundle, and a practitionerinformation FHIR Bundle.

Note: Up to 5 patients, not always exactly 5 patients, because of how Synthea uses modules (explained here https://github.com/synthetichealth/synthea/wiki/Keep-Patients-Module)

