package org.dealstalker.com;

import java.net.UnknownHostException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

import com.mongodb.MongoClient;
import com.mongodb.MongoClientURI;

public class DriverLoader {
	public static void Load(){
		try {
	        Class.forName("com.mysql.jdbc.Driver").newInstance();
	    } catch (Exception ex) {
	    	System.out.println(ex.getStackTrace());
	    }
	}
	
	
	public static Connection getMySqlConnection() {
		Connection conn = null;
		try {
		    conn =
		       DriverManager.getConnection("jdbc:mysql://localhost/dealstalker?use"
		       		+ "Unicode=true&"
		       		+ "useJDBCCompliantTimezoneShift="
		       		+ "true&useLegacyDatetimeCode="
		       		+ "false&serverTimezone=UTC&useSSL=false&" +
		                                   "user=root&password=12345Black!");
		    // Do something with the Connection
		} catch (SQLException ex) {
		    // handle any errors
		    System.out.println("SQLException: " + ex.getMessage());
		    System.out.println("SQLState: " + ex.getSQLState());
		    System.out.println("VendorError: " + ex.getErrorCode());
		}
		
		return conn;
	}
	
	public static MongoClient getMongoClient() {
		try {
			return new MongoClient(new MongoClientURI("mongodb://localhost:27017"));
		} catch (UnknownHostException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return null;
	}
}
