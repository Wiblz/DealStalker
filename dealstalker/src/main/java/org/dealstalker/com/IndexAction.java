/*
 * Copyright 2006 The Apache Software Foundation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.dealstalker.com;


import com.opensymphony.xwork2.ActionSupport;

import java.awt.List;
import java.util.ArrayList;
import java.util.Date;
import com.opensymphony.xwork2.conversion.annotations.Conversion;
import com.opensymphony.xwork2.conversion.annotations.TypeConversion;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;


/**
 * 
 */
@Conversion()
public class IndexAction extends ActionSupport {
	
	
	ArrayList<Product> productList = new ArrayList<Product>();
	Integer currentPage = 0;
	Integer productPerPage = 50;
	
    public String execute() throws Exception {
        Connection cnx = DriverLoader.getConnection();
        Statement stmt = null;
        String query = "Select * from Products;";
        
        try {
        	    stmt =  cnx.createStatement(
        	                           ResultSet.TYPE_FORWARD_ONLY,
        	                           ResultSet.CONCUR_READ_ONLY);
        	    
        	    ResultSet rs =  stmt.executeQuery(query);
        	    Product tempProduct = null;
                
        	    while (rs.next()) {
        	    	
        	    	tempProduct = new Product();
        	    	tempProduct.setId((rs.getInt("id")));
        	    	tempProduct.setBrandName(rs.getString("Brend"));
        	    	tempProduct.setPrimaryCategory((rs.getString("PrimaryCategory")));
        	    	tempProduct.setSubCategory(rs.getString("SubCategory"));
        	    	tempProduct.setModelName(rs.getString("ModelName"));
        	    	tempProduct.setPrice(rs.getFloat("Price"));
        	    	tempProduct.setPriceCurrency(rs.getString("PriceCurrency"));
        	    	tempProduct.setDescription(rs.getString("Description"));
        	    	tempProduct.setSource(rs.getString("SourceUrl"));
        	    	tempProduct.setResource(rs.getString("ResourceUrl"));
        	    	tempProduct.setIsDiscounted(rs.getInt("isDiscounted"));
        	    	
        	    	productList.add(tempProduct);
                }
        	 
        	}
        	catch(Exception ex) {
        		System.out.println("Handle me please, I am Mysql exception");
        	}
        	finally {		
        		  if (stmt != null) {  stmt.close(); }
        		  cnx.close();
        	}
        
        
    	
        return SUCCESS;
    }
    
    
    
    public ArrayList<Product> getProductList() {
    	return (productList.size() == 0) ? productList : 
    		(ArrayList<Product>) productList.subList(currentPage*50, 
    			((currentPage + 1) * 50 < productList.size()) ? 
    					(currentPage+1) * 50 : productList.size() - 1);
    }
    
    public void setProductList(ArrayList<Product> productList) {
    	this.productList = productList;
    }
    
    
}
