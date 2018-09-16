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

			PreparedStatement ps = con.prepareStatement("INSERT into customers(firstName, secondName, email, hash, salt) values(?, ?, ?, ?, ?)");  
			ps.setString(1, customer.getFirstName());  
			ps.setString(2, customer.getLastName());  
			ps.setString(3, customer.getEmail());  
			ps.setBytes(4, Passwords.hash(customer.getPassword().toCharArray(), salt));  
			ps.setBytes(5, salt);  

			status = ps.executeUpdate();  

		} catch(Exception e) {
			e.printStackTrace();
		}  
		return status;  
	}  
}  