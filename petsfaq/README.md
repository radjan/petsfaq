========================= Pets FAQ =======================


1. License
	Currently, all license reserved to Rad Jan.



2. Purpose
	Pets Care Web Site
 


3. Notes
	3.1 api/: restapi for easy client integration	
	    	  This largly depends on service/ and model/

		Using a simple restAPI base class, 4 put/get api was done:
		/api/v1/hospital
		/api/v1/account
		/api/v1/person
		/api/v1/role
		However, it accepts only simple JSON and require more work on
		extending structure. (for example, extends role to vets...)

	3.2 test/curl.test.sh: this keeps RestAPI test method


	
