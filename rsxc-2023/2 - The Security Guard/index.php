<head>
	<title>The Security Guard</title>
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
	<h1>The Security Guard</h1>
	<form method="post">
		<p>Input a valid IP to ping:</p>
		<input type="text" name="ip">
		<input type="submit" value="Ping">
	</form>
	<?php
	if ($_SERVER['REQUEST_METHOD'] == 'POST') {
		$ip = $_POST['ip'];
		
		if (preg_match('/[;`\'"]/',$ip)) {
			echo "<p align='center' style='color:red;'>Illegal Input Discovered</p>";
			die();
		}
		
		$output = shell_exec("ping -c 1 $ip");
		echo "<pre class='output'>$output</pre>";
	}
	?>
</body>
</html>