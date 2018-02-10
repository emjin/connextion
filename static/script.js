function returnResults() { //gets and prints results from 
	document.getElementById("showrec").innerHTML = "- Results -";
	document.getElementById("dashes").innerHTML = "- - -";
	
	var mysql      = require('mysql');
	var connection = mysql.createConnection({
	  host     : 'connextionopps.database.windows.net',
	  user     : 'connextion',
	  password : 'T1n4andEmm4andM1r4nd4!',
	  database : 'Opportunities'
	});

	connection.connect();

	connection.query('SELECT * from programs where cost=0', function(err, rows, fields) {
	  if (!err)
	    console.log('The solution is: ', rows);
	  else
 	   console.log('Error while performing Query.');
	});

	connection.end();
}
