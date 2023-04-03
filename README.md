# FHIR SQL Builder Demo

This is a set of instructions to run and modify the FHIRSQLBuilder demo, including an outline of how it works.

## Overview:

- We generate synthetic patient populations via Synthea
- Send them via HTTP to a FHIR Server hosted on AWS
- Use the FHIRSQLBuilder to map the properties of FHIR resources into columns in custom table definitions
- The FHIRSQLBuilder then loads the data into these tables automatically
- We can build custom cubes based on these tables and create dashboards on top of the cubes to visualise the data

## To explore our existing demo:

- Start the instance i-04d2542875fdd193a named UKFHIRSERVER on the UK Sales Engineering AWS account
- Add your IP Address to the inbound security rules for both ports 22 and 52773, protocol: TCP 
- Download PuTTY at https://www.putty.org/ to SSH to the instance
  - IP: 52.56.68.107
  - Connection/SSH/Auth/Credentials/Private Key File for Authentication: UKFHIR.ppk
  - Run:   iris start irishealth   from the PuTTY command line to start the IRIS instance
 - Open the Management Portal at http://52.56.68.107:52773/csp/sys/%25CSP.Portal.Home.zen?$NAMESPACE=FHIR
    - Log in with Username: SuperUser , Password: ensemble

- Go to https://wrc.intersystems.com/wrc/coDistEvaluation.csp and follow the instructions to set up the FHIR SQL Builder in a container
  - You may have to add   command: --check-caps false  to the docker compose file (as attached)
  - Also note that steps 8 and 15 should say port 52773 not 52772
  - You will also need to add the IP Address of your container to the inbound security rules on the UKFHIRSERVER, port 52773
 
- Open the FHIR SQL Builder UI at http://localhost:52773/csp/fhirsql/index.csp#/. Here you can inspect or edit the current transformation specifications (mappings from FHIR resources to tables), refresh the projections, or add new repositories to analyse. 
 
 Warning: Editing the Specifications may affect functionality of later parts of the demo if not careful (see Editing the Specifications section below) 
 
 Note also that at the time of writing, the Builder needs to be 'woken up' by inspecting the Transformation Specification of a local repository before editing Transformation Specification on a remote repository (like the one on AWS).

Everything should now be set up. You can explore:
 - The Transformation Specifications in the SQLBuilder UI
 - The generated tables in System Explorer in the Management Portal
 - The cubes in the Architect
 - The dashboards (called Busy Dash and Quieter Dash) in the User Portal

## Deeper look at the components:

### Generating Patients:


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

### The FHIR Server:

Installation instructions at https://docs.intersystems.com/irisforhealth20221/csp/docbook/DocBook.UI.Page.cls?KEY=HXFHIR_server_install, or use our instance i-04d2542875fdd193a named UKFHIRSERVER on the UK Sales Engineering AWS account (access as in the 'To explore our existing demo' section)

If you want to load your generated data onto the instance:
 - Edit the directory variable in postall.py to your output folder in the Synthea directory
 - Add your IP to the S

