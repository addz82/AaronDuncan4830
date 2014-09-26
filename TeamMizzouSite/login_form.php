<!DOCTYPE html>
<html>
<head>
<title>Login</title>
<style type="text/css" media="all">
.error {
color: red;
}
</style>
</head>
<body>
<h1>Login</h1>
<?php if ($error) {
	print "<p class=\"error\">$error</p>\n";
} ?>
<form name="Login" action="login.php" method="POST">
<input type="hidden" name="action" value="do_login" />
<p><label for="username">User name:</label><input type="text" name="username" id="username" value="<?php print $username; ?>" /></p>
<p><label for="password">Password:</label><input type="password" name="password" id="password" /></p>
<p><input type="submit" name="submit" value="Submit" /></p></form>
</body>
</html>