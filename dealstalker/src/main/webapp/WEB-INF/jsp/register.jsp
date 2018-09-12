<%@ taglib prefix="s" uri="/struts-tags" %>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Register</title>
  </head>
  <body style="text-align: center; background-color: #E5E5E5; padding-top: 50px;">
    <h3>Register for monitoring stuff by completing this form.</h3>

    <s:form action="register" style="display: flex; flex-direction: column; width: 40%; margin: 0 auto;">
      <s:textfield style="font-size: 18px; margin: 5px 5px; height: 20px; text-align: center;" name="customerBean.firstName" label="First name" />
      <s:textfield style="font-size: 18px; margin: 5px 5px; height: 20px; text-align: center;" name="customerBean.lastName" label="Last name" />
      <s:textfield style="font-size: 18px; margin: 5px 5px; height: 20px; text-align: center;" name="customerBean.email"  label ="Email"/>  
      <s:textfield style="font-size: 18px; margin: 5px 5px; height: 20px; text-align: center;" name="customerBean.age"  label="Age"  />
      <s:textfield style="font-size: 18px; margin: 5px 5px; height: 20px; text-align: center;" name="customerBean.password"  label="Password"  /> 
      <s:textfield style="font-size: 18px; margin: 5px 5px; height: 20px; text-align: center;" name="customerBean.reapetedPassword"  label="Repeat Password"  /> 
      <s:submit/>
    </s:form>	
  </body>
</html>
