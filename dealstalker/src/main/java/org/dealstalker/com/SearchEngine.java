package org.dealstalker.com;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import com.opensymphony.xwork2.ActionSupport;

public class SearchEngine {
	
	static public ArrayList<Product> Search(SearchEntry entry) throws SQLException{
        
		Connection cnx = DriverLoader.getMySqlConnection();
        Statement stmt = null;
        String query = "Select * from Products LIMIT 10000;";
        String queryWithParam = createQuery(entry);
        System.out.println(queryWithParam);
        

        
        ArrayList<Product> productList = new ArrayList<Product>();
        
        try {
        	    stmt =  cnx.createStatement(
        	                           ResultSet.TYPE_FORWARD_ONLY,
        	                           ResultSet.CONCUR_READ_ONLY);
        	    
        	    ResultSet rs =  stmt.executeQuery(queryWithParam);
        	    Product tempProduct = null;
                
        	    while (rs.next()) {
        	    	tempProduct = new Product();
        	    	tempProduct.setId((rs.getInt("id")));
        	    	tempProduct.setBrandName(rs.getString("Brand"));
        	    	tempProduct.setPrimaryCategory((rs.getString("PrimaryCategory")));
        	    	tempProduct.setSubCategory(rs.getString("SubCategory"));
        	    	tempProduct.setModelName(rs.getString("ModelName"));
        	    	tempProduct.setPrice(rs.getFloat("Price"));
        	    	tempProduct.setPriceCurrency(rs.getString("PriceCurrency"));
        	    	tempProduct.setDescription(rs.getString("Description"));
        	    	tempProduct.setSource(rs.getString("SourceUrl"));
        	    	tempProduct.setResource(rs.getString("ResourceUrl"));
        	    	tempProduct.setIsDiscounted(rs.getInt("isDiscounted"));
        	    	tempProduct.setImageUrl(rs.getString("ImageUrl"));
        	    	productList.add(tempProduct);
                }
        	 
        	}
        	catch(Exception ex) {
        		System.out.println("Handle me please, I am Mysql exception");
        	}
        	finally {		
        		  if (stmt != null) {  stmt.close(); }
        		  try {
					cnx.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}
        	}
	
        
        return productList;
	}
	public static String createQuery(SearchEntry entry) {
		StringBuilder query = new StringBuilder("SELECT * FROM Products WHERE ");
		
		String[] str = entry.getSearchQuery().split("\\s+");
		String gender = "";
		System.out.println(entry.getGender());
		
		if(entry.getGender().equals("Male"))
			gender = "m";
		if(entry.getGender().equals("Female"))
			gender = "w";
		
		if(!gender.equals(""))
			query.append("Gender = '"+ gender + "' OR");
		
		if(!entry.getSearchQuery().equals(""))
			for(int i = 0; i< str.length; i++) {				
				query.append(" (ModelName LIKE '" + str[i] +"' OR");
				query.append(" Description LIKE '" + str[i] +"' OR");
				query.append(" Brand LIKE '" + str[i] +"') AND ");
			}
		
		for(String s: entry.getaSubCategory()) {
			query.append(" SubCategory='" + s +"' OR ");
		}
		
		for(String s: entry.getbSubCategory()) {
			query.append(" SubCategory='" + s +"' OR ");
		}
		
		
		for(String s: entry.getcSubCategory()) {
			query.append(" SubCategory='" + s +"' OR ");
		}
		
		return (String) query.subSequence(0, query.length()-4);
	}
}
