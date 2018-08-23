package org.dealstalker.com;

import com.opensymphony.xwork2.ActionSupport;

public class StartSignin extends ActionSupport{
    
	int signinTries = 0;
	
	public String execute() throws Exception {
        
		signinTries++;
		return SUCCESS;
    }
}
