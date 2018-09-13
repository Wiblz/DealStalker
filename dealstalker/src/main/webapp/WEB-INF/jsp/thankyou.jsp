<%@ taglib prefix="s" uri="/struts-tags" %>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Registration Successful</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  </head>
  <body style="background-image: url(./backgrounds/background.jpg); text-align: center; padding-top: 50px;">
    <div class="container">
      <div class="row">
        <h3>Thank you for registering for a prize.</h3>

        <p style="font-weight: bold;">Your registration information: <s:property value="customerBean" /> </p>

        <a style="text-decoration: none; font-weight: bold;" href="<s:url action='index' />" >Return to home page.</a>
      </div>
    </div>
  </body>
</html>
