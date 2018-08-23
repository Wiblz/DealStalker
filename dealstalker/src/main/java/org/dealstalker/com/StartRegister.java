package org.dealstalker.com;

import com.opensymphony.xwork2.ActionSupport;

public class StartRegister extends ActionSupport{
    
	int registrationTries = 0;
	public String execute() throws Exception {
        
		registrationTries++;
		return SUCCESS;
    }
}
