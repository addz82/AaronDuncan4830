<?php
	if(!session_start()) {
		header("Location: error.php");
		exit;
	}
	
	//unset($_SESSION['loggedin']);
	
	/*
		http://www.php.net/manual/en/function.session-destroy.php
	*/
	$_SESSION = array(); // unset session variables
	if (ini_get("session.use_cookies")) {
		$params = session_get_cookie_params();
		setcookie(session_name(), '', 1,
			$params["path"], $params["domain"],
			$params["secure"], $params["httponly"]
		);
	}
	session_destroy(); // destroy session
	
	header("Location: login.php");
	exit;
?>