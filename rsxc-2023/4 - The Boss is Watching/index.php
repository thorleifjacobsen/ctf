<html>
<head>
	<title>The Boss is Watching</title>
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
	<h1>The Boss is Watching</h1>
	<form method="post">
		<p>Input a valid IP to ping:</p>
		<input type="text" name="ip">
		<input type="submit" value="Ping">
	</form>
	<pre class='output'><html>
<head>
	<title>The Boss is Watching</title>
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
	<h1>The Boss is Watching</h1>
	<form method="post">
		<p>Input a valid IP to ping:</p>
		<input type="text" name="ip">
		<input type="submit" value="Ping">
	</form>
	<?php
	if ($_SERVER['REQUEST_METHOD'] == 'POST') {
		$ip = $_POST['ip'];
		
		if (preg_match('/[&|;`\'" ]/',$ip)) {
			echo "<p align='center' style='color:red;'>Illegal Input Discovered</p>";
			die();
		}
		
		$blocked_commands = array("dir", "strings", "ls", "cat", "whoami", "pwd", "ps", "id", "echo", "kill", "touch", "more");
		foreach($blocked_commands as $command) {
			if (stripos($ip, $command) !== false) {
				echo "<p align='center' style='color:red;'>Illegal Command Discovered</p>";
				die();
			}
		}
		
		$output = shell_exec("ping -c 1 $ip");
		echo "<pre class='output'>$output</pre>";
	}
	?>
</body>
</html>
</pre></body>
</html>
