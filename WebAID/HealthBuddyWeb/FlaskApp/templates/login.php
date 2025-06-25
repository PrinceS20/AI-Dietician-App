<?php
	// Database connection
	$servername = "localhost";
	$username = "root";
	$password = "";
	$dbname = "users";

	$conn = new mysqli($servername, $username, $password, $dbname);
	if ($conn->connect_error) {
		die("Connection failed: " . $conn->connect_error);
	}

	// Retrieve user input
	if ($_SERVER["REQUEST_METHOD"] == "POST") {
		$username = $_POST["username"];
		$password = $_POST["password"];

		// Server-side validation
		if (empty($username) || empty($password)) {
			echo "Please fill in all fields.";
		} else {
			if ($_POST["form_type"] == "register") {
				// Check if username already exists
				$query = "SELECT * FROM users WHERE username = '$username'";
				$result = $conn->query($query);
				if ($result->num_rows > 0) {
					echo "Username already exists. Please choose a different username.";
				} else {
					// Insert new user into the database
					$query = "INSERT INTO users (username, password) VALUES ('$username', '$password')";
					if ($conn->query($query) === TRUE) {
						echo "Registration successful. You can now log in.";
					} else {
						echo "Error: " . $query . "<br>" . $conn->error;
					}
				}
			} elseif ($_POST["form_type"] == "login") {
				// Check if username and password match in the database
				$query = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
				$result = $conn->query($query);
				if ($result->num_rows > 0) {
					echo "Login successful. Welcome, " . $username . "!";
				} else {
					echo "Invalid username or password.";
				}
			}
		}
	}

	$conn->close();
	?>