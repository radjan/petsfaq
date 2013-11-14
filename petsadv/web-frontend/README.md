========================= Pets FAQ web-frontend=======================


1. License

	Currently, all license reserved to Rad Jan.



2. Purpose

	Create frontend modules through AngularJS.
 


3. Enviroments

	3.1. Use Node.js as develop server. http://nodejs.org/

	3.2. Use yeoman as develop tool, include YEOMAN, GRUNT, BOWER. http://yeoman.io/
		
		$ sudo npm install -g yo

	3.3. Use Ruby and Campass as develop tool. http://compass-style.org/install/

		$ sudo gem update --system

		$ sudo gem install compass

	3.4. Use generator-angular to create modules. https://github.com/yeoman/generator-angular

		$ sudo npm install -g generator-angular

	ATTENTION: Please use 'genratro-angular' to add components in a module, and use 'bower' to install libs.

	3.5. Prepare local development environments: after pull web-frontend, switch to the project folder. e.g.: hopital

		$ npm install   // to install dependencies in package.json for node.js environment 

		$ bower update  // to install modules in bower.json for app



4. Useful commands

	The following commands need to be executed in module root folder.


	4.1. start test server:

		grunt server


	4.2. add angular objects, factory, directive ... (e.g. create a factory named test)

	(learn more in https://github.com/yeoman/generator-angular)
		
		yo angular:factory test


	4.3. add outside libs. (e.g. jquery-ui)
		
		bower install jquery-ui



	
