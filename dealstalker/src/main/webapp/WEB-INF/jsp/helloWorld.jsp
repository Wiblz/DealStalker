<!DOCTYPE html PUBLIC
	"-//W3C//DTD XHTML 1.1 Transitional//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<%@taglib prefix="s" uri="/struts-tags" %>

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
	<title>Hello World</title>
	<meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
	<s:head />
</head>
<body style="background-image: url('./backgrounds/background.jpg'); text-align: center; padding-top: 100px; font-size: 25px;">
	<div class="container">
		<div class="row">
			<div style="text-align: center; width: 50%; margin: 200px auto; color: white; font-size: 20px; font-weight: bold;">
				Hello <s:property value="name"/>, today is <s:property value="dateNow" /><br/>
			</div>
		</div>
	</div>
</body>
</html>
