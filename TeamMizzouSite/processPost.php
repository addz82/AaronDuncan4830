<?php
// We can also traverse $_POST with a foreach
// Reference: http://us1.php.net/manual/en/control-structures.foreach.php
foreach ($_POST as $key => $value) {
	print "$key = $value<br />\n";
}
?>
