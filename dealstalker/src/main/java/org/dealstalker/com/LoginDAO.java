package org.dealstalker.com;

import java.sql.Blob;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;


public class LoginDAO {
	public static boolean validate(String login, String password) {  
		boolean status = false;  
		try {
			Connection con = DriverLoader.getMySqlConnection();

			PreparedStatement ps = con.prepareStatement(  
					"select hash, salt from customers where login=?");
			ps.setString(1, login.toLowerCase());
			ResultSet rs = ps.executeQuery();  
			status = rs.next();  
			
			if (status) {
				Blob salt = rs.getBlob("salt");
				Blob hash = rs.getBlob("hash");
				status = Passwords.isExpectedPassword(password.toCharArray(), salt.getBytes(1, (int)salt.length()),
													   				 		  hash.getBytes(1, (int)hash.length()));
			}
			
		} catch (Exception e) {
			e.printStackTrace();
		}  
		return status;  
	}  
}
