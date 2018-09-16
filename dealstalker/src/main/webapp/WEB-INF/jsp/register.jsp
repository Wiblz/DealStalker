<%@ taglib prefix="s" uri="/struts-tags" %>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Register</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  </head>
  <body style="background-image: url('./backgrounds/background.jpg'); text-align: center; padding-top: 50px;">
    <div class="container">
      <div class="row">
        <h3>Register for monitoring stuff by completing this form.</h3>

        <s:form action="register" style="display: flex; flex-direction: column; width: 40%; margin: 0 auto;">
          <s:textfield style="font-size: 18px; margin: 5px 5px; height: 20px; text-align: center;" name="customerBean.firstName" label="First name" />
          <s:textfield style="font-size: 18px; margin: 5px 5px; height: 20px; text-align: center;" name="customerBean.lastName" label="Last name" />
          <s:textfield style="font-size: 18px; margin: 5px 5px; height: 20px; text-align: center;" name="customerBean.email"  label ="Email"/>
          <s:textfield style="font-size: 18px; margin: 5px 5px; height: 20px; text-align: center;" name="customerBean.password"  label="Password"  />
          <s:textfield style="font-size: 18px; margin: 5px 5px; height: 20px; text-align: center;" name="customerBean.reapetedPassword"  label="Repeat Password"  />
          <s:submit style="display: inline-block; margin: 0 auto; width: 100px; height: 30px; border-radius: 15px;"/>
        </s:form>
      </div>
    </div>
  </body>
</html>
