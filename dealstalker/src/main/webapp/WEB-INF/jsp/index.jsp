<!DOCTYPE html PUBLIC
	"-//W3C//DTD XHTML 1.1 Transitional//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<%@taglib prefix="s" uri="/struts-tags" %>

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
	<title>Deal Stalker</title>
	<meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
	<s:head />
</head>
<body>
	<div class="container" style="background-image: url('./backgrounds/background.jpg');">
		<c:choose>
    		<c:when test="${session.login != null}">
    			<div>
    				<s:property value="#session.login" />
    			</div>
    		</c:when>    
    		
    		<c:otherwise>
    			<div>
    				<span> Hello, dear guest. </span>
    			</div>
    		</c:otherwise>
		</c:choose>
		<div class="row">
			<div style="display: flex; flex-direction: column; text-align: center; padding-top: 50px;">
		    <div>
		    	<s:form action="searchItems" >
			        <s:textfield style="display: inline-block; margin: 0 auto; border-radius: 20px; margin-top: 10px; width: 600px; height: 30px; margin-bottom: 20px; text-align: center; font-size: 20px; color: black;" placeholder="Search" type="text" name="entry.searchQuery" label="Search" />
		        	<s:radio key="entry.gender" list="genders" />
		     		<s:checkboxlist key="entry.aSubCategory" list="aCat" />
		     		<s:checkboxlist key="entry.bSubCategory" list="bCat" />
		     	    <s:checkboxlist key="entry.cSubCategory" list="cCat" />
		     	    <s:select key="entry.brand" list="brands" />
		        	<s:submit value="Search" style="display: inline-block; margin: 0 auto; width: 100px; height: 30px; border-radius: 15px;"/>
		        </s:form>
		    </div>

			<div>
				 <div style="box-sizing: border-box; padding: 7px; height: 40px; text-align: center; width: 200px; border: 2px solid #e5e5e5; margin: 20px auto; border-radius: 20px;">
				 	<a style="font-weight: bold; font-size: 18px; color: black; text-decoration: none;" href="<s:url action="startRegister" />">Sign up</a>
				 </div>
				 <div style="box-sizing: border-box; padding: 7px; height: 40px; text-align: center; width: 200px; border: 2px solid #e5e5e5; margin: 0px auto; border-radius: 20px;">
				 	<a style="font-weight: bold; font-size: 18px; color: black; text-decoration: none;" href="<s:url action="startSignin" />">Sign in</a>
				 </div>
		    </div>

		</div>
		</div>
			<div style="display: flex; flex-wrap: wrap; flex-direction: row; justify-content: space-around; width: 100%; margin: 0 auto; margin-top: 50px;">
	        <s:iterator var="entry" value="productList" status="st">
	        <s:form action="itemInfo.action">
				<div style="width: 30%; display: flex; flex-direction: row; justify-content: space-around; margin-top: 15px; margin-bottom: 15px;">
		    	<div style="margin-right: 30px;">
		      </div>
		      <div style="display: flex; flex-direction: column; justify-content: space-around;">
              <p style="font-size: 16px; font-weight: bold;"><s:property value="entry.modelName"/></p>
		      	<p style="font-size: 16px; font-weight: bold;"><s:property value="entry.price"/></p>
		      	<p style="font-size: 16px; font-weight: bold;"><s:property value="entry.priceCurrency"/></p>
		      	<p style="font-size: 16px; font-weight: bold;"><s:property value="entry.id"/></p>
		      	<s:hidden name="id" value="%{#entry.id}" />
		      	<s:submit type="image" value="" name ="item" src="%{#entry.imageUrl}" style="width: 200px; height: 300px; border: 2px solid #e5e5e5; border-radius: 10px;"/>
		      </div>
				</div>
			</s:form>	
			</s:iterator>
		    </div>
		    
		    <div>
		    	<s:form action="next" >
		    		<s:submit value="Next" style="display: inline-block; margin: 0 auto; width: 100px; height: 30px; border-radius: 15px;"/>
		    	</s:form>
		        <s:form action="prev" >
		            <s:submit value="Previous" style="display: inline-block; margin: 0 auto; width: 100px; height: 30px; border-radius: 15px;"/>
		    	</s:form>
		    	<s:property value="currentPage" />
		    </div>
	</div>
</body>
</html>
