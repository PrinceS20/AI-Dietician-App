<?php

$conn = "";

try {
	$dbname = "";
	$username = "root";
	$password = "$Prince83";

	$conn = new PDO(
	 dbname=,
		$username, $password
	);
	
$conn->setAttribute(PDO::ATTR_ERRMODE,
					PDO::ERRMODE_EXCEPTION);
}
catch(PDOException $e) {
	echo "Connection failed: " . $e->getMessage();
}

?>
