<%@ taglib prefix="s" uri="/struts-tags" %>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Register</title>
  </head>
  <body>
    <h3>Register for monitoring stuff by completing this form.</h3>

    <s:form action="register">
      <s:textfield name="customerBean.firstName" label="First name" />
      <s:textfield name="customerBean.lastName" label="Last name" />
      <s:textfield name="customerBean.email"  label ="Email"/>  
      <s:textfield name="customerBean.age"  label="Age"  />
      <s:textfield name="customerBean.password"  label="Password"  /> 
      <s:textfield name="customerBean.reapetedPassword"  label="Repeat Password"  /> 
      <s:submit/>
    </s:form>	
  </body>
</html>
