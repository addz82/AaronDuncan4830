<?php
// We can use a foreach to traverse the $_GET array
// Reference: http://us1.php.net/manual/en/control-structures.foreach.php
foreach ($_GET as $key => $value) {
	print "$key = $value<br />\n";
	// $_GET['interests'] and $_GET['name'] are both arrays, so we need another foreach to print out their values
	if ($key == 'fname' || $key == 'lname') {
		foreach ($value as $k => $v) {
			print "- $k = $v<br />\n";
		}
	}
}

?>
