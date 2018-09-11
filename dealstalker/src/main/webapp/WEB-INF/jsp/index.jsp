<!DOCTYPE html PUBLIC 
	"-//W3C//DTD XHTML 1.1 Transitional//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
	
<%@page import="java.util.ArrayList"%>
	
<%@taglib prefix="s" uri="/struts-tags" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
	<title>Deal Stalker</title>
	<s:head />
</head>
<body>
	<div>
		 <div><p><a href="<s:url action="startRegister" />"> Sign up</a>.</p></div>
		 <div><p><a href="<s:url action="startSignin" />"> Sign in</a>.</p></div>
    </div>
    
    <div>
	    <c:forEach var="item" items="${productList}">
	    	<td>${item.id}<td>
		</c:forEach> 
    </div>

</body>
</html>
	
