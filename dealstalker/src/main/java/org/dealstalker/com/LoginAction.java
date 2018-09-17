package org.dealstalker.com;

import java.util.Map;

import org.apache.struts2.dispatcher.SessionMap;
import org.apache.struts2.interceptor.SessionAware;

import com.opensymphony.xwork2.ActionSupport;

public class LoginAction extends ActionSupport implements SessionAware {

	private String login;
	private String password;  
	SessionMap<String, Object> sessionmap;  
	
	
	public String getLogin() {  
	    return login;  
	}  
	  
	public void setLogin(String login) {  
	    this.login = login;  
	}  
	  
	public String getPassword() {  
	    return password;  
	}  
	  
	public void setPassword(String password) {  
	    this.password = password;  
	}  
	  
	public String execute() {
	    if (LoginDAO.validate(login, password)) {
		    sessionmap.put("login", login);
	        return "success";  
	    }  
	    else {  
	        return "error";  
	    }  
	}  
	
	@Override
	public void setSession(Map<String, Object> session) {
		sessionmap = (SessionMap<String, Object>) session;  
	    sessionmap.put("login", login);  
	}

	public String logout() {   
	    sessionmap.invalidate();  
	    return "success";  
	}  
}
