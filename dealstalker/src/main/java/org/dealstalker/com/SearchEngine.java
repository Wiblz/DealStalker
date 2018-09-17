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
        String queryWithParam = createQuery(entry);
        System.out.println(queryWithParam);
        
        if(!checkEntryIfNotEmpty(entry)) {
        	queryWithParam = "SELECT * FROM Products LIMIT 10000";
        }
        
        ArrayList<Product> productList = new ArrayList<Product>();        
        return selectProducts(productList, stmt, cnx,  queryWithParam);
	}
	
	public static ArrayList<Product> selectProducts(ArrayList<Product> productList,Statement stmt,
			Connection cnx, String queryWithParam) throws SQLException {
        
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
		
		appendGender(entry,query);
		appendSearchQuery(entry,query);
		appendCategories(entry,query);
		checkEnd(query);
			
		
		return query.toString();
	}
	
	
	private static void appendGender(SearchEntry entry, StringBuilder query) {
		String gender = "";
		
		if(entry.getGender().equals("Male")) {
			gender = "m";
		}
		if(entry.getGender().equals("Female")) {
			gender = "w";
			
			StringBuilder sb = new StringBuilder();
			ArrayList<String> arr = new ArrayList<>();
			for(String s: entry.getaSubCategory()) {
				sb.append(s + " [W]");
				arr.add(sb.toString());
			}
			entry.setaSubCategory(arr);
			for(String s: entry.getbSubCategory()) {
				arr = new ArrayList<>();
				sb.append(s + " [W]");
				arr.add(sb.toString());
			}
			entry.setbSubCategory(arr);
			for(String s: entry.getcSubCategory()) {
				arr = new ArrayList<>();
				sb.append(s + " [W]");
				arr.add(sb.toString());
			}
			entry.setcSubCategory(arr);
		}
		
		if(!gender.equals("")) {
			query.append("Gender = '"+ gender + "' AND");
		}
	}
	
	private static void appendSearchQuery(SearchEntry entry, StringBuilder query) {
		String[] str = entry.getSearchQuery().split("\\s+");
		if(!entry.getSearchQuery().equals(""))
			for(int i = 0; i< str.length; i++) {				
				query.append(" (ModelName LIKE '" + str[i] +"' OR");
				query.append(" Description LIKE '" + str[i] +"' OR");
				query.append(" Brand LIKE '" + str[i] +"')  AND");
			}
	}
	
	private static void appendCategories(SearchEntry entry, StringBuilder query) {
		boolean isPresentAny = entry.getcSubCategory().size() > 0 || 
				entry.getaSubCategory().size() >0 || 
				entry.getbSubCategory().size() > 0; 
		
		if(!isPresentAny) return;
	    
	    query.append( "(" );
		
		for(String s: entry.getaSubCategory()) {
			query.append(" SubCategory='" + s +"' OR");
		}
		
		for(String s: entry.getbSubCategory()) {
			query.append(" SubCategory='" + s +"' OR");
		}
		
		
		for(String s: entry.getcSubCategory()) {
			query.append(" SubCategory='" + s +"' OR");
		}
	}
	
	private static void checkEnd(StringBuilder query) {
		if(query.subSequence(query.length()-2, query.length()).equals("OR")) {
			query = query.delete(query.length()-2, query.length());
			query.append( ")" );
		}
		if(query.subSequence(query.length()-3, query.length()).equals("AND")) {
			query = query.delete(query.length()-3, query.length());
		}
	}
	
	private static boolean checkEntryIfNotEmpty(SearchEntry entry) {
		if(entry == null)
			return false;
		if(!entry.getSearchQuery().equals(""))
			return true;
		if(entry.getcSubCategory().size() > 0 || 
				entry.getaSubCategory().size() > 0 || 
				entry.getbSubCategory().size() > 0)
			return true;
		
		if(!entry.getGender().equals(""))
			return true;
		
		
		return false;
	}
}
