<html>
<head>
	<title>Blind Ambition</title>
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
	<h1>Blind Ambition</h1>
	<form method="post">
		<p>Input a valid IP to ping:</p>
		<input type="text" name="ip">
		<input type="submit" value="Ping">
	</form>
	<?php
	if ($_SERVER['REQUEST_METHOD'] == 'POST') {
		$ip = $_POST['ip'];
		
		if (preg_match('/[&|;`\'"{}@]/',$ip)) {
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
		
		$ping_command = "ping -c 1 $ip";
		exec($ping_command, $output, $return_var);
		
		if ($return_var === 0) {
			echo "<p align='center' style='color:#0F0;'>Host is up, the results will be sent via e-mail.</p>";
		} else {
			echo "<p align='center' style='color:red;'>Host is down, the results will be sent via e-mail</p>";
		}
		
		// Send IP address and output via email
		//$to = "*SENSORED*@*SENSORED*.com";
		//$subject = "Ping result for $ip";
		//$message = "Ping command: $ping_command \n\n Output: \n\n" . implode("\n", $output);
		//mail($to, $subject, $message);
	}
	?>
</body>
</html>