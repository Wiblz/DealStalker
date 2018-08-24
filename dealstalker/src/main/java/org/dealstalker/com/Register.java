package org.dealstalker.com;

import com.opensymphony.xwork2.ActionSupport;

public class Register extends ActionSupport {
    
    private static final long serialVersionUID = 1L;
    
    private Customer customerBean;


    public String execute() throws Exception {
        //call Service class to store personBean's state in database
        
        return SUCCESS;
    }
    
    public Customer getCustomerBean() {
        return customerBean;
    }
    
    public void setCustomerBean(Customer customer) {
    	customerBean = customer;
    }
    

	public void validate(){
	    if (customerBean.getFirstName().length() == 0) {
	        addFieldError("personBean.firstName", "First name is required.");
	    }
	
	    if (customerBean.getEmail().length() == 0) {
	        addFieldError("personBean.email", "Email is required.");
	    }
	
	    if (customerBean.getAge() < 18) {
	        addFieldError("personBean.age", "Age is required and must be 18 or older");
	    }
	    
	    if (!customerBean.getPassword().equals(customerBean.getRepeatedPassword())) {
	        addFieldError("personBean.repeatedPassword", "Password should be identical");
	    }
	}

}


