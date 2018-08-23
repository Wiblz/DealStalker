<%@ taglib prefix="s" uri="/struts-tags" %>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Register</title>
  </head>
  <body>
    <s:form action="signin">
      <s:textfield name="customerBean.email"  label ="Email"/>  
      <s:textfield name="customerBean.password"  label="Password" type="password"/> 
      <s:submit/>
    </s:form>	
  </body>
</html>
