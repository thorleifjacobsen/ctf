<head>
	<title>Easy As Pie</title>
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
	<h1>Easy As Pie</h1>
	<form method="post">
		<p>Input a valid IP to ping:</p>
		<input type="text" name="ip">
		<input type="submit" value="Ping">
	</form>
	<?php
	if ($_SERVER['REQUEST_METHOD'] == 'POST') {
		$ip = $_POST['ip'];
		$output = shell_exec("ping -c 1 $ip");
		echo "<pre class='output'>$output</pre>";
	}
	?>
</body>
</html>
