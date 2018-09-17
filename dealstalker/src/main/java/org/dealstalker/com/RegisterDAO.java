package org.dealstalker.com;

import java.sql.Connection;
import java.sql.PreparedStatement;

public class RegisterDAO {

	public static int save(RegisterAction r) {  
		int status = 0;  
		try {  
			byte[] salt = Passwords.getNextSalt();
			Customer customer = r.getCustomerBean(); 
			Connection con = DriverLoader.getMySqlConnection();  

			PreparedStatement ps = con.prepareStatement("INSERT into customers(login, email, hash, salt) values(?, ?, ?, ?)");  
			ps.setString(1, customer.getLogin().toLowerCase());
			ps.setString(2, customer.getEmail().toLowerCase());  
			ps.setBytes(3, Passwords.hash(customer.getPassword().toCharArray(), salt));  
			ps.setBytes(4, salt);  

			status = ps.executeUpdate();  

		} catch(Exception e) {
			e.printStackTrace();
		}  
		return status;  
	}  
}  