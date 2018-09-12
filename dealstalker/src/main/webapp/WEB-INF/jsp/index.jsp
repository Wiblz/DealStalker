<!DOCTYPE html PUBLIC 
	"-//W3C//DTD XHTML 1.1 Transitional//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
	

	
<%@taglib prefix="s" uri="/struts-tags" %>

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
	<title>Deal Stalker</title>
	<s:head />
</head>
<body>

    <div>
    	<s:form action="searchItems">
	        <s:textfield name="searchString" label="Search" />
        	<s:submit/>
        </s:form>
    </div>
    
	<div>
		 <div><p><a href="<s:url action="startRegister" />"> Sign up</a>.</p></div>
		 <div><p><a href="<s:url action="startSignin" />"> Sign in</a>.</p></div>
    </div>
    
    
    <div>
		<s:iterator value="productList">
			<div>
		      	<p><s:property value="modelName"/></p>
		        <p><s:property value="imageUrl"/></p>
		      	<img src="<s:property value="imageUrl"/>" > 
		 	</div>
		</s:iterator>
    </div>

</body>
</html>
	
