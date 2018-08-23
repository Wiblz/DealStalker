package org.dealstalker.com;

import com.opensymphony.xwork2.ActionSupport;

public class Register extends ActionSupport {
    
    private static final long serialVersionUID = 1L;
    
    private Customer customerBean;


    public String execute() throws Exception {
        //call Service class to store personBean's state in database
        
        return SUCCESS;
    }
    
    public Customer getPersonBean() {
        return customerBean;
    }
    
    public void setPersonBean(Customer person) {
    	customerBean = person;
    }

}


