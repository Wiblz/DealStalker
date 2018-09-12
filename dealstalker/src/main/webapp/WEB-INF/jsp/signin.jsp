<%@ taglib prefix="s" uri="/struts-tags" %>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Register</title>
  </head>
  <body style="background-color: #e5e5e5; text-align: center;">
    <h3>Login Form</h3>
    <s:form action="signin" style="display: flex; flex-direction: column; width: 40%; margin: 0 auto;">
      <s:textfield style="font-size: 18px; margin: 5px 5px; height: 20px; text-align: center;" name="customerBean.email"  label ="Email"/>  
      <s:textfield style="font-size: 18px; margin: 5px 5px; height: 20px; text-align: center;" name="customerBean.password"  label="Password" type="password"/> 
      <s:submit/>
    </s:form>	
  </body>
</html>
