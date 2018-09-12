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
	<div style="display: flex; flex-direction: column; text-align: center; padding-top: 50px;">
    <div>
    	<s:form action="searchItems" style="display: flex; justify-content: space-around; margin: 0 auto; width: 50%; height: 54px; margin-bottom: 50px;">
	        <s:textfield style=" margin-top: 10px; width: 70%; height: 30px; text-align: center; font-size: 20px; color: black;" placeholder="Search" type="text" name="searchString" label="Search" />
        	<s:submit/>
        </s:form>
    </div>
    
	<div>
		 <div style="box-sizing: border-box; padding: 7px; height: 40px; text-align: center; width: 200px; border: 2px solid #e5e5e5; margin: 20px auto; border-radius: 20px;">
		 	<a style="font-weight: bold; font-size: 18px; color: black; text-decoration: none;" href="<s:url action="startRegister" />"> Sign up</a>.
		 </div>
		 <div style="box-sizing: border-box; padding: 7px; height: 40px; text-align: center; width: 200px; border: 2px solid #e5e5e5; margin: 0px auto; border-radius: 20px;">
		 	<a style="font-weight: bold; font-size: 18px; color: black; text-decoration: none;" href="<s:url action="startSignin" />"> Sign in</a>.
		 </div>
    </div>
    
    
    <div style="width: 80%; margin: 0 auto;">
	    <s:iterator value="productList">
			<div style="display: flex; flex-direction: row;">
				<div style="width: 30%; margin-right: 30px;">
		      		<p><s:property value="modelName"/></p>
		        	<p><s:property value="imageUrl"/></p>
		    	</div>
		    	<div style="width: 200px; height: 200px;">
		      		<img style="width: 100%; border: 2px solid #e5e5e5; border-radius: 10px;" src="<s:property value="imageUrl"/>" alt="image" > 
		      	</div>
		 	</div>
		</s:iterator>
    </div>
	</div>
</body>
</html>
	
