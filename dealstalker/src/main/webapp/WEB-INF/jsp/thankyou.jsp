<%@ taglib prefix="s" uri="/struts-tags" %>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Registration Successful</title>
  </head>
  <body style="text-align: center; padding-top: 50px; background-color: #e5e5e5;">
    <h3>Thank you for registering for a prize.</h3>

    <p style="font-weight: bold;">Your registration information: <s:property value="customerBean" /> </p>

    <a style="text-decoration: none; font-weight: bold;" href="<s:url action='index' />" >Return to home page.</a>
  </body>
</html>
