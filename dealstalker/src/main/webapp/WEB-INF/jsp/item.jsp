<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>

<%@taglib prefix="s" uri="/struts-tags" %>

<html>
<head>
<meta charset="UTF-8">
<title>Item</title>
</head>
<body>
<div>
	<div style="display: flex; flex-wrap: wrap; flex-direction: row; justify-content: space-around; width: 100%; margin: 0 auto; margin-top: 50px;">
		<s:property value="currentProduct.modelName"/>
		<s:property value="currentProduct.description"/>
	</div>
	<div >
		<img src=<s:property value="currentProduct.imageUrl"/> style="width: 200px; height: 300px; border: 2px solid #e5e5e5; border-radius: 10px;">
	</div>
	<div style="display: flex; flex-wrap: wrap; flex-direction: row; justify-content: space-around; width: 100%; margin: 0 auto; margin-top: 50px;">
		<s:property value="currentProduct.price"/>
		<s:property value="currentProduct.priceCurrency"/>
	</div>
    <div style="display: flex; flex-wrap: wrap; flex-direction: row; justify-content: space-around; width: 100%; margin: 0 auto; margin-top: 50px;">
		<p> Color: <s:property value="currentProduct.color"/></p>
		<p> Inner ID: <s:property value="currentProduct.innerId"/></p>
		<p> Category: <s:property value="currentProduct.subCategory"/></p>
		<p> Resource: <s:property value="currentProduct.resource"/></p>
		<p> Brand: <s:property value="currentProduct.brandName"/></p>
	</div>
	<div style="display: flex; flex-wrap: wrap; flex-direction: row; justify-content: space-around; width: 100%; margin: 0 auto; margin-top: 50px;">
		<s:property value="currentProduct.brand" />
	</div>
</div>
</body>
</html>