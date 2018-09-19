package org.dealstalker.com;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
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
		
		appendBrand(entry,query);
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
		
		if(entry.getGender().equals("Doesn`t matter!")) {
			query.append("(Gender = 'm' OR Gender = 'w' OR Gender='u')AND");
			return;
		}
		
		if(!gender.equals("")) {
			query.append("(Gender ='u' OR Gender = '"+ gender + "') AND");
		}
	}
	
	private static void appendSearchQuery(SearchEntry entry, StringBuilder query) {
		String[] str = entry.getSearchQuery().split("\\s+");
		if(!entry.getSearchQuery().equals(""))
			for(int i = 0; i< str.length; i++) {				
				query.append(" (ModelName LIKE '%" + str[i] +"%' OR");
				query.append(" Description LIKE '%" + str[i] +"%' OR");
				query.append(" Brand LIKE '%" + str[i] +"%')  AND");
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
		
		if(!entry.getBrand().equals("") && !entry.getBrand().equals("ALL BRANDS"))
			return true;
		
		
		return false;
	}
	
	private static void appendBrand(SearchEntry entry, StringBuilder query) {
		if(entry.getBrand().equals("") || entry.getBrand().equals("ALL BRANDS"))
			return;
		query.append("Brand='"+entry.getBrand()+"' AND");
	}
	
	
	public static ArrayList<String> getBrands() throws SQLException{
		ArrayList<String> brands = new ArrayList<String>();
		Connection cnx = DriverLoader.getMySqlConnection();
        Statement stmt = null;
        
       
        String queryWithParam = "SELECT Brand FROM Products LIMIT 10000;";
		try {
    	    stmt =  cnx.createStatement(
    	                           ResultSet.TYPE_FORWARD_ONLY,
    	                           ResultSet.CONCUR_READ_ONLY);
    	    
    	    ResultSet rs =  stmt.executeQuery(queryWithParam);
    	    while (rs.next()) {
    	    	if(!brands.contains(rs.getString("Brand"))) {
    	    		brands.add(rs.getString("Brand"));
    	    	}
            }
    	    Collections.sort(brands);
    	    brands.add(0,"ALL BRANDS");
    	 
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
		return brands;
	}
	
	public static Product getProductItem(int id) throws SQLException {		
		Product tempProduct = new Product();
		if(id == -1)
			return tempProduct;
		String queryWithParam = "SELECT * FROM Products WHERE id='" + String.valueOf(id) + "';";
		Connection cnx = DriverLoader.getMySqlConnection();
        Statement stmt = null;
        System.out.println(queryWithParam);
		try {
    	    stmt =  cnx.createStatement(
    	                           ResultSet.TYPE_FORWARD_ONLY,
    	                           ResultSet.CONCUR_READ_ONLY);
    	    
    	    ResultSet rs =  stmt.executeQuery(queryWithParam);
    	    while (rs.next()) {
    	    	tempProduct.setId((rs.getInt("id")));
    	    	tempProduct.setBrandName(rs.getString("Brand"));
    	    	tempProduct.setSubCategory(rs.getString("SubCategory"));
    	    	tempProduct.setModelName(rs.getString("ModelName"));
    	    	tempProduct.setPrice(rs.getFloat("Price"));
    	    	tempProduct.setPriceCurrency(rs.getString("PriceCurrency"));
    	    	tempProduct.setDescription(rs.getString("Description"));
    	    	tempProduct.setSource(rs.getString("SourceUrl"));
    	    	tempProduct.setResource(rs.getString("ResourceUrl"));
    	    	tempProduct.setIsDiscounted(rs.getInt("isDiscounted"));
    	    	tempProduct.setImageUrl(rs.getString("ImageUrl"));
    	    	tempProduct.setInnerId(rs.getString("InnerId"));
    	    	tempProduct.setColor(rs.getString("Color"));
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
		return tempProduct;
	}
}
