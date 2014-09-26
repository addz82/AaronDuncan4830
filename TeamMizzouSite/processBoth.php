<?php
	// GET and POST can be used at the same time
	
	print "Post data<br/ >\n";
	foreach ($_POST as $key => $value) {
		print "$key = $value<br />\n";
	}
	
	print "Get data<br/ >\n";
	foreach ($_GET as $key => $value) {
		print "$key = $value<br />\n";
	}
?>