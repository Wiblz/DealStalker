package org.dealstalker.com;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class RegisterDAO {

	public static final int LOGIN_IS_TAKEN = -1;
	
	public static int save(RegisterAction r) {  
		int status = 0;  
		try {  
			byte[] salt = Passwords.getNextSalt();
			Customer customer = r.getCustomerBean(); 
			Connection con = DriverLoader.getMySqlConnection();  
			
			status = checkLogin(con, customer.getLogin());
			if (status != 0) {
				return status;
			}

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
	
	private static int checkLogin(Connection con, String login) throws SQLException {
		PreparedStatement ps = con.prepareStatement("SELECT id FROM customers WHERE login=?");
		ps.setString(1, login);
		
		ResultSet rs = ps.executeQuery(); 
		if (!rs.next()) {
			return 0;
		} else {
			return LOGIN_IS_TAKEN;
		}
	}
}  